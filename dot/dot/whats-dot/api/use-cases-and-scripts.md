# Use Cases and Scripts

Here is a list of common ways to use the API. All examples are done in Python.

Prerequisite: [Get an API token](./#everything-starts-with-a-token-of-trust).

<details>

<summary>Add labels to a conversation</summary>

```python
import requests

# Configuration
BASE_URL = "https://app.getdot.ai"
ADD_LABEL_ENDPOINT = "/api/add_label_to_chat"

# Replace with your API token obtained from your account settings.
API_TOKEN = "dot-your_token_here"

# Chat details
CHAT_ID = "your_chat_id"
LABELS = ["your_label"]

def add_label_to_chat(chat_id, labels):
    """Add labels to a chat using token-based authentication."""
    headers = {
        "API-KEY": API_TOKEN,
        "Content-Type": "application/json"
    }
    data = {"chat_id": chat_id, "labels": labels}
    
    try:
        response = requests.post(f"{BASE_URL}{ADD_LABEL_ENDPOINT}", headers=headers, json=data)
        response.raise_for_status()
        print("Successfully added labels to chat.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to add labels to chat: {e}")

def main():
    add_label_to_chat(CHAT_ID, LABELS)

if __name__ == "__main__":
    main()
```

</details>

<details>

<summary> Ask a question to Dot and follow up</summary>

```python
"""
Dot API Client Example

A minimal example showing how to interact with the Dot API to ask questions
about your data and follow up with additional questions in the same conversation.

Posting a question returns the conversation once Dot has finished answering.
A long investigation can outlast the request, so the example also shows how to
poll for the answer afterwards using the same chat_id.

This pattern applies to both initial questions and follow-up questions.

Usage:
    python3 test_api.py

Requirements:
    - Python 3.6+
    - requests library (pip install requests)
"""

import requests
import uuid

# API Configuration
# Replace with your Dot API key from the Settings page
API_KEY = "dot-YOUR_API_KEY_HERE"  

# Replace with your Dot API endpoint
# For cloud: "https://app.getdot.ai/api" or "https://eu.getdot.ai/api"
BASE_URL = "https://app.getdot.ai/api"
HEADERS = {"API-KEY": API_KEY, "Content-Type": "application/json"}


def ask_question(question):
    """
    Send a question to Dot and return the conversation.
    
    Returns:
        tuple: (messages, chat_id)
    """
    # Generate a unique chat ID for this conversation
    chat_id = str(uuid.uuid4())
    
    print(f"Asking question: '{question}'")
    endpoint = f"{BASE_URL}/agentic"
    payload = {"messages": [{"role": "user", "content": question}], "chat_id": chat_id}
    # Optional: "mode": "economy" | "balanced" | "frontier"
    
    response = requests.post(endpoint, headers=HEADERS, json=payload, timeout=600)
    response.raise_for_status()
    
    return response.json(), chat_id


def ask_follow_up(question, chat_id):
    """
    Send a follow-up question using the same chat session.
    
    Returns:
        list: The updated conversation
    """
    print(f"Asking follow-up: '{question}'")
    endpoint = f"{BASE_URL}/agentic_with_history"
    payload = {"new_message": {"role": "user", "content": question}, "chat_id": chat_id}
    
    response = requests.post(endpoint, headers=HEADERS, json=payload, timeout=600)
    response.raise_for_status()
    
    return response.json()


def fetch_conversation(chat_id):
    """
    Read a conversation back later, or poll for an answer that outlasted the request.
    
    Note the shape difference: posting a question returns the messages as a list,
    while this endpoint wraps them in {"messages": [...]}.
    """
    response = requests.get(f"{BASE_URL}/c2/{chat_id}", headers=HEADERS)
    response.raise_for_status()
    return response.json().get("messages", [])


def answer_text(messages):
    """
    Pull the user-visible answer out of a conversation.
    
    Dot's answer is the last message carrying a formatted result. That result is a
    list of parts — text, tables, charts — and the text parts joined together are
    what a person reads in the app.
    """
    if isinstance(messages, dict):
        messages = messages.get("messages", [])
    
    for message in reversed(messages or []):
        parts = (message.get("additional_data") or {}).get("formatted_result") or []
        texts = [str(p["data"]) for p in parts if p.get("type") == "text" and p.get("data")]
        if texts:
            return "\n\n".join(texts)
        
        content = message.get("content")
        if isinstance(content, str) and content.strip() and content.strip().lower() != "success":
            return content.strip()
    
    return ""


def print_response(messages):
    """Print the answer, if there is one."""
    answer = answer_text(messages)
    if answer:
        print("\n=== ANSWER ===")
        print(answer)
        print("\n")
    else:
        print("No answer yet — try fetch_conversation(chat_id) in a few seconds.")


def main():
    """
    Demonstrate the Dot API conversation flow.
    
    This shows a complete conversation with:
    1. An initial question
    2. A follow-up question using the same conversation context
    """
    try:
        # Ask an initial question
        initial_question = "What were our total sales last month?"
        try:
            user_input = input("Enter your question: ")
            if user_input.strip():
                initial_question = user_input
        except EOFError:
            print(f"Using default question: '{initial_question}'")
        
        # Step 1: Send the initial question and get the conversation back
        messages, chat_id = ask_question(initial_question)
        print_response(messages)
        print(f"Chat ID: {chat_id} (save this if you want to continue the conversation later)")
        
        # Ask a follow-up question in the same conversation
        follow_up = "How does that compare to the previous month?"
        try:
            user_input = input("Enter a follow-up question: ")
            if user_input.strip():
                follow_up = user_input
        except EOFError:
            print(f"Using default follow-up: '{follow_up}'")
        
        # Step 2: Send the follow-up question using the same chat_id
        follow_up_response = ask_follow_up(follow_up, chat_id)
        print_response(follow_up_response)
        
        print("Conversation complete! You can continue by using the same chat_id.")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
```

</details>

<details>

<summary>Sync a confluence page to the note</summary>

```python
import os, re, requests, markdownify

# ---------- 1)  Confluence ----------------------------------------------------
ATL_SITE  = "https://<your-site>.atlassian.net/wiki"
PAGE_ID   = "<confluence_page_id>"
ATL_AUTH  = (os.getenv("ATLASSIAN_EMAIL"), os.getenv("ATLASSIAN_API_TOKEN"))

r = requests.get(
    f"{ATL_SITE}/rest/api/content/{PAGE_ID}?expand=body.storage",
    auth=ATL_AUTH,
)
r.raise_for_status()
html = r.json()["body"]["storage"]["value"]
md   = markdownify.markdownify(html, heading_style="ATX")
page_url = f"{ATL_SITE}/pages/{PAGE_ID}"

# ---------- 2)  Dot – read org & note ----------------------------------------
DOT_BASE = "https://eu.getdot.ai/api"   # or https://app.getdot.ai/api for US
HEADERS  = {"API-KEY": os.getenv("DOT_API_KEY")}

notes    = requests.get(f"{DOT_BASE}/org_notes", headers=HEADERS).json()
existing = next((n for n in notes if n.get("title") == "Confluence FAQ"), None)
note     = existing.get("note", "") if existing else ""

# ---------- 3)  insert / replace the <faq> block ------------------------------
new_faq = f'<faq confluence_page_url="{page_url}">\n\n{md}\n\n</faq>'
note    = re.sub(r"<faq[^>]*>.*?</faq>", new_faq, note, flags=re.I|re.S) \
          if "<faq" in note.lower() else f"{note.rstrip()}\n\n{new_faq}"

# ---------- 4)  Dot – save the updated note -----------------------------------
if existing:
    requests.put(f"{DOT_BASE}/org_notes/{existing['id']}", headers=HEADERS,
                 json={"title": "Confluence FAQ", "note": note}).raise_for_status()
else:
    requests.post(f"{DOT_BASE}/org_notes", headers=HEADERS,
                  json={"title": "Confluence FAQ", "note": note}).raise_for_status()

print("✅  org‑note updated")
```

</details>


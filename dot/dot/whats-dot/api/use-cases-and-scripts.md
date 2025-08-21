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

The API flow has two main steps:
1. Send a question to Dot API (asynchronous processing)
2. Fetch the results when they're ready

This pattern applies to both initial questions and follow-up questions.

Usage:
    python3 test_api.py

Requirements:
    - Python 3.6+
    - requests library (pip install requests)
"""

import requests
import time
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
    Send a question to Dot API and fetch results.
    
    Returns:
        tuple: (response_data, chat_id)
    """
    # Generate a unique chat ID for this conversation
    chat_id = str(uuid.uuid4())
    
    # Step 1: Send the initial question
    print(f"Asking question: '{question}'")
    ask_endpoint = f"{BASE_URL}/ask"
    ask_payload = {"messages": [{"role": "user", "content": question}], "chat_id": chat_id}
    
    response = requests.post(ask_endpoint, headers=HEADERS, json=ask_payload)
    response.raise_for_status()
    
    # Step 2: Fetch the results
    print("Fetching results...")
    results_endpoint = f"{BASE_URL}/c2/{chat_id}"
    time.sleep(2)  # Brief pause to let processing complete
    
    result_response = requests.get(results_endpoint, headers=HEADERS)
    result_response.raise_for_status()
    
    return result_response.json(), chat_id


def ask_follow_up(question, chat_id):
    """
    Send a follow-up question using the same chat session.
    
    Returns:
        dict: Updated conversation with the answer
    """
    # Step 1: Send the follow-up question
    print(f"Asking follow-up: '{question}'")
    endpoint = f"{BASE_URL}/ask_with_history"
    payload = {"new_message": {"role": "user", "content": question}, "chat_id": chat_id}
    
    response = requests.post(endpoint, headers=HEADERS, json=payload)
    response.raise_for_status()
    
    # Step 2: Fetch the updated results
    print("Fetching updated results...")
    results_endpoint = f"{BASE_URL}/c2/{chat_id}"
    time.sleep(2)  # Brief pause to let processing complete
    
    result_response = requests.get(results_endpoint, headers=HEADERS)
    result_response.raise_for_status()
    
    return result_response.json()


def print_response(response):
    """
    Print the important parts of the response.
    
    This extracts the answer text from the conversation history.
    The API returns the full conversation, so we need to find
    the last assistant message to get the most recent answer.
    """
    if not response:
        print("No response received")
        return
        
    # For chat history responses, get the last assistant message (the answer)
    if "messages" in response and len(response["messages"]) > 0:
        messages = response["messages"]
        # Find the last assistant message
        assistant_messages = [m for m in messages if m.get("role") == "assistant"]
        if assistant_messages:
            last_message = assistant_messages[-1]
            
            # Print the explanation if available
            if "explanation" in last_message and last_message["explanation"]:
                print("\n=== ANSWER ===")
                print(last_message["explanation"])
                print("\n")
                
            # You can uncomment this to see all available fields
            # print("Available fields:", list(last_message.keys()))


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
        
        # Step 1: Send the initial question and get response
        response, chat_id = ask_question(initial_question)
        print_response(response)
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

org  = requests.get(f"{DOT_BASE}/org", headers=HEADERS).json()   # org has id & note
note = org.get("note") or ""
org_id = org["id"]

# ---------- 3)  insert / replace the <faq> block ------------------------------
new_faq = f'<faq confluence_page_url="{page_url}">\n\n{md}\n\n</faq>'
note    = re.sub(r"<faq[^>]*>.*?</faq>", new_faq, note, flags=re.I|re.S) \
          if "<faq" in note.lower() else f"{note.rstrip()}\n\n{new_faq}"

# ---------- 4)  Dot – save the updated note -----------------------------------
payload = {"org_id": org_id, "note": note}
requests.post(f"{DOT_BASE}/save_note", headers=HEADERS, json=payload).raise_for_status()

print("✅  org‑note updated")
```

</details>


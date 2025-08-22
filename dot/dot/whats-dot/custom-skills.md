---
description: Extend what Dot can do.
---

# Custom Skills

> This is a premium feature. Please contact us for access.

Custom skills allows you to teach new things to Dot. It's mostly intended for connecting to external systems. Here are some of the things you might want to do.

<details>

<summary>Query Another Dot Instance</summary>

This example shows how to query data from another Dot instance using its API. The response will be properly formatted for Dot's custom skill parser.

Paste this code into custom skills in Model > Custom Skills > Add skill

The parameters are:

* user\_request (String): The user's question
* chat\_id (String): The conversation ID (use "new" for new conversations)

**Description**

Please add this description to the skill along with whatever else you want to add.

```
The chat_id parameter determines the conversation state:
- If chat_id is "new", it will start a new chat
- If you provide an existing chat_id, it will continue that conversation

When a DataFrame is returned:
- It's automatically stored in your  memory
- You can use it like a normal DataFrame to chain with other tools
- For example: visualize it or display it

Example workflow:
1. First call: "Show me sales by region" (chat_id="new")
   → Returns data and a chat_id
2. Follow-up: "Now show only regions over $1M" (use returned chat_id)
   → Continues the same conversation context

```

**Code**

```python
import requests
import time
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration - Replace with your actual values
API_KEY = os.getenv("DOT_API_KEY")  # Get from Settings > API Tokens in your Dot instance
BASE_URL = "https://app.getdot.ai/api"  # Or "https://eu.getdot.ai/api" for EU

# Set up headers for API requests
headers = {"API-KEY": API_KEY, "Content-Type": "application/json"}

# These variables are injected by Dot when running as a custom skill:
# - user_request: The user's question
# - chat_id: Conversation ID (use "new" or None for new conversations)

# For local testing, uncomment these:
user_request = "Show me total sales by product category"
chat_id = "new"


try:
    # Check if this is a new conversation
    # Handle case where chat_id is not defined
    if "chat_id" not in locals() and "chat_id" not in globals():
        chat_id = "new"

    is_new_chat = chat_id is None or chat_id == "" or chat_id == "new"

    # Prepare the API request
    if is_new_chat:
        # Start a new conversation
        chat_id = str(uuid.uuid4())
        url = f"{BASE_URL}/ask"
        payload = {"messages": [{"role": "user", "content": user_request}], "chat_id": chat_id}
    else:
        # Continue existing conversation
        url = f"{BASE_URL}/ask_with_history"
        payload = {"new_message": {"role": "user", "content": user_request}, "chat_id": chat_id}

    # Send the request
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    # Wait a moment for processing
    time.sleep(2)

    # Get the answer
    answer_response = requests.get(f"{BASE_URL}/c2/{chat_id}", headers=headers)
    answer_response.raise_for_status()

    # Extract and display the response
    data = answer_response.json()
    if "messages" in data:
        # Find the assistant's response
        for message in reversed(data["messages"]):
            if message.get("role") == "assistant":
                # Dot will automatically parse the response and do appropriate formatting
                print(message)
                break

    # Provide the chat ID for continuing the conversation
    print(f"\nTo continue this conversation, use chat_id: {chat_id}")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to Dot API. Please check your BASE_URL and network connection.")
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 401:
        print("Error: Invalid API key. Please check your API_KEY in Settings > API Tokens.")
        print(e)
    elif e.response.status_code == 404:
        print("Error: API endpoint not found. Please check your BASE_URL.")
        print(e)
    else:
        print(f"HTTP Error {e.response.status_code}: {e.response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error calling Dot API: {str(e)}")
except Exception as e:
    print(f"Unexpected error: {str(e)}")
 
```



</details>

<details>

<summary>Create a Notion ticket</summary>

Opens a Notion ticket whenever a specific condition is met and specified by the customer

### **What gets created in Notion**

**Name** → short summary of the task (Dot always summarizes)

**Description** → brief context + next steps (Dot always writes both)

**Status** → one of: Not started | To do | In progress | Done, or the ones you need

**Due Date** → format YYYY-MM-DD

**Priority** → must match an existing option in your Notion DB

### **What you see in chat**

```
Notion ticket created succesfully ✅ - You can review the notion ticket <a href="{{page_url}}">here</a> and all tickets in <a href="{{database_url}}">here</a>
```

The first link opens the new page, the second opens the database. You can also personalize this in the Dot description.

### **Inputs Dot needs**

**name** → short summary (action-oriented)

**description** → context + next steps

**status\_name** → Not started | To do | In progress | Done

**priority** → existing Priority option in your DB

**due\_date** → YYYY-MM-DD

### **How it works behind the scenes**

Skill maps everything into a single main() that uses the Notion API to create the page and fetch the page/database URLs

Your Notion token and database ID are configured in the Dot skill setup window (no local setup needed)

### **Example**

**name:** Reach out to ACME about low weekly queries

**description:** Usage dipped below threshold. Next steps: email champion with best-practice guide; schedule 20-min optimization session

**status\_name:** To do

**priority:** High

**due\_date:** 2025-08-25

Dot creates the ticket with those fields and replies with the two links

### Dot Skill Description

```markdown
Open a new notion ticket if the usage of Dot for a customer is too low. Everything should be mapped to the main() function.

You should always summarize the task as part of the name parametr, and create a brief description and next steps for the description parameter.

You should consider for the status parameter the following available options: "Not started", "To do", "In progress", "Done".

You should always consider dates to have the format "YYYY-MM-DD".

For the message output to the user, please retrieve both URLs for the Notion Page and Database for easy access.

The message output should look like this:

"Notion ticket created succesfully ✅ - You can review the notion ticket here and all tickets in here" - You should include the links to the page and database as part of the a tags in the first and second "here" words that are part of the message. They should be clickable for better experience.
```

### Python Function

```python
#!/usr/bin/env python3
"""
Single-file Notion API integration script.

This script provides a complete Notion API wrapper with helper functions
for creating pages in Notion databases. Uses only the requests library.

Usage:
    Set environment variables:
    - NOTION_API_TOKEN: Your Notion integration token
    - NOTION_DATABASE_ID: Target database ID (optional, can be passed directly)
    
    Then run: python notion_integration.py
    
    Or import and use the functions in your automation:
    from notion_integration import NotionWrapper, title_prop, rich_text
"""

import json
import logging
import os
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

import requests

# Configure logging
def setup_logging():
    """Set up logging configuration."""
    level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        level=getattr(logging, level, logging.INFO),
        format="%(asctime)s | %(levelname)-8s | %(message)s",
    )

class NotionWrapperError(Exception):
    """Custom exception for Notion wrapper operations."""
    pass

class NotionWrapper:
    """Simple Notion API wrapper using only requests."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize with Notion API token."""
        self.token = token or os.getenv('NOTION_API_TOKEN')
        if not self.token:
            raise NotionWrapperError("NOTION_API_TOKEN required")
        
        self.base_url = "<https://api.notion.com/v1>"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        logging.info("NotionWrapper initialized")
    
    def create_page(self, database_id: str, properties: Dict[str, Any]) -> str:
        """Create a new page in a Notion database."""
        if not database_id or not properties:
            raise NotionWrapperError("database_id and properties required")
        
        url = f"{self.base_url}/pages"
        data = {
            "parent": {"database_id": database_id},
            "properties": properties
        }
        
        try:
            response = requests.post(url, headers=self.headers, json=data)
            
            if response.status_code != 200:
                # Get detailed error information
                try:
                    error_details = response.json()
                    error_msg = f"Notion API Error {response.status_code}:\\n"
                    error_msg += f"Message: {error_details.get('message', 'No message provided')}\\n"
                    if 'code' in error_details:
                        error_msg += f"Code: {error_details['code']}\\n"
                    if 'details' in error_details:
                        error_msg += f"Details: {error_details['details']}\\n"
                    error_msg += f"\\nRequest data sent:\\n{json.dumps(data, indent=2)}"
                except:
                    error_msg = f"HTTP {response.status_code}: {response.text}\\n"
                    error_msg += f"Request data sent:\\n{json.dumps(data, indent=2)}"
                
                logging.error(error_msg)
                raise NotionWrapperError(error_msg)
            
            page_id = response.json()["id"]
            logging.info(f"Created page: {page_id}")
            return page_id
            
        except requests.exceptions.RequestException as e:
            error_msg = f"Request failed: {e}"
            logging.error(error_msg)
            raise NotionWrapperError(error_msg)

# Helper functions for property types
def title_prop(text: str) -> Dict[str, Any]:
    """Create title property."""
    return {"title": [{"text": {"content": text}}]}

def rich_text(text: str) -> Dict[str, Any]:
    """Create rich text property."""
    return {"rich_text": [{"text": {"content": text}}]}

def select(name: str) -> Dict[str, Any]:
    """Create select property."""
    return {"select": {"name": name}}

def multi_select(names: List[str]) -> Dict[str, Any]:
    """Create multi-select property."""
    return {"multi_select": [{"name": name} for name in names]}

def status(name: str) -> Dict[str, Any]:
    """Create status property."""
    return {"status": {"name": name}}

def date(start: str, end: Optional[str] = None) -> Dict[str, Any]:
    """Create date property."""
    return {"date": {"start": start, "end": end}}

def number(value: Union[int, float]) -> Dict[str, Any]:
    """Create number property."""
    return {"number": value}

def checkbox(checked: bool) -> Dict[str, Any]:
    """Create checkbox property."""
    return {"checkbox": checked}

def url(link: str) -> Dict[str, Any]:
    """Create URL property."""
    return {"url": link}

def email(address: str) -> Dict[str, Any]:
    """Create email property."""
    return {"email": address}

def phone_number(number: str) -> Dict[str, Any]:
    """Create phone number property."""
    return {"phone_number": number}

def relation(page_ids: List[str]) -> Dict[str, Any]:
    """Create relation property."""
    return {"relation": [{"id": page_id} for page_id in page_ids]}

def get_page_url(page_id: str) -> str:
    """Get the actual page URL from Notion API."""
    try:
        token = os.getenv('NOTION_API_TOKEN')
        headers = {
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2022-06-28",
        }
        response = requests.get(f"<https://api.notion.com/v1/pages/{page_id}>", headers=headers)
        response.raise_for_status()
        page_data = response.json()
        return page_data.get('url', '')
    except requests.exceptions.RequestException as e:
        logging.error(f"Could not retrieve page URL: {e}")
        return ""

def get_database_url(database_id: str) -> str:
    """Get the actual database URL from Notion API."""
    try:
        token = os.getenv('NOTION_API_TOKEN')
        headers = {
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2022-06-28",
        }
        response = requests.get(f"<https://api.notion.com/v1/databases/{database_id}>", headers=headers)
        response.raise_for_status()
        db_data = response.json()
        return db_data.get('url', '')
    except requests.exceptions.RequestException as e:
        logging.error(f"Could not retrieve database URL: {e}")
        return ""

def main(name, description, status_name, priority, due_date):
    """Main function for testing."""
    setup_logging()
    
    # Check for required environment variables
    db_id = os.getenv("NOTION_DATABASE_ID")
    if not db_id:
        print("❌ NOTION_DATABASE_ID not set")
        print("Set it with: export NOTION_DATABASE_ID='your_database_id'")
        sys.exit(1)
    
    token = os.getenv("NOTION_API_TOKEN")
    if not token:
        print("❌ NOTION_API_TOKEN not set")
        print("Set it with: export NOTION_API_TOKEN='your_token'")
        sys.exit(1)
    
    try:
        # Create page with only Name property (since that's what your database has)
        notion = NotionWrapper()
        properties = {
            "Name": title_prop(f"{name}"),
            "Description": rich_text(description),
            "Status": status(status_name),
            "Due Date": date(due_date),
            "Priority": select(priority)
        }
        page_id = notion.create_page(db_id, properties)
        
        # Generate URLs
        page_url = get_page_url(page_id)
        database_url = get_database_url(db_id)
        
        print("\\n🎉 Success! Created Notion page:")
        print(f"📝 Page ID: {page_id}")
        print(f"🔗 Page URL: {page_url}")
        print(f"📊 Database URL: {database_url}")
        print("\\nYou can click these URLs to view in Notion!")
        
        return {
            "page_id": page_id,
            "page_url": page_url,
            "database_id": db_id,
            "database_url": database_url
        }
        
    except NotionWrapperError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main(name, description, status_name, priority, due_date)

```

</details>

### Common Use Cases

1. **Workflow automation** based on data analysis results from Dot: Create Jira/Linear tickets, update Notion docs, send Slack/email messages with findings from Dot.
2. **Enrich Analysis with Additional Data:** Connect data that is not available in your data warehouse, like customer info from a CRM or real-time data from a WMS.
3. **Advanced Analysis Beyond SQL:** Run small ML models inside the sandbox, or host them on a server behind an API that Dot can call. This opens up a whole new world of ML and other analysis. For example forecasting important metrics on the fly.

### **How Custom Skills Work**

Custom skills appear as natural extensions of Dot's capabilities. Users simply ask questions in plain language, and Dot automatically:

1. Identifies when a custom skill is relevant based on the query
2. Extracts required parameters from the conversation context
3. Executes the skill and presents results accordingly.



### **Creating Custom Skills**

Admins create and manage skills through the UI.

Navigate to the model page → skill tab (/skills page) and you will find the section to add custom skills.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Here you can define the following:

1. **Name**: Name of the custom skill. Be descriptive as it will help Dot use the skill more effectively (e.g., add\_issue\_to\_jira). Limited to alphanumeric characters, underscores, and hyphens (maximum 128 characters).
2. **Description**: Explain what the skill does and when to use it—this helps Dot select the appropriate skill for user queries. Be detailed: add all information that a developer would need to use this function. If there are common mistakes that Dot might make when using the skill, mention them here.
3. **Parameters**: Define the inputs your function requires. Remember that Dot will decide all these parameters when calling this function. Keep them minimal and simple. If you have static values (API endpoints, hard-coded params), define them as variables.
   * **Types**: `str`, `number`, `bool`, `dataframe`. Note that if the type is dataframe, the skill can only be used in Agentic mode.
4. **Code**: Your Python function. Parameters are passed as global variables at runtime to this script. Use print(variable) to pass data back to Dot.
5. **Secrets**: Encrypted storage for API keys and credentials.
6. **Groups**: Control which user groups can access this skill.
7. **Active**: Toggle to enable or disable the skill.

Use the **Test** button to validate your skill with sample data before saving.

### Custom Skills in Normal Chat vs Agentic Mode

If any of the input parameters for the custom skill is a `dataframe` - the skill can only be used in agentic mode.

What this means in practice is that it is better to reserve complex tools like data prediction or data manipulation tools for the agentic mode.

The key difference: In Deep Analysis mode, Dot can chain multiple operations together, using output from your skill as input for further analysis. Skills become building blocks in a larger analytical workflow.

### **Technical Architecture**

#### **Execution Environment**

* **Isolation**: Each execution runs in a Docker container with process-level isolation and resource limitations.
* **Timeout**: 600 seconds maximum per execution
* **Python Version**: 3.12

#### **Available Packages**

Pre-installed in the execution environment:

* `pandas` - Data manipulation and analysis
* `numpy` - Numerical computing
*   `requests` - HTTP requests

    If you need additional packages, please contact us and we will be happy to assist.

### Best Practices

#### 1. Parameter Validation

There is a chance Dot makes a mistake. Try to catch as many errors as possible programmatically. Be defensive and provide good feedback. Validation need not be limited to just types—it can be more complex (e.g., len(df) < 1000, check if combinations of parameters are valid).

```python

# process_data function
# argument: df: pd.DataFrame, threshold: float

  # Validate dataframe
  if df.empty:
      print("Error: Empty dataframe provided")

  required_columns = ['amount', 'date', 'category']
  missing = [col for col in required_columns if col not in df.columns]
  if missing:
      print(f"Error: Missing columns: {missing}")

  # Validate threshold
  if not 0 <= threshold <= 1:
      print("Error: Threshold must be between 0 and 1")

```

#### 2. Result Handling

You can pass back results using the `print()` statement.

In agentic mode, you can pass back a dataframe to Dot by doing:

`print(dataframe)` — we will automatically handle the logic to convert this into a format that Dot can understand.

Currently we only support print statements with one argument inside (print(a,b) will not work).

Structure your print statements to be clear and easily understandable for Dot. Include only the relevant info and no unnecessary logs.

If something goes wrong during execution, handle it gracefully. Be explicit. Always try to pass back the status of the tool execution (complete/partial/failed). If failed or partial, provide feedback to Dot on what went wrong and how to fix it.

<details>

<summary>Example Python script with explicit error handling</summary>

```python

# fetch_customer_data_from_crm(account_name: str)

api_key = os.environ.get('CRM_API_KEY')
if not api_key:
    print("Status: FAILED - CRM_API_KEY not configured in skill secrets")
    exit()

# Validate input
if 'account_name' not in locals():
    print("Status: FAILED - Account name is required")
    exit()

if not account_name:
    print("Status: FAILED - Account name is required")
    exit()

if not isinstance(account_name, str):
    print("Status: FAILED - Account name must be a string")
    exit()

try:
    # Search for account
    search_url = f"<https://api.crm.com/accounts?name={account_name}>"
    search_response = requests.get(
        search_url,
        headers={"Authorization": f"Bearer {api_key}"}
    )

    if search_response.status_code != 200:
        print(f"Status: FAILED - CRM API error {search_response.status_code}")
        exit()

    accounts = search_response.json()

    if not accounts:
        print(f"Status: PARTIAL - No account found matching '{account_name}'. Try a different spelling or partial name.")
        exit()

    if len(accounts) > 1:
        # Multiple matches - return what we found
        account_list = [f"- {acc.get('name', 'N/A')} (ID: {acc.get('id', 'N/A')})" for acc in accounts[:5]]
        output = (
            f"Status: PARTIAL\\\\n"
            f"Found {len(accounts)} accounts matchIf something goes wrong during execution, handle it gracefully. Be explicit. Always try to pass back the status of the tool execution (complete/partial/failed). If failed or partial, provide feedback to Dot on what went wrong and how to fix it.ing '{account_name}':\\\\n"
            f"{chr(10).join(account_list)}\\\\n"
            f"Please be more specific in your query."
        )
        print(output)
        exit()

    # Single match - get full details
    account_id = accounts[0].get('id')
    if not account_id:
        print("Status: FAILED - Account data missing 'id' field.")
        exit()

    details_url = f"<https://api.crm.com/accounts/{account_id}/details>"
    details_response = requests.get(
        details_url,
        headers={"Authorization": f"Bearer {api_key}"}
    )

    if details_response.status_code == 200:
        account_data = details_response.json()

        # Convert to dataframe for analysis
        df = pd.DataFrame([account_data])
        print(df)  # Make dataframe available to agent

        summary = (
            f"Status: COMPLETE\\\\n"
            f"Retrieved data for {account_data.get('name', 'N/A')}\\\\n"
            f"Industry: {account_data.get('industry', 'N/A')}\\\\n"
            f"Annual Revenue: ${account_data.get('annual_revenue', 0):,.2f}\\\\n"
            f"Employee Count: {account_data.get('employees', 'N/A')}\\\\n"
            f"Full details available in dataframe"
        )
        print(summary)

    else:
        output = (
            f"Status: PARTIAL\\\\n"
            f"Found account {accounts[0].get('name', 'N/A')} but could not fetch details\\\\n"
            f"Error: API returned {details_response.status_code}\\\\n"
            f"Basic info: ID={account_id}"
        )
        print(output)

except requests.exceptions.Timeout:
    print("Status: FAILED - Request timed out. API may be slow or unavailable.")
except requests.exceptions.ConnectionError:
    print("Status: FAILED - Could not connect to CRM API. Check network settings.")
except ValueError as e:
    print(f"Status: FAILED - Invalid JSON response from API: {str(e)}")
except Exception as e:
    print(f"Status: FAILED - Unexpected error: {str(e)}")

```



</details>

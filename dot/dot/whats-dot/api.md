---
description: automate as much as you like
---

# API



## Automatically Sync Dot

To keep Dot in sync with your production environment, it is recommended to trigger the following API endpoint

{% openapi src="../../.gitbook/assets/dot_openapi2.json" path="/api/sync/{connection_type}/{connection_id}" method="post" %}
[dot_openapi2.json](../../.gitbook/assets/dot_openapi2.json)
{% endopenapi %}

```javascript
// URL endpoint
https://{region}.getdot.ai/api/sync/{connection_type}/{connection_type}?user_id={user}&api_token={api_token}
```

* **Region**: `app` (US)  or `eu` (EU)
* **Connection Type**: `postgres`, `redshift`, `snowflake`, `mssql`, `bigquery`, `databricks`, `looker`, `dbt`
* **User ID**: usually email of the user [(url encoded)](https://www.urlencoder.io/)
* **API Token**: can get created (and overwritten) by clicking `Copy API Token` in Settings/Users/Actions/···

\
**Trigger with curl (CLI)**

```javascript
curl -X "POST" "https://eu.getdot.ai/api/sync/bigquery/my-bg-id?user_id=sync_user%40contoso.com&api_token=42673584be9724a21e1550336d6fe509f4a04207461ec9a926ca2a27cbd27fa0
```



**Trigger with dbt webhooks**

Call the api endpoint after your dbt run completed.

{% embed url="https://docs.getdbt.com/docs/deploy/webhooks#create-a-webhook-subscription" %}
Documentation how to setup a dbt webhooks
{% endembed %}







## Import External Assets

Inform Dot about key external knowledge assets, such as BI dashboards or custom data apps, so it can recommend them to users and assist with discovery and understanding. Authentication works similarly to the Sync Connection endpoint.

{% openapi src="../../.gitbook/assets/openapi.json" path="/api/import_and_overwrite_external_asset" method="post" %}
[openapi.json](../../.gitbook/assets/openapi.json)
{% endopenapi %}



## Export Conversation History

Export all conversations together with relevant meta data fields such as number of messages or author.

{% openapi src="../../.gitbook/assets/openapi_2024-12-05.json" path="/api/export_history" method="get" %}
[openapi_2024-12-05.json](../../.gitbook/assets/openapi_2024-12-05.json)
{% endopenapi %}







## Authentication for all other endpoints

For most operations on Dot you first need to login.

<details>

<summary>Example of Python script to authenticate and adding a label to a chat</summary>

```

import requests
import json

# Configuration
BASE_URL = "https://app.getdot.ai"
LOGIN_ENDPOINT = "/api/auth/token"
ADD_LABEL_ENDPOINT = "/api/add_label_to_chat"

# Replace these with your actual credentials and chat details
USERNAME = "your_username"
PASSWORD = "your_password"
CHAT_ID = "your_chat_id"
LABELS = ["your_label"]

def authenticate():
    """Authenticate and get access token."""
    data = {
        "grant_type": "password",
        "username": USERNAME,
        "password": PASSWORD
    }
    
    try:
        response = requests.post(f"{BASE_URL}{LOGIN_ENDPOINT}", data=data)
        response.raise_for_status()
        return response.json().get("access_token")
    except requests.exceptions.RequestException as e:
        print(f"Authentication failed: {e}")
        return None

def add_label_to_chat(access_token, chat_id, labels):
    """Add labels to a chat."""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "chat_id": chat_id,
        "labels": labels
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}{ADD_LABEL_ENDPOINT}",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        print("Successfully added labels to chat.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to add labels to chat: {e}")

def main():
    access_token = authenticate()
    if access_token:
        add_label_to_chat(access_token, CHAT_ID, LABELS)

if __name__ == "__main__":
    main()

```

</details>



{% openapi src="../../.gitbook/assets/dot_openapi.json" path="/api/auth/token" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endopenapi %}



For embedded use cases that require SSO, where your end users have individual permissions you can use this endpoint to obtain an access token for users that is valid for 24h. Here is an example on how you can use it to [embed](embed.md) Dot in your application.&#x20;

Please make sure that enabled this flag on settings: "Allow admins to authenticate for users to enable SSO in embed&#x73;**".**

{% openapi src="../../.gitbook/assets/openapi_2024_12_11.json" path="/api/auth/embedded_user_login" method="post" %}
[openapi_2024_12_11.json](../../.gitbook/assets/openapi_2024_12_11.json)
{% endopenapi %}

## User Administration

{% openapi src="../../.gitbook/assets/dot_openapi.json" path="/api/get_users" method="get" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/dot_openapi.json" path="/api/send_invitations" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/dot_openapi.json" path="/api/delete_user" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/dot_openapi.json" path="/api/change_user_role" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/dot_openapi.json" path="/api/add_user_to_group" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/dot_openapi.json" path="/api/remove_user_from_group" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/openapi(2) (1).json" path="/api/create_user" method="post" %}
[openapi(2) (1).json](<../../.gitbook/assets/openapi(2) (1).json>)
{% endopenapi %}

## Ask questions

{% openapi src="../../.gitbook/assets/dot_openapi.json" path="/api/ask_with_history" method="post" expanded="false" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/dot_openapi.json" path="/api/ask" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endopenapi %}




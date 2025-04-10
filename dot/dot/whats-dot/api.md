---
description: automate as much as you like
---

# API

## Everything starts with a token of trust

All API endpoints can be accessed via an API token that is tied to the permissions of a user account. You can also let them expire after some time.

### How to get a token?

1. Go to **Settings / Users**
2. Click **Create New Token**

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

3. **Enter a name**, description, and expiration period
4. **Copy the token** (it's only shown once)



### How to use the token?

You have two ways. You either pass the token as a header with `API-KEY` or you pass it as a url parameter  in `api_token` . As a header is usually more secure because automated loggers don't store them, but in some places you can't set headers (e.g. dbt webhooks) and then you can use the URL parameter.

#### Via Headers

Call the user endpoint via command line interface.

```bash
# Basic API request with token
curl -H "API-KEY: dot-your_token_here" <https://[app or eu].getdot.ai/api/auth/me>
```

Call the user endpoint via Python.

```python
import requests
headers = {"API-KEY": "dot-your_token_here"}
response = requests.get("<https://[app or eu].getdot.ai/api/auth/me>", headers=headers)
```

#### Via URL - Parameters

For the following endpoints you can also use a URL based authentication:

* Sync connection
* Import external asserts
* Export conversation history

Call the endpoint only via url:

```bash
curl "https://{region}.getdot.ai/api/sync/{connection_type}/{connection_type}" \
     "?user_id={user}&api_token={api_token}"
```





## Automatically Sync Dot

To keep Dot in sync with your production environment, it is recommended to trigger the following API endpoint

{% openapi-operation spec="dot-openapi" path="/api/sync/{connection_type}/{connection_id}" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

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
curl -X "POST" "https://eu.getdot.ai/api/sync/bigquery/my-bg-id?user_id=sync_user%40contoso.com&api_token=dot-42673584be9724a21e1550336d6fe509f4a04207461ec9a926ca2a27cbd27fa0
```



**Trigger with dbt webhooks**

Call the api endpoint after your dbt run completed.

{% embed url="https://docs.getdbt.com/docs/deploy/webhooks#create-a-webhook-subscription" %}
Documentation how to setup a dbt webhooks
{% endembed %}







## Import External Assets

Inform Dot about key external knowledge assets, such as BI dashboards or custom data apps, so it can recommend them to users and assist with discovery and understanding. Authentication works similarly to the Sync Connection endpoint.

{% openapi-operation spec="dot-openapi" path="/api/import_and_overwrite_external_asset" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}



## Export Conversation History

Export all conversations together with relevant meta data fields such as number of messages or author.

{% openapi-operation spec="dot-openapi" path="/api/export_history" method="get" %}
[Broken link](broken-reference)
{% endopenapi-operation %}







## All endpoints

Once you [created your token](api.md#everything-starts-with-a-token-of-trust), you can use [all API endpoints](https://test.getdot.ai/redoc). Here is selection of frequently used endpoints and some examples on how the API got used.



#### Examples

<details>

<summary>Example of Python script to add labels to a conversation</summary>

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





## Ask Dot Automatically

{% openapi-operation spec="dot-openapi" path="/api/ask" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/ask_with_history" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

Trigger Deep Analysis

{% openapi-operation spec="dot-openapi" path="/api/agentic" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}



## User Administration

{% openapi-operation spec="dot-openapi" path="/api/get_users" method="get" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/send_invitations" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/delete_user" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/change_user_role" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/add_user_to_group" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/remove_user_from_group" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/create_user" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

## Automatically Authenticate Embedded Users

For embedded use cases that require SSO, where your end users have individual permissions you can use this endpoint to obtain an access token for users that is valid for 24h. Here is an example on how you can use it to [embed](embed.md) Dot in your application.&#x20;

Please make sure that you enabled this flag on settings: **"Allow admins to authenticate for users to enable SSO in embeds".**

{% openapi-operation spec="dot-openapi" path="/api/auth/embedded_user_login" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}




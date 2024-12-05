---
description: automate as much as you like
---

# API



## Automatically Sync Dot

To keep Dot in sync with your production environment, it is recommended to trigger the following API endpoint

{% swagger src="../../.gitbook/assets/dot_openapi2.json" path="/api/sync/{connection_type}/{connection_id}" method="post" %}
[dot_openapi2.json](../../.gitbook/assets/dot_openapi2.json)
{% endswagger %}

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

{% swagger src="../../.gitbook/assets/openapi.json" path="/api/import_and_overwrite_external_asset" method="post" %}
[openapi.json](../../.gitbook/assets/openapi.json)
{% endswagger %}



## Export Conversation History

Export all conversations together with relevant meta data fields such as number of messages or author.

{% swagger src="../../.gitbook/assets/openapi_2024-12-05.json" path="/api/export_history" method="get" %}
[openapi_2024-12-05.json](../../.gitbook/assets/openapi_2024-12-05.json)
{% endswagger %}







## Authentication for all other endpoints

For most operations on Dot you first need to login.

{% swagger src="../../.gitbook/assets/dot_openapi.json" path="/api/auth/token" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endswagger %}



## User Administration

{% swagger src="../../.gitbook/assets/dot_openapi.json" path="/api/get_users" method="get" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endswagger %}

{% swagger src="../../.gitbook/assets/dot_openapi.json" path="/api/send_invitations" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endswagger %}

{% swagger src="../../.gitbook/assets/dot_openapi.json" path="/api/delete_user" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endswagger %}

{% swagger src="../../.gitbook/assets/dot_openapi.json" path="/api/change_user_role" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endswagger %}

{% swagger src="../../.gitbook/assets/dot_openapi.json" path="/api/add_user_to_group" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endswagger %}

{% swagger src="../../.gitbook/assets/dot_openapi.json" path="/api/remove_user_from_group" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endswagger %}

{% swagger src="../../.gitbook/assets/openapi(2) (1).json" path="/api/create_user" method="post" %}
[openapi(2) (1).json](<../../.gitbook/assets/openapi(2) (1).json>)
{% endswagger %}

## Ask questions

{% swagger src="../../.gitbook/assets/dot_openapi.json" path="/api/ask_with_history" method="post" expanded="false" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endswagger %}

{% swagger src="../../.gitbook/assets/dot_openapi.json" path="/api/ask" method="post" %}
[dot_openapi.json](../../.gitbook/assets/dot_openapi.json)
{% endswagger %}




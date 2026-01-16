# Commonly used Endpoints

## Automatically Sync Dot

To keep Dot in sync with your production environment, it is recommended to trigger the following API endpoint

{% openapi-operation spec="dot-openapi" path="/api/sync/{connection_type}/{connection_id}" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
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
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}



## Export Conversation History

Export all conversations together with relevant meta data fields such as number of messages or author.

{% openapi-operation spec="dot-openapi" path="/api/export_history" method="get" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}





## Ask Dot Automatically

{% openapi-operation spec="dot-openapi" path="/api/ask" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/ask_with_history" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

Trigger Deep Analysis

{% openapi-operation spec="dot-openapi" path="/api/agentic" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}



## User Administration

{% openapi-operation spec="dot-openapi" path="/api/get_users" method="get" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/send_invitations" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/delete_user" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/change_user_role" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/add_user_to_group" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/remove_user_from_group" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="dot-openapi" path="/api/create_user" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

## Automatically Authenticate Embedded Users

For embedded use cases that require SSO, where your end users have individual permissions you can use this endpoint to obtain an access token for users that is valid for 24h. Here is an example on how you can use it to [embed](../embed.md) Dot in your application. 

Please make sure that you enabled this flag on settings: **"Allow admins to authenticate for users to enable SSO in embeds".**

{% openapi-operation spec="dot-openapi" path="/api/auth/embedded_user_login" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}




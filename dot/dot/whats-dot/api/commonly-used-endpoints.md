# Commonly used Endpoints

## Automatically Sync Dot

To keep Dot in sync with your production environment, it is recommended to trigger the following API endpoint

{% openapi-operation spec="dot-openapi" path="/api/sync/{connection_type}/{connection_id}" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

```javascript
// URL endpoint
https://{region}.getdot.ai/api/sync/{connection_type}/{connection_id}?user_id={user}&api_token={api_token}
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

`/api/agentic` is how you ask Dot anything. It is the same engine behind the app, Slack and Teams: Dot reads your model, writes and runs SQL, builds charts, and keeps going until it can answer. A one-line lookup and a multi-step investigation use this one endpoint — Dot decides how far to go.

Send a question with a `chat_id` you generate. The call returns the conversation once Dot has finished.

{% openapi-operation spec="dot-openapi" path="/api/agentic" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

Follow up by posting to `/api/agentic_with_history` with the same `chat_id`, so Dot keeps the context of everything already asked.

{% openapi-operation spec="dot-openapi" path="/api/agentic_with_history" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

Both take an optional `mode` — `economy`, `balanced` or `frontier` — the same dial as the [energy mode](../analyze.md#energy-modes) selector in the app. Left out, your workspace default applies.

To ask against an [environment](../environments.md) instead of production, send its id in the `X-Dot-Environment` header. That works on every endpoint on this page, not just these two.

The answer sits in the last message carrying a `formatted_result`: a list of parts, of which the `text` ones joined together are what a person reads. A long investigation can outlast the request, so fetch it later with `GET /api/c2/{chat_id}` using the same `chat_id`. There is a [worked example](use-cases-and-scripts.md) of both.



## Evaluate Dot from your Pipeline

Keep a set of questions whose answers you already know, and re-run them whenever the thing underneath changes — after a dbt run, before you promote an environment, or nightly. Dot answers each question for real and tells you which ones still come out right, so a definition that quietly drifted shows up in your pipeline instead of in someone's dashboard.

Questions live in **Model → Evaluation**. A question evaluates itself when you give it the query that produces the right answer and switch on **Auto-Evaluate**: Dot answers the question, runs both its own query and yours, and compares the results — numbers count as equal within the similarity set on the question, so a metric that is meant to move a little doesn't cry wolf. A question without a correct query still runs, but only a person can judge its answer; it comes back as `needs_review` rather than passing or failing.

### Start a run

Posting an empty body runs every evaluation question. Pass `question_ids` to run a subset — the metrics your change touched, say.

{% openapi-operation spec="dot-openapi" path="/api/run_questions" method="post" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

```bash
curl -X POST "https://{region}.getdot.ai/api/run_questions" \
     -H "API-KEY: dot-your_token_here" \
     -H "Content-Type: application/json" \
     -d '{}'
```

```json
{
  "batch_id": "batch-1f0c7d2e-…",
  "started": [
    { "question_id": "eq-…", "question_number": 1, "question_text": "How many orders were completed last month?", "run_id": "er-…" }
  ],
  "skipped": []
}
```

Keep the `batch_id`. A question that is already running is reported in `skipped` instead of being started twice, so `started` is exactly what this batch will report on — and if `started` comes back empty, nothing was queued and there is no batch to wait for.

### Wait for the verdicts

{% openapi-operation spec="dot-openapi" path="/api/eval_run" method="get" %}
[OpenAPI dot-openapi](https://test.getdot.ai/openapi.json)
{% endopenapi-operation %}

```bash
curl "https://{region}.getdot.ai/api/eval_run?batch_id=batch-1f0c7d2e-…" \
     -H "API-KEY: dot-your_token_here"
```

```json
{
  "finished": true,
  "summary": { "total": 12, "pass": 10, "fail": 1, "needs_review": 1, "error": 0, "pending": 0 },
  "results": [
    { "question_number": 1, "question_text": "How many orders were completed last month?",
      "verdict": "pass", "run_id": "er-…" },
    { "question_number": 2, "question_text": "What was revenue last month?",
      "verdict": "fail", "reason": "There are value differences in the data.", "run_id": "er-…" }
  ]
}
```

Poll until `finished` is `true`, then gate the build on `summary`: fail it when `fail` or `error` is above zero. Dot answers every question from scratch, so budget a couple of minutes per question and poll every 10–15 seconds.

Any verdict is one click from its evidence — open `https://{region}.getdot.ai/evaluation/question?c={run_id}` to see the answer Dot gave, the SQL it wrote, and the comparison against yours.

{% hint style="info" %}
Evaluation runs answer questions with the workspace's production model. To check a change before it reaches production, run the batch against the [environment](../environments.md) that holds it by sending its id in the `X-Dot-Environment` header.
{% endhint %}

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




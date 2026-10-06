---
description: >-
  Connect Dot to the dbt Semantic Layer so it answers with the metrics you
  define in dbt. Covers the service token, environment ID, and GraphQL URL.
---

# dbt Semantic Layer

Connect the dbt Semantic Layer and Dot answers questions with the metrics you define in dbt.

{% embed url="https://www.loom.com/share/4849e276a2f649a5b84538b062a33320?sid=dd7fa11e-a404-4274-a097-3045b65003f2" fullWidth="true" %}
Demo of Dot on dbt
{% endembed %}

{% hint style="info" %}
**Requirements**

* A **dbt platform** (formerly dbt Cloud) account on the Starter, Enterprise, or Enterprise+ plan. The free Developer plan doesn't include the Semantic Layer.
* Admin access in Dot.
* Admin access in dbt, so you can create service tokens.
* The Semantic Layer [set up in dbt](https://docs.getdbt.com/docs/use-dbt-semantic-layer/setup-sl), with a Semantic Layer credential.
{% endhint %}

## Create a service token

Create the token in your project's Semantic Layer settings. That links it to your Semantic Layer credential.

1. In dbt, click your account name in the left menu and select **Account settings**.
2. Click **Projects** and select your project.
3. In the **Semantic Layer** section, open **Credentials & service tokens**.
4. Under **Linked Service Tokens**, click **+ Add Service Token**.
5. Name the token, for example `Dot`.
6. Check that its permission sets are **Semantic Layer Only** and **Metadata Only**.
7. Click **Save**.
8. Copy the token. dbt shows it only once.

{% hint style="warning" %}
dbt runs each Semantic Layer query with the credential the token is linked to. If the token isn't linked to a credential, Dot's queries fail. A token you create on the **Service tokens** page is only linked if you map it to your Semantic Layer credential there.
{% endhint %}

## Get Environment ID

Dot needs the ID of the deployment environment you set up for the Semantic Layer.

1. In dbt, go to **Orchestration** > **Environments**.
2. Open that environment.
3. Copy the number at the end of the page URL. For example, if the URL ends in `/environments/12345`, the Environment ID is `12345`.

## Get Your GraphQL URL

Depending on where your dbt account is hosted, you need a different URL.

| Where dbt hosts your account | GraphQL URL |
| --- | --- |
| North America multi-tenant | `https://semantic-layer.cloud.getdbt.com/api/graphql` |
| EMEA multi-tenant | `https://semantic-layer.emea.dbt.com/api/graphql` |
| APAC multi-tenant | `https://semantic-layer.au.dbt.com/api/graphql` |
| Multi-cell | `https://ACCOUNT_PREFIX.semantic-layer.REGION.dbt.com/api/graphql` |
| Single tenant | `https://semantic-layer.YOUR_ACCESS_URL/api/graphql` |

If you open dbt at an address with an account prefix, such as `abc123.us1.dbt.com`, use the multi-cell pattern. For that address, the GraphQL URL is `https://abc123.semantic-layer.us1.dbt.com/api/graphql`. dbt also lists it under **Account settings** > **Account information**.

For single tenant, replace `YOUR_ACCESS_URL` with your access URL. For example, `abc123.getdbt.com` becomes `https://semantic-layer.abc123.getdbt.com/api/graphql`.

The GraphQL URL is optional in Dot. If you leave it blank, Dot uses the North America multi-tenant URL.

Here are the official docs on the different schema explorer/GraphQL URLs:

{% embed url="https://docs.getdbt.com/docs/dbt-apis/sl-graphql#dbt-semantic-layer-graphql-api" %}

## Connect in Dot

1. In Dot, go to **Settings** > **Connections**.
2. Under **Semantic Layers**, open **dbt**.
3. Enter the **Environment ID** and the **Token**.
4. Enter the **GraphQL URL**. You can leave it blank if your account is North America multi-tenant.
5. Click **Connect**.

Dot checks the connection, saves it, and syncs your metrics. If Dot answers "No metrics found", it did not save the connection. Check that the Environment ID belongs to the environment you set up for the Semantic Layer.

Dot doesn't sync the Semantic Layer again on its own. After you change metrics in dbt, run a job in the Semantic Layer environment. Then click **Sync** on the connection in Dot. To sync on a schedule, turn on **Schedule sync**.

## What Dot does with the Semantic Layer

* Each metric shows up in [Model](../../whats-dot/model/README.md) as a table named after the metric.
* The metric's dimensions and entities become the table's columns.
* Dot turns on new metrics automatically.
* Dot removes metrics you delete in dbt at the next sync.
* Dot reads each metric's label, tags, and `meta` from dbt's Discovery API. That's why the token needs **Metadata Only**.
* During a sync, Dot queries a few sample values for each dimension.
* To answer a question, Dot writes a Semantic Layer query. dbt runs it on your warehouse with the token's credential.

## Allow Dot IPs

If your organization uses a firewall to manage dbt access, Dot will only access your dbt account through the following IPs:

* `5.78.211.110`
* `178.105.217.177`

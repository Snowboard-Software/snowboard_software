---
description: Tell Dot about your most important metrics.
---

# dbt Semantic Layer

{% embed url="https://www.loom.com/share/4849e276a2f649a5b84538b062a33320?sid=dd7fa11e-a404-4274-a097-3045b65003f2" fullWidth="true" %}
Demo of Dot on dbt
{% endembed %}

To connect you need admin access to **dbt cloud** and you need to have [setup the semantic layer](https://docs.getdbt.com/docs/use-dbt-semantic-layer/quickstart-sl).

## Create API token

1. Go to ⚙️ | Accout Settings&#x20;

<figure><img src="../../.gitbook/assets/grafik (23).png" alt=""><figcaption></figcaption></figure>

2. Click on Service Tokens

<div align="center">

<figure><img src="../../.gitbook/assets/grafik (24).png" alt="" width="548"><figcaption></figcaption></figure>

</div>



3. Create new Token with permissions for `Semantic Layer` and `Metadata`&#x20;

<figure><img src="../../.gitbook/assets/grafik (25).png" alt=""><figcaption></figcaption></figure>

4. Copy and Save Generated Token

<figure><img src="../../.gitbook/assets/grafik (26).png" alt=""><figcaption></figcaption></figure>





## Get Environment ID

1. Go to Environments

<figure><img src="../../.gitbook/assets/grafik (27).png" alt=""><figcaption></figcaption></figure>



2. Click on your production environment and copy the last part of the url ( e.g. 12345)

<figure><img src="../../.gitbook/assets/grafik (28).png" alt=""><figcaption></figcaption></figure>



## Get Your GraphQL URL

\
Depending on where your dbt account is hosted, you need to obtain a different url.

Here are the official docs on the different schema explorer/Graph QL URLs

{% embed url="https://docs.getdbt.com/docs/dbt-cloud-apis/sl-graphql#dbt-semantic-layer-graphql-api" %}

Example: `https://semantic-layer.cloud.getdbt.com/api/graphql`

## Allow Dot IPs

If your organization uses a firewall to manage dbt access, Dot will only access your dbtthrough the following IPs:

* `3.229.110.216`
* `3.122.135.165`


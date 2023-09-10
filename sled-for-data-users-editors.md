---
description: >-
  Data professionals know dashboards are just the tip of the iceberg. For people
  who directly work with data, Sled is a powerful tool to find data, understand
  it, curate it and build trust.
---

# Sled for Data Users (Editors)

Editors can see the same things as Viewers (see [sled-for-business-users-viewer.md](sled-for-business-users-viewer.md "mention")) + more technical metadata + can edit almost everything.

## Find data

Discover data tables, business definitions or curated dashboards from the landing page.

<figure><img src=".gitbook/assets/grafik (16).png" alt=""><figcaption></figcaption></figure>

Data users can browse data by&#x20;

1\) Technical Tree Structure (left pane)

2\) Curated topics, e.g. for business domains or projects

3\) Searching for something specific and filtering by topic, objects type or object properties (e.g. if something contains PII information or data ownership)



## Understand Data

Get structured and high-quality meta data about your all the data in your Snowflake account, and quickly differentiate between your most used & most important assets and your other data.

<figure><img src=".gitbook/assets/grafik (12).png" alt=""><figcaption></figcaption></figure>

* **Documentation:** Each table has a page in the catalog, with a quick description and automatically assigned meta data. Complex or ambigious expressions are explained with Terms that quickly allow you to navigate to the definition or find other places, where `#orders` are used.
* **Column Profiles**: You can also drill deeper to the column-level to understand the shape and details of the data. Among other things, you can see column usage, completeness and how many unique values are stored.
* **Lineage:** Understand where data comes from, how it was created and where it is used down-stream. Read more about [lineage.md](lineage.md "mention")
* **Timeline**: shows updates and usage of this table over time

<figure><img src=".gitbook/assets/grafik (13).png" alt=""><figcaption></figcaption></figure>

## Build Data Products

Having a bunch of tables somewhere in your Snowflake account is not good enough to enable reliable and scalable business value. Successful data teams think of data with a product mindset.

A data product is a self-contained unit of data that serves a specific business or technical purpose. It is owned and managed by a cross-functional team that is responsible for its quality, reliability, and accessibility.

To enable that you can document, categorize, check and approve data in your Snowflake to become data products.&#x20;

### Document

Help data users (people or AI) to understand your data to create correct analytics.\
On the table level, we recommend to start each table description with this sentence:\
"_Each row represents ..._" e.g. an order in our online-shop.

```
Each row represents an order in our online-shop.
Each row represents a sales opportunity tracked in Salesforce.
Each row represents usage KPIs per customer and month.
```

For columns it's often good enough to give a busines label (e.g. Unique Customer ID) and write business formulas for KPIs (e.g. Number of Active Users / Number of Active Companies).

{% hint style="info" %}
Use the "AI describe" button to automatically use the power of LLMs to generate the documentation and only edit the suggestion.
{% endhint %}

Read more about [How to document data?](https://www.sled.so/blog/how-to-document-data)

### Categorize

While documentation is free text, you can use topics and properties to structure important metadata. It's always recommended to have a property called `owner`. But you could also classify the confidentially of your data, tag PII data or just assign all your data products to a domain topic like `finance`, `product` or `marketing`

{% hint style="info" %}
As a data engineer categorize your tables directly in Snowflake with [Object Tags](https://docs.snowflake.com/en/user-guide/object-tagging). They will get syned with Sled as properties or topics (click on "sync property values to topics" in Settings).
{% endhint %}

Use topics to cureate your data into categories you and your business users care about. They are displayed prominently on the landing page and easy to filter by.&#x20;

<figure><img src=".gitbook/assets/grafik (14).png" alt=""><figcaption></figcaption></figure>

### Check

Things break. That should be expected, but it's important that you know when it happens that everybody has transparency about the current quality of your data products.&#x20;

In [checks.md](checks.md "mention") you can easily enable no-code checks that control the basic data quality dimensions and allow you to define custom SQL checks (soon also AI generated) to test custom business logic.

### Approve

As soon as, you data is in a good shape, properly documented, categorized and checked, you can approve it, so that everybody knows they are can use it.&#x20;

<figure><img src=".gitbook/assets/grafik (15).png" alt="" width="291"><figcaption></figcaption></figure>

Approving things, makes them visible to viewers and promotes their position in Search and on the landing page.



That's it for know, if you are interested in more, please reach out to us. :)&#x20;

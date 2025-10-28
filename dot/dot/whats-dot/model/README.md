---
description: Train Dot on your data model, semantic layer, documentation, ...
---

# Model

Every good analysis is not just based on writing SQL, but on understanding how your business relates to the data you capture. The Model/Training space is for the data team to configure:

* Which data should Dot have access to?
* What does each table, column and row represent?
* What are existing analyses that can be build upon?



## Select Data&#x20;

**Datasource**\
Click on all the tables or explores that Dot will search through.

<figure><img src="../../../.gitbook/assets/grafik (14).png" alt="" width="257"><figcaption></figcaption></figure>



**Fields**

Select all fields in a datasource that Dot should know about.

<figure><img src="../../../.gitbook/assets/grafik (12).png" alt=""><figcaption></figcaption></figure>

## **Describe Data**

You can click suggest to automatically generate documentation and fetch sample values.

<figure><img src="../../../.gitbook/assets/Recording 2023-05-17 at 14.12.36 (1).gif" alt=""><figcaption></figcaption></figure>

Make sure to save the changes you made. ⬆️



## Provide Example Questions + Answers

_Giving example questions to Dot helps to get consistent and validated answers from Dot._

Depending on your data model, there are multiple ways to answer a question.

E.g. _How was our shop performance in the last 10 weeks?_\
Without more context there are many ways to answer this question.

The Questions section in Dot gives data teams a chance to build a collection of questions and answers that Dot will reuse.

<figure><img src="../../../.gitbook/assets/grafik (19).png" alt=""><figcaption><p>Calculates revenue and number of customers over time to answer question.</p></figcaption></figure>





## Define Relationships / Joins

Joining data across different tables is really powerful because it allows us to answer much more broad questions about our business. However, joining data correctly is requires a good understanding of the relationships between your tables.

To ensure Dot avoid join [fan-outs or the chasm trap](https://chat.openai.com/share/790888e3-3ff5-4004-9b58-e04947322757), you can predefine relationships.&#x20;

For each table, you would specify the foreign key references.&#x20;

Note:&#x20;

* a foreign key can be composed key, consisting of multiple columns
* foreign keys should usually refer to primary or natural keys

**Example**

<figure><img src="../../../.gitbook/assets/grafik (32).png" alt=""><figcaption></figcaption></figure>

Given the data model above, you want to define 2 Relationships:

* For Orders
  * Foreign Key: `user_id`
  * Referenced Table: `Users`
  * Referenced Keys: `id`
* For OrderItems
  * Foreign Key: `order_id`
  * Referenced Table: `Orders`
  * Referenced Keys: `id`


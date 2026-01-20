---
description: Train Dot on your data model, semantic layer, documentation, ...
---

# Model

Every good analysis is not just based on writing SQL, but on understanding how your business relates to the data you capture. The Model/Training space is for the data team to configure:

* Which data should Dot have access to?
* What does each table, column and row represent?
* What are existing analyses that can be build upon?



## Select Data 

**Datasource**\
Click on all the tables or explores that Dot will search through.

<figure><img src="../../../.gitbook/assets/grafik (14).png" alt="" width="257"><figcaption></figcaption></figure>



**Fields**

Select all fields in a datasource that Dot should know about.

<figure><img src="../../../.gitbook/assets/grafik (12).png" alt=""><figcaption></figcaption></figure>

## **Describe Data**

You can click suggest to automatically generate documentation and fetch sample values. Make sure to save your changes.




## Define Relationships / Joins

Joining data across different tables is really powerful because it allows us to answer much more broad questions about our business. However, joining data correctly is requires a good understanding of the relationships between your tables.

To ensure Dot avoid join [fan-outs or the chasm trap](https://chat.openai.com/share/790888e3-3ff5-4004-9b58-e04947322757), you can predefine relationships. 

For each table, you would specify the foreign key references. 

Note: 

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


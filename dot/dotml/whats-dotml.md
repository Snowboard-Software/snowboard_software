---
description: A minimal semantic layer for consistent analytics
hidden: true
---

# What's DotML?

DotML stands for _Dot Markup Language_; it's the language that is used to create semantic data models. You can use DotML to describe dimensions, aggregates, calculations, and data relationships in your SQL database

\
For data engineers, DotML enables consistency, meaning you write SQL expressions _once, in one place,_ and DotML uses the code repeatedly to generate ad hoc SQL queries. Business users can then use the results to query important data, focusing only on the content they need, not the complexities of SQL structure.

> DotML is similar to HTML (HyperText Markup Language), but it's for data.&#x20;
>
> While HTML defines how content is structured for consistent display,&#x20;
>
> DotML defines how data is queried for consistent calculations.

## Why do we need a semantic layer?

1. **To get trustworthy and consistent results in analytics**
2. To save engineering time, following the DRY (don't repeat yourself) principle
3. To preserve important business logic in a central place

## Elements

<figure><img src="../.gitbook/assets/grafik (21).png" alt=""><figcaption><p>diagram about main elements in DotML</p></figcaption></figure>

**Cube:** a cube is based on one table and defines how metrics and dimensions are calculated. The main difference between a flat table and a cube is the ability to query metrics dynamically (e.g. conversion rate by month, week, day, ...).

**Dimension**: A characteristic or attribute of your data. Examples include customer ID, product name, or date. It's usually a column in your database. Dimensions are what you use to segment your data.

**Metric**: A calculation based on your dimensions. Examples include sum of sales, average order value, or count of users. Metrics are values you want to analyze.

**Join**: The action of linking two or more cubes based on a related column between them. This lets you combine data from different tables for more comprehensive analysis.



## Query Flow

<figure><img src="../.gitbook/assets/grafik (22).png" alt=""><figcaption><p>a semantic query gets compiled to a SQL query based on the business logic defined in cubes.yaml</p></figcaption></figure>

Technically, the DotML layer is a configuration file (e.g. cubes.yaml) that is typically version-controlled through a Git repository. The cubes file contains information about which tables will be used and how the tables should be joined. It also describes how information is calculated about each table (or across multiple tables if the joins permit this).

DotML separates structure from content, so the query structure (how tables are joined) is independent of the query content (the columns to access, derived fields, aggregate functions to compute, and filtering expressions to apply).


---
description: the core of your semantic layer for trustworthy analytics
hidden: true
---

# Define Metrics & Dimensions

[Read here](whats-dotml.md), why you need them.

## Dimensions

A characteristic or attribute of your data. Examples include customer ID, product name, or date. It's usually a column in your database. Dimensions are what you use to segment your data.

They are defined in the `dimensions` section of a cube

```yaml
dimensions:
  - name: short_id
    label: Short Identifier
    sql: SUBSTRING(${table}._AIRBYTE_ORDERS_HASHID, 8)
  - name: status
    label: Order Status
    sql: ${table}.STATUS
  - name: payment_method
    label: Payment Method
    sql: ${table}.PAYMENT_METHOD
  - name: date
    label: Payment Date
    sql: date_trunc(${time_frame},${table}.DATE_CREATED)
    variants:
      - time_frame: [day, week, month, quarter, year]

```

In the example above we defined 4 dimensions:

* Short Identifier: is a calculated dimension, where we take a part of the column `_AIRBYTE_ORDERS_HASHID`
* Status, Payment Method: are just passed directly and only labelled more user friendly
* Date: is also a calculated dimension, but with a variant variable `time_frame` that will create multiple variations: `date_day, date_week, date_month, date_quarter, date_year`. This allows the end user to query multiple the data in different granularities

### Variants

Variants allow us to keep the semantic layer DRY and easy to read.\
We can either just have a list of values like above:

<pre class="language-yaml"><code class="lang-yaml">- name: date
<strong>  sql: date_trunc(${time_frame},${table}.DATE_CREATED)
</strong>  variants:
  - time_frame: [day, week, month, quarter, year]
</code></pre>

or we specify key value pairs, if we want to pass more complex values along, but keep the created fields clean (`date_day, date_month, date_year`):

<pre class="language-yaml"><code class="lang-yaml">- name: date
<strong>  sql: date_trunc(${time_frame},${table}.DATE_CREATED)
</strong><strong>  variants:
</strong>    - time_frame:
        - day: "%Y-%m-%d"
        - month: "%Y-%m-01"
        - year: "%Y-01-01"
</code></pre>



## Metrics

A calculation based on your dimensions. Examples include sum of sales, average order value, or count of users. Measures are values you want to analyze.

They are defined in the `metrics` section of a cube.

```yaml
metrics:
  - name: total_revenue
    label: Total Revenue
    sql: sum(${table}.TOTAL)
  - name: average_order_value
    label: Average Order Value
    sql: avg(${table}.TOTAL)
  - name: number_of_orders
    label: Number of Orders
    sql: count(${table}._AIRBYTE_ORDERS_HASHID)
  - name: distinct_customers
    label: Number of Customers
    sql: count(distinct ${table}.CUSTOMER_ID)
  - name: orders_over_customers
    label: Ratio of Orders per Customer
    sql:  ${number_of_orders} / ${distinct_customers}
  - name: orders_credit_card
    label: Amount of Orders with Credit Card
    sql: count(case when ${table}.PAYMENT_METHOD = 'credit_card' then 1 else null end)
  - name: revenue_credit_card
    label: Revenue from Credit Card Payments
    sql: sum( case when ${table}.PAYMENT_METHOD = 'credit_card' then ${table}.TOTAL else 0 end )
```

In the example above we defined 7 metrics:

* Total Revenue: is a sum of the column `TOTAL`
* Average Order Value: is the average of the column `TOTAL`
* Number of Orders: counts unique transaction ids
* Number of Customers: counts unique customer ids
* Ratio of Orders per Customer: is a metric **composed** of the two previous metrics
* Amount of Orders with Credit Card: counts orders whose payment method is `credit_card`
* Revenue from Credit Card Payments: sum up `TOTAL` of orders whose payment method is `credit_card`

## SQL Notation and ${placeholder}

DotML is database agnostic, which means you can write any SQL expressions you want for your database. If you database supports something cool like `Correlation(col1, col2)` DotML also supports it.

The placeholder notation `${placeholder}` allows DotML to dynamically generate the correct SQL statement or to reuse existing dimensions and metrics in other definitions. \
There are 3 different placeholders:

* `${table}.column_name` for correctly identifying a column name in the base table
* `${dimension_name}` or `${metric_name}` for reusing an existing definition
* `${variant_name}` for configuring the substitution place of the variants

It's like specifying a template that gets filled with the correct value at runtime.


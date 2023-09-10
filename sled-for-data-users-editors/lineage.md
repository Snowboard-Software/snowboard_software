# Lineage and Data Flows

The lineage section for an asset shows how data is transformed and used across different assets. It can show e.g. how multiple source tables are joined to create a core table that is then used by multiple BI reports.

## Interpretation

Each box represents an assets (e.g. a table, view or report) and each arrow represents a data flow (e.g. transformation or consumption). A box with a solid border is a persisted asset (e.g. table), while a dashed border is a virtual asset (e.g. view). Boxes are color coded based on the schema they are a part of. Arrows that are transformations can be clicked to show more information about the SQL statement that defines the data flow. Gray arrows are past transformations, while a black arrow is a data flow that ran in the last 24 hours.

## Use Cases

### Impact Analysis

Understanding all downstream dependencies before making a change can help avoid corrupting assets downstream.

### Refactoring Data Debt

A high-level view of data pipelines can help see anti-patterns, e.g.:

* Identify duplicated data assets: often core tables are used to create derived data sets that are redundant. Combining derived assets aligns data quality efforts and boosts productivity
* Spot circular data flows: a circle happens if a data asset is computed from another asset that uses information from the original asset. This setup leads to complicated update logic that easily leads to data inconsistencies.
* Understand if data flows follow your architecture guidelines. E.g.: a good practice is to create marts for data consumers. These marts should not contain heavy data pipelines.



## Field / Column Lineage

A deeper level than table to dashboard lineage is field lineage, where a user can track where a single column was coming from, how it was transformed and where it is used downstream.



## Background

Every interaction with data in Snowflake happens with SQL queries, e.g.:

```sql
CREATE TABLE orders AS
    SELECT *
    FROM raw_orders
    WHERE status != 'canceled'
```

Snowboard parses statements like these to analyze data flows and connects `raw_orders` with `orders` in the lineage graph.

## Limitations

**General**

* Data transformations that happen outside of Snowflake are not captured. E.g. a python script that pulls data from view `customers`, enriches the data and writes it back to another table `customers_enriched`. In this case no sql statement is used and no connection will be shown.
* Both target and source table need to be indexed in Snowboard. E.g. if the Snowboard user does not have privileges to access the source table `raw_orders`. Snowboard will ignore the connection with `orders` until it gets privileges to access `raw_orders`.

**Column Lineage**

* Transformations that are based on views and use `alias.*` notation in the select statement are currently not supported.
* Transformationas that happen in UDTF (user defined table functions) are currently not analyzed
* Multistep table creation with temporary tables is not analyzed for column lineage
* Column expressions longer than 500 characters can show incomplete lineage


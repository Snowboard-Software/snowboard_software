# Welcome to Snowboard

Snowboard helps you to find, understand and trust your analytics. We build it for the Snowflake data cloud, because we believe deep integration enables better workflows and allows us to double down on hard platform specific challenges.&#x20;

Snowboard has two engines: one for metadata, one for metrics. Both work hand in hand to make your analytics scalable and trustworthy.&#x20;

**Data Catalog and Observability - it's meta data management!**

* Search everything, from columns in Snowflake to dashboards in Tableau
* Discover and observe your data with data profiles
* Document your data and visualization assets
* Understand data flows down to to the column level (Lineage)
* View access rights and manage ownership of your assets

**Metric Store - Define once, use everywhere. **

* All Calculations should live in one place, your data warehouse.&#x20;
* Define metrics once and consume them with SQL in any other tool.&#x20;
* Discover and document your metrics in the catalog.&#x20;

****

![](.gitbook/assets/overview\_architecture.png)

Snowboard connects directly with your cloud data warehouse. It needs access to the system database and tables of the warehouse (e.g. in `SNOWFLAKE.ACCOUNT_USAGE`). The metadata engine also connects to dbt cloud, Tableau cloud and PowerBI.&#x20;


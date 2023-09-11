# Background Tasks for Snowflake

These background tasks can run on a schedule.

## Discover Tables

This task should run often as it refreshes the meta data of your tables (e.g. every hour). It does not start a warehouse. It discovers tables, views, external tables and materialized views.

## Parse Query Log

This task also starts a warehouse. Running it every 8 hours or daily is a good default. The query parser is responsible for the timeline, usage statistics and lineage. If your query history is really big this can take some time to complete. This task also extracts information from other system tables that track e.g. how often materialized views get updated.&#x20;

## Sync Meta Data to Snowflake

This task starts a warehouse. Running it daily is a good default. This job writes back important meta data to Snowflake. Which enables you to create custom analysis on top of your meta data. It also writes back user activity data to track how useful Sled is in your organization.&#x20;

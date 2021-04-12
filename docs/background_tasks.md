Background Tasks for Snowflake 
===========

There are three background tasks that can run on a schedule.

## Discover Tables
This task should run often as it refreshes the meta data of your tables (e.g. every hour). It does not start a warehouse. 
It discovers tables, views, external tables and materialized views. 


## Profile Data
The data profiler is the most expensive task. It's usually enough to run it daily or even weekly.
It generates a sample of 100k rows for every table or view, computes data quality metrics and the data profiles.
If it can not compute a profile for a view within 5 minutes it will stop. 
The sampler is super fast, even for big tables (TBs) the calculation usually completes within 5 minutes.

## Parse Query Log
This task also starts a warehouse. Running it every 8 hours or daily is a good default. 
The query parser is responsible for the timeline, usage statistics and lineage. 
If your query history is really big this can take some time to complete.


Configure Paths for Background Tasks
===========

Paths define which tables and views the discovery task or profiler task should work on.
All paths need to be valid [regular expressions](https://docs.python.org/3.8/library/re.html#regular-expression-syntax).
The regex is not case sensitive. [(see examples)](#Examples)



## Discovery Paths
This controls, which objects should be available in the catalog and for the other tasks.

### include
These data objects (databases, schemas, tables, views) will be indexed for the catalog.
`<Empty>` includes everything.
If multiple paths are specified, all of them are searched. Overlapping paths will only be indexed once.  

### exclude
These objects are excluded from the catalog. 
`<Empty>` excludes nothing.

An object in the excluded paths will always be excluded (even if it was included above).


## Profile Paths
This controls, which objects shall be profiled by the scheduler. 

### include
These data objects (databases, schemas, tables, views) will be profiled.
`<Empty>` includes everything.
If multiple paths are specified, all of them are profiled. Overlapping paths will only be profiled once.  

### exclude
These objects are not profiled. 
`<Empty>` excludes nothing.
**💡 You should specify calculation-heavy views or views that rely on streams here.**
The profiler is a DML statement as it stores the results on Snowflake. Therefore it could consume the stream.

An object in the excluded paths will always be excluded (even if it was included above).


## Examples

### Match all tables or views of a database
```regexp
demo_db\..*
```
This would match all objects that start with `DEMO_DB.`. 
Please note that the `.`(dot) needs to be escaped otherwise it matches every character.

### Match all tables or views with certain names
Match all tables or views of a schema that start with `my_` and end with `deprecated`
```regexp
my_database\.with_schema\.my_.*deprecated
```
It would match e.g. `MY_DATABASE.WITH_SCHEMA.my_temporary_table_deprecated`.

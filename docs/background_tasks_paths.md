Configure Paths for Background Tasks
===========

Paths define which tables and views the discovery task or profiler task should work on.
All paths need to be valid [regular expressions](https://docs.python.org/3.8/library/re.html#regular-expression-syntax).
The regex is not case sensitive. [(see examples)](#examples)



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
```text
demo_db\..*
```
This would match all objects that start with `DEMO_DB.`. 
Please note that the `.`(dot) needs to be escaped otherwise it matches every character.

### Match all tables or views with certain names
Match all tables or views of a schema that start with `my_` and end with `deprecated`
```text
my_database\.with_schema\.my_.*deprecated
```
It would match e.g. `MY_DATABASE.WITH_SCHEMA.my_temporary_table_deprecated`.

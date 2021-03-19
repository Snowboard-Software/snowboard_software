Connect with Snowflake 
===========
***~ 15 min to complete***

You need an `ACCOUNTADMIN` user to follow this guide. 

## Create a Role and a User
This creates a dedicated role and technical user. Replace `example_wh` with your preferred warehouse. 
`XS` is enough for most installations. It is ok to share this warehouse with other workloads to save costs. 
**Set a secure password.**
```sql
create role snowboard_role;
create user snowboard_user
    --specify your own password and remember it for later
    password = '<something secret>' 
    --specify your warehouse
    default_warehouse = example_wh 
    default_role = snowboard_role
    default_namespace = snowboard
    comment = 'Technical User for Snowboard Data Catalog 🏂';

--allow usage of your warehouse
grant usage on warehouse example_wh to role snowboard_role;
```

## Create the Snowboard Database
This database will be used to store profiling results and the parsed query log. You can also easily access it.
Data ownership is great.
```sql
create database snowboard;
grant ownership on database snowboard to role snowboard_role;
```

## Grants Read Access to Data
For each database or schema that should be added to the data catalog execute these statements.
Replace `example_db` with the correct name.
```mysql
set db_name = 'example_db';
grant usage on database identifier($db_name) to role snowboard_role;
grant usage on all schemas in database identifier($db_name) to role snowboard_role;
grant usage on future schemas in database identifier($db_name) to role snowboard_role;
grant select, references on all tables in database identifier($db_name) to role snowboard_role;
grant select, references on future tables in database identifier($db_name) to role snowboard_role;
grant select, references on all views in database identifier($db_name) to role snowboard_role;
grant select, references on future views in database identifier($db_name) to role snowboard_role;
```

For shared databases the following statement is enough. Replace `external_db` with the correct name.
```sql
grant imported privileges on database external_db to role snowboard_role;
```

## Grants Read Access to Account Information
Grant access to the query log and further meta data from Snowflake.
```sql
grant imported privileges on database snowflake to role snowboard_role;
```

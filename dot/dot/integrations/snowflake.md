# Snowflake

## Create a Role and a User

This creates a dedicated role and technical user. Replace `example_wh` with your preferred warehouse. `XS` is enough for most installations. It is ok to share this warehouse with other workloads to save costs. **Set a secure password.**

```sql
create role dot_role;
create user dot_user
    password = '<something secret>' -- remember that!
    default_warehouse = example_wh  -- specify your warehouse
    default_role = dot_role;
grant role dot_role to user dot_user;

--allow usage of your warehouse
grant usage on warehouse example_wh to role dot_role;
```



## Grants Read Access to Data

It is recommended to grant permissions only to schemas or tables your end-users should have access to. This is usually a schema with core or reporting tables.

```sql
-- gives access to all objects in a schema 
set db_name = 'example_db'; -- specify name of database 
set schema_name = 'example_schema'; -- specify name of schema 
set db_schema_name = $db_name || '.' || $schema_name; 

grant usage on database identifier($db_name) to role dot_role; 
grant usage on schema identifier($db_schema_name) to role dot_role; 
grant select on all tables in schema identifier($db_schema_name) to role dot_role; 
grant select on future tables in schema identifier($db_schema_name) to role dot_role; 
grant select on all views in schema identifier($db_schema_name) to role dot_role; 
grant select on future views in schema identifier($db_schema_name) to role dot_role; 
grant select on all materialized views in schema identifier($db_schema_name) to role dot_role; 
grant select on future materialized views in schema identifier($db_schema_name) to role dot_role;
```



For shared databases the following statement is enough.&#x20;

```sql
grant imported privileges on database shared_external_db to role dot_role;
```

## Grants Read Access to Account Information (optional)

Grant access to the query history from Snowflake.

```sql
grant imported privileges on database snowflake to role dot_role;
```

## Allow Dot IPs

If your organization uses a network policy to manage Snowflake access, Dot will only access your Snowflake through the following IPs:

* `3.229.110.216`
* `3.122.135.165`\

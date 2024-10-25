# Postgres

## Create a Group and a User

As a super user, execute the following SQL commands to create a group, a user assigned to that group, and permissions to access a system table.

```sql
CREATE USER dot_user PASSWORD '<something secret>';

CREATE GROUP dot_group;

ALTER GROUP dot_group ADD USER dot_user;

-- Grant Postgres' monitor role for meta data
GRANT pg_monitor TO dot_group
```



## Grants Read Access to Data

Then for each schema `schema`, execute the following three commands to grant read-only access.

```sql
-- Grant usage on schema and select on current and future child tables
GRANT USAGE ON SCHEMA "schema" TO GROUP dot_group;
GRANT SELECT ON ALL TABLES IN SCHEMA "schema" TO GROUP dot_group;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schema" GRANT SELECT ON TABLES TO GROUP dot_group;
```



**Note**: to programmatically generate these three queries for all schemas, you can use the following command. These commands still need to be executed.

```sql
SELECT 
    'GRANT USAGE ON SCHEMA "' || schema_name || '" TO GROUP dot_group;' || '\n' ||
    'GRANT SELECT ON ALL TABLES IN SCHEMA "' || schema_name || '" TO GROUP dot_group;' || '\n' ||
    'ALTER DEFAULT PRIVILEGES IN SCHEMA "' || schema_name || '" GRANT SELECT ON TABLES TO GROUP dot_group;' AS single_schema_statement
FROM svv_all_schemas
WHERE schema_name not in ('information_schema', 'pg_catalog', 'pg_internal');
```

## Allow Dot IPs

If your organization uses a firewall to manage Postgres access, Dot will only access your Postgres through the following IPs:

* `3.229.110.216`
* `3.122.135.165`

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



For shared databases the following statement is enough. 

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

* `5.78.211.110`
* `178.105.217.177`<br>


## Sync Snowflake Roles (optional)

Snowflake can stay the single source of truth for who sees what. The Snowflake connection has two role-sync toggles (both off by default, under **Settings → Connections → Snowflake**):

### Sync Snowflake Roles — tables

On every sync, each table is tagged with the Snowflake roles that can `SELECT` it (from `SHOW GRANTS`), as Dot groups. Only users in a matching group can see and query the table through Dot.

Note: this overwrites the table's existing groups on every sync — Snowflake owns table access from then on.

### Sync Snowflake Roles to Users

The counterpart for people: on every sync, Snowflake users are matched to Dot users by email (the user's `email` or `login_name`), and their granted roles are assigned as Dot groups — using the same group names as the table side, so role-gated tables and role-granted users line up automatically. When someone changes teams in Snowflake, their Dot access follows on the next sync.

* Groups assigned by the sync are tracked separately: a revoked Snowflake role is removed again, while groups you assigned manually in Dot are never touched.
* Disabled Snowflake users are skipped.

Listing users requires extra visibility for the connection role:

```sql
grant manage grants on account to role dot_role;
```

Without it, the user sync skips safely (with a hint in the sync log) and no user is modified — table syncing is unaffected.

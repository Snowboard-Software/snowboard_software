# Redshift

## Create a Group and a User

As a super user, execute the following SQL commands to create a group, a user assigned to that group, and permissions to access a system table.

```sql
CREATE USER dot_user PASSWORD '<something secret>' SYSLOG ACCESS UNRESTRICTED;
ALTER USER dot_user SYSLOG ACCESS UNRESTRICTED;

CREATE GROUP dot_group;

ALTER GROUP dot_group ADD USER dot_user;

-- Grant select to system table for meta data
GRANT SELECT ON svv_table_info TO GROUP dot_group;
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

If your organization uses a network policy to manage Redshift access, Dot will only access your Redshift through the following IPs:

* `3.229.110.216`
* `3.122.135.165`

1. In the Redshift dashboard, **click on the desired cluster name**.

<div align="left"><figure><img src="https://files.readme.io/39a5a42-1.png" alt="" width="375"><figcaption></figcaption></figure></div>

2. When viewing information for your Redshift cluster, click the **Properties** tab.

![1918](https://files.readme.io/fcb267a-2.png)

3. Scroll down to the **Network and security settings** section.

![1918](https://files.readme.io/7ed17e1-Screen_Shot_2021-04-19_at_3.13.51_PM.png)

4. If **Public Accessibility** is not enabled, click **Edit publicly accessible** button then enable.

![1914](https://files.readme.io/a7472c2-4.png)![1918](https://files.readme.io/a18855d-3_-_publicly_accessible.png)

5. Click **VPC security group link**.

![1918](https://files.readme.io/c321c34-3.png)

6. Click **Edit inbound rules**.

![1918](https://files.readme.io/fcced0a-5.png)

7. Add the following IPs of Type `Redshift`:

* `3.229.110.216`
* `3.122.135.165`

![](<../../.gitbook/assets/image (1) (1) (1) (1) (1).png>)\



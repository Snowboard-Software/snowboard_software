# Microsoft SQL Server

## **Create a Login and a User**

To set up access in SQL Server, one would create a login at the server level and then a user at the database level linked to that login. Below is an equivalent SQL Server script:

```sql
-- Replace placeholder values (YourDatabaseName, YourSchemaName, and <something secret>) 
-- with your actual values.

-- Create server-level login
CREATE LOGIN dot_login WITH PASSWORD = '<something secret>';

-- Use the desired database
USE YourDatabaseName;

-- Create database-level user linked to the server login
CREATE USER dot_user FOR LOGIN dot_login;

-- Add user to a role (for demonstration purposes, using db_datareader which gives read-only access)
ALTER ROLE db_datareader ADD MEMBER dot_user;

```

## **Grants Read Access to Data**

In SQL Server, the **`db_datareader`** role grants read-only access to all current and future tables in the database. If you've added the user to this role, you don't need to do schema-specific grants. However, if you wish to grant read access only on specific schemas:

```sql
-- Grant select on all current tables in a schema
GRANT SELECT ON SCHEMA::YourSchemaName TO dot_user;

-- Note: SQL Server does not support the concept of default privileges.
-- Any new tables or views would need permissions assigned explicitly.

```

## **Allow Dot IPs** 

If you are using SQL Server's firewall features or another firewall mechanism to control access, ensure that you whitelist the following IPs to allow Dot to access your SQL Server:

* 3.229.110.216
* 3.122.135.165


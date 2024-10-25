# Vertica (soon)

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

To use the Vertica as a data source, you'll need:

* A Vertica server version 10.0 or above

Dot only supports connecting to your Vertica instances with SSL or TLS encryption. TLS is used by default. You'll need the following information to configure the Vertica destination:

* **Host** - The host name of the server.
* **Port** - Defaults to the VSQL™ standard port number (5433).
* **Username**
* **Password**
* **Default Schema Name** - Specify the schema (or several schemas separated by commas) to be set in the search-path. These schemas will be used to resolve unqualified object names used in statements executed over this connection.
* **Database** - The database name. The default is to connect to a database with the same name as the user name.



## Create a Role and a User

As a super user, execute the following SQL commands to create a group, a user assigned to that group, and permissions to access a system table.

```sql
-- Create a User
CREATE USER dot_user IDENTIFIED BY '<something secret>';

-- Create a Role (Vertica doesn't have groups, but uses roles instead)
CREATE ROLE dot_group;

-- Grant the role to the user
GRANT dot_group TO dot_user;
```



## Grants Read Access to Data

Then for each schema `schema`, execute the following commands to grant read-only access.

```sql
-- Grant usage on schema and select on current and future child tables
GRANT USAGE ON SCHEMA "schema" TO dot_group;
GRANT SELECT ON ALL TABLES IN SCHEMA "schema" TO dot_group;
```



## Allow Dot IPs

If your organization uses a firewall to manage Postgres access, Dot will only access your Postgres through the following IPs:

* `3.229.110.216`
* `3.122.135.165`

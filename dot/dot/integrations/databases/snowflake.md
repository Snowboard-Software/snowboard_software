---
description: Connect Dot to Snowflake with a service user that signs in with a key pair.
---

# Snowflake

Dot connects to Snowflake as a service user that signs in with a key pair. You need to be an admin in Dot to add the connection.

Run the SQL on this page in Snowflake with a role that can create users and grant privileges, like `SECURITYADMIN`.

## Create a Role and a Service User

This creates a dedicated role and a service user. Replace `example_wh` with your preferred warehouse. `XS` is enough for most installations. It is ok to share this warehouse with other workloads to save costs.

```sql
create role dot_role;
create user dot_user
    type = service
    default_warehouse = example_wh  -- specify your warehouse
    default_role = dot_role;
grant role dot_role to user dot_user;

--allow usage of your warehouse
grant usage on warehouse example_wh to role dot_role;
```

`type = service` tells Snowflake that `dot_user` is an application, not a person. A service user can't sign in with a password, and Snowflake never asks it for a second factor.

Don't grant `dot_user` any other role. Snowflake activates all of a user's roles by default, so another role could widen what Dot can query.

## Create a Key Pair

Dot signs in with a private key. Snowflake checks it against the public key you assign to `dot_user`. These steps follow Snowflake's [key-pair authentication guide](https://docs.snowflake.com/en/user-guide/key-pair-auth).

1.  Create an encrypted private key. OpenSSL asks you to choose a passphrase.

    ```bash
    openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 aes-256-cbc -inform PEM -out rsa_key.p8
    ```
2.  Create the public key from it. OpenSSL asks for the passphrase again.

    ```bash
    openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
    ```
3.  Print the public key on one line, without its `BEGIN` and `END` lines.

    ```bash
    grep -v "PUBLIC KEY" rsa_key.pub | tr -d '\n'
    ```
4.  Assign the public key to `dot_user` in Snowflake.

    ```sql
    alter user dot_user set rsa_public_key = 'MIIBIjANBgkqh...'; -- paste your one-line public key
    ```

Keep `rsa_key.p8` and its passphrase somewhere safe, like a password manager. Anyone who has both can sign in as `dot_user`.

## Grant Read Access to Data

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

## Grant Read Access to Query History (optional)

Dot can read the last 7 days of your account's query history. It uses it to find the tables and columns your team queries most, and to pick example queries for your tables. Dot works without it.

Query history holds the text of every query run in your account. To share it with Dot, run this as `ACCOUNTADMIN`:

```sql
grant database role snowflake.governance_viewer to role dot_role;
```

This database role lets `dot_role` read Snowflake's governance views, including `ACCESS_HISTORY` and `QUERY_HISTORY` in `SNOWFLAKE.ACCOUNT_USAGE`.

## Allow Dot IPs

If your organization uses a network policy to manage Snowflake access, Dot will only access your Snowflake through the following IPs:

* `5.78.211.110`
* `178.105.217.177`

## Connect in Dot

1. Go to **Settings → Connections**.
2. Under **Databases**, open **Snowflake**.
3. In **Account Identifier**, enter your account identifier, like `myorg-myaccount`. To look it up, run `SELECT CURRENT_ORGANIZATION_NAME() || '-' || CURRENT_ACCOUNT_NAME();` in Snowflake.
4. In **Username**, enter `dot_user`.
5. Turn on **Key-pair**.
6. In **Private Key**, paste the whole contents of `rsa_key.p8`, including the `-----BEGIN` and `-----END` lines.
7. In **Passphrase**, enter the key's passphrase. If your key has no passphrase, leave the field empty.
8. In **Role**, enter `dot_role`.
9. In **Warehouse**, enter your warehouse, like `example_wh`.
10. Click **Connect**.

Dot checks that it can see the warehouse, saves the connection, and starts a sync. After the sync, pick the tables Dot should use in [Model](../../whats-dot/model/README.md).

If Dot says the warehouse was not found, check the name and that `dot_role` has `usage` on it.

## Sign In with a Password

Snowflake is phasing out sign-ins that use only a password. Use a key pair instead.

* A service user, like the one above, can't sign in with a password.
* Between August and October 2026, Snowflake blocks passwords for all service users, including `LEGACY_SERVICE` users. It also requires a second factor for every person who signs in with a password.
* Dot can't answer a second factor. Once Snowflake enforces this in your account, a password connection stops working.

Snowflake enforces this account by account and tells you the date for yours. Trial accounts are exempt. See [Snowflake's timeline](https://docs.snowflake.com/en/user-guide/security-mfa-rollout).

If you have to use the **Password** field, paste a [programmatic access token](https://docs.snowflake.com/en/user-guide/programmatic-access-tokens) instead of a password. Snowflake accepts a token in place of a password. By default, it only accepts a service user's token when the user has a network policy, so allow Dot's IPs in that policy. A token expires after 15 days by default. You can choose up to 365 days. Paste a new one in Dot before it expires.

## Sync Snowflake Roles

{% hint style="warning" %}
Snowflake role sync is being fixed. Keep **Sync Snowflake Roles** and **Sync Snowflake Roles to Users** off for now. To control who can query a table, use [groups in Dot](../../whats-dot/permissions.md#data-access-control).
{% endhint %}

## Internal Marketplace (optional)

If your Snowflake organization publishes data products internally, Dot can list them and search them alongside your other tables.

Turn on **Internal Marketplace** under **Settings → Connections → Snowflake**. It is off by default. Turning it on also switches on the Snowflake Marketplace skill under **Settings → Skills**.

Dot reads the organizational listings your connection's role can see, and refreshes them every time the connection syncs. If that refresh fails, the rest of the sync still finishes and the sync log says what went wrong.

Dot only reads the catalog. Mounting a listing's data, and granting your Dot role access to it, still happens in Snowflake.

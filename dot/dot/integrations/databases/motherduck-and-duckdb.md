---
description: Connect Dot to MotherDuck with an access token and ask questions about your data in plain language.
---

# MotherDuck & DuckDB

## MotherDuck

Dot connects to MotherDuck with a connection string that holds an access token. You need to be an admin in Dot to add the connection.

### Create a token for Dot

1. Open the [MotherDuck UI](https://app.motherduck.com).
2. Click your organization name in the top left, then click **Settings**.
3. Click **+ Create token** and give it a name you will recognize, like `Dot`.
4. Create the token and copy it.

A token only for Dot lets you revoke Dot's access without affecting anything else.

### Build the connection string

The connection string follows this pattern:

`md:<database_name>?motherduck_token=<your_token>`

For example: `md:sample_data?motherduck_token=eyABC...`

The connection string contains your token. Treat it like a password.

### Connect in Dot

1. Go to **Settings → Connections**.
2. Under **Databases**, open **DuckDB / MotherDuck**.
3. Paste the connection string into **Database Location**.
4. Optional: in **Databases**, list the databases Dot should sync, separated by commas. One token can see every database in your MotherDuck workspace. Leave the field empty to sync all of them.
5. Optional: in **Schemas**, list the schemas Dot should sync, separated by commas. Leave the field empty to sync every schema.
6. Click **Connect**.

Dot checks the connection, saves it, and starts a sync. The sync reads your tables, views, and columns. Column comments you wrote in MotherDuck become descriptions in Dot. After the sync, pick the tables Dot should use in [Model](../../whats-dot/model/README.md).

If Dot answers "No tables found", it did not save the connection. Check the database name, the **Databases** and **Schemas** fields, and that the token can see your data.

{% hint style="info" %}
Dot only runs read queries on MotherDuck. Each query Dot runs to answer a question starts with a `/* Dot:: ... */` comment. The comment names the Dot user and the chat the question came from.
{% endhint %}

Dot runs DuckDB on its own servers, on a client version MotherDuck supports. You don't need to install anything.

## DuckDB

If you have your data in a local duckdb file you can either host it yourself (e.g. on S3) or [talk to us](../../support.md).

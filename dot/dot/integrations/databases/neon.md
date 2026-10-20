---
description: Connect Dot to Neon with a read-only role and ask questions about your data in plain language.
---

# Neon

Dot connects to your Neon database with a read-only Postgres role. You need to be an admin in Dot to add the connection.

## Create a read-only role for Dot

A role you create in the Neon Console gets admin rights, so it can change your data. Create Dot's role with SQL instead.

1. Open the [Neon Console](https://console.neon.tech) and select your project.
2. Open the **SQL Editor**. Pick the branch and the database Dot should read.
3. Run the statements below. Replace `neondb` with your database name.

```sql
CREATE ROLE dot_reader WITH LOGIN PASSWORD '<password>';
GRANT CONNECT ON DATABASE neondb TO dot_reader;
GRANT USAGE ON SCHEMA public TO dot_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO dot_reader;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO dot_reader;
```

Repeat the last three statements for each schema Dot should read.

Neon only accepts a password with at least 60 bits of entropy. Use at least 12 characters, and mix lowercase and uppercase letters, numbers, and symbols. A weaker password fails with an "insecure password" error.

## Copy the connection string

1. In the Neon Console, click **Connect**.
2. Pick the branch, the database, and the `dot_reader` role, not the owner role.
3. Copy the connection string.

Each branch has its own host. Pick the branch your team's data is on, usually your production branch.

The connection string contains the password. Treat it like a password.

## Allow Dot's IP addresses

If you limit access with Neon's [IP Allow](https://neon.com/docs/introduction/ip-allow), add Dot's IP addresses before you connect:

1. In the Neon Console, open your project and click **Settings**.
2. Click **Networking**.
3. Under **Public internet access**, add both of Dot's IP addresses to the allowlist:
   * `5.78.211.110` (US)
   * `178.105.217.177` (EU)
4. Click **Save changes**.

## Connect in Dot

1. Go to **Settings → Connections**.
2. Under **Databases**, open **Neon**.
3. Paste the connection string into **Host**. Dot fills in the host, port, database, username, and password.
4. Optional: in **Schemas**, list the schemas Dot should sync, separated by commas. Leave it empty to sync every schema you gave `dot_reader` access to.
5. Click **Connect**.

Dot checks the connection, saves it, and starts a sync. The sync reads your tables, views, and columns. Comments you wrote on tables and columns in Neon become descriptions in Dot.

Dot always connects to Neon with SSL mode `require`, so the connection is encrypted. Neon refuses connections without SSL.

{% hint style="info" %}
Pooled and direct connection strings both work. Dot always connects to Neon directly, so it removes `-pooler` from a pooled host. Neon's connection pooler does not accept the time limit Dot sets on each query.
{% endhint %}

## Choose the tables Dot uses

After the first sync, open [Model](../../whats-dot/model/README.md) and turn on the tables Dot should use. Dot answers only from tables that are on. When Neon is your company's first database in Dot and only you have used Dot so far, Dot turns on up to 10 tables that look most useful and lists them at the end of the sync log. Otherwise every table starts off, so turn on the ones your team asks about.

## If something goes wrong

* If Dot answers "No tables found", it did not save the connection. Check that you picked the database that holds your tables.
* If a table is missing in Dot, grant `dot_reader` SELECT on it and sync again.
* If the sync log says Dot has no SELECT privilege on some tables, the log also lists the GRANT statements that fix it. Run them and sync again.

## Good to know

* By default, Neon suspends a compute after 5 minutes without queries. A question or a sync wakes it, so the first query after a pause takes a little longer.
* Each query Dot runs to answer a question starts with a `/* Dot:: ... */` comment. The comment names the Dot user and the chat the question came from.

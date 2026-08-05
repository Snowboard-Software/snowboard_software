---
description: Connect Dot to Firebolt and ask questions over your sub-second analytics engine.
---

# Firebolt

Firebolt is built for interactive, sub-second analytics. Pairing it with Dot means that speed isn't reserved for the people who write SQL — anyone can ask in plain language, and the engine's performance carries straight through to their answer.

## Create a service account for Dot

Dot authenticates with a Firebolt service account:

1. In Firebolt, go to **Configure → Service accounts** and create one for Dot.
2. Attach it to a user whose role has read access to the data you want to expose (`SELECT` on the relevant database plus `USAGE` on the engine — a read-only role is all Dot needs).
3. Note the **client ID** and **client secret**, plus your **account name**, the **database**, and the **engine** Dot should use.

## Connect in Dot

1. Go to **Settings → Connections** and choose **Firebolt**.
2. Enter the client ID, client secret, account name, database, and engine.
3. Connect. Dot syncs your tables and columns, generates descriptions, and is ready for questions.

{% hint style="info" %}
Dot only issues `SELECT` queries — a read-only role is the right scope. Table and column selection, descriptions, and everything else works the same as for any other database in your Model.
{% endhint %}

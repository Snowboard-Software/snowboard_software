---
description: Connect Dot to your data warehouse
---

# Databases

## Removing a connection

Removing a connection keeps the work you put into your tables. Tables that were switched on are archived instead of deleted, so their descriptions and column comments stay with them.

Reconnect the same warehouse and Dot restores those tables on the next sync, and switches them back on. It matches them by database, schema, and table name, not by the old connection, so re-adding the same warehouse under a different host still works.

Tables that were switched off are removed for good, together with the queries saved against them.

An archived table stays visible on the Model page with a note explaining that it is no longer reachable. From there you can leave it for a future reconnect, or click **Delete Permanently** to remove it.

{% hint style="warning" %}
The remove dialog has a checkbox, **Also delete table setup**. Tick it only if you want the descriptions, the column comments, and the record of which tables were on to be gone for good. Reconnecting does not bring them back.
{% endhint %}


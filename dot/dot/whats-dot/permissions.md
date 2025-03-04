---
description: permissive or restrictive, however you like it
---

# Permissions

## Roles in Dot

There are two roles that control what you can do with Dot.&#x20;

* **Admins** can control the data model, data source settings and permissions.
* **Users** can chat.

Roles are managed by admins on the Settings page.

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption><p>User Settings page</p></figcaption></figure>

## Data Access Control

Groups manage who gets access to what. Users can access a table if they are in the same group (e.g. in sales).

A user can belong to multiple groups, a table can also belong to multiple groups.

By default all new tables get assigned the group `all_users` and new users get also added to this group. An admin can configure that new users don't automatically get assigned to this group if your organization operates rather on the "Need to know" principle.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption><p>group section for table on Model page</p></figcaption></figure>



## Row Level Permissions

Groups can also be used to apply row-level filtering on tables.

To enable row level permissions, you can go to a table, click on the toggle and specify a where clause.

The where clause should contain the placeholder `${groupname}` that will be replaced by the actual name of the group when the user is requesting information.

Theoretically, you could also use the where clause without the placeholder, then the filtering is the same for all users.

<figure><img src="../../.gitbook/assets/grafik (33).png" alt=""><figcaption></figcaption></figure>




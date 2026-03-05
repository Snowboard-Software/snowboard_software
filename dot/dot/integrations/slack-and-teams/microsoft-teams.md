---
description: Use Dot where you work with your team
---

# Microsoft Teams

## Cloud Setup

1. In Settings Click on Add Dot to Teams

<figure><img src="../../../.gitbook/assets/grafik (2).png" alt="" width="292"><figcaption></figcaption></figure>

2. Install App in Teams App Store
3. Add Dot to group channel or chat with @Dot EU/US
4. Say `@Dot EU hello` 
5. Copy the tenant id to settings and save
6. Chat! 🎉



## Self-hosted Setup

Please contact us at [hi@getdot.ai](mailto:hi@getdot.ai). 

This setup requires to manually add the Teams app with the correct endpoints to your Tenant.



## Tips for talking with Dot

1. To start a new topic, begin a new conversation with `@Dot` in a group channel or chat.
2. In a group channel, follow-up questions can be asked directly in the thread — Dot uses the whole thread as context. No need to tag `@Dot` again.
3. In a direct chat, Dot uses your previous messages as context. Say `@Dot reset` to start fresh.
4. If Dot didn't get it right, just rephrase. You can also check which data source Dot picked to understand what it can answer.
5. You can upload files (CSVs, spreadsheets) and Dot will analyze them.
6. Ask Dot to create charts, generate PowerPoint presentations, or schedule recurring reports to your email or Slack.



## Permissions

Dot uses group-based permissions to control access. This means a user’s ability to access data via Dot depends on the groups they belong to.

In Microsoft Teams, Dot distinguishes between two types of user contexts:

**1. Direct Messages**

* Dot is used in a 1:1 conversation with an individual user.
* The user is identified by their email address (e.g., claude.shannon@bell.com).
* On first interaction, Dot automatically creates a user profile using default settings.<br>

**2. Chats and Team Channels**

* Dot is used in a group context—either a group chat or a team channel.
* Dot creates a shared user profile for the group or channel, not for each individual.
* All users within that group or channel will have the same permissions in Dot.
* This is useful for managing access by organizational domain or function, such as having separate permissions for a marketing channel and a finance channel.
* Example user ID for a team channel: 

<pre><code><strong>teams_19:04ca1344-6505-41l3-b743-e64bcf1124f8_5d982b38-eb38-46b6-b929-42ff0392d01a@unq.gbl.spaces@getdot.ai
</strong></code></pre>

Admins can assign different groups (and thus different permissions) to these shared group-level users, allowing tailored access control without managing individual users within each channel.

## Next Steps

See [Channel Routing](channel-routing.md) to route specific channels to different workspaces.


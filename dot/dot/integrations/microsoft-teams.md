---
description: Use Dot where you work with your team
---

# Microsoft Teams

## Cloud Setup

1. In Settings Click on Add Dot to Teams

<figure><img src="../../.gitbook/assets/grafik (2).png" alt="" width="292"><figcaption></figcaption></figure>

2. Install App in Teams App Store
3. Add Dot to group channel or chat with @Dot EU/US
4. Say `@Dot EU hello`&#x20;
5. Copy the tenant id to settings and save
6. Chat! 🎉



## Self-hosted Setup

Please contact us at [hi@getdot.ai](mailto:hi@getdot.ai).&#x20;

This setup requires to manually add the Teams app with the correct endpoints to your Tenant.



## Tips for talking with Dot

1. To speak about a new topic, start a new conversation with `@Dot` in a group channel or chat.&#x20;
2. In a group channel follow up questions can be directly asked in the thread using the whole thread as context. No additional `@Dot` is needed.
3. In a chat Dot will automatically use the previous 3 messages as context, unless you reset it with `@Dot reset`
4. If Dot did not get it right, just rephrase your question and try again. It can help to look at the found data source to see which questions Dot might answer on it.

![](<../../.gitbook/assets/grafik (16).png>)

5.  To analyze complex topics it can help to break the questions up in multiple parts:\
    **What's our total revenue per country and its percentage change over time?**

    -> Show me total revenue over time (1)\
    -> Split it by country (2)\
    -> Calculate percentage change of revenue over time (3)\


    This helps Dot to build up context first. Most great things are created iteratively. 🛶⛵🚢\

6. Dot is trained to analyze data, not to configure visualizations (yet). It can not build a pie chart. 🍰 But it can format the output data and thus influence the chart, e.g. filter by dimensions or aggregate data differently. The goal of Dot is to come up with the best visualization to answer the question itself.



## Permissions

Dot uses group based [permissions](../whats-dot/permissions.md). That means users can access data via Dot based on the groups they are a part of. Not in Microsoft teams there are 2 different user types:

* **Direct Messages**: here Dot is available to an individual user and Dot will identify this user with their email address. If it's the first time Dot interacts with them Dot will automatically create the user with the default settings. For example `claude.shannon@bell.com`
* **Chats /Team Channels**: here Dot is available to a group of users. In these cases Dot will create a user for the chat or channel, meaning that all users in this chat or channel have the **same** permissions. This is useful e.g. for different domains, where you might have a marketing channel and a finance channel. Then, on the Dot side this would create only 2 users that an admin could grant separate groups to. For example `teams_19:04ca1344-6505-41l3-b743-e64bcf1124f8_5d982b38-eb38-46b6-b929-42ff0392d01a@unq.gbl.spaces@getdot.ai`

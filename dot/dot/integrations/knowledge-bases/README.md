---
description: >-
  Bring your team's written knowledge — docs, wikis, and tickets — into Dot so
  its agents can search, read, ask, and (where enabled) write.
---

# Knowledge Bases

Most of what a data team needs to answer a question well isn't in the warehouse — it's the tribal knowledge written down in a wiki, a notes app, or a ticket. Knowledge-base connectors let Dot reach that content directly: its agents can **search**, **read**, and **ask questions** across your documentation, and for some tools **create or update** pages and issues on your behalf.

These are the connectors that answer the original ask behind this whole category — *"all our company documentation lives in Slite / Confluence / Notion, how do I feed that to Dot?"*

## Available connectors

| Connector | Good for | Dot can… |
|---|---|---|
| [Slite](slite.md) | Slite workspaces | Ask (hosted Q&A), search, read notes — **read-only** |
| [Notion](notion.md) | Notion workspaces | Search, read pages & databases, create/update pages, comments |
| [Confluence](confluence.md) | Atlassian Cloud wikis | Search, read, create/update pages, attachments, comments |
| [Jira](jira.md) | Atlassian Cloud issues | Search, read, create/update/transition issues, comments |

## How they work

**1. Connect once, in Settings.** Each connector is a card under **Settings → Connections**, in the group the app labels **Context Connectors**. You supply an API token (or, for Notion, authorize via OAuth) and Dot validates it.

**2. Govern each action, in Model → Skills.** Once connected, the connector appears as a **skill** under **Model → Skills**. Expand **Configure permissions** to see each action as its own toggle — an admin turns individual actions on or off. A disabled action is refused with a message naming the exact permission to flip, so nothing runs that you haven't allowed.

**3. Dot uses it at query time.** Unlike a database sync, these connectors don't copy your content into Dot. Dot's agents reach into the source *when a question needs it* — searching, reading, or asking against the live workspace. This keeps answers current and means access always reflects the connected account's own permissions in the source tool.

{% hint style="info" %}
**Permission defaults follow a simple rule.** Non-destructive reads (and, for Notion/Confluence/Jira, ordinary writes) default **on** — connecting the tool implies you want Dot to use it. Destructive or privacy-sensitive actions (delete, archive, listing workspace members) default **off** and must be turned on explicitly.
{% endhint %}

## Related

Knowledge-base connectors are one of the tools available to [Root, Dot's Context Agent](../../whats-dot/context-agent.md) — the agent that builds and maintains your organization's knowledge base. Pointing Root at your Confluence space or Slite workspace lets it extract business logic straight from your existing documentation.

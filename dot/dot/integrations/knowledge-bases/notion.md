---
description: Let Dot read and write your Notion pages, databases, and comments.
---

# Notion

Connect your [Notion](https://notion.com) workspace so Dot can search, read pages and databases, and — when enabled — create or update pages and post comments. Writes are attributed to Dot: agent-created page titles are prefixed with `[Dot]`, and comments carry a `[Dot, on behalf of <user>]` byline so authorship stays traceable.

## Prerequisites

- A Notion workspace and a Dot admin account.
- Permission to authorize an integration and choose which pages it may access.

## Connect in Dot

1. Go to **Settings → Connections** and find **Notion** under **Context Connectors**.
2. Click **Connect Notion**. This opens Notion's authorize page.
3. Choose the pages and databases the integration may access, and confirm. Dot shows the connected workspace once it's done.

{% hint style="warning" %}
**Notion shares by page.** The integration only sees pages you explicitly share with it. If Dot's searches come back empty, share more pages (or their parent) with the integration in Notion.
{% endhint %}

## What Dot can do

Each action is a separately governed permission under **Model → Skills → Notion**.

| Permission | What it allows | Default |
|---|---|---|
| `notion.search` | Title search across reachable pages and databases | On |
| `notion.pages.read` | Reading pages and their block content | On |
| `notion.pages.write` | Creating and updating pages, appending content | On |
| `notion.pages.archive` | Archiving (soft-deleting) or restoring pages | Off |
| `notion.databases.read` | Reading database schemas and querying rows | On |
| `notion.comments.read` | Reading comment threads | Off |
| `notion.comments.write` | Posting comments | Off |
| `notion.users.read` | Listing workspace members (surfaces names & emails) | Off |

To change a permission, open **Model → Skills**, expand the **Notion** skill, and toggle it.

{% hint style="info" %}
**Comments and member listing need a second opt-in on Notion's side.** Those permissions also depend on capabilities configured on the Notion integration itself (e.g. "Read comments"). That's why they default off — enable the capability in Notion's integration settings *and* the matching permission in Dot. Turning on only one side still refuses the call.
{% endhint %}

## Limitations

- The integration sees only pages shared with it (see above).
- Markdown ↔ Notion conversion covers common blocks (paragraphs, headings, lists, to-dos, code, quotes, dividers, links, inline formatting). Toggle, callout, and synced blocks degrade to plain paragraphs.
- Very large or deeply nested pages are read in bounded chunks.

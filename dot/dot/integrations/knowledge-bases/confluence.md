---
description: Let Dot read and write your Confluence pages, spaces, and comments.
---

# Confluence

Connect your Atlassian Cloud account so Dot can search, read, and — when enabled — create or update Confluence pages, upload attachments, and post comments. Dot writes plain Markdown and converts it to Confluence's native format, so tables, headings, lists, and embedded charts render correctly.

{% hint style="info" %}
**One connection, two skills.** Confluence and [Jira](jira.md) share a single **Atlassian (Confluence + Jira)** connection and API token, but each is a separate skill you toggle independently under **Model → Skills**. Connecting once enables both.
{% endhint %}

## Prerequisites

- An **Atlassian Cloud** site (Server / Data Center is not supported).
- A Dot admin account and an Atlassian **API token**.

## Get an Atlassian API token

1. Go to [id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens).
2. Click **Create API token**, name it, and copy the value.

The token acts as the account that created it — Confluence records that account as the author of pages and comments Dot writes.

## Connect in Dot

1. Go to **Settings → Connections** and find **Atlassian (Confluence + Jira)** under **Context Connectors**.
2. Fill in:
   - **Site URL** — e.g. `https://your-org.atlassian.net`
   - **Account email** — the email of the account that owns the token
   - **API token** — the token you just created
3. Click **Connect**.

## What Dot can do

Each action is a separately governed permission under **Model → Skills → Confluence**.

| Permission | What it allows | Default |
|---|---|---|
| `confluence.search` | Cross-space full-text search | On |
| `confluence.spaces.read` | Listing spaces | On |
| `confluence.pages.read` | Reading pages, ancestors, and page trees | On |
| `confluence.pages.write` | Creating/updating pages, uploading attachments | On |
| `confluence.pages.delete` | Trashing pages (reversible for 30 days) | Off |
| `confluence.comments.read` | Reading footer and inline comments | On |
| `confluence.comments.write` | Posting footer comments | On |

To change a permission, open **Model → Skills**, expand the **Confluence** skill, and toggle it.

## Attribution

Pages and comments Dot writes are marked as its own: page titles are prefixed with `[Dot]`, page bodies end with a *"…on behalf of &lt;user&gt;"* byline, and comments are prefixed with `[Dot, on behalf of <user>]`.

## Limitations

- **Atlassian Cloud only** — no Server / Data Center.
- Markdown conversion covers paragraphs, headings, lists, GFM tables, quotes, code blocks, dividers, links, and inline formatting; images embed via attachment upload. Confluence-specific macros (panel, expand, status) render as plain paragraphs.

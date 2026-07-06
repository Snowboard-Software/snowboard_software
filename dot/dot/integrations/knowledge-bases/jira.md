---
description: Let Dot read, create, and transition your Jira issues.
---

# Jira

Connect your Atlassian Cloud account so Dot can search issues with JQL, read them, and — when enabled — create, edit, transition, or comment on issues. A common pattern is letting Dot file a ticket straight from an analysis: *"usage dropped for this customer — open a Jira issue with the findings."*

{% hint style="info" %}
**One connection, two skills.** Jira and [Confluence](confluence.md) share a single **Atlassian (Confluence + Jira)** connection and API token, but each is a separate skill you toggle independently under **Model → Skills**. Connecting once enables both.
{% endhint %}

## Prerequisites

- An **Atlassian Cloud** site (Server / Data Center is not supported).
- A Dot admin account and an Atlassian **API token**.

## Get an Atlassian API token

1. Go to [id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens).
2. Click **Create API token**, name it, and copy the value.

The token acts as the account that created it — Jira records that account as the reporter of issues and author of comments Dot writes.

## Connect in Dot

If you've already connected Atlassian for Confluence, Jira is ready — skip this. Otherwise:

1. Go to **Settings → Connections** and find **Atlassian (Confluence + Jira)** under **Context Connectors**.
2. Fill in **Site URL** (e.g. `https://your-org.atlassian.net`), **Account email**, and **API token**.
3. Click **Connect**.

## What Dot can do

Each action is a separately governed permission under **Model → Skills → Jira**.

| Permission | What it allows | Default |
|---|---|---|
| `jira.search` | JQL search across issues | On |
| `jira.issues.read` | Reading issues and their available transitions | On |
| `jira.issues.write` | Creating/editing issues, uploading attachments | On |
| `jira.issues.transition` | Moving an issue to a new status | On |
| `jira.issues.delete` | Deleting issues (not recoverable) | Off |
| `jira.comments.read` | Reading issue comments | On |
| `jira.comments.write` | Adding issue comments | On |

To change a permission, open **Model → Skills**, expand the **Jira** skill, and toggle it.

## Attribution

Issues and comments Dot writes are marked as its own: issue summaries are prefixed with `[Dot]`, descriptions end with a *"…on behalf of &lt;user&gt;"* byline, and comments are prefixed with `[Dot, on behalf of <user>]`.

## Limitations

- **Atlassian Cloud only** — no Server / Data Center.
- Descriptions and comments accept Markdown (paragraphs, headings, lists, GFM tables, quotes, code blocks, links, inline formatting), converted to Jira's format on submission. Attachments upload to the issue's Attachments panel; inline-embedding an image in a description isn't supported.

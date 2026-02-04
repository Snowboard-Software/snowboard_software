---
description: Sync your context files with GitHub for version control, collaboration, and automation interoperability
---

# GitHub Sync

GitHub Sync enables bidirectional synchronization between Dot's context files and a GitHub repository. This integration transforms your data context into a collaborative, version-controlled asset that can be maintained alongside your code.

## Why GitHub Sync Matters

### Beyond Version Control

While version control for your notes and table documentation is valuable, the real power of GitHub Sync lies in **interoperability**. By storing your context in GitHub using open file formats (Markdown with YAML frontmatter), you enable:

- **Coding agents** (Claude Code, Cursor, GitHub Copilot) to read and contribute to the same context that Dot uses
- **CI/CD pipelines** to validate or transform documentation automatically
- **Other automations** to consume and produce context without being locked into any single tool
- **Team collaboration** through pull requests, code review, and branch workflows

This approach follows the principle that context should not be siloed in a single tool. Your data documentation becomes a shared asset that multiple AI assistants and automation systems can leverage.

### Open File Formats

All synced files use simple, universal formats:

| File Type | Format | Description |
|-----------|--------|-------------|
| Notes | `.md` (Markdown) | Business context and documentation with YAML frontmatter |
| Table Docs | `.md` (Markdown) | Table and column documentation with YAML frontmatter |
| Relationships | `.yaml` | Table relationship definitions |

Any tool that can read Markdown and YAML can work with your Dot context.

## What Gets Synced

GitHub Sync synchronizes these files from your Dot model:

```
notes/
├── active/          # Active notes (visible to Dot)
│   └── *.md
└── inactive/        # Archived notes
    └── *.md

data_sources/
├── active/          # Active table documentation
│   └── *.md
└── inactive/        # Archived table documentation
    └── *.md

relationships.yaml   # Table relationships
```

{% hint style="info" %}
Only context files are synced. Database connections, user settings, and chat history remain in Dot and are not pushed to GitHub.
{% endhint %}

## Setting Up GitHub Sync

### Prerequisites

- Admin access to your Dot organization
- A GitHub account (personal or organization)
- Permission to install GitHub Apps on your GitHub account/org

### Step 1: Connect with GitHub

1. Go to **Settings** > scroll to **Version Control** > click **GitHub**
2. Click **Connect with GitHub**
3. You'll be redirected to GitHub to install the Dot Context Sync app
4. Choose whether to grant access to **All repositories** or **Selected repositories**

{% hint style="warning" %}
If you select specific repositories, you won't be able to create new repositories from within Dot. Choose "All repositories" if you want Dot to create a new repo for you.
{% endhint %}

### Step 2: Configure Your Repository

After connecting, you have two options:

#### Option A: Create a New Repository (Recommended)

1. Select **Create new repository**
2. Enter a repository name (e.g., `dot-context` or `data-context`)
3. Optionally add a description
4. Choose a branch name (default: `main`)
5. Click **Create & Configure**

Dot will create a private repository and push all your existing context files in a single atomic commit.

#### Option B: Use an Existing Repository

1. Select **Select existing repository**
2. Choose a repository from the dropdown
3. Enter the branch name to sync with
4. Click **Configure**

{% hint style="info" %}
When using an existing repository, Dot will merge your files with any existing content. Consider using an empty repository or a dedicated branch to avoid conflicts.
{% endhint %}

### Step 3: Enable Auto-Sync

Once configured, toggle **Auto-sync enabled** to automatically push changes whenever you update context in Dot's UI.

## How Sync Works

### Push (Dot → GitHub)

When auto-sync is enabled, any changes made in Dot are automatically pushed to GitHub:

- Creating or editing a note
- Updating table documentation
- Modifying relationships

Each change creates a commit in your GitHub repository with a descriptive message like "Sync from Dot: notes/active/revenue-metrics.md".

### Pull (GitHub → Dot)

Changes made directly in GitHub are automatically pulled into Dot via webhooks:

- Editing files through GitHub's UI
- Merging pull requests
- Commits from coding agents or other tools

{% hint style="success" %}
**Collaboration workflow**: Team members or AI coding assistants can submit pull requests to update context. Once merged, changes automatically appear in Dot.
{% endhint %}

### Manual Sync

You can also trigger sync manually:

- **Push to GitHub**: Force push all current Dot context to GitHub
- **Pull from GitHub**: Force pull all GitHub files into Dot

Use manual sync if auto-sync is disabled or if you need to resolve sync issues.

## Example: Coding Agent Workflow

Here's how a coding agent like Claude Code can contribute to your Dot context:

1. **Agent reads context**: The agent reads your `notes/active/*.md` files to understand business context
2. **Agent updates documentation**: While working on a data pipeline, the agent updates `data_sources/active/orders.md` with new column documentation
3. **Agent commits changes**: The agent commits and pushes to your context repository
4. **Dot receives update**: GitHub webhook notifies Dot of the change
5. **Dot pulls changes**: New documentation is immediately available in Dot

This creates a virtuous cycle where both human analysts (via Dot's UI) and AI agents (via GitHub) can maintain your data context.

## Example File Structure

Here's what a synced repository might look like:

```
dot-context/
├── notes/
│   └── active/
│       ├── revenue-metrics.md
│       ├── customer-segments.md
│       └── data-quality-rules.md
├── data_sources/
│   └── active/
│       ├── orders.md
│       ├── customers.md
│       └── products.md
└── relationships.yaml
```

### Sample Note File

```markdown
---
title: Revenue Metrics
created: 2024-01-15T10:30:00Z
updated: 2024-02-01T14:22:00Z
---

# Revenue Metrics

## MRR (Monthly Recurring Revenue)

MRR is calculated as the sum of all active subscription values,
normalized to a monthly amount.

**Key rules:**
- Annual subscriptions are divided by 12
- Exclude one-time fees
- Include expansion revenue from upgrades
```

### Sample Table Documentation

```markdown
---
table: orders
schema: analytics
database: warehouse
---

# Orders

The orders table contains all customer orders including...

## Columns

### order_id
Primary key. UUID generated at order creation.

### total_amount
Order total in USD. Excludes tax and shipping.
```

## Disconnecting

To stop syncing with GitHub:

1. Go to **Settings** > **Version Control** > **GitHub**
2. Click **Disconnect**
3. Confirm the disconnection

{% hint style="info" %}
Disconnecting does not delete your GitHub repository or its contents. Your context files remain in GitHub and in Dot independently.
{% endhint %}

## Limitations

### Current Limitations

- **One repository per organization**: Each Dot organization can sync with one GitHub repository
- **One branch**: Sync happens with a single branch (configurable, default `main`)
- **Markdown and YAML only**: Only `.md` files in sync directories and `relationships.yaml` are synced
- **No conflict resolution UI**: If the same file is modified in both Dot and GitHub simultaneously, the last write wins

### Not Synced

The following are **not** included in GitHub Sync:

- Database connection credentials
- User accounts and permissions
- Chat history and saved questions
- Scheduled reports configuration
- Organization settings

## Troubleshooting

### Sync Not Working

1. **Check connection status**: Go to Settings > GitHub and verify "Auto-sync enabled" is on
2. **Verify webhook**: Ensure the GitHub App has webhook permissions on your repository
3. **Check branch**: Confirm you're pushing to the correct branch

### Permission Errors

If you see permission errors:

1. Go to your GitHub Settings > Applications > Dot Context Sync
2. Verify the app has access to your repository
3. If using "Selected repositories", ensure your context repo is included

### Files Not Appearing

- Only files in `notes/`, `data_sources/`, and `relationships.yaml` are synced
- Files must have the correct extension (`.md` for notes/docs, `.yaml` for relationships)
- Check that files are in the `active/` or `inactive/` subdirectories

## Security

- **Private by default**: Repositories created by Dot are private
- **GitHub App authentication**: Uses secure GitHub App tokens, not personal access tokens
- **Scoped access**: The app only accesses repositories you explicitly grant
- **Webhook verification**: All webhook payloads are cryptographically verified

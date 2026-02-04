---
description: Sync your context files with GitHub for version control and automation interoperability
---

# GitHub Sync

GitHub Sync enables bidirectional synchronization between Dot's context files and a GitHub repository.

## Why GitHub Sync Matters

The real power lies in **interoperability**. By storing context in GitHub using open formats (Markdown with YAML frontmatter), you enable:

- **Coding agents** (Claude Code, Cursor, GitHub Copilot) to read and contribute to the same context Dot uses
- **CI/CD pipelines** to validate or transform documentation automatically
- **Team collaboration** through pull requests and code review

Your data documentation becomes a shared asset that multiple AI assistants can leverage.

## What Gets Synced

```
notes/
├── active/          # Active notes
└── inactive/        # Archived notes

data_sources/
├── active/          # Active table documentation
└── inactive/        # Archived table documentation

relationships.yaml   # Table relationships
```

All files use Markdown (`.md`) with YAML frontmatter, or plain YAML.

{% hint style="info" %}
Only context files are synced. Database connections, user settings, and chat history remain in Dot.
{% endhint %}

## Setting Up GitHub Sync

### Prerequisites

- Admin access to your Dot organization
- A GitHub account with permission to install GitHub Apps

### Step 1: Connect with GitHub

1. Go to **Settings** > **Version Control** > **GitHub**
2. Click **Connect with GitHub**

<figure><img src="../../.gitbook/assets/github-sync-connect.png" alt="GitHub sync panel in Dot settings"><figcaption><p>Click Connect with GitHub to start the setup</p></figcaption></figure>

3. Install the Dot Context Sync app and choose repository access

<figure><img src="../../.gitbook/assets/github-sync-install.png" alt="GitHub App installation page"><figcaption><p>Choose "All repositories" to let Dot create new repos</p></figcaption></figure>

{% hint style="warning" %}
If you select specific repositories, you won't be able to create new repos from Dot. Choose "All repositories" if you want Dot to create a new repo for you.
{% endhint %}

### Step 2: Configure Your Repository

**Create new repository** (recommended): Enter a name, choose a branch, and Dot will create a private repo with all your existing context.

**Use existing repository**: Select a repo and branch. Consider using an empty repo or dedicated branch to avoid conflicts.

### Step 3: Enable Auto-Sync

Toggle **Auto-sync enabled** to automatically push changes when you update context in Dot's UI.

## How Sync Works

**Push (Dot → GitHub)**: Changes in Dot automatically commit to GitHub when auto-sync is enabled.

**Pull (GitHub → Dot)**: Changes in GitHub (commits, merged PRs) automatically sync to Dot via webhooks.

{% hint style="success" %}
**Collaboration workflow**: Team members or AI coding assistants can submit pull requests. Once merged, changes automatically appear in Dot.
{% endhint %}

**Manual sync**: Force push or pull all files from Settings if needed.

## Limitations

- **One repository per organization**, syncing with a single branch
- **Markdown and YAML only** in the specified directories
- **Last write wins** for simultaneous edits (no conflict resolution UI)

**Not synced**: Database credentials, user accounts, chat history, scheduled reports, organization settings.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Sync not working | Check Settings > GitHub for connection status and auto-sync toggle |
| Permission errors | Verify the GitHub App has access to your repo in GitHub Settings > Applications |
| Files not appearing | Ensure files are in `notes/`, `data_sources/`, or `relationships.yaml` with correct extensions |

## Security

Repositories created by Dot are private. Uses secure GitHub App tokens with scoped access. All webhook payloads are cryptographically verified.

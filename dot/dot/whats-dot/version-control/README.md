---
description: Sync your context files with a Git provider for version control, audit trail, and AI/CI interoperability
---

# Version Control

Dot can sync the files it manages — notes, table documentation, relationships, custom skills, reports — with a Git repository. Pick the provider you already use:

* [**GitHub**](github.md) — install the Dot Context Sync GitHub App and pick a repo. Webhooks are auto-created for you.
* [**GitLab**](gitlab.md) — paste a Personal Access Token (gitlab.com or self-hosted). Webhook is set up manually with a URL and secret Dot displays for you.

You can connect both providers at the same time — every change in Dot fans out to all configured repos in parallel, and webhook events from any provider pull changes back into Dot.

## Why version-control your context

Your context lives in plain Markdown and YAML files. Keeping it in Git gives you:

* **Audit trail** — every change is a commit. `git blame` shows who changed which note and why.
* **Backup + disaster recovery** — restore an accidentally deleted note with `git revert`, or rebuild a fresh server from the repo.
* **AI/coding-agent interop** — Claude Code, Cursor, and GitHub Copilot can read and contribute to the same context Dot uses.
* **Code review** — important notes and skills go through PR review before reaching production.
* **Cross-environment promotion** — point staging at `dev` and prod at `main` of the same repo, then promote with a PR.
* **Bulk edits in your editor** — power users grep/sed across hundreds of notes locally, push, and Dot picks up the changes.

## What gets synced

```
notes/
├── active/          # Active notes
└── inactive/        # Archived notes

data_sources/
├── active/          # Active table documentation
└── inactive/        # Archived table documentation

relationships.yaml   # Table relationships
reports/             # Saved reports
skills/              # Custom skills
```

All files use Markdown (`.md`) with YAML frontmatter, or plain YAML.

{% hint style="info" %}
Only context files are synced. Database connections, user accounts, chat history, schedules, and billing settings stay in Dot.
{% endhint %}

## Workspaces

Each org and each workspace has its own independent connection — switching to a workspace shows the empty Connect panel even if the parent org is connected. This lets you keep separate workspaces pointing at separate repos (or no repo at all).

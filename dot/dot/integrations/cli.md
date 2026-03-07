---
description: Query your company data from the terminal using Dot's CLI tool — works with Claude Code, Cursor, and any terminal.
---

# CLI

### What is the Dot CLI?

The Dot CLI (`getdot`) lets you query your company's databases directly from the terminal. Dot writes SQL, runs queries, generates charts, and explains results — all from a single command.

It works standalone in any terminal, and integrates with AI coding assistants like **Claude Code** and **Cursor** through a skill file that teaches them when and how to use it.

### Why use the CLI?

* **Stay in your flow** — ask data questions without switching to a browser
* **AI coding assistants** — Claude Code and Cursor can query your data autonomously while coding
* **Scriptable** — pipe output to other tools, automate reports
* **Cached** — repeated questions return instantly from local cache
* **Secure** — credentials stored locally with restrictive permissions, tokens scoped per user

### Quick Start

#### 1. Install

```bash
curl -fsSL https://raw.githubusercontent.com/Snowboard-Software/getdot/main/scripts/install.sh | sh
```

This installs a native binary — no Node.js or other runtime required. Supports macOS (ARM & Intel), Linux (x64 & ARM), and Windows.

{% hint style="info" %}
On Windows, download the binary directly from [GitHub Releases](https://github.com/Snowboard-Software/getdot/releases/latest).
{% endhint %}

#### 2. Login

```bash
getdot login
```

This opens your browser to authenticate with your Dot account. Your token is saved locally at `~/.config/getdot/config.json`.

For environments without a browser (CI, remote servers):

```bash
getdot login --token <YOUR_API_TOKEN>
```

#### 3. Ask a question

```bash
getdot "What were total sales last month?"
```

### Using with Claude Code

Claude Code automatically discovers Dot's CLI through the `SKILL.md` file. Once `getdot` is installed and authenticated, Claude Code can:

* Query your company data when you ask data questions
* Run `getdot catalog` to understand what tables are available
* Use follow-up questions with `--chat` to refine results
* Read chart PNGs and CSV files from the output

**Example prompts for Claude Code:**

* "What were our top 10 customers by revenue last quarter?"
* "Check the database — is the orders table growing?"
* "Ask Dot to show me monthly active users for the past year"

{% hint style="info" %}
The `SKILL.md` file in the getdot package tells Claude Code when and how to invoke the CLI. No additional configuration is needed — just install and login.
{% endhint %}

### Using with Cursor

Cursor IDE also supports skill files. After installing `getdot`, Cursor's AI can use it the same way as Claude Code — discovering the tool and querying data when relevant.

### Commands

#### Ask a question

```bash
getdot "What were total sales last month?"
```

The output includes:
* **Text explanation** — natural language answer
* **SQL query** — the exact SQL that was executed
* **Data preview** — first rows with column statistics
* **Chart** — saved as PNG to a local temp path
* **CSV data** — saved locally for further analysis
* **Dot URL** — link to the full interactive analysis in the browser
* **Suggested follow-ups** — use these to dig deeper

#### Follow-up questions

Every response includes a chat ID. Use `--chat` to continue the conversation:

```bash
getdot "Now break down by region" --chat cli-m1abc2d-x4y5z6
```

#### View available data

```bash
getdot catalog
```

Returns instantly (no AI call) and shows:
* Available capabilities (SQL, visualizations, scheduled reports)
* Custom skills configured for your org
* Data source connections with table counts
* Active tables with descriptions, column counts, and row counts
* External assets (Looker dashboards, etc.)

#### Other commands

```bash
getdot status          # Show login status and token info
getdot logout          # Clear credentials
getdot --version       # Show version
getdot --help          # Show all options
```

### Caching

Ask responses are cached permanently on disk so repeated questions return instantly:

* `getdot "question"` — cached forever until `--clear-cache`
* Follow-ups with `--chat` are never cached (always fresh)
* `getdot catalog` is never cached (already fast, no AI call)

```bash
getdot "question" --no-cache    # Force fresh request
getdot --clear-cache            # Clear all cached responses
```

Cache is stored at `~/.cache/getdot/` and is scoped to your user identity — different users on the same machine won't see each other's cached results.

### Security

#### Token Management

* Tokens are stored locally at `~/.config/getdot/config.json` with `600` file permissions
* One CLI token per user — generating a new token revokes the previous one
* Tokens expire after 365 days
* Run `getdot logout` to clear credentials immediately

#### Data Access

* The CLI respects all your Dot permissions and user group restrictions
* Queries run within your organization's scope
* All data filtering rules (row-level security) are enforced
* All queries are logged in Dot for compliance

### Troubleshooting

**"Not authenticated" error**

Run `getdot login` to authenticate, or check your token with `getdot status`.

**"Connection failed" error**

* Check your network connection
* If using a custom server, verify the URL: `getdot login --server https://your-server.com`

**Slow responses**

First queries take 10-30 seconds (Dot runs the full AI analysis pipeline). Subsequent identical queries return instantly from cache. Use `getdot catalog` first to understand available data — more specific questions get faster answers.

**Custom server URL**

For self-hosted Dot instances:

```bash
getdot login --server https://your-dot-instance.com
```

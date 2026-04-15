---
description: Give your AI coding assistant direct access to your company's data. One install, and Claude Code, Cursor, Codex, and Gemini CLI can query your databases while you work.
---

# CLI & AI Agent Skill

Most data questions interrupt your flow. You leave your editor, open a browser, wait for an answer, copy it back. The Dot skill eliminates that loop.

Once installed, Claude Code treats Dot like a sub-agent. It delegates data questions to Dot automatically: "what were our top customers last quarter?" gets answered in seconds, right in your terminal. You never context-switch.

<figure><img src="../../.gitbook/assets/claude-code-skill.png" alt="Claude Code loading the Dot skill via /dot command"><figcaption><p>Type /dot in Claude Code to query your company data</p></figcaption></figure>

Works with **Claude Code**, **Cursor**, **OpenAI Codex**, and **Gemini CLI**. The installer detects which agents you have and configures the skill for each one.

### Install

Use the URL that matches your Dot region:

| Region | URL |
|--------|-----|
| US | `app.getdot.ai` |
| EU | `eu.getdot.ai` |

**macOS / Linux:**

```bash
# US region
curl -fsSL https://app.getdot.ai/install.sh | sh

# EU region
curl -fsSL https://eu.getdot.ai/install.sh | sh
```

**Windows (PowerShell):**

```powershell
# US region
irm https://app.getdot.ai/install.ps1 | iex

# EU region
irm https://eu.getdot.ai/install.ps1 | iex
```

Then log in:

```bash
dot login
```

Opens your browser to authenticate. Token is saved locally.

That's it. Your AI agent can now query your data.

{% hint style="info" %}
You can also install from the **Set Up CLI** page in your Dot dashboard (`/cli-setup`). It generates a command with your auth token embedded so you skip the login step.
{% endhint %}

**Self-hosted Dot:**

```bash
curl -fsSL https://your-dot-instance.com/install.sh | sh
```

**CI / headless servers:**

```bash
dot login --token <YOUR_API_TOKEN>
```

### How it works

The installer puts a native `dot` binary on your PATH and drops a `SKILL.md` file into the right location for each AI agent. That skill file teaches your coding assistant when and how to call Dot. It's the bridge between a natural language question and your data.

When an agent invokes the skill, it runs `dot` as a sub-agent. Dot queries your database and returns a structured answer: text explanation, data preview, chart, CSV, and a link to the full analysis in the browser. The agent reads all of this and uses it in context.

No runtime dependencies. No configuration beyond `dot login`.

### Using with AI agents

#### Claude Code

Type **`/dot`** followed by your question:

```
/dot What data sources do we have?
```

Or just ask naturally. Claude Code will delegate to Dot when it recognizes a data question:

* "What were our top 10 customers by revenue last quarter?"
* "Is the orders table growing?"
* "Show me monthly active users for the past year"

Claude Code uses Dot like any other tool in its toolkit. It decides when to call it, reads the results, and incorporates them into its response.

#### Cursor, Codex, and Gemini CLI

Same behavior. The installer configures each agent it detects. The skill file tells the agent what Dot can do and when to use it. No manual setup.

### Standalone usage

You can also use Dot directly from any terminal:

```bash
dot "What were total sales last month?"
```

Returns a text explanation, data preview, chart (PNG), CSV data, a link to the full analysis in Dot, and suggested follow-ups.

#### Follow-up questions

Every response includes a chat ID. Continue the conversation:

```bash
dot "Now break down by region" --chat cli-m1abc2d-x4y5z6
```

#### View available data

```bash
dot catalog
```

Instant response. Shows your connections, tables, column counts, row counts, and any external assets like Looker dashboards.

#### Other commands

```bash
dot update          # Update to latest version
dot status          # Login status and token info
dot logout          # Clear credentials
dot --version       # Show version
dot --help          # Show all options
```

### Workspace management

The CLI is designed as the AI interface to Dot. When you use Claude Code, Cursor, or Codex, your AI assistant manages your Dot workspace through these commands — selecting relevant tables, creating notes with metric definitions, and fixing context gaps. You don't need to type these commands yourself; your AI agent handles it.

{% hint style="info" %}
**How AI agents use this:** When you say "help me set up Dot for our revenue data", your AI assistant will run `dot catalog` to see what's available, `dot tables list` to check active tables, `dot notes list` to audit existing context, and then interview you to fill gaps — creating notes from your answers.
{% endhint %}

#### Notes

Notes teach Dot how to query your data. They contain metric definitions, SQL patterns, business context, and operating principles. See [Notes](../../whats-dot/model/notes.md) for what to put in them.

```bash
dot notes list                          # List all notes (tree view)
dot notes get <id>                      # Read a note
dot notes create <title> [content]      # Create a note
dot notes update <id> [content]         # Update a note
dot notes delete <id>                   # Delete a note
dot notes activate <id>                 # Activate a note
dot notes deactivate <id>              # Deactivate a note
```

Create notes from files or stdin for longer content:

```bash
dot notes create "Metric Glossary" --file metrics.md
cat playbook.md | dot notes create "Campaign Review Playbook"
```

Organize notes with groups and parent relationships:

```bash
dot notes create "SQL Patterns" --parent <parent-id> --group data-team
```

Inactive notes are not used by Dot when answering questions. Deactivate instead of deleting to archive notes you might need later.

#### Tables

Control which database tables Dot can access. Deactivated tables are hidden from Dot entirely.

```bash
dot tables list                         # Active tables, grouped by connection
dot tables list --all                   # Include inactive tables
dot tables get <id>                     # Table details with columns
dot tables activate <id> [id2 ...]      # Activate table(s)
dot tables deactivate <id> [id2 ...]    # Deactivate table(s)
```

Batch operations work with multiple IDs:

```bash
dot tables activate table-1 table-2 table-3
```

#### Chat history

Retrieve the full conversation history for any previous query:

```bash
dot chat <chat-id>
```

Shows all messages with SQL queries, tool calls, and timestamps. Useful for auditing what Dot did or retrieving answers you saw earlier.

#### Feature requests

Submit feedback or feature requests directly from the terminal:

```bash
dot wish "I want better date filtering"
```

### Training Dot effectively

The biggest leverage in Dot accuracy comes from good context management. Here's the recommended approach:

**Start with tables.** Select the right data sources and document what each table represents — especially granularity (what does one row mean?) and primary keys. For wide tables or semantic models with hundreds of fields, curate which columns are active.

**Layer in notes.** After tables are set up, add notes for metric definitions, operating principles, and business context. Use strong, unambiguous language: "Always filter out internal users", "Revenue means recognized revenue, not bookings."

**Fix bad answers at the root.** When Dot gives a wrong answer, don't just correct it — investigate why. Wrong table? Activate the right one. Wrong logic? Add a metric definition. Missing context? Add a business context note.

**Audit regularly.** Review existing notes for contradictions. If one note says "use fct\_orders for revenue" and another says "use fct\_arr for revenue" — that ambiguity will produce inconsistent answers. Remove or reconcile.

**Front-load, then prune.** It's better to give too much context upfront and dial it back than to discover gaps one bad answer at a time.

### Caching

Responses are cached on disk. Repeated questions return instantly.

```bash
dot "question" --no-cache    # Skip cache, force fresh
dot --clear-cache            # Clear all cached responses
```

Follow-ups (`--chat`) and `dot catalog` are never cached. Cache lives at `~/.cache/dot/`, scoped per user.

### Security

* Tokens stored locally with `600` permissions
* One token per user. Generating a new one revokes the old one
* Tokens expire after 365 days
* All Dot permissions and row-level security enforced
* All queries logged for compliance

### Troubleshooting

**"Not authenticated"** Run `dot login` or check with `dot status`.

**"Connection failed"** Check your network. For custom servers: `dot login --server https://your-server.com`.

**Slow responses** First query takes 10-30 seconds (full analysis pipeline). Identical queries return instantly from cache after that.

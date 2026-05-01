---
name: dot
description: >
  Query company data using Dot, an AI data analyst with access to your
  databases. Use when users ask about data, metrics, KPIs, reports, SQL,
  dashboards, or say "ask dot" or "check the numbers".
compatibility: >
  Works with the Dot CLI (`dot` binary) or the Dot MCP server
  (https://app.getdot.ai/ai/mcp). Pick whichever is available in the host.
metadata:
  author: Snowboard-Software
  version: "0.2.0"
---

# dot — AI Data Analyst

`dot` connects to your company's databases through Dot, an AI data analyst. You ask a question in plain English. Dot finds the right tables, writes SQL, executes the query, and returns the answer with charts and data.

You can reach Dot through either of two interfaces — pick whichever your environment supports. The skill works the same either way.

| Interface | Best for | Pattern |
|---|---|---|
| **CLI** (`dot ...`) | Coding agents (Claude Code, Cursor, Codex, Gemini CLI), terminals, shell scripts | Synchronous: each command blocks until done |
| **MCP server** | Claude Desktop / Web / Cowork, ChatGPT, Cursor, Windsurf, Raycast, any MCP-aware client | Async: `ask_dot` → `wait` → `get_result` |

If both are available, prefer the CLI inside coding agents (richer output, file-based artifacts on disk) and the MCP server inside chat clients.

## Setup

### CLI

If `dot` is not in PATH:

```bash
# macOS / Linux
curl -fsSL https://app.getdot.ai/install.sh | sh

# Windows
irm https://app.getdot.ai/install.ps1 | iex
```

Then authenticate:

```bash
dot login                                    # OAuth in browser
dot login --token <TOKEN> --server <URL>     # Headless / CI
dot status                                   # Verify: shows email, org, server
```

### MCP

The Dot MCP server is hosted by Dot — you don't run anything locally, just point your client at the URL.

| Region | URL |
|---|---|
| US | `https://app.getdot.ai/ai/mcp` |
| EU | `https://eu.getdot.ai/ai/mcp` |

Most modern MCP clients (Claude, Cursor, Windsurf) support OAuth — paste the URL and click **Allow** in your browser. For clients without OAuth support (ChatGPT, Raycast, generic clients), generate an MCP token in Dot's *Settings → Integrations* and append it to the URL: `https://app.getdot.ai/ai/mcp?token=YOUR_TOKEN`.

The MCP server exposes four tools:

| Tool | Purpose |
|---|---|
| `get_catalog` | Instant — connections, tables, capabilities (no LLM call) |
| `ask_dot(question, chat_id?)` | Submit a question; returns a `chat_id` immediately |
| `get_result(chat_id)` | Poll for the final answer |
| `wait(seconds)` | Sleep between `ask_dot` and `get_result` |

## When to use

Use Dot when the user asks about:
- Data: "What were sales last month?", "Show me top customers"
- Metrics / KPIs: "What's our churn rate?", "Revenue by region"
- SQL: "Write a query to find...", "Check the database for..."
- Reports: "Generate a summary of...", "Break down..."
- Or says: "ask dot", "check the numbers", "query the data"

## Decision tree

```
User asks what data is available?      →  catalog
User asks a vague question?            →  catalog first, then a targeted question
User asks a specific data question?    →  ask
User wants to continue a thread?       →  ask with the previous chat_id
```

## Asking questions

### CLI

```bash
dot "What were total sales last month?"
```

Blocks for 15–60 seconds while Dot runs the full pipeline (tool selection → SQL → execution → visualization), then prints the answer.

### MCP

The MCP server is asynchronous: `ask_dot` returns immediately with a `chat_id`, then you poll with `get_result`. Always insert a `wait` between them so the analysis has time to finish.

```
ask_dot(question="What were total sales last month?")
  → returns: chat_id = "abc-123"

wait(seconds=30)

get_result(chat_id="abc-123")
  → returns the full answer
  → if still running, returns "Still processing" — wait again and retry
```

Typical pattern: `wait(30)` after `ask_dot`, then `get_result`. If still processing, `wait(15)` and try again. Stop polling after ~3 minutes — if it hasn't finished by then, surface the issue to the user.

### Example output (both paths return the same shape)

```
There were $1.2M in total sales last month, up 15% from January.

SQL Query:
  SELECT SUM(amount) AS total_sales
  FROM orders
  WHERE order_date >= '2026-02-01' AND order_date < '2026-03-01'

Data (1 rows x 1 columns):
  total_sales
  1,234,567.89

Data saved to: /tmp/dot/cli-m1abc2d-x4y5z6/df_sales.csv
This chart shows monthly sales trending upward over the past 12 months.

Chart saved to: /tmp/dot/cli-m1abc2d-x4y5z6/viz_monthly.png

Open in Dot: https://app.getdot.ai/?c=cli-m1abc2d-x4y5z6
Follow up: dot "Your next question" --chat cli-m1abc2d-x4y5z6

Suggested follow-ups:
  - Break down by region
  - Compare to last year
```

The MCP path returns the same content as a structured response — charts and CSVs come back as content blocks rather than file paths, so read them through the MCP host instead of `cat`.

### How to handle the response

1. **Text answer** — the natural-language summary at the top. Present this to the user.
2. **Chart image** — if a chart is included (CLI: `Chart saved to: <path>`; MCP: image content block), READ it. You're multimodal — describe what the chart shows.
3. **CSV data** — if data is attached (CLI: `Data saved to: <path>`; MCP: CSV content block), read it when the user needs deeper analysis or custom calculations.
4. **Follow up** — capture the `chat_id` so you can continue the conversation. Pass it on the next call.
5. **Suggested follow-ups** — proactively offer these if relevant to what the user asked.

### Follow-up questions

```bash
# CLI
dot "Now break down by region" --chat cli-m1abc2d-x4y5z6
```

```
# MCP
ask_dot(question="Now break down by region", chat_id="cli-m1abc2d-x4y5z6")
wait(seconds=30)
get_result(chat_id="cli-m1abc2d-x4y5z6")
```

## Discover available data

Returns instantly (no LLM call): connections with table counts, top tables with descriptions / column / row counts, capabilities, custom skills, external assets.

```bash
# CLI
dot catalog
```

```
# MCP
get_catalog()
```

Run this first when the question is vague or you need to know what tables exist.

## Workspace management (CLI only)

Tables, notes, and chat history are managed via the CLI. The MCP server is read-only for now (`get_catalog`, `ask_dot`, `get_result`, `wait`) — for training Dot, drop into a CLI session.

**Tables are the foundation.** Select the right tables and Dot can find the data. The most important thing to document for each table is its granularity (what does one row represent?) and primary key.

```bash
dot tables list [--all]                              # Active tables, grouped by connection
dot tables get <id>                                  # Table details with all columns
dot tables scan <id> [id2 ...] [--concurrency N]     # Refresh samples + descriptions (parallel)
dot tables activate <id> [id2 ...]                   # Flip active flag (run scan first for fresh metadata)
dot tables deactivate <id> [id2 ...]                 # Hide table(s) from Dot
```

For first-time activation run both: `dot tables scan <ids>` then `dot tables activate <ids>` — `scan` samples rows and generates descriptions (10–40s per table, parallelized across multiple IDs), `activate` just flips the flag. For re-enabling a previously-scanned table, `activate` alone is enough.

For complex data models with many columns (semantic layers, Looker explores), also curate which fields are active to reduce ambiguity — especially when multiple columns could mean the same thing.

**Notes are where you spend most of your time.** After tables are set up, notes teach Dot the business logic: metric definitions, operating principles, SQL patterns, and domain context.

```bash
dot notes list                          # List all notes (tree view)
dot notes get <id>                      # Read a note
dot notes create <title> [content]      # Create (also: --file <path> or stdin)
dot notes update <id> [content]         # Update (also: --title, --file)
dot notes delete <id>
dot notes activate <id>                 # Active notes are used by Dot
dot notes deactivate <id>               # Inactive notes are ignored
```

**Chat history** — review what Dot did for any previous query:

```bash
dot chat <chat-id>                      # All messages, SQL, tool calls
```

### Context management strategy

When the user asks you to help manage their Dot workspace:

**1. Be proactive about gaps.** After reading the catalog and existing notes, identify what's missing. Revenue data for a B2B SaaS company but no ARR definition — that's a gap. Orders table but no definition of what counts as a "completed" order — flag it. Think about what a new analyst would need to know on day one.

**2. Interview the expert.** Don't just wait for the user to tell you what to add. Ask targeted questions to pull domain knowledge out of them:
- "How do you define revenue? Booked, recognized, or invoiced?"
- "Should queries filter out internal/test users by default?"
- "When someone asks about 'customers', do they mean accounts or individual users?"

Turn their answers into well-structured notes.

**3. Audit for inconsistency.** Before adding a new note, read the existing ones (`dot notes list`, then `dot notes get <id>` for each). Check that:
- No two notes define the same metric differently
- Filter rules don't contradict each other
- Table references in notes match actually active tables

**4. Front-load, then refine.** Encourage dumping context upfront — business model, key metrics, common filters, known gotchas. It's easier to prune later than to discover gaps one bad answer at a time.

**5. Fix bad answers at the root.** When Dot gives a wrong answer, investigate why:
- Wrong table? → Activate the right one, deactivate misleading ones
- Wrong logic? → Add a note with the correct metric definition or SQL pattern
- Missing context? → Add a business context note about what the user actually wanted

Good notes use strong, unambiguous language: "Always", "Never", "Only use X when Y".

## Cache

CLI responses are cached permanently per question.

```bash
dot "question"                          # Uses cache if available
dot "question" --no-cache               # Force fresh request
dot --clear-cache                       # Wipe all cached responses
```

Use `--no-cache` when the question involves "today", "current", "latest", or the user says "refresh" or "re-run". Follow-ups (`--chat`) are never cached.

The MCP server doesn't expose cache controls — it always runs the full pipeline.

## Error handling

| Error | Meaning | Fix |
|---|---|---|
| `Not authenticated` (CLI) | No token saved | `dot login` |
| `authentication failed (401)` | Token expired or invalid | `dot login` (CLI) or re-authorize the MCP connector |
| `not found (404)` | Resource doesn't exist | Check the ID |
| `connection failed` | Server unreachable | Check internet, verify with `dot status` |
| `request timed out` | Server took too long | Try again — Dot retries automatically on 502/503/504 |
| `Still processing` (MCP) | Background analysis isn't done yet | `wait` and call `get_result` again |
| `Chat not found` (MCP) | Bad `chat_id` passed to `get_result` | Check the ID returned by `ask_dot` |

For manual CLI token setup (headless, CI, no browser):
1. Open Dot dashboard → Settings → Users → API Tokens
2. Create token with `api:full` scope
3. `dot login --token <TOKEN> --server <SERVER_URL>`

## Debugging

```bash
dot status       # Who is logged in, which server, token expiration
dot chat <id>    # Full conversation history with SQL and tool calls
```

## Multi-step analysis

You can orchestrate multi-step data analysis:
1. Run `catalog` to understand available data
2. Ask an initial question
3. Read the CSV output for deeper analysis or custom calculations
4. Ask follow-up questions with the same `chat_id` to refine results
5. Compare results across multiple queries

## Tips

- Be specific: include metric names, time periods, filters
- One question at a time works best
- Use follow-ups (same `chat_id`) to refine rather than compound questions
- For charts: say "show me a chart of..." or "visualize..."
- Start with `catalog` if you're unsure what data exists
- When helping an admin set up Dot, interview them — ask about business model, key metrics, common queries. Create notes from their answers
- Proactively identify gaps in context: if you know the industry and data model, you can predict what definitions are missing
- On MCP, always pair `ask_dot` with `wait` + `get_result`. The answer is **never** in the `ask_dot` response itself

## Feedback

```bash
dot wish "I want better date filtering"
```

Submit a feature request or report an issue. Use `dot wish` whenever the user wants to request a feature, report a bug, or give feedback.

## Examples

```bash
# CLI
dot catalog
dot "What were total sales last month?"
dot "Compare to the same period last year" --chat cli-m1abc2d-x4y5z6
dot "Show me a chart of monthly revenue trend for the past 12 months"
dot "Top 10 customers by order count in Q4 2025, US only"
dot "What were total sales last month?" --no-cache
dot wish "I want better date filtering"
```

```
# MCP
get_catalog()

ask_dot(question="What were total sales last month?")
wait(seconds=30)
get_result(chat_id="<id from ask_dot>")

# Follow-up on the same chat
ask_dot(question="Compare to the same period last year", chat_id="<id>")
wait(seconds=30)
get_result(chat_id="<id>")
```

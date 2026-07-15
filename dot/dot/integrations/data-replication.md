---
description: >-
  Replicate data from your SaaS tools (Stripe, HubSpot, Salesforce, and more)
  into a managed warehouse Dot can query
---

# Data Replication

Data replication copies data from your SaaS tools (Stripe, HubSpot,
Salesforce, and more) into a managed data warehouse that Dot can query.
Once a source is replicated, its tables become part of your data model and
you can ask questions about them in chat exactly like any other connection.

Use it when the data you want to analyze lives in a SaaS product that Dot
can't query directly — replication brings that data into a warehouse on a
schedule so it's always available for analysis.

## How it works

Replication is powered by a separate replicator service that runs
[dlt](https://dlthub.com/) pipelines and loads the extracted data into a
per-organization tenant in Dot's managed data warehouse.

The lifecycle of a replication source is:

1. You pick a source and enter its credentials in **Settings → Connections**.
2. Dot provisions an isolated warehouse tenant for your organization (if one
   doesn't already exist) and stores your (encrypted) credentials.
3. Dot triggers a first **full** sync immediately. (OAuth sources such as
   Google Ads are the exception — see [Authentication](data-replication.md#authentication).)
4. On a schedule you choose, Dot runs **incremental** syncs to keep the data
   fresh.
5. After each successful sync, Dot scans the new tables so they show up in
   your data model and become queryable in chat.

The heavy lifting — extracting from the source API and loading into the
warehouse — happens on the replicator service, so a large first-time load can
run for a long time (minutes to hours for big sources) without blocking Dot.

## Prerequisites

- **Admin access.** All replication management is admin-only.
- **Your organization must be enabled for replication.** Data replication is
  enabled per organization by the Dot team (see
  [Availability](data-replication.md#availability) below). If your organization
  doesn't have data replication enabled, the **Data Replication** section
  simply won't appear in your connections settings.
- **Credentials for the source** you want to replicate (an API key, token, or —
  for OAuth sources — the ability to complete a sign-in flow).

### Availability

{% hint style="info" %}
Replication is opt-in per organization and enabling it is a deliberate,
Dot-side change (it is intentionally _not_ a self-serve feature flag). If you'd
like it turned on for your organization, contact the Dot team.
{% endhint %}

Workspaces inherit their parent organization's access: if the parent
organization is enabled, its workspaces are enabled too.

If your organization is not enabled, the replication API endpoints return
"not found" and the feature stays hidden in the UI — there's no visible locked
state to discover.

## Supported sources

The list of available sources is served live from the replicator, so the exact
set can change over time. Sources are grouped into two quality tiers:

- **Verified** — tested end-to-end by the Dot team against real credentials.
- **Experimental** — available but not yet fully verified by the Dot team.

At the time of writing, the catalog includes:

| Category         | Sources                                            | Tier         |
| ---------------- | -------------------------------------------------- | ------------ |
| Payments         | Stripe                                             | Verified     |
| Customer Success | Vitally                                            | Verified     |
| CRM              | HubSpot, Pipedrive, Salesforce                     | Experimental |
| Support          | Freshdesk, Zendesk                                 | Experimental |
| Communication    | Slack                                              | Experimental |
| Productivity     | Notion, Jira, Airtable, Asana, Google Sheets       | Experimental |
| Developer        | GitHub                                             | Experimental |
| Commerce         | Shopify                                            | Experimental |
| HR               | Workable, Personio                                 | Experimental |
| CMS              | Strapi                                             | Experimental |
| Analytics        | Matomo, Google Analytics                           | Experimental |
| Ads              | Meta Ads, Google Ads                               | Experimental |
| Media            | Mux                                                | Experimental |
| Database         | MongoDB, SQL Database (Postgres / MySQL / MariaDB) | Experimental |
| Generic          | REST API (any JSON REST endpoint)                  | Experimental |

Each source declares its own set of credential fields (for example, Stripe
needs a secret key; Salesforce needs a username, password, and security token;
a SQL database needs a connection URL). The connection form shows exactly which
fields a source requires.

## Setting up a replication source

1. Go to **Settings → Connections**.
2. Scroll to the **Data Replication** section and open a new data source.
3. Pick the source you want from the source picker.
4. Fill in the credential fields the source asks for. Optional fields (for
   example, limiting which tables, schemas, or date range to load) are marked
   as such.
5. Click **Connect**.

Dot then provisions your warehouse tenant (if needed), saves the config, and
kicks off the first full sync right away. You'll see the source appear with a
**Syncing…** status; it flips to **Synced** when the first load finishes.

You can connect **one source of each type** per organization. To replicate two
Stripe accounts, for example, you'd need a second organization or workspace.

### Authentication

Most sources authenticate with an API key or token that you paste into the
connection form. Secret fields (passwords, API keys, tokens, and pasted
service-account JSON) are **encrypted at rest**; non-secret fields (like a
property ID or a backfill start date) are stored in the clear so the form can
show them back to you when editing.

Credentials are **validated on the first sync**, not at the moment you click
Connect. If a credential is wrong, the source will show a **Failed** status
with the error from the replicator — fix the credential (see
[Managing a source](data-replication.md#managing-a-source)) and click
**Sync Now** to retry.

**OAuth sources** (currently Google Ads) work differently: instead of a
credential form you'll see a **Connect** button that opens a sign-in popup.
You approve access with the provider and Dot captures and stores the tokens
server-side — you never copy or paste a token. Because the sign-in itself
proves access, OAuth sources are validated at connect time rather than on the
first sync. Connecting one does **not** kick off an immediate sync, though —
the first load runs on the next scheduled dispatch, or right away if you click
**Sync Now**.

## Sync behavior

- **First sync** is a full load for sources you connect with a credential
  form — it's triggered immediately on connect. OAuth sources (Google Ads) are
  the exception: connecting doesn't trigger a sync, and their first run (on the
  next schedule or via **Sync Now**) is incremental like any other. See
  [Authentication](data-replication.md#authentication).
- **Scheduled syncs** are incremental and run automatically. You choose the
  frequency per source: every **1, 3, 6 (default), 12, or 24 hours**.
- **Sync Now** triggers an immediate manual sync. It always loads
  incrementally, the same as scheduled syncs.
- Only one sync runs per source at a time. While a sync is running the
  **Sync Now** button is disabled; if you trigger one anyway the request is
  rejected with _"A sync is already running for this source."_ A scheduled run
  that overlaps an in-flight sync is skipped until the current one finishes.

While a sync is running, the source card shows progress where the source
supports it — rows loaded so far and the table currently loading. When it
finishes, the status shows the last sync time and the total rows loaded, or the
error if it failed.

A sync that gets stuck (for example, if a worker crashes mid-run) is
automatically reclaimed after 24 hours so scheduled syncs don't stall
permanently.

## Managing a source

From a connected source's card you can:

- **Change the sync frequency** — takes effect on the next scheduled run.
- **Edit credentials** — rotate an API key or update a non-secret field. Leave
  a secret field blank to keep the stored value; only re-type it if you want to
  change it. After saving, click **Sync Now** to validate the new credentials.
- **Sync Now** — trigger an immediate sync.
- **Remove** — click **Edit**, then **Remove** to delete the replication
  config. This stops future syncs but **does not delete data already loaded
  into the warehouse** — the tables remain queryable until you remove them from
  your data model.

## Querying replicated data

Replicated data lands in your organization's managed warehouse tenant, which
appears in Dot as a regular database connection. Each source loads into its own
schema (named after the source — e.g. `stripe`, `hubspot`, `salesforce`).

After a successful sync, Dot automatically scans the replicated schemas so the
new tables are added to your data model. From there you query them just like
any other connection:

- Ask questions in chat that reference the replicated data — Dot picks the
  right tables automatically.
- The replicated tables appear in your model alongside your other connections'
  tables, so you can build relationships, documentation, and reports on them.

The metadata scan is scoped to the schemas created by replication, so it won't
pick up unrelated warehouse internals or other tenants' data.

## Troubleshooting

- **The Data Replication section doesn't appear.** Your organization doesn't
  have data replication enabled — contact the Dot team — or you're not signed
  in as an admin. See [Availability](data-replication.md#availability).
- **A source shows "Failed".** Open the source to read the error. The most
  common cause is an incorrect or expired credential — edit the credential and
  click **Sync Now**. For OAuth sources, use **Reconnect** to refresh access.
- **The first sync is taking a long time.** Large sources (Stripe, HubSpot,
  Salesforce) can take minutes to hours on their first full load. The status
  updates with rows-so-far while it runs; you don't need to keep the page open.
- **I removed a source but its data is still there.** Removing a source stops
  syncing but intentionally leaves already-replicated data in the warehouse.
  Remove the tables from your data model if you no longer want them.

---
description: Connect Dot to REST APIs as data sources
---

# API Connectors

API connectors let you connect Dot to external REST APIs and query them using natural language, just like a database. Instead of writing SQL, Dot automatically selects the right API endpoint, extracts the correct parameters from your question, and returns the data as a table you can analyze and visualize.

## How It Works

1. **Connect** — Select an API type in Settings > Connections, enter your credentials, and click Connect
2. **Sync** — Dot loads the API's endpoint catalog and creates table-like entries in your Model
3. **Ask questions** — Ask questions in natural language. Dot picks the right endpoint, calls the API, and returns the results as a table

API endpoints appear in the Model tab alongside your database tables. You can activate/deactivate them, edit descriptions, and manage them the same way.

## Available Connectors

| Connector | Authentication | Description |
| --------- | -------------- | ----------- |
| [Frankfurter (Exchange Rates)](frankfurter.md) | None (free API) | European Central Bank exchange rates |
| [Stripe](stripe.md) | API Key | Payment processing data — charges, customers, subscriptions, invoices, and more |

More connectors are being added. If you need a specific API integration, [contact support](../../support.md).

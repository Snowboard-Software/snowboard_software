# Stripe

The Stripe connector gives Dot access to your Stripe payment data — charges, customers, subscriptions, invoices, payouts, and more.

## Setup

1. Go to **Settings > Connections**
2. Click **Add Connection** and select **API**
3. Select **Stripe** from the type dropdown
4. Enter your **Stripe Secret Key** (starts with `sk_live_` or `sk_test_`)
5. Click **Connect**

### Getting Your API Key

1. Log in to the [Stripe Dashboard](https://dashboard.stripe.com)
2. Go to **Developers > API Keys**
3. Copy the **Secret key** (you may need to click "Reveal")
4. For testing, use a test-mode key (`sk_test_...`) to avoid touching production data

{% hint style="info" %}
Dot uses **read-only** API calls. It never creates, modifies, or deletes any data in your Stripe account.
{% endhint %}

## Available Endpoints

After connecting, these endpoints appear in your Model:

| Endpoint | Description |
| -------- | ----------- |
| Balance Transactions | Revenue, fees, payouts, and other balance changes |
| Charges | Individual payment charges |
| Customers | Customer records with email, name, and metadata |
| Invoices | Invoice history with amounts and statuses |
| Subscriptions | Active and past subscriptions |
| Products | Your product catalog |
| Payouts | Bank payouts and their statuses |
| Refunds | Refund history |

## Example Questions

* "What was our total revenue last month?"
* "Show me the top 10 customers by lifetime spend"
* "How many new subscriptions were created this quarter?"
* "What's our refund rate over the past 6 months?"
* "List all failed charges from last week"
* "What's the average invoice amount by month?"

## Parameters

Dot extracts filtering parameters automatically from your questions. Common filters include:

| Parameter | Description | Endpoints |
| --------- | ----------- | --------- |
| `created[gte]` / `created[lte]` | Date range filter | All endpoints |
| `status` | Filter by status (e.g., paid, active, failed) | Charges, Invoices, Subscriptions |
| `customer` | Filter by customer ID | Charges, Invoices, Subscriptions |
| `currency` | Filter by currency code | Balance Transactions, Charges |
| `limit` | Number of records to return | All endpoints |

## Data Handling

* **Amounts** are automatically converted from cents to dollars (e.g., Stripe's `2499` becomes `24.99`)
* **Timestamps** are converted from Unix format to readable ISO 8601 dates
* **Pagination** is handled automatically — Dot fetches up to 10,000 records across multiple pages

# Frankfurter (Exchange Rates)

The Frankfurter connector provides access to exchange rate data from the European Central Bank via the free [Frankfurter API](https://frankfurter.dev). No API key is required.

## Setup

1. Go to **Settings > Connections**
2. Click **Add Connection** and select **API**
3. Select **Frankfurter (Exchange Rates)** from the type dropdown
4. The Base URL is pre-filled (`https://api.frankfurter.dev/v1`) — leave it as-is unless you're self-hosting
5. Click **Connect**

## Available Endpoints

After connecting, three endpoints appear in your Model:

| Endpoint | Description |
| -------- | ----------- |
| Latest Exchange Rates | Current exchange rates from the ECB |
| Historical Exchange Rates | Rates for a specific past date |
| Exchange Rate Time Series | Rates over a date range for trend analysis |

## Example Questions

* "What is the current EUR to USD exchange rate?"
* "What was the EUR/GBP rate on 2024-01-15?"
* "How did EUR/USD change over the last month?"
* "Show me exchange rate trends for GBP this quarter"

## Parameters

Dot extracts these automatically from your questions:

| Parameter | Description |
| --------- | ----------- |
| `base` | Base currency code (default: EUR) |
| `symbols` | Target currencies to return (e.g., USD, GBP) |
| `date` | Specific date for historical rates (YYYY-MM-DD) |
| `start_date` / `end_date` | Date range for time series |

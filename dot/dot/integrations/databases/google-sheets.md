---
description: Paste a link and query your spreadsheet like a database table — always the live values.
---

# Google Sheets

A lot of business truth never makes it into the warehouse: budgets, targets, headcount plans, campaign trackers, hand-maintained mappings. Connect those sheets and Dot can answer with them — instead of pretending they don't exist.

There is no export-import loop. Dot reads the sheet live on every query, so answers always reflect what the spreadsheet says right now.

## Prerequisites

* A Google Sheet shared as **Anyone with the link → Viewer**. Dot reads sheets through Google's CSV export, so there is no service account to create and no OAuth flow.
* Data laid out as a table: headers in the first row, one record per row.

## Connect in Dot

1. In Google Sheets, click **Share → Anyone with the link → Viewer** and copy the link.
2. In Dot, go to **Settings → Connections** and choose **Google Sheets**.
3. Paste one or more spreadsheet URLs and connect.

Dot discovers every tab in each spreadsheet, skips the ones that aren't shaped like a table, and creates one table per remaining tab — with a short, descriptive name inferred from the content. Names of tabs you've already synced stay stable across re-connects, so notes and saved questions keep working.

{% hint style="info" %}
Odd delimiters, European decimal commas, extra header rows — Dot samples each tab and configures parsing automatically. If a tab comes out wrong, fix the layout in the sheet and sync again.
{% endhint %}

{% hint style="warning" %}
**Anyone with the link means exactly that.** Anyone holding the URL can view the sheet. Use this for data you'd be comfortable circulating internally, and keep sensitive data in a governed source instead.
{% endhint %}

## Good to know

* **Always fresh** — queries read the live sheet; there is no cached copy to go stale.
* **A table like any other** — sheets appear in your Model where you can activate them, describe them, and use them in questions and dashboards alongside your other sources.

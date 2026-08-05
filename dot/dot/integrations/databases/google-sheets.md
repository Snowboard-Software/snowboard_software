---
description: Ask questions about data that lives in a spreadsheet
---

# Google Sheets

Plenty of useful data never makes it into the warehouse. Targets, headcount plans, and account owners often live in a spreadsheet somebody maintains by hand. Connect that sheet and Dot can answer questions about it, and join it to your warehouse tables.

## Share the sheet

Dot reads your sheet over a link, so the link has to work without a Google login.

1. Open the sheet in Google Sheets and click **Share**.
2. Under general access, choose **Anyone with the link**.
3. Set the role to **Viewer**.

## Connect it

1. Open **Settings → Connections** and add a **Google Sheets** connection.
2. Paste the URL of the sheet.
3. Click connect.

One URL covers one tab. The URL you copy from the address bar points at the tab you are looking at, so open the tab you want first. To bring in more tabs, or more spreadsheets, add a row for each one.

## Keeping it up to date

Dot reads the values live on every query, so edits to rows and cells show up straight away. There is nothing to sync when the numbers change.

Changing the shape of the sheet is different. Adding, renaming, or removing a **column** changes the table Dot queries, so tell Dot about it:

* Click **Sync** on the connection. Modelers use **Sync now** in the connection panel.
* Or set up **Schedule sync** in the connection panel to refresh it daily or weekly, the same as a warehouse.

{% hint style="warning" %}
If a sheet stops being shared with "Anyone with the link", the sync log says how many sheets could not be refreshed. Re-share the sheet and sync again.
{% endhint %}

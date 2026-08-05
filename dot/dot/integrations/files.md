---
description: Drop a CSV or Excel file into Dot and query it like a table.
---

# CSV & Excel Files

Not everything worth analyzing lives in a database. Board exports, vendor reports, one-off extracts, the spreadsheet finance mails around — drop them into Dot and ask your questions, without waiting for anyone to load them into the warehouse first.

There are two ways to use files, depending on how long they should live.

## Attach a file to a chat

Attach a CSV or Excel file directly to your question in the web app. Dot reads it, profiles the columns, and analyzes it in place — ideal for one-off questions where the file *is* the dataset.

## Upload as a lasting table

For files the whole team should query repeatedly, an admin can upload them under **Settings → Connections → Upload Files**. The file becomes a table in your Model like any other source: Dot detects column names and types automatically, you can add descriptions and relationships, and everyone can ask questions against it.

Supported formats: `.csv`, `.xlsx`, and `.xls`.

{% hint style="info" %}
Files are a great on-ramp, not a governance strategy. When a spreadsheet becomes a system of record, move it to a governed source — or connect it as a [Google Sheet](databases/google-sheets.md) so at least everyone reads the same live version.
{% endhint %}

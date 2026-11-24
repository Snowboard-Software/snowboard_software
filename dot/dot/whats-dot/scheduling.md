---
description: Automate recurring reports
---

# Scheduling

Schedule Deep Analysis reports to be delivered automatically via Email, Slack, or Teams.

Unlike dashboard snapshots that show numbers, scheduled reports explain what changed and why—with trends, anomalies, and recommendations included.

### Use Cases

**Meeting prep**: Schedule 30 minutes before recurring meetings. Your team gets context without manually checking dashboards.

**Weekly reviews**: "What changed this week?" delivered Monday morning to Slack—ready for discussion.

**Replace dashboard check-ins**: Instead of pulling data, insights come to you.

### Creating a Schedule

You can schedule a Deep Analysis response or an [app](apps/README.md). On an app, open the menu and pick **Schedule delivery...**.

1. Run a Deep Analysis query
2. Click the **Schedule** button on the response

<figure><img src="../../.gitbook/assets/scheduling-button.png" alt=""><figcaption><p>Click Schedule to set up recurring delivery</p></figcaption></figure>

3. Under **To**, choose the channel (Email/Slack/Teams) and add recipients
4. Under **Name**, keep the chat's or app's title or give the schedule its own. Every message is titled with it
5. Under **Each run**, choose what is sent (see below)
6. Under **Every**, set the frequency: day, weekday, week (pick the day) or month (pick the date), and the time
7. Click **Schedule**

<figure><img src="../../.gitbook/assets/scheduling-dialog.png" alt=""><figcaption><p>Configure channel, recipients, and frequency</p></figcaption></figure>

Click **Test** to send a preview before committing. **Attach PDF** adds a PDF to each delivery. For apps sent by email, **Native** shows the app's images and tables in the email itself. An app too long for one email shows its first part and says the rest is in the app.

### Each Run

| Option | What is sent | Cost |
|--------|--------------|------|
| Latest numbers | The same charts and tables, refreshed. No analysis. | 0.005 ACC |
| Brief | Latest numbers plus a short summary of what changed | 0.25 ACC |
| Fresh analysis | Dot re-investigates and writes up new findings | Metered |

Latest numbers and Brief need queries that can run again. If a message can't be re-run, only Fresh analysis is offered.

### What Recipients Receive

A scheduled report arrives as one message, laid out the same way on email, Slack and Teams. From the top:

1. The schedule's name and the date.
2. Why it came now, when a condition on a chart sent it.
3. The news in one sentence (Brief and Fresh analysis). Brief adds up to two short points.
4. One picture: the answer's first chart, else the first rows of its first table. An app shows its top.
5. A link to **Continue in Dot**, or to **Open** the app. Admins can hide it with **Hide 'View Online' links** under **Settings → Advanced Settings → Sharing & privacy**.
6. The documents: the run's files, one CSV per table, and the PDF when **Attach PDF** is on.

The rest of the run follows below a rule in email, in the thread in Slack, and below a separator in the Teams card. With Fresh analysis, that is the whole analysis. With Latest numbers and Brief, it is the answer's other charts and tables. An app's rest is the app itself, one click away.

The answer's charts, tables and files travel like this:

- Each chart or diagram is drawn in the message.
- Each table shows its first rows in the message, and the whole table comes as a CSV, up to 100,000 rows.
- Files are attached in email and Slack, and linked on a Teams card. A CSV linked on Teams opens for signed-in members of your organization.
- An archive, such as a .zip, is sent only when it is the only file.
- An image file is sent as a file, not drawn. To see a picture in the message, ask for a chart.

Long reports are cut to fit. An email draws tables up to a size limit, and the tables past it come as CSVs only. A Teams card that fills up ends by pointing to the rest in Dot.

The layout is Dot's own: a run can't send its own email, so there is no custom HTML body, style or subject line. The email subject is the schedule's name and the date. When a condition on a chart sent it, the subject names that condition instead of the date. To change what the message holds, ask Dot for the charts, tables and files you want in the answer.

### Managing Schedules

Open the schedule modal on any scheduled message to:
- Edit frequency or recipients
- View run history (past deliveries and costs)
- Delete the schedule

### Only Send When...

Reduce noise by writing a plain-English condition under **Only send when...**. Leave it empty to send every run. Clear the text to remove a condition.

**Examples:**

- _"signups drop below 1,000"_
- _"revenue fell more than 5% week-over-week"_

Dot decides how to answer it:

- **A number on one of the app's charts** (on Latest numbers or Brief): click **Check**. Dot shows what it understood, the value right now, and how often it would have sent over the chart's history. Each run compares the numbers it already refreshed, so quiet runs cost nothing and show as `not_triggered` in run history. Once it sends, the same condition won't send again for at least a day by default.
- **Anything that needs judgement:** Dot runs a Fresh analysis every run and delivers only when your condition holds. Saving switches **Each run** to Fresh analysis, and every run is metered, sent or not. Suppressed reports show as `result_gate_suppressed` in run history.

On a chart in an app, the **Alert me** pill starts a condition for that chart.

### Pre-check on Messages

A scheduled message can have a pre-check that Dot writes for you in chat, based on a condition you describe. It runs first. If it fails, the run is skipped, no credits are used, and run history shows `work_gate_blocked`. The schedule dialog says "Only runs when its pre-check passes". Ask Dot in chat to change it.

{% hint style="info" %}
If the pre-check hits an error, the run goes ahead anyway, so you never silently miss a report.
{% endhint %}

---

### Schedules as Code

Each app schedule is also a file in your model repo at `schedules/{id}.yaml`, so changes can be reviewed like other model changes. If a file edit changes who the run executes as or where it is sent, the schedule pauses until the owner or an admin confirms it in Dot.

### Scheduled Scripts

On workspaces where scheduled scripts are turned on, admins can have the Context Agent set up a Python script that runs on a schedule, at most hourly. It lives in `scheduled_scripts/{slug}/` in the model repo and must be confirmed before it runs. Scripts keep files between runs in a state folder, and can send Slack or email messages through Dot's API. They appear on the **Schedules** page.

---

### Costs & Limits

- **Latest numbers** costs 0.005 ACC (Agent Compute Credit) per run, **Brief** 0.25 ACC, and **Fresh analysis** is metered
- Pre-check blocks do **not** use credits, and neither do runs where a Latest numbers or Brief condition is not met
- A condition on a Fresh analysis **does** use credits (the agent ran, only delivery was held back)

### Admin Feature: Run As User

Admins can schedule reports to run as another user—useful for delivering reports with that user's data permissions.

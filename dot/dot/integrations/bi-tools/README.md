---
description: Connect your BI tools so Dot learns your business logic, and rebuild dashboards as Dot apps
---

# BI Tools

Connect the BI tools your team already uses, like Tableau, Metabase, Sigma, and Qlik. Dot reads your dashboards to learn how your business defines its metrics. That way its answers match the numbers people already trust.

Once a BI tool is connected, there's a second thing you can do: rebuild one of its dashboards as a Dot app.

## Migrate a dashboard to Dot

You can turn a Tableau, Metabase, or Sigma dashboard into a Dot app. Ask Dot to migrate a dashboard by name and it recreates it piece by piece, the same charts and tables and layout, but now backed by live SQL you can question and change in plain language.

Why do this? Some teams want to move off their BI tool and keep the dashboards they rely on. Others just want a live, conversational version sitting next to the original, so anyone can drill in without opening the BI tool.

Dot checks its own work as it goes. For each tile it compares its result against the original and marks whether the two match. When every tile matches, the migration is a true copy of the dashboard. If a tile can't be matched exactly, Dot tells you which one, so you can decide whether the difference matters.

To try it, connect the BI tool first, then ask Dot something like "migrate our Weekly Revenue dashboard from Tableau."

## Connect a BI tool

* [Tableau](tableau.md)
* [Metabase](metabase.md)
* [Sigma](sigma.md)
* [Qlik](qlik.md)

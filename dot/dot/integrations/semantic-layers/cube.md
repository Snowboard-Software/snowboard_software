---
description: Dot answers through your Cube semantic layer, so every number matches your governed definitions.
---

# Cube

If your team has invested in a [Cube](https://cube.dev) semantic layer, your metric logic already lives in one governed place. Connect it to Dot and Dot won't re-derive revenue from raw tables — it asks Cube, so its answers match every other tool built on the same definitions.

## What you need

* Your Cube **REST API endpoint**, for example `https://<deployment>.cubecloud.dev/cubejs-api/v1` (or your self-hosted equivalent)
* An **API token** your Cube deployment accepts

## Connect in Dot

1. Go to **Settings → Connections** and choose **Cube**.
2. Enter the API URL and the token, then connect.

Dot syncs your cubes — measures, dimensions, and joins — into its Model, where you activate the ones Dot should use and enrich them with descriptions.

## How Dot queries Cube

Questions are answered through Cube's REST API, never with raw SQL against the underlying warehouse. That means:

* **Pre-aggregations** accelerate Dot like any other Cube client.
* The **token's security context** applies, so Cube-side access rules keep working.
* Metric math has one home: change a definition in Cube and Dot follows automatically.

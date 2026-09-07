---
description: Run numerical analytics tests with the Dot CLI and use the results as a CI gate.
---

# Evaluations in CI

Run the same [evaluation](../evaluation.md) locally and in CI. The CLI submits the questions, waits for the run, checks the results, and writes reports. Your pipeline can fail when a trusted number changes or a previously passing question regresses.

{% hint style="info" %}
These commands require a Dot CLI release with `dot eval` support and the matching evaluation API. Run `dot eval --help` to check availability. If the command is unavailable, update the CLI after your workspace has received the evaluation CI release.
{% endhint %}

## Before you start

* Install the [Dot CLI](../../integrations/cli.md).
* Create an [API token](README.md) for a user permitted to run evaluations. Use a full API token, rather than an MCP-only token.
* Connect the data and document the metrics Dot should use.
* Use a controlled data snapshot, or regenerate expected answers against the same data target immediately before testing.

Set credentials in your shell or CI secret store:

```bash
export DOT_API_BASE_URL="https://app.getdot.ai"
export DOT_API_TOKEN="YOUR_API_TOKEN"
```

Use `https://eu.getdot.ai` for an EU workspace. The CLI reads the token from the environment, so CI does not need an interactive login.

## Define a suite

Start with `dot eval init suite.json` to generate an example, or save your question set as `suite.json`. Each question needs a stable `id`, `question`, and `expected_answer`. Numeric answer types are `number`, `count`, `currency`, `percent`, and `ratio`. `tolerance_pct` defaults to 3%.

```json
{
  "name": "Sales regression checks",
  "description": "Fixed January 2026 sales fixture. Exclude cancelled orders and subtract refunds from gross revenue.",
  "questions": [
    {
      "id": "january-net-revenue",
      "question": "What was net revenue in USD for completed orders in January 2026?",
      "expected_answer": "900",
      "answer_type": "currency",
      "tolerance_pct": 0,
      "concept_name": "Net revenue",
      "source": {
        "system": "sql_fixture",
        "definition": "Sum gross_amount minus refund_amount for completed orders from 2026-01-01 inclusive to 2026-02-01 exclusive."
      }
    },
    {
      "id": "january-completed-orders",
      "question": "How many completed orders were placed in January 2026?",
      "expected_answer": "4",
      "answer_type": "count",
      "tolerance_pct": 0
    },
    {
      "id": "january-refund-rate",
      "question": "For completed orders in January 2026, what percentage of gross revenue was refunded?",
      "expected_answer": "10%",
      "answer_type": "percent",
      "tolerance_pct": 0
    },
    {
      "id": "january-invalid-amounts",
      "question": "How many completed orders in January 2026 have a negative gross amount, a negative refund amount, or refunds greater than gross amount? Return the count, including zero if there are none.",
      "expected_answer": "0",
      "answer_type": "count",
      "tolerance_pct": 0
    }
  ]
}
```

The answers above use the synthetic dataset below. Replace the questions and answers with reviewed values from your own data when adopting this suite. Question IDs must be unique within the suite. Initial examples may use slugs. After saving, keep the assigned IDs stable when editing a question so file, UI, and exported runs refer to the same tests. A new question can start with a new unique slug.

`concept_name` groups related questions. `source` records the origin of the expected answer; it does not execute a reference query. If you include a BI dashboard source, preserve the provenance fields from the exported evaluation.

### Reproduce the example

Create the fixture in a test PostgreSQL database connected to Dot:

```sql
CREATE SCHEMA IF NOT EXISTS evaluation_ci;
CREATE TABLE evaluation_ci.orders (
  order_id integer PRIMARY KEY,
  order_date date NOT NULL,
  status text NOT NULL,
  gross_amount numeric(12, 2) NOT NULL,
  refund_amount numeric(12, 2) NOT NULL
);
INSERT INTO evaluation_ci.orders VALUES
  (1, '2026-01-03', 'completed', 100, 0),
  (2, '2026-01-10', 'completed', 200, 0),
  (3, '2026-01-18', 'completed', 300, 100),
  (4, '2026-01-31', 'completed', 400, 0),
  (5, '2026-01-15', 'cancelled', 500, 0),
  (6, '2026-02-01', 'completed', 700, 0);
```

Activate and scan this table in Dot. Add a note defining net revenue as gross amount minus refunds, using completed orders and `order_date` for the reporting period. Use a dedicated evaluation environment so these questions refer to the fixture rather than another orders table.

For January completed orders, gross revenue is 1,000 USD, refunds are 100 USD, and net revenue is 900 USD. There are four orders, refunds are 10% of gross revenue, and zero orders violate the amount checks. The cancelled order and February order catch missing status and date filters.

Run the suite to establish a baseline. To prove your CI gate catches failures, change only the net-revenue expected answer to `1000` in a temporary copy and run it without a baseline: a 900 USD answer must fail the exact check. Restore the reviewed expectation of `900` afterward. To test a context regression, change the net-revenue definition in a candidate environment, compare against the passing baseline, then restore the definition and rerun.

## Save once, then run

Create the evaluation once:

```bash
dot eval create suite.json
```

The command saves the evaluation and updates the file with its `evaluation_id` and the assigned question IDs and canonical fields. Commit that updated file to Git. Reuse it for subsequent CI runs; calling `create` again on a saved suite is rejected.

```bash
dot eval run suite.json --target production \
  --output artifacts/evaluation.json \
  --junit artifacts/evaluation.xml
```

The command waits for completion and uses the questions in the file for that run. You can also run an existing saved evaluation by supplying its ID instead of a JSON file.

To start from a question set created in the web UI:

```bash
dot eval list
dot eval export YOUR_EVALUATION_ID --output suite.json
```

Export writes a new file and refuses to overwrite an existing one.

### Check a candidate environment

Use an environment ID to test context changes before promoting them:

```bash
dot eval run suite.json --target YOUR_ENVIRONMENT_ID \
  --expect-commit YOUR_DOT_CONTEXT_COMMIT \
  --output artifacts/evaluation.json
```

`--expect-commit` checks the Dot context revision being evaluated. Use the revision in Dot, which may differ from your application or dbt repository's Git commit. It does not sync a branch or pin warehouse data. Set up the environment and its [warehouse target](../environments.md#work-against-your-dbt-dev-target) first.

### Set the release gate

The default minimum pass rate is 100%. To accept a lower rate, set it explicitly:

```bash
dot eval run suite.json --target production --min-pass-rate 95
```

Errors and incomplete runs always fail the gate, even with a lower pass-rate threshold. An empty or invalid suite is an error, not a passing run.

| Exit code | Meaning |
| --- | --- |
| `0` | The completed run satisfies the gate. |
| `1` | Numerical results do not satisfy the pass-rate or regression gate. |
| `2` | Configuration, execution, incomplete-run, or baseline-compatibility error. |

Do not use `continue-on-error` or `|| true` on the evaluation command when its result should block a release.

### Compare with a baseline

Choose a previously reviewed run as the baseline:

```bash
dot eval run suite.json --target YOUR_ENVIRONMENT_ID \
  --baseline YOUR_BASELINE_RUN_ID \
  --output artifacts/evaluation.json
```

A baseline must use the same question fingerprint as the new run. Changing the questions, expected answers, or tolerances requires a compatible baseline. The gate rejects a newly failing question that passed in the baseline, even when the overall pass rate remains above your threshold. Errors always fail closed.

### Bound execution

The default timeout is 1,800 seconds. Set another timeout for your pipeline:

```bash
dot eval run suite.json --target production --timeout 900
```

On timeout or interruption, the CLI requests cancellation and exits with code `2`. If cancellation cannot be confirmed, it prints the run ID and a cancellation command.

Use `--idempotency-key` when retrying the same logical run after a connection failure. Reuse the key with the same request; use a new key for a new run.

## GitHub Actions

Commit `suite.json` with its saved `evaluation_id`. Add `DOT_API_TOKEN` as a GitHub Actions secret. This workflow runs on manual dispatch and pull requests within the same repository and saves both report formats even if a test fails. The CLI automatically appends the gate result, failures, context commit, and run link to `GITHUB_STEP_SUMMARY`.

```yaml
name: Evaluate Dot

on:
  workflow_dispatch:
  pull_request:
    paths:
      - 'suite.json'
      - '.github/workflows/evaluate-dot.yml'

permissions:
  contents: read

jobs:
  evaluate:
    if: github.event_name == 'workflow_dispatch' || github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    timeout-minutes: 35
    env:
      DOT_API_BASE_URL: https://app.getdot.ai
      DOT_API_TOKEN: ${{ secrets.DOT_API_TOKEN }}
    steps:
      - uses: actions/checkout@v4

      - name: Install Dot
        shell: bash
        run: |
          curl -fsSL "$DOT_API_BASE_URL/install" -o "$RUNNER_TEMP/install-dot.sh"
          sh "$RUNNER_TEMP/install-dot.sh"
          echo "$HOME/.local/bin" >> "$GITHUB_PATH"

      - name: Evaluate
        id: evaluation
        shell: bash
        run: |
          dot --version
          dot eval run suite.json --target production \
            --timeout 1800 \
            --idempotency-key "gh-${GITHUB_RUN_ID}-${GITHUB_RUN_ATTEMPT}" \
            --output artifacts/evaluation.json \
            --junit artifacts/evaluation.xml

      - name: Upload reports
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: dot-evaluation-${{ github.run_id }}-${{ github.run_attempt }}
          path: artifacts/
          if-no-files-found: warn
```

This example tests Production against committed expectations. To gate candidate context, prepare an environment before the evaluation step, then supply its ID and expected Dot context commit. Add your context or metric files to the workflow's `paths` filter as appropriate.

Fork pull requests skip this job because GitHub does not provide the workspace secret to them. The job's artifacts remain available after numerical failures. If setup fails before a report exists, the failed job and its logs identify the error.

## Inspect a report

Progress goes to stderr. Add `--json` for JSON-only stdout; `--output` saves the same report to a file. Reports include `schema_version`, `run_url`, the gate decision in `gate`, and the API run with its question results in `run`.

```bash
dot eval results YOUR_RUN_ID --json
dot eval compare YOUR_BASELINE_RUN_ID YOUR_RUN_ID --output comparison.json
dot eval cancel YOUR_RUN_ID
```

`results` and `compare` read stored results and apply the gate without asking the agent again. JUnit reports include question results and a release-gate failure/error when the overall check does not pass. Files may contain business questions and answers; use your normal access and retention settings for CI artifacts.

## Use dbt in the same pipeline

Run `dbt build` against your test target before evaluating. If your expected values come from dbt or MetricFlow, use your existing tooling to calculate them and write the numerical answers into `suite.json`. Point the Dot environment at that same target.

Keep the metric definition revision and data snapshot with your CI evidence. `--expect-commit` verifies Dot's context revision; it does not establish that the dbt build or warehouse snapshot is identical.

## Troubleshoot a failed check

* **Numeric mismatch:** compare expected and observed values, then open the linked conversation to inspect the query and business logic.
* **No usable answer:** inspect the conversation for missing data, permissions, or an ambiguous question. Evaluation can send one follow-up before reporting the result.
* **Authentication failure:** check the token, API scope, user permissions, and regional server URL.
* **Commit mismatch:** finish syncing the intended Dot context and use its actual revision.
* **Baseline mismatch:** compare the suite definitions and choose a baseline for the same question fingerprint.

## Call the API directly

For an existing evaluation, start a run with the same regional URL and API token:

```bash
curl --fail-with-body \
  -H "X-API-KEY: $DOT_API_TOKEN" \
  -H 'Content-Type: application/json' \
  "$DOT_API_BASE_URL/api/evaluations/YOUR_EVALUATION_ID/runs" \
  --data '{"trigger":"api","target":{"kind":"production"},"idempotency_key":"release-42-attempt-1"}'
```

Use the returned `id` to poll `GET /api/evaluation_runs/{id}` or request cancellation with `POST /api/evaluation_runs/{id}/cancel`. A run status of `completed` does not establish that the answers passed; inspect the results and error count, or use `dot eval results` to apply the CLI gate.

The create-run request accepts these optional fields:

| Field | Purpose |
| --- | --- |
| `target` | `{"kind":"production"}` or `{"kind":"environment","environment_id":"…"}`. |
| `questions` | A per-run question snapshot, using the suite's question objects and stable IDs. Omit to use the saved evaluation's questions. |
| `expected_target_commit` | Full lowercase 40-character Dot context SHA that must match the target. |
| `idempotency_key` | Reattach to an accepted run when replaying the same request. |
| `metadata` | String key/value pairs for your source revision and CI job identifiers. |
| `trigger` | `api`, `cli`, or `manual`; use `api` for direct integrations. |

The CLI records GitHub repository, source SHA, run ID, and attempt from the GitHub Actions environment when present. Those identifiers are separate from the captured Dot target commit.

See the [evaluation API reference](https://test.getdot.ai/redoc#tag/evaluations) for saved-evaluation creation, question management, and complete request/response schemas.

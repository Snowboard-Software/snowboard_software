---
description: Run trusted business questions as a CI check.
---

# Evaluations in CI

Use an [evaluation](../evaluation.md) to check that Dot still answers your business questions correctly after a change. The CLI waits for results, fails the check when answers miss the gate, and saves JSON or JUnit reports.

Already have an evaluation? Open **Run in CI** in Dot to download its questions and copy a workflow for your workspace.

## 1. Connect

Install the [Dot CLI](../../integrations/cli.md) (0.3.1 or later) and create a [full API token](README.md) for a user allowed to run evaluations.

```bash
export DOT_API_BASE_URL="https://app.getdot.ai" # EU: https://eu.getdot.ai
export DOT_API_TOKEN="YOUR_API_TOKEN"
export DOT_ENV="" # Saved evaluation is in Production.
```

Use an environment ID for `DOT_ENV` when working with a draft evaluation. Keep CI tokens in your CI secret store.

## 2. Save a suite

Save this as `suite.yaml`, replacing the question and answer with a trusted value from your data:

```yaml
name: Revenue checks
questions:
  - question: What was net revenue in EUR for January 2026?
    expected_answer: "125000"
    answer_type: currency
    unit: EUR
    tolerance_pct: 3
```

JSON works too. Expected answers can be numbers or ISO dates; quote dates and formatted values in YAML. Numeric tolerance defaults to 3%; use `0` for an exact check. Use stable data, or refresh expected answers against the same data Dot will query.

```bash
dot eval validate suite.yaml
dot eval create suite.yaml
```

`validate` is offline. `create` saves once and writes evaluation and question IDs into the file. Commit that updated file and keep its IDs when editing questions.

To use an existing evaluation instead:

```bash
dot eval export YOUR_EVALUATION_ID --output suite.json
```

Exported suites are portable snapshots. They have a different schema from the model repository's `evaluations/*.yaml` files; use `export` to convert.

## 3. Preview and run

```bash
dot eval run suite.yaml --target production --dry-run
dot eval run suite.yaml --target production \
  --output artifacts/results.json --junit artifacts/results.xml
```

The preview starts no agent and spends no evaluation credits. The run grades the file's questions without changing the saved definition. Open the report's run link to investigate failures.

**Environment selection:** `DOT_ENV` selects the saved evaluation; `--target` selects the context and warehouse overrides to test. Replace `production` with an environment ID to test a candidate, even if that environment predates the suite. Without `--target`, execution uses the active environment or Production. If you supply an evaluation ID instead of a file, the target must contain its saved definition.

The default gate requires every question to pass:

| Exit | Meaning |
| --- | --- |
| `0` | Gate passed. |
| `1` | Answers failed the pass-rate or regression gate. |
| `2` | Invalid setup, execution error, or incomplete results. |

Useful options:

* `--baseline RUN_ID` also rejects newly failing questions. The baseline must match the questions, expected answers, types, units, and tolerances.
* `--min-pass-rate 95` allows some mismatches; errors still fail.
* `--expect-commit SHA` requires an exact Dot context revision. Read it with `dot eval target --target ENV_ID --json`.

See `dot eval --help` for timeout, cancellation, and report commands.

## GitHub Actions

Commit your saved `suite.yaml`, add `DOT_API_TOKEN` as a repository secret, and save this as `.github/workflows/evaluate-dot.yml`. Run it from GitHub's **Actions** tab.

```yaml
name: Evaluate Dot
on: workflow_dispatch
permissions:
  contents: read
jobs:
  evaluate:
    runs-on: ubuntu-latest
    timeout-minutes: 35
    env:
      DOT_API_BASE_URL: https://app.getdot.ai
      DOT_API_TOKEN: ${{ secrets.DOT_API_TOKEN }}
      DOT_ENV: ""
    steps:
      - uses: actions/checkout@v4
      - name: Install Dot
        run: |
          curl -fsSL "$DOT_API_BASE_URL/install" -o "$RUNNER_TEMP/install-dot.sh"
          sh "$RUNNER_TEMP/install-dot.sh"
          echo "$HOME/.local/bin" >> "$GITHUB_PATH"
      - name: Evaluate
        run: |
          dot eval validate suite.yaml
          dot eval run suite.yaml --target production \
            --output artifacts/results.json --junit artifacts/results.xml
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: evaluation-results
          path: artifacts/
```

For direct integrations, see the [evaluation API reference](https://test.getdot.ai/redoc#tag/evaluations).

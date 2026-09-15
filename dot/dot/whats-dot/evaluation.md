---
description: Test Dot against trusted numbers in the UI, terminal, or CI pipeline.
---

# Evaluation

Evaluations check whether Dot answers your business questions correctly. Pair each question with a trusted number, run the set against Production or an environment, and inspect the differences. You can use the same evaluation in the web UI and your CI pipeline, independently of Train.

Start with a few questions that matter: revenue after refunds, paying customers, conversion rate. A single number makes each result easy to understand and each regression easy to investigate.

## Write a useful test

Each question should identify a metric, time period, and any relevant filters. Keep the wording close to what your users ask. Put the business definition in Dot's context so the test checks whether Dot uses it correctly.

For example:

> What was our net revenue in January 2026, in USD?

Use a trusted dashboard, reviewed SQL, or governed metric to obtain the expected value. Record where it came from. Avoid creating expected answers from the same agent response you are testing.

Choose a stable dataset. A closed month can still change after a backfill, so use a controlled warehouse snapshot for repeatable regression tests. When testing live data, refresh the expected answers against the same data Dot will query.

## What a result means

Dot extracts the answer and compares it with the expected value. For a nonzero expected value, the relative difference is:

```text
abs(observed − expected) / abs(expected) × 100
```

The default tolerance is **3%**. Set `tolerance_pct` to `0` for an exact check or to another percentage appropriate for the metric. For example, `tolerance_pct: 1` means 1%, not 0.01%.

| Result | Meaning |
| --- | --- |
| Pass | The observed answer satisfies the comparison. |
| Fail | Dot returned an answer outside the allowed tolerance. |
| Error | The question could not be evaluated successfully. |
| Pending | The question has not finished. |

Percentage answers support percentage/ratio normalization, such as `25%` and `0.25`. Use `answer_type: "percent"` and write the unit in the question. Counts and currency do not receive this normalization.

For an expected value of zero, the current scorer reports zero difference when the observed value is zero and 100% difference otherwise. Use a tolerance below 100% when zero must remain zero.

{% hint style="info" %}
Evaluation currently runs Dot in Economy mode. If the first response asks for clarification or does not provide a usable answer, the runner can send one follow-up requesting a best-effort answer. The score includes that recovery attempt; it is not a separate measurement of first-response accuracy or another energy mode.
{% endhint %}

## Use the web UI

Open **Model → Evaluation**, choose **New evaluation**, and follow the setup conversation to create a question set with trusted expected answers. Use the [environment switcher](environments.md) to select the saved evaluation version you want to test, then start a run against that environment (or Production). Inspect failed questions using their expected and observed values and linked conversations.

CLI runs preserve the questions recorded at submission. Their web view shows that snapshot, including questions added or changed in a suite file. Choose **View saved questions** to edit the persisted question set for future runs, then **View run** to return to the recorded results. **Run saved questions** runs the saved set; use the CLI to rerun a file with different questions.

Choose **Run in CI** for a guided setup: download the saved questions, check the regional server, and copy terminal commands or a GitHub Actions workflow. The setup shows the saved-question count explicitly. Run details identify the tested Dot context commit and, when available, the originating CI job and source revision.

A completed run means that processing finished. It does not mean every question passed. Look at the question results and error count when deciding whether a change is ready.

Use **Needs attention** to focus on failed questions, execution errors, or missing expected answers. Search by question or metric to find a specific check. Filtering the table leaves the overall run score unchanged; choose **All** and clear the search to restore the full list.

<figure><img src="../../.gitbook/assets/evaluation-ci-triage.png" alt="Needs attention filter showing the net-revenue and refund-rate failures while the overall result stays at two of four questions passing"><figcaption><p>Removing a 100 USD refund produces two failures. Needs attention focuses the table on those checks while preserving the full run score.</p></figcaption></figure>

## Keep evaluations in Git

Evaluations are saved as `evaluations/<evaluation-id>.yaml` in Dot's model repository. Each environment has its own version of the file. Changes stay in that environment until you merge them to Production, and the files participate in [GitHub](version-control/github.md) and [GitLab](version-control/gitlab.md) sync.

Every save creates a commit. Open **History** on an evaluation to inspect an older version read-only or restore it as a new commit. Archiving keeps the file, its history, and previous runs. CLI and API runs retain their question snapshots and results when the saved definition changes. Eligible manual runs can be regraded when you correct an expected answer or tolerance in the UI. Once a linked training freezes its evaluation version, subsequent evaluation edits do not change the ground truth it grades against.

For terminal and CI workflows, the [Dot CLI](../integrations/cli.md) accepts a portable suite in JSON or YAML. `dot eval create` saves it in the selected environment and writes the evaluation ID and assigned question IDs back into the suite. Commit that updated suite and retain the IDs when editing existing questions.

| File | Purpose |
| --- | --- |
| `evaluations/<evaluation-id>.yaml` in the model repository | Dot's saved definition, including identity, audit metadata, and questions; edited and promoted through the environment lifecycle. |
| `suite.json` or `suite.yaml` in your CI repository | A portable question snapshot accepted by the CLI; exported suites use JSON. Running it does not update the saved definition. |

These formats have different schemas. Use `dot eval export` to produce a CLI suite from a saved evaluation; do not pass a model-repository file directly to `dot eval run`.

```bash
export DOT_ENV="" # Save and read the evaluation in Production.
dot eval create suite.json
dot eval validate suite.json
dot eval run suite.json --target production --dry-run
dot eval run suite.json --target production \
  --output artifacts/evaluation.json \
  --junit artifacts/evaluation.xml
```

See [Evaluations in CI](api/evaluations-in-ci.md) for the suite format, setup, exit codes, baseline comparisons, and a complete GitHub Actions workflow.

## Improve an answer

When a test fails, open its conversation and inspect the query and answer. Check whether Dot selected the right data, applied the metric definition, and used the requested dates and filters. Update the relevant [notes](model/notes.md) or table documentation in an environment, then rerun the same questions against the same data.

Keep the expected value fixed while correcting a regression. Change it when the approved business definition or source data changes, and review that change alongside its source.

## Use existing dbt definitions

Dot can use the [dbt Semantic Layer](../integrations/semantic-layers/dbt-semantic-layer.md) during analysis. Your evaluation can use those same governed definitions as the source of expected numbers.

Run your existing dbt, MetricFlow, or warehouse tooling to calculate the expected values, write them into the suite JSON, and run Dot against the matching data target. The evaluation CLI accepts expected answers; it does not execute reference dbt metrics or SQL from the suite.

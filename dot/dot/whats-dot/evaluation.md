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

Open **Evaluations**, choose **New evaluation**, and follow the setup conversation to create a question set with trusted expected answers. Choose Production or an [environment](environments.md) as the target and start a run. Inspect failed questions using their expected and observed values and linked conversations.

CLI runs preserve the questions recorded at submission. Their web view shows that snapshot, including questions added or changed in a suite file. Choose **View saved questions** to edit the persisted question set for future runs, then **View run** to return to the recorded results. **Run saved questions** runs the saved set; use the CLI to rerun a file with different questions.

A completed run means that processing finished. It does not mean every question passed. Look at the question results and error count when deciding whether a change is ready.

## Keep evaluations in Git

The [Dot CLI](../integrations/cli.md) lets you save an evaluation as JSON, review changes to its questions and expected answers, and run it from your terminal. Stable question IDs keep results associated with the same test as wording and definitions evolve. `dot eval create` saves the evaluation and updates the suite file with the evaluation ID and assigned question IDs. Commit the updated file and retain those IDs when editing existing questions.

```bash
dot eval create suite.json
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

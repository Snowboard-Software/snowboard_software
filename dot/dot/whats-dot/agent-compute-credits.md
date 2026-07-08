---
description: What Agent Compute Credits are and how Dot measures usage
---

# Agent Compute Credits

Dot usage is measured in Agent Compute Credits (ACCs). An ACC reflects the amount of work Dot does to answer a request. A quick lookup uses very little. A complex, multi step investigation uses more.

You purchase a pool of ACCs, and each request draws from that pool based on the work it takes to answer.

### What consumes ACCs

When Dot answers a question, it does real work behind the scenes. The main drivers of cost are:

- Database queries it runs
- Reasoning steps it takes
- Visualizations it builds
- Web searches, when they are enabled

The more steps a question needs, and the more data Dot has to explore, the more ACCs it uses.

### Rough guidance

The figures below are averages for orientation, not fixed prices. Actual usage depends on the specific question.

| Type of request | Typical cost |
|---|---|
| Simple question, returning a number with a chart and the underlying data | about 1 ACC |
| Data governance question | about 0.5 ACC |
| [Deep Analysis](deep-analysis.md) | 2 to 15 ACCs |

### Why the same question can vary

Dot is built on large language models, which are not deterministic. The same question can take a slightly different path from one day to the next, so it might use 2 ACCs today and 5 tomorrow. Treat the numbers above as a guide and plan with a small buffer.

### Keeping usage predictable

Admins can set limits on how many ACCs a single user or a group of users can consume. This keeps spend predictable and stops any one user from drawing down the pool unexpectedly. You configure these limits in Dot's settings.

{% hint style="info" %}
You can also keep Dot focused with a note in its context, for example to answer only questions about your business data and to politely decline off topic requests. This improves answers and saves ACCs, because Dot declines early instead of doing the work.
{% endhint %}

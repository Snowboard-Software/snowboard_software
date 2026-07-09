---
description: What Agent Compute Credits are and how Dot measures usage
---

# Agent Compute Credits

Dot usage is measured in Agent Compute Credits (ACCs). An ACC reflects the amount of work Dot does to answer a request. A quick lookup uses very little. A complex, multi step investigation uses more.

### What consumes ACCs

When Dot answers a question, it does real work behind the scenes. The main drivers of cost are:

- The database queries it runs
- The reasoning steps it takes
- The computation to process and analyze the data
- The visualizations it builds
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

The cost of a question is not fixed. Dot is developed continuously, the underlying large language models are updated regularly, and the context Dot works with keeps changing. As a result, the same question can take a different path and a different amount of work over time, whether you ask it twice on the same day or weeks apart. It might use 1.5 credits today, 1.7 tomorrow, and 0.9 the day after. The numbers here are a guide, not a guarantee.

### How to think about total usage

Total credit consumption is roughly the product of three things:

**Number of users × tasks per user × complexity per task**

Each factor pushes usage up on its own. When all three grow together, total consumption can climb quickly over time, so it helps to keep an eye on all three.

### Keeping usage predictable

Admins can set limits on how many ACCs a single user or a group of users can consume. This keeps spend predictable and stops any one user from drawing down the pool unexpectedly. You configure these limits in Dot's settings.

{% hint style="info" %}
You can also keep Dot focused with a note in its context, for example to answer only questions about your business data and to politely decline off topic requests. This improves answers and saves ACCs, because Dot declines early instead of doing the work.
{% endhint %}

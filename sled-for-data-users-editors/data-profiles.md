---
description: show the shape of your data
---

# Data Profiles

<figure><img src="../.gitbook/assets/grafik (1).png" alt=""><figcaption></figcaption></figure>

The first time any users visits a table page, a data profile is generated. This profile can be manually refreshed with  `🔄️Profile`.\
\
It generates a sample of 100k rows for every table or view, computes data quality metrics and the data profiles. If it can not compute a profile for a view within 5 minutes it will stop. The sampler is super fast, even for big tables (TBs) the calculation usually completes within 5 minutes.

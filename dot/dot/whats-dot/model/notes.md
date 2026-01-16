---
description: Context is all you need
---

# Notes

Notes allow you to add useful context to Dot or to provide instructions on how to behave in certain situations. Helping business users with their data questions or creating an impactful churn analysis requires Dot to understand more about your business and your information architecture than can be found on the internet (usually). 

Here are four types of notes that we found to be most useful:

## Organization Notes

This is Wikipedia style knowledge about your company, the products and services your selling, the internal processes that you follow, etc. While these things can change aim to go top down and start with the things that are probably still true two years from now.

**Example**

```
TinyTrucks is a children's toy company. 
We manufature educational and entertaining toy trucks.
We sell directly them online to parents in Europe and the US.
```

The example is a lot shorter than what you usually want to add as background. 



## Agent Operating Principles

These are instructions on how to behave in certain situations and what principles to follow. The key is to write these as instructions and to use strong language with words like: `Always`, `Never`, `Only`

**Example**

```
Always clarify with the user if they want live or booked revenue when they ask about revenue.
Always by default filter out internal users (IS_INTERNAL = FALSE).
Always use the table fct_arr_consolidated when this table is enough to answer questions about ARR.
Never answer questions about a/b tests and rather refer them to https://experiments.internal.com
```



## Playbooks / Use Cases

For your high value use cases, you already have a lot of intuition and tribal knowledge on how to analyze certain situations. For example, when you review a marketing campaign, you have your go to data sources, you know which metrics you care most about, how you think about attribution etc. 

Playbooks are about encoding and documenting this knowledge, so that the analytics agent can replicate it.

**Example**

{% code overflow="wrap" expandable="true" %}
````
# Use Case: Marketing Campaign Review Report

This prompt generates a comprehensive performance review for a digital marketing campaign, focusing on key channels like **Google Ads and Facebook Ads**. The report MUST analyze performance against KPI targets, segmented by **Channel, Audience Type (Prospecting vs. Retargeting), and Creative Format**. It provides a clear narrative on what's working and what isn't, projects end-of-campaign outcomes, and offers actionable recommendations for optimization.

---
## Important Notes:
- When referring to KPI performance, always specify which of the following you are referring to: **Spend-to-Date (STD), Campaign Target, Current Attainment, or Pacing Projection**.
- KPIs like **Cost Per Acquisition (CPA)** and **Cost Per Click (CPC)** are efficiency metrics; a value higher than the target indicates underperformance.
- **Return On Ad Spend (ROAS)** = (Total Conversion Value / Total Spend).
- All "overall" language MUST read **“Overall Campaign ROAS”** or **“Overall Campaign CPA”**.
- **Channel Groups**: Group all Google Ads campaigns → **Paid Search**; group all Facebook/Instagram Ads campaigns → **Paid Social**.
- **Audience Types**: Group campaigns targeting new users (e.g., based on interests, lookalikes, keywords) → **Prospecting**. Group campaigns targeting past website visitors or customer lists → **Retargeting**.
- Use **UTM parameters** as the primary source for consistent cross-channel tracking.
- Exclude all data where `utm_campaign` contains "test" or "internal".
- Ensure the **same aggregated dataset** is used for the summary narrative and the charts to avoid discrepancies.
- **Formatting**: Money as **$X,XXX** or **$X.XK**; percentages with **one decimal place + "%"**; ROAS as a ratio like **X.X:1**.
- **Chart Order**: In channel comparisons, always show **Paid Search, Paid Social**. In audience comparisons, show **Prospecting, Retargeting**.
- Use safe division (`NULLIF(denominator, 0)`) in all calculations.
---
## **Introduction**
Evaluating the performance of digital advertising campaigns requires a consolidated view across multiple platforms. Siloed reports from Google and Facebook make it difficult to assess overall effectiveness and make strategic budget decisions. This report template unifies critical data into a single, actionable review, allowing marketing teams to quickly identify top-performing channels, audiences, and creatives, and to optimize spend for maximum return.
---
## Definitions
### 1) Key Performance Indicators (KPIs)
- **Spend**: The total amount of money spent on advertising.
- **Impressions**: The number of times ads were shown.
- **Clicks**: The number of clicks on ads.
- **Click-Through Rate (CTR)**: The percentage of impressions that resulted in a click (`Clicks / Impressions`).
- **Cost Per Click (CPC)**: The average cost for each click (`Spend / Clicks`).
- **Conversions**: The number of desired actions completed (e.g., purchases, leads).
- **Cost Per Acquisition (CPA)**: The average cost for each conversion (`Spend / Conversions`).
- **Return On Ad Spend (ROAS)**: The total revenue generated for every dollar spent (`Revenue / Spend`).
### 2) Core Segments
- **Channels**: Paid Search (Google Ads), Paid Social (Facebook/Meta Ads).
- **Audience Types**: Prospecting (reaching new customers), Retargeting (re-engaging past visitors).
- **Creative Formats**: Video, Image, Carousel, Text Ad.
---
## Query Templates:
```
-- Fetch overall campaign KPIs vs targets
SELECT
  SUM(spend) AS total_spend,
  SUM(revenue) AS total_revenue,
  SAFE_DIVIDE(SUM(revenue), SUM(spend)) AS overall_roas,
  SAFE_DIVIDE(SUM(spend), SUM(conversions)) AS overall_cpa
FROM
  `your_project.your_dataset.marketing_campaign_data`
WHERE
  date BETWEEN '{{start_date}}' AND '{{end_date}}'
  AND campaign_name = '{{campaign_name}}';
-- Note: Targets are often stored in a separate table or spreadsheet and joined.
```
```
-- Breakdown performance by channel and audience type
SELECT
  channel,          -- 'Paid Search', 'Paid Social'
  audience_type,    -- 'Prospecting', 'Retargeting'
  SUM(spend) AS spend,
  SUM(revenue) AS revenue,
  SAFE_DIVIDE(SUM(revenue), SUM(spend)) AS roas,
  SAFE_DIVIDE(SUM(spend), SUM(conversions)) AS cpa
FROM
  `your_project.your_dataset.marketing_campaign_data`
WHERE
  date BETWEEN '{{start_date}}' AND '{{end_date}}'
  AND campaign_name = '{{campaign_name}}'
GROUP BY
  channel, audience_type;
```
```
-- Get daily ROAS to plot performance over time
SELECT
  date,
  SAFE_DIVIDE(SUM(revenue), SUM(spend)) AS daily_roas
FROM
  `your_project.your_dataset.marketing_campaign_data`
WHERE
  campaign_name = '{{campaign_name}}'
GROUP BY
  date
ORDER BY
  date ASC;
```
```
-- Identify the best and worst performing ads by ROAS or CPA
(SELECT ad_name, SAFE_DIVIDE(SUM(revenue), SUM(spend)) AS roas FROM `your_project.your_dataset.marketing_campaign_data` WHERE campaign_name = '{{campaign_name}}' GROUP BY ad_name ORDER BY roas DESC LIMIT 5)
UNION ALL
(SELECT ad_name, SAFE_DIVIDE(SUM(revenue), SUM(spend)) AS roas FROM `your_project.your_dataset.marketing_campaign_data` WHERE campaign_name = '{{campaign_name}}' GROUP BY ad_name ORDER BY roas ASC LIMIT 5);
```
---
## **Output to User: Follow this format in your response**
---
## Marketing Campaign Review: Q4 Holiday Sale
### 📝 Executive Summary
The Q4 Holiday Sale campaign is performing above target, achieving an **Overall ROAS of 4.2:1** against a goal of 3.5:1, and a **CPA of $28** against a target of $35. **Paid Social (Facebook/Instagram) is the primary driver of this success**, especially with video creative targeted at retargeting audiences. **Paid Search (Google Ads) is currently underperforming**, with high CPCs on non-branded keywords diluting overall profitability. Immediate action is recommended to re-allocate 20% of the remaining Paid Search budget to top-performing Paid Social campaigns.
### 💡 Key Insights & Recommendations
-   **Overall Performance**: The campaign is profitable and on track to exceed its revenue goals by an estimated 15%.
-   **Channel Performance**: Paid Social is delivering a **5.8:1 ROAS**, while Paid Search is lagging at **2.1:1 ROAS**.
    -   **Recommendation**: Decrease spend on underperforming Google Ads ad groups and move that budget to Facebook retargeting campaigns.
-   **Audience Performance**: Retargeting audiences are the most profitable segment with a **CPA of $15**, compared to a **$55 CPA** for Prospecting audiences.
    -   **Recommendation**: While Prospecting is necessary for growth, we should refine our Prospecting audiences on Facebook to focus on lookalikes of high-value customers to improve efficiency.
-   **Creative Performance**: Video ads on Facebook/Instagram Reels are the top performers, generating **2x the ROAS of static image ads**.
    -   **Recommendation**: Pause the bottom 10% of static image ads and create new variations of the top-performing video creative.
---
### 📈 Performance Deep Dive
#### Key Performance Indicators (KPIs) at a Glance
| Metric | Current Result | Target | Status |
| :--- | :--- | :--- | :--- |
| **Return On Ad Spend (ROAS)** | **4.2:1** | 3.5:1 | ✅ On Track |
| **Cost Per Acquisition (CPA)** | **$28** | $35 | ✅ On Track |
| **Total Spend** | $50,000 | $100,000 | ⏳ Pacing |
| **Total Revenue** | $210,000 | $350,000 | ⏳ Pacing |
**Charts (ALL REQUIRED, dark background, light text):**
1.  **ROAS by Channel**
    -   A vertical bar chart comparing the ROAS of Paid Search and Paid Social.
    -   A horizontal dashed line indicates the target ROAS of 3.5:1.
    -   Bars are labeled with their ROAS value (e.g., "5.8:1").
2.  **CPA by Audience Type**
    -   A vertical bar chart comparing the CPA for Prospecting and Retargeting audiences.
    -   A horizontal dashed line indicates the target CPA of $35.
    -   Bars are colored green if below target and red if above.
3.  **Campaign ROAS Trend (Daily)**
    -   A line chart showing the daily ROAS over the campaign's duration.
    -   This helps visualize performance trends, decay, or the impact of optimizations.
---
### 🔍 Creative & Ad-Level Analysis
Analysis of individual ads reveals a clear pattern: engaging, short-form video content is dramatically outperforming static assets. Our top ad, "Holiday-Video-Ad-01," has generated over $30k in revenue on its own. Conversely, several text ads on Google are failing to convert, despite high click costs.
**Top 5 & Bottom 5 Ads by ROAS:**
-   A horizontal bar chart showing two groups of bars.
-   **Top 5 Ads**: Green bars extending to the right, labeled with the ad name and its high ROAS.
-   **Bottom 5 Ads**: Red bars extending to the left, labeled with the ad name and its low (or negative) ROAS. This creates a clear visual contrast between winners and losers.

````
{% endcode %}



## Metric Glossary

You wouldn't trust an analyst that regularly reports different numbers than what your well-maintained dashboards show. It's not because the numbers are necessarily wrong, but since they are inconsistent you have to figure out which one is more correct. A metric glossary can help with that. Here you just list all your most important KPIs/metrics with

* name of metric
* short description (maybe with synonyms)
* query on how to calculate the metric



Dot will use those definitions when giving answers. 

**Example**

````
This is our metric glossary. 
Always use the definitions specified here to write queries

## ARR: Annual Recurring Revenue
```sql
SELECT sum(contract_value)
FROM opportunities_table
WHERE status = 'closed'
```

## NRR: Net Revenue Retention
...
````



{% hint style="info" %}
You can nest notes in a hierarchy to stay organized.

You can assign access groups to notes to manage different domains or access patterns.
{% endhint %}


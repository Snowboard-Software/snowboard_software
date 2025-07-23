# Usage / Metered Pricing (Pay-per-Use)

**Definition (short).** Customers pay in proportion to what they consume—API calls, GB stored, kWh, messages, transactions. Revenue scales with usage, not (only) with time or seats; pricing can be linear or tiered.

**Recent examples.** AWS, Azure, and GCP bill per compute hour, GB, or request; AWS alone produced >$100 B in 2024 revenue. Utilities charge [\~16.4¢ per kWh](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a\&utm_source=chatgpt.com) to U.S. residential customers on average (Apr 2025), and the average home uses [\~10,500 kWh/year](https://www.eia.gov/energyexplained/use-of-energy/electricity-use-in-homes.php?utm_source=chatgpt.com) (≈875 kWh/mo).

**Historical example.** Edison’s Pearl Street Station (1882) billed electricity by the kilowatt‐hour—one of the earliest metered models. Taxi meters (1890s) and postage (per-letter) are other classic pay-per-use forebears.

<figure><img src="../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

#### KPI Definitions&#x20;

1.  **Profit per Unit of Usage (PPUU)**\
    &#xNAN;_&#x45;N:_ Profit generated for each billable unit (after variable costs).\
    &#xNAN;_&#x50;seudo:_ `PPUU = (Effective_Unit_Price - Unit_Cost) / Unit` or more commonly `(Revenue - Variable_Costs) / Total_Units`&#x20;

    _Why:_ Forces clarity on both monetization (price) and efficiency (cost). High volume without profit per unit is a trap; high margin without volume underutilizes the model.\
    &#xNAN;_&#x42;enchmark:_ Digital infra aims **70–85% gross margin**.
2. **Total Usage Volume (UV)**\
   &#xNAN;_&#x45;N:_ Sum of consumed units (API calls, kWh, GB, etc.).\
   &#xNAN;_&#x50;seudo:_ `Σ usage_units_all_customers`\
   &#xNAN;_&#x57;hy:_ Primary revenue driver; shows engagement/demand intensity.\
   &#xNAN;_&#x42;enchmark:_ Target **>30–50% YoY** usage growth early on.
3. **Effective Unit Price (EUP)**\
   &#xNAN;_&#x45;N:_ Average realized price per unit after tiers/discounts.\
   &#xNAN;_&#x50;seudo:_ `Total_Usage_Revenue / Total_Usage_Volume`\
   &#xNAN;_&#x57;hy:_ Monetization efficiency; erosion may signal commoditization.
4. **Gross Margin per Unit % (GMU)**\
   &#xNAN;_&#x45;N:_ % of unit price kept after variable cost.\
   &#xNAN;_&#x50;seudo:_ `(EUP - Unit_Cost) / EUP * 100`\
   &#xNAN;_&#x57;hy:_ Unit economics; determines scalability of volume growth.
5. **Active Users / Accounts (AU)**\
   &#xNAN;_&#x45;N:_ Unique customers generating billable usage in period.\
   &#xNAN;_&#x50;seudo:_ `COUNT(DISTINCT user_id WHERE usage>0)`\
   &#xNAN;_&#x57;hy:_ Breadth of adoption; needed to diversify revenue and de-risk whale dependence.
6. **Average Usage per User (AUPU)**\
   &#xNAN;_&#x45;N:_ Mean consumption per active user.\
   &#xNAN;_&#x50;seudo:_ `Total_Usage_Volume / Active_Users`\
   &#xNAN;_&#x57;hy:_ Depth of engagement; helps forecast infra needs.
7. **Tiered / Overages Mix % (TIER)**\
   &#xNAN;_&#x45;N:_ Share of revenue from higher tiers or overage charges vs base rate.\
   &#xNAN;_&#x50;seudo:_ `Revenue_from_Tiers_>1 / Total_Usage_Revenue * 100`\
   &#xNAN;_&#x57;hy:_ Shows success of pricing design in capturing heavy users’ value.
8. **Unit Cost (Variable)**\
   &#xNAN;_&#x45;N:_ Direct variable cost per unit (bandwidth, compute, fuel).\
   &#xNAN;_&#x50;seudo:_ `Variable_Costs / Total_Units`\
   &#xNAN;_&#x57;hy:_ Drives GMU; optimizing infra/vendor deals pushes PPUU up.
9. **New Active Users (ACQ)**\
   &#xNAN;_&#x45;N:_ Fresh customers who generated usage this period.\
   &#xNAN;_&#x50;seudo:_ `COUNT(users with first_usage_date in period)`\
   &#xNAN;_&#x57;hy:_ Pipeline for future volume; complements expansion of existing users.
10. **Expansion Usage % (EXPu)**\
    &#xNAN;_&#x45;N:_ Incremental usage from existing users vs last period.\
    &#xNAN;_&#x50;seudo:_ `(Usage_existing_t - Usage_existing_{t-1}) / Usage_existing_{t-1} * 100`\
    &#xNAN;_&#x57;hy:_ Land-and-expand health metric in usage world.
11. **Growth Efficiency Factor (GEF)** _EN:_ How efficiently you convert capacity (supply) growth into profitable usage growth. _Pseudo:_ `GEF = (Demand_Growth % / Capacity_Growth %) * (GMU / 100)` _Why:_ If you scale infra faster than demand or without keeping margins, you destroy PPUU. GEF >1 means you’re growing demand faster than capacity (or holding margin so growth is efficient). _Benchmark idea:_ Cloud/API teams often target **GEF ≥ 1.2** in growth phases; utilities, constrained by regulation, hover near 1 (capacity expansions match load forecasts).
12. **Demand (Usage) Growth % (DG)** _EN:_ Year-over-year change in total billed usage units. _Pseudo:_ `(Usage_t − Usage_{t−1}) / Usage_{t−1} * 100` _Why:_ Core top-line driver in metered models; faster than price hikes, usage growth proves product value. _Benchmark idea:_ Early-stage APIs: **30–50%+ YoY**; mature utilities: **1–2% YoY**.
13. **Capacity Growth % (CG)** _EN:_ YoY change in maximum deliverable capacity (compute throughput, MW, TPS). _Pseudo:_ `(Cap_t − Cap_{t−1}) / Cap_{t−1} * 100` _Why:_ Overbuild wastes capex; underbuild throttles revenue (throttling, outages). _Benchmark idea:_ hyperscalers expand capacity \~in line with forecasted demand + buffer (e.g., **20–40% YoY** during high-growth years).
14. **Capacity Utilization % (CI)** _EN:_ Average share of provisioned capacity actually used (often measured at peak window or averaged). _Pseudo:_ `Avg_Usage / Provisioned_Capacity * 100` _Why:_ Direct efficiency metric—too low means idle assets, too high means no headroom for spikes. _Benchmark idea:_ Power plants target **\~60–80%** load factors; cloud infra teams often aim **40–60% average** to leave burst room.
15. **Provisioned Capacity (PC)** _EN:_ The maximum sustained throughput you can deliver (e.g., kWh/day, requests/sec). _Pseudo:_ `Cap = Σ(node_capacity)` (or grid MW installed) _Why:_ Sets the ceiling; also denominator for utilization. Needed for capex planning.
16. **Peak Usage / Peak Load (PU)** _EN:_ Highest instantaneous (or short-window) usage observed in the period. _Pseudo:_ `max(usage_rate_t)` over period&#x20;

    _Why:_ Determines required headroom and auto-scaling needs; drives worst-case cost.

    _Benchmark:_ Peak multiples of 1.5–3× average are common; extreme bursty APIs can see 10×.


17. **Peak-to-Average Ratio (PAR)** _EN:_ Ratio of peak load to average load. _Pseudo:_ `Peak_Usage / Average_Usage`&#x20;

    _Why:_ Quantifies burstiness; high PAR stresses infra cost and pricing design (need overage/tier pricing).&#x20;

    _Benchmark:_ Utilities PAR \~1.3–1.6; consumer APIs (chat/LLM) can be **>3–5** during viral events.


18. **Capex per Unit Capacity (CAPU)** _EN:_ Capital required to add one unit of capacity (e.g., $ per kW, $ per 1k TPS). _Pseudo:_ `Capex_added / Capacity_added`&#x20;

    _Why:_ Guides ROI on expansion; lower CAPU means cheaper scaling.&#x20;

    _Benchmark:_ Data center build costs ≈ **$7–12M per MW**; GPU clusters vary wildly but trend \~$25–40 per deployable TFLOP.


19. **Auto-Scaling Latency (ASL)** _EN:_ Time it takes to provision additional capacity after demand spike. _Pseudo:_ `t(scale_complete) - t(threshold_trigger)`&#x20;

    _Why:_ Slow scaling means you must over-provision; fast scaling lets you run lean.&#x20;

    _Benchmark:_ Best cloud-native infra targets **seconds–minutes**; regulated utilities can’t “auto-scale,” they plan years ahead.


20. **Headroom % (HR)** _EN:_ Buffer capacity above expected peak. _Pseudo:_ `(Provisioned_Capacity - Expected_Peak) / Provisioned_Capacity * 100`&#x20;

    _Why:_ Prevents outages and throttling; too much wastes capital.&#x20;

    _Benchmark:_ Cloud SREs often keep **20–30%** headroom; grid operators maintain N-1 redundancy (varies but \~15–25% capacity reserve).
21. **Usage Concentration Risk %** _(auxiliary)_\
    &#xNAN;_&#x45;N:_ % of total usage (or revenue) coming from top X customers.\
    &#xNAN;_&#x50;seudo:_ `Usage_top_X / Total_Usage * 100`\
    &#xNAN;_&#x57;hy:_ Whales are great—until they churn. Tracks fragility of revenue base.\
    &#xNAN;_&#x42;enchmark:_ Aim <30% from top 5; many infra/API firms start >50% and work it down over time.

# Selling Ads

**Definition (short).** You give users content or utility (often free or subsidized) and monetize by selling their attention and/or data to advertisers or sponsors. Revenue scales with audience size, engagement (impressions), and the price per impression/click/action.

**Recent example.** Meta booked **$164.5 billion in 2024 revenue, \~97% from ads** across Facebook, Instagram, and now Threads. [Meta booked $164.5 billion in 2024 revenue, \~97% from ads](https://investor.atmeta.com/investor-news/press-release-details/2025/Meta-Reports-Fourth-Quarter-and-Full-Year-2024-Results/default.aspx?utm_source=chatgpt.com). YouTube ads brought Alphabet **$10.47 billion in Q4 2024 (up 13.8%)**, while Google overall still derived **\~76% of 2024 revenue from ads**. [Google overall still derived \~76% of 2024 revenue from ads](https://www.marketingdive.com/news/google-ad-revenue-growth-sluggish-ai/739274/?utm_source=chatgpt.com).\
**Historical example.** U.S. broadcast TV has been ad-funded since the 1950s; newspapers in the late 19th century (e.g., _NYT_) sold papers cheaply and made money on classifieds and display ads—pioneering CPM pricing long before digital.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

#### KPI Definitions

**Net Ad Profit Growth % (NAPR).** Year-over-year growth of (Ad Revenue − Direct Ad Ops Costs).\
&#xNAN;_&#x50;seudo:_ `((AdRev - AdOpsCost)_t - (AdRev - AdOpsCost)_{t-1}) / (AdRev - AdOpsCost)_{t-1} * 100`.\
&#xNAN;_&#x57;hy it matters:_ It unifies scale (revenue), monetization efficiency (eCPM/fill), and cost control. CEOs don’t want just bigger top-line; they want profitable growth.\
&#xNAN;_&#x42;enchmark:_ Mature ad giants are posting **\~20%+ YoY ad revenue growth with expanding margins** post-2023 rebound—top decile for scale players. [20%+ YoY ad revenue growth with expanding margins](https://investor.atmeta.com/investor-news/press-release-details/2025/Meta-Reports-Fourth-Quarter-and-Full-Year-2024-Results/default.aspx?utm_source=chatgpt.com)

**Ad Revenue $ (AR).** Total dollars from advertising/sponsorship in the period.\
&#xNAN;_&#x50;seudo:_ `Σ(ad_impressions * price_per_impression) + sponsorship_fees`.\
&#xNAN;_&#x57;hy it matters:_ It’s the core top line for an ad business; almost every other KPI feeds into it.\
&#xNAN;_&#x42;enchmark:_ Meta ads **$160.6 B in 2024**; Alphabet ads **\~76% of $307 B revenue**; ByteDance surpassed Meta in Q1 2025 ad revenue (\~$43 B vs $42.3 B).

**Ad Margin % (AM).** Gross margin on ad revenue after traffic acquisition costs (TAC), content costs, sales ops.\
&#xNAN;_&#x50;seudo:_ `(AdRev − AdDirectCosts) / AdRev * 100`.\
&#xNAN;_&#x57;hy it matters:_ High-volume inventory can still be low-margin if TAC is high. Margin signals pricing power and efficiency.\
&#xNAN;_&#x42;enchmark:_ Large platforms often report **70–80%+ gross margin on ad revenue** (digital distribution is cheap once built).

**Total Ad Impressions (IMP).** Count of ads actually shown.\
&#xNAN;_&#x50;seudo:_ `COUNT(ad_served_id)`.\
&#xNAN;_&#x57;hy it matters:_ Impressions are your monetizable inventory. Inventory growth (with stable CPM) = revenue growth.\
&#xNAN;_&#x42;enchmark:_ Social feeds can serve **dozens of ads per user per day** (e.g., \~40–50 on Facebook).

**Effective CPM/CPC/RPM (eCPM).** Average price per 1,000 impressions (or per click).\
&#xNAN;_&#x50;seudo:_ `eCPM = (AdRev / Impressions) * 1000`.\
&#xNAN;_&#x57;hy it matters:_ Shows monetization quality. Better targeting/format raises eCPM.\
&#xNAN;_&#x42;enchmark:_ Facebook/Meta global CPM hovered around **$13–14 in late 2024**; YouTube CPM **$2–$15 depending on niche/geo**. [Facebook/Meta global CPM hovered around $13–14 in late 2024](https://www.barrons.com/articles/meta-threads-platform-ads-0d941270?utm_source=chatgpt.com)

**Fill Rate % (FILL).** Percentage of ad slots filled with paid ads.\
&#xNAN;_&#x50;seudo:_ `Paid_Impressions / Total_Available_Slots * 100`.\
&#xNAN;_&#x57;hy it matters:_ Low fill = lost revenue or weak demand. High fill supports stable CPMs.\
&#xNAN;_&#x42;enchmark:_ Top platforms approach **\~100% fill** via auction backfill; smaller publishers may sit at **50–70%**.

**Format Mix % (MIXF).** Share of revenue from each ad format (video, display, search, native).\
&#xNAN;_&#x50;seudo:_ `Rev_format / AdRev * 100`.\
&#xNAN;_&#x57;hy it matters:_ Video has higher CPM but fewer slots; mix optimization drives ARPU.\
&#xNAN;_&#x42;enchmark:_ YouTube video ads grew **13.8% YoY in Q4 2024** and now form a rising share of Alphabet’s ad mix.

**Audience Size (MAU/DAU/Reach) (AUD).** Unique users/viewers in a period.\
&#xNAN;_&#x50;seudo:_ `COUNT(DISTINCT user_id within window)`.\
&#xNAN;_&#x57;hy it matters:_ Advertisers pay for reach; network value scales with audience.\
&#xNAN;_&#x42;enchmark:_ Meta MAUs \~3 B; Threads **300 M MAU in 2025**; large TV events still reach tens of millions.

**DAU/MAU % (STICK).** Stickiness—how many monthly users come daily.\
&#xNAN;_&#x50;seudo:_ `DAU / MAU * 100`.\
&#xNAN;_&#x57;hy it matters:_ Higher stickiness = more daily impressions and dependable inventory.\
&#xNAN;_&#x42;enchmark:_ Facebook historically \~**66–70% DAU/MAU**.

**Engagement / Impressions per User (ENG).** Average ads served per active user.\
&#xNAN;_&#x50;seudo:_ `IMP / Active_Users`.\
&#xNAN;_&#x57;hy it matters:_ Deeper engagement = more sellable slots per user.\
&#xNAN;_&#x42;enchmark:_ Heavy social users see **1000+ ads/month**; typical site visitors see far fewer.

**Average Time Spent / Sessions (ATS).** Minutes per user per day or sessions/user.\
&#xNAN;_&#x50;seudo:_ `Σ minutes_viewed / Active_Users`.\
&#xNAN;_&#x57;hy it matters:_ Time is a proxy for potential ad load without harming UX.\
&#xNAN;_&#x42;enchmark:_ TikTok/YouTube top \~**40–60 min/day**; Facebook/Instagram \~33 min/day.

**Yield Management Uplift % (YIELD).** Incremental revenue from optimization (better targeting, floor prices, header bidding).\
&#xNAN;_&#x50;seudo:_ `(Optimized_Rev − Baseline_Rev)/Baseline_Rev * 100`.\
&#xNAN;_&#x57;hy it matters:_ Smart yield lifts revenue without more ads.\
&#xNAN;_&#x42;enchmark:_ Smart bidding/header bidding rollouts often add **5–15% yield**.

**Ad Load / UX Risk Index (RISK) (aux).** Internal index of ad density vs. user satisfaction.\
&#xNAN;_&#x50;seudo:_ `ad_slots_per_session / UX_score`.\
&#xNAN;_&#x57;hy it matters:_ Over-monetization kills engagement; this guardrail protects long-term NAPR.\
&#xNAN;_&#x42;enchmark:_ Facebook publicly capped feed ad load increases after reaching “meaningful saturation” (\~15% of feed items).

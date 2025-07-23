# AirBnB

**Definition (short).** You connect two sides (guests–hosts) and monetize via service fees. Core economics = **Gross Booking Value (GBV) × implied take rate − operating costs**. GBV is the dollar value of bookings (host earnings + fees + taxes, net of cancellations). ([SEC](https://www.sec.gov/Archives/edgar/data/1559720/000119312522138654/d711122dex991.htm?utm_source=chatgpt.com))

**Recent example.** Q1’25: **GBV $24.5B**, **Nights & Experiences 143.1M**, **ADR $171**, **Revenue $2.3B**, **Net income $154M (7% margin)**, **Adj. EBITDA $417M (18%)**, **TTM FCF $4.4B (39%)**. Implied take rate = **\~9.3%** for the quarter.

**Historical example.** Auction houses (Sotheby’s 1744, Christie’s 1766) long charged commissions to match buyers and sellers—Airbnb is the digital analog for lodging. ([Airbnb Newsroom](https://news.airbnb.com/airbnb-q4-2023-and-full-year-financial-results/?utm_source=chatgpt.com))

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

#### KPI Definitions

**Gross Booking Value (GBV).**\
&#xNAN;_&#x50;seudo:_ `Σ booking_amounts (host earnings + fees + taxes − cancels)`\
&#xNAN;_&#x57;hy it matters:_ Top-of-funnel \$$ volume; everything downstream scales from here. ([SEC](https://www.sec.gov/Archives/edgar/data/1559720/000119312522138654/d711122dex991.htm?utm_source=chatgpt.com))\
&#xNAN;_&#x42;enchmark:_ $24.5B in Q1’25; $82B+ in 2024. ([FourWeekMBA](https://fourweekmba.com/airbnb-gross-booking-value/?utm_source=chatgpt.com))

**Nights & Experiences Booked (NEB).**\
&#xNAN;_&#x50;seudo:_ `COUNT(booked_units_net)`\
&#xNAN;_&#x57;hy it matters:_ Core demand/usage driver of GBV.\
&#xNAN;_&#x42;enchmark:_ 143.1M in Q1’25 (+8% YoY).

**Average Daily Rate (ADR).**\
&#xNAN;_&#x50;seudo:_ `ADR = GBV / Nights & Experiences Booked`\
&#xNAN;_&#x57;hy it matters:_ Price/mix lever (geo, FX, LOS, product type).\
&#xNAN;_&#x42;enchmark:_ $171 in Q1’25 (−1% YoY; +1% ex-FX).

**Implied Take Rate % (TR).**\
&#xNAN;_&#x50;seudo:_ `Revenue / GBV * 100`\
&#xNAN;_&#x57;hy it matters:_ Monetization efficiency—how much value Airbnb captures. ([SEC](https://www.sec.gov/Archives/edgar/data/1559720/000119312522138654/d711122dex991.htm?utm_source=chatgpt.com))\
&#xNAN;_&#x42;enchmark:_ 9.3% in Q1’25; \~13.6% for FY 2024. ([FourWeekMBA](https://fourweekmba.com/how-much-does-airbnb-take/?utm_source=chatgpt.com))

**Revenue.**\
&#xNAN;_&#x50;seudo:_ `GBV × TR`\
&#xNAN;_&#x57;hy it matters:_ Primary operating outcome they steer to before costs.\
&#xNAN;_&#x42;enchmark:_ $2.3B in Q1’25 (+6% YoY; +8% ex-FX).

**Adjusted EBITDA (and Margin).**\
&#xNAN;_&#x50;seudo:_ `Revenue − (Cash Opex + CoR) +/− adjustments`\
&#xNAN;_&#x57;hy it matters:_ Management’s efficiency lens (ex some non-cash/one-offs).\
&#xNAN;_&#x42;enchmark:_ $417M (18% margin) in Q1’25.

**Net Income (and Margin).**\
&#xNAN;_&#x50;seudo:_ `GAAP bottom line`\
&#xNAN;_&#x57;hy it matters:_ Ultimate profitability after SBC, taxes, interest.\
&#xNAN;_&#x42;enchmark:_ $154M (7% margin) in Q1’25.

**Free Cash Flow (TTM).**\
&#xNAN;_&#x50;seudo:_ `Operating Cash Flow − Capex`\
&#xNAN;_&#x57;hy it matters:_ Real cash to fund buybacks/new bets; validates model durability.\
&#xNAN;_&#x42;enchmark:_ $4.4B TTM (39% margin).

**Active Listings / Supply Health (contextual driver).**\
&#xNAN;_&#x50;seudo:_ `Distinct live listings; removals of low-quality supply`\
&#xNAN;_&#x57;hy it matters:_ Liquidity & match quality sustain NEB and ADR. ([Airbnb Newsroom](https://news.airbnb.com/airbnb-q4-2023-and-full-year-financial-results/?utm_source=chatgpt.com))\
&#xNAN;_&#x42;enchmark:_ 7.7M active listings at YE 2023; 450k low-quality removed since 2023. ([Airbnb Newsroom](https://news.airbnb.com/airbnb-q4-2023-and-full-year-financial-results/?utm_source=chatgpt.com))

***

Let me know if you want this dropped into slides or a SQL/Python model.

# Intermediation / Commission (Marketplaces)

**Definition (short).** You connect two (or more) sides of a transaction (buyers–sellers, riders–drivers, hosts–guests) and charge a commission or fee. You rarely own the underlying good/service; your economics are driven by **GMV volume × take rate**, minus operating costs.

**Recent example.** Airbnb’s effective take rate was [\~ 13 – 15 % on $60 B+ GBV in 2023](https://fourweekmba.com/airbnb-take-rate/?utm_source=chatgpt.com). Uber takes [\~ 20 – 28 % of each fare](https://stockanalysis.com/stocks/uber/metrics/?utm_source=chatgpt.com) after incentives. Amazon Marketplace charges [8 – 15 % category commissions](https://productscope.ai/blog/amazon-referral-fee/?utm_source=chatgpt.com); eBay averages \~ 10 %.

**Historical example.** Sotheby’s (1744) and Christie’s (1766) have always taken [auction commissions](https://www.investopedia.com/articles/active-trading/031215/how-real-estate-agent-and-broker-fees-work.asp?utm_source=chatgpt.com). Stockbrokers since the 17th century charged per trade, and newspaper classifieds were proto-marketplaces taking small fees to connect local buyers and sellers.

<figure><img src="../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### KPI Definitions

**Net Commission Profit Growth % (NCPG).**\
&#xNAN;_&#x50;seudo:_ `((Commission_Rev - Operating_Costs)_t - (Commission_Rev - Operating_Costs)_{t-1}) / (Commission_Rev - Operating_Costs)_{t-1} * 100`.\
&#xNAN;_&#x57;hy it matters:_ GMV without monetization, or take rate without efficiency, equals vanity. NCPG unifies the three real levers: volume (GMV), monetization (take rate), and cost discipline.\
&#xNAN;_&#x42;enchmark:_ Mature marketplaces target [double-digit profit growth](https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm?utm_source=chatgpt.com).

**Gross Merchandise / Transaction Value (GMV).**\
&#xNAN;_&#x50;seudo:_ `Σ transaction_amounts`.\
&#xNAN;_&#x57;hy it matters:_ Commission dollars usually scale linearly with GMV. Investors use GMV to size the marketplace even before profits.\
&#xNAN;_&#x42;enchmark:_ Airbnb GBV [$63 B (2022)](https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm?utm_source=chatgpt.com).

**Take Rate % (TR).**\
&#xNAN;_&#x50;seudo:_ `TR = Commission_Revenue / GMV * 100`.\
&#xNAN;_&#x57;hy it matters:_ It shows value capture and pricing power; raising TR without hurting liquidity is gold.\
&#xNAN;_&#x42;enchmark:_ Product marketplaces [5 – 15 %](https://productscope.ai/blog/amazon-referral-fee/?utm_source=chatgpt.com); service marketplaces 15 – 30 %.

**Operating Cost % of Commission Rev (OPEX).**\
&#xNAN;_&#x50;seudo:_ `OPEX / Commission_Revenue * 100`.\
&#xNAN;_&#x57;hy it matters:_ High opex eats into take rate gains; scale should drive this down.\
&#xNAN;_&#x42;enchmark:_ Post-scale marketplaces target [< 50 % opex/commission rev](https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm?utm_source=chatgpt.com).

**Number of Transactions (NT).**\
&#xNAN;_&#x50;seudo:_ `COUNT(txn_id)`.\
&#xNAN;_&#x57;hy it matters:_ Frequency matters for habit and network effects; many small orders can equal one large one in GMV, but frequency builds stickiness.\
&#xNAN;_&#x42;enchmark:_ DoorDash did [512 million orders in Q1 2023](https://ir.doordash.com/news/news-details/2023/DoorDash-Releases-First-Quarter-2023-Financial-Results/default.aspx?utm_source=chatgpt.com).

**Average Transaction Value $ (ATV).**\
&#xNAN;_&#x50;seudo:_ `ATV = GMV / NT`.\
&#xNAN;_&#x57;hy it matters:_ Shifts in product mix or user behavior drive ATV; high ATV can boost revenue per txn but often comes with lower frequency.\
&#xNAN;_&#x42;enchmark:_ E-commerce AOV [$50 – $100](https://www.irpcommerce.com/en/us/ecommercemarketdata.aspx?utm_source=chatgpt.com).

**Other Fees % of GMV (OTHERF).**\
&#xNAN;_&#x50;seudo:_ `Other_Fee_Revenue / GMV * 100`.\
&#xNAN;_&#x57;hy it matters:_ Diversifies income and effectively raises take rate without raising headline commission.\
&#xNAN;_&#x42;enchmark:_ Etsy charges [listing + promoted listings fees](https://investors.etsy.com/overview/key-figures/default.aspx?utm_source=chatgpt.com) adding a few extra %.

**Mix of Commission vs Subscriptions % (MIXT).**\
&#xNAN;_&#x50;seudo:_ `Subscription_Revenue / Total_Revenue * 100`.\
&#xNAN;_&#x57;hy it matters:_ Subscriptions stabilize revenue and raise LTV; but too much may deter small sellers.\
&#xNAN;_&#x42;enchmark:_ Some B2B marketplaces get [> 20 % of revenue from subscriptions](https://investors.etsy.com/overview/key-figures/default.aspx?utm_source=chatgpt.com).

**Active Buyers (ACTB).**\
&#xNAN;_&#x50;seudo:_ `COUNT(DISTINCT buyer_id WHERE txn>0)`.\
&#xNAN;_&#x57;hy it matters:_ Demand-side depth; more buyers improve liquidity, justify higher TR.\
&#xNAN;_&#x42;enchmark:_ Etsy had [95.1 M active buyers (2022)](https://app.stocklight.com/stocks/us/nasdaq-etsy/etsy/annual-reports/nasdaq-etsy-2023-10K-23655284.pdf?utm_source=chatgpt.com).

**Active Sellers (ACTS).**\
&#xNAN;_&#x50;seudo:_ `COUNT(DISTINCT seller_id WHERE txn>0)`.\
&#xNAN;_&#x57;hy it matters:_ Supply depth; too few sellers causes stockouts/price spikes; too many with no sales drives churn.\
&#xNAN;_&#x42;enchmark:_ Etsy reported [7.5 M active sellers (2022)](https://app.stocklight.com/stocks/us/nasdaq-etsy/etsy/annual-reports/nasdaq-etsy-2023-10K-23655284.pdf?utm_source=chatgpt.com).

**Buyer Conversion Rate % (CONV).**\
&#xNAN;_&#x50;seudo:_ `Purchases / Qualified_Sessions * 100`.\
&#xNAN;_&#x57;hy it matters:_ It signals liquidity and UX quality; higher conversion usually lifts both GMV and TR.\
&#xNAN;_&#x42;enchmark:_ General e-commerce sees [2 – 3 % conversion rates](https://www.invespcro.com/cro/conversion-rate-by-industry/?utm_source=chatgpt.com).

**Purchase Frequency / Buyer (LFQ).**\
&#xNAN;_&#x50;seudo:_ `NT / Active_Buyers`.\
&#xNAN;_&#x57;hy it matters:_ Frequency drives lifetime value and defensibility.\
&#xNAN;_&#x42;enchmark:_ Top “habit” marketplaces push [> 5 – 10 orders per buyer per year](https://ir.doordash.com/news/news-details/2023/DoorDash-Releases-First-Quarter-2023-Financial-Results/default.aspx?utm_source=chatgpt.com).

**Supply Health / Listings Liquidity % (SUPH).**\
&#xNAN;_&#x50;seudo:_ `Listings_sold / Listings_posted_in_window * 100`.\
&#xNAN;_&#x57;hy it matters:_ If sellers don’t sell, they churn; liquidity is the soul of a marketplace.\
&#xNAN;_&#x42;enchmark:_ Healthy resale marketplaces target [> 50 % sell-through over 60 – 90 days](https://ir.doordash.com/news/news-details/2023/DoorDash-Releases-First-Quarter-2023-Financial-Results/default.aspx?utm_source=chatgpt.com).

**Disintermediation / Leakage Rate % (RISK) (aux).**\
&#xNAN;_&#x50;seudo:_ `Off_platform_transactions_est / Total_matches_est * 100`.\
&#xNAN;_&#x57;hy it matters:_ High leakage erodes take rate and weakens the moat.\
&#xNAN;_&#x42;enchmark:_ Service marketplaces often battle [> 20 % leakage early on](https://investors.etsy.com/overview/key-figures/default.aspx?utm_source=chatgpt.com).

# Financial Spread / Underwriting (Banks & Insurers)

**Definition (short).** You earn by pricing and absorbing financial risk: banks capture **interest spread** (lend high, borrow low), insurers keep **premium minus claims/expenses** (combined ratio <100%). Profitability rests on margin (spread/ratio), volume (assets/premiums), and risk (defaults/claims).

**Recent example.** U.S. banks’ average **net interest margin was 3.30% in 2023** (up 35 bps YoY). [Net interest margin was 3.30% in 2023](https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2023dec/qbp.pdf?utm_source=chatgpt.com). U.S. P\&C insurers’ combined ratio improved to **101.7% in 2023** (still an underwriting loss), then to **\~96.5% in 2024** (profit) as price hikes beat claims. [Combined ratio improved to 101.7% in 2023, then to \~96.5% in 2024](https://www.ft.com/content/74109807-82d8-4281-a842-7681af0366fa?utm_source=chatgpt.com).\
**Historical example.** Lloyd’s of London (1680s) pioneered marine underwriting; medieval moneylenders lived on interest spreads; 19th-century savings & loans profited on mortgage spreads; the “combined ratio” has been an insurance staple since early 20th century.

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

#### KPI Definitions

**Net Interest/Underwriting Spread Profit Growth % (NISG).** YoY growth of profit from core spread/underwriting before investment gains.\
&#xNAN;_&#x50;seudo:_ `((Spread_Profit)_t - (Spread_Profit)_{t-1}) / (Spread_Profit)_{t-1} * 100`.\
&#xNAN;_&#x57;hy it matters:_ Captures whether you’re expanding the core engine (margin×volume) after losses/claims.\
&#xNAN;_&#x42;enchmark:_ Post-rate hikes, many U.S. banks grew spread profit double digits in 2023; P\&C insurers returned to underwriting profit in 2024 (combined \~96.5%).

**Net Interest Margin % (NIM).** (Banks) Interest income minus interest expense, over average earning assets.\
&#xNAN;_&#x50;seudo:_ `(IntInc − IntExp) / Avg_Earning_Assets * 100`.\
\*Why it matters

:\* It’s the core spread metric; a few bps swing moves billions for big banks.\
&#xNAN;_&#x42;enchmark:_ U.S. banks **3.30% in 2023**; large money-center banks 2.6–3.2%; credit cards lenders 5–7%.

**Combined Ratio % (CR).** (Insurers) Loss ratio + expense ratio; <100% means underwriting profit.\
&#xNAN;_&#x50;seudo:_ `(Claims/Premiums + Expenses/Premiums) * 100`.\
&#xNAN;_&#x57;hy it matters:_ The single best underwriting KPI—tells if pricing outweighs claims+costs.\
&#xNAN;_&#x42;enchmark:_ U.S. P\&C **101.7% in 2023** (loss), **96.5% in 2024** (profit). Top performers target **<90–95%**.

**Volume of Earning Assets / Premiums (VOL).** Loans outstanding or gross written premiums.\
&#xNAN;_&#x50;seudo:_ `Σ(loans) or Σ(premiums)`.\
&#xNAN;_&#x57;hy it matters:_ Spread × volume = dollars. Scale matters, but not at the expense of risk.\
&#xNAN;_&#x42;enchmark:_ Healthy banks target **5–10% loan growth**; P\&C premium growth mid-single digits, spiking during “hard markets”.

**Cost of Funds % (COF).** Average interest rate paid on deposits/borrowings.\
&#xNAN;_&#x50;seudo:_ `IntExp / Avg_Funding * 100`.\
&#xNAN;_&#x57;hy it matters:_ Lower COF widens NIM without raising borrower rates.\
&#xNAN;_&#x42;enchmark:_ Large banks enjoy low-cost checking (near 0% for years), now rising but still below wholesale rates.

**Average Yield on Assets % (YLD).** Interest/ premium yield on loans/investments.\
&#xNAN;_&#x50;seudo:_ `IntInc / Avg_Earning_Assets * 100`.\
&#xNAN;_&#x57;hy it matters:_ Determines top side of NIM; asset mix and rate environment drive it.\
&#xNAN;_&#x42;enchmark:_ With 2023–24 rate hikes, banks’ asset yields rose several hundred bps; insurers’ bond portfolio new-money yields moved toward **4–5%**.

**Loss Ratio % (LR).** Claims paid ÷ premiums (insurance).\
&#xNAN;_&#x50;seudo:_ `Claims / Premiums * 100`.\
&#xNAN;_&#x57;hy it matters:_ Core risk pricing—too high implies underpricing or bad luck (cats).\
&#xNAN;_&#x42;enchmark:_ Personal lines saw LR >70% in 2023; after rate hikes, LR fell, driving combined ratio down to 96.5%.

**Expense Ratio % (ER).** Operating expenses ÷ premiums.\
&#xNAN;_&#x50;seudo:_ `Underwriting_Expenses / Premiums * 100`.\
&#xNAN;_&#x57;hy it matters:_ Operational efficiency lever; trimming ER improves CR directly.\
&#xNAN;_&#x42;enchmark:_ Many P\&C insurers run **\~25–30%** ER; best-in-class trims to low 20s.

**Loan/Premium Growth % (GROW).** Period-over-period growth in loans or premiums.\
&#xNAN;_&#x50;seudo:_ `(ThisPeriod − LastPeriod) / LastPeriod * 100`.\
&#xNAN;_&#x57;hy it matters:_ Indicates demand, share gain, and pricing power.\
&#xNAN;_&#x42;enchmark:_ Banks: **mid-single digits normal**, 10%+ aggressive. Insurers: **3–5% typical**, >10% in hard market cycles.

**Loan-to-Deposit Ratio % / Policy Retention % (LDR).** Banks: loans ÷ deposits; Insurers: % of policies renewed.\
&#xNAN;_&#x50;seudo:_ `Loans/Deposits * 100` or `Policies_Renewed/Policies_Up * 100`.\
&#xNAN;_&#x57;hy it matters:_ Funding stability (banks) and sticky business (insurers).\
&#xNAN;_&#x42;enchmark:_ Banks target **80–90% L/D**; Insurers retention **>85–90%** in personal lines is strong.

**Non-Performing Loan % / Charge-off % (NPL).** Share of loans in default or written off.\
&#xNAN;_&#x50;seudo:_ `NPL / Total_Loans * 100`.\
&#xNAN;_&#x57;hy it matters:_ Credit quality; high NPL erodes spread via provisions.\
&#xNAN;_&#x42;enchmark:_ U.S. banks’ NPL often **<2%** in good times; credit cards charge-offs **\~3%**.

**Catastrophe Loss % of Premiums (CAT).** P\&C cat claims as a % of earned premiums.\
&#xNAN;_&#x50;seudo:_ `CatLosses / Premiums * 100`.\
&#xNAN;_&#x57;hy it matters:_ Volatility driver; high CAT years wreck CR.\
&#xNAN;_&#x42;enchmark:_ 2024 saw $320 B global disaster losses; U.S. insurers still hit **96.5% CR** thanks to pricing.

**Investment Yield % (INVY) (aux).** Return on invested assets/float.\
&#xNAN;_&#x50;seudo:_ `Investment_Income / Invested_Assets * 100`.\
&#xNAN;_&#x57;hy it matters:_ Insurers rely on investment income to offset underwriting cycles; banks too on securities portfolios.\
&#xNAN;_&#x42;enchmark:_ With rates up, insurers’ new money yields **\~4–5%**; bonds dominated portfolios.

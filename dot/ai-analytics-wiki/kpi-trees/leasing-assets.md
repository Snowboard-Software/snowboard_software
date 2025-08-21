# Leasing Assets



**Definition (short).** Customers pay for time-bound use of an asset (room, car, excavator, desk). You retain ownership; revenue hinges on utilization (how often it’s rented) and rate (what you charge per unit-time).

**Recent examples.** U.S. hotels posted [**record ADR ($155.62), record RevPAR ($97.97), and 63% occupancy in 2023**](https://www.traveldailynews.com/statistics-trends/u-s-hotels-posted-record-high-adr-and-revpar-in-2023/?utm_source=chatgpt.com), marking a full recovery in pricing and near-recovery in utilization. The U.S. car rental industry hit $38.3 billion revenue in 2023, up 5% YoY—another record.

**Historical example.** [Blockbuster](https://en.wikipedia.org/wiki/Blockbuster_LLC) rented movies/games for a few days: at its 2004 peak it ran \~9,000 stores and earned $5.9 billion—pure temporary access to physical media.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### KPI Definitions

1.  **Profitable Utilization**

    _EN_: How much profit you generate for every unit of capacity you could rent (room-night, car-day, excavator-hour).

    _Pseudo_:

    * Profitable Utilization = RevPU \* EBIT\_Margin
    * or equivalently ((Revenue − Opex − Maintenance − Depreciation) / (Units \* Time))

    _Why_: Blends the two levers that matter most in renting: rate × fill (RevPU) and cost discipline (margin). One number forces trade-off clarity between pushing price/occupancy and controlling asset & operating costs.

    _Benchmark idea_: Hotels often track GOPPAR (gross operating profit per available room). This version just generalizes that: Profit per Available Unit-Time (PPAU). Set a target (e.g., grow PPAU ≥ X% YoY while occupancy stays between 70–85%).
2. **Revenue Growth %**\
   &#xNAN;_&#x45;N:_ YoY % change in lease/rental revenue.\
   &#xNAN;_&#x50;seudo:_ `(Rev_t − Rev_{t−1}) / Rev_{t−1} * 100`\
   &#xNAN;_&#x57;hy:_ Shows demand/pricing momentum, especially critical post-shocks (pandemics, recessions).\
   &#xNAN;_&#x42;enchmark:_ U.S. hotel RevPAR grew +4.9% in 2023; car rental revenue +5% YoY.
3. **Revenue per Available Unit (RevPAR / RPU)**\
   &#xNAN;_&#x45;N:_ Revenue divided by total unit-time available.\
   &#xNAN;_&#x50;seudo:_ `Revenue / (Units * Time)` or `Occupancy * ADR`.\
   &#xNAN;_&#x57;hy:_ Single metric blending rate and utilization; gold standard for asset productivity.\
   &#xNAN;_&#x42;enchmark:_ U.S. hotels averaged RevPAR $97.97 in 2023.
4. **Occupancy / Utilization %**\
   &#xNAN;_&#x45;N:_ % of available unit-time actually rented.\
   &#xNAN;_&#x50;seudo:_ `Occupied_Time / Available_Time * 100`\
   &#xNAN;_&#x57;hy:_ Idle assets = lost revenue; too high leaves no room for peak pricing.\
   &#xNAN;_&#x42;enchmark:_ U.S. hotel occupancy 63% in 2023; top-city properties routinely hit 80%+ in peak seasons.
5. **Average Rental Rate (ADR/ARR)**\
   &#xNAN;_&#x45;N:_ Average realized price per rented unit-time.\
   &#xNAN;_&#x50;seudo:_ `Revenue / Rented_Time`\
   &#xNAN;_&#x57;hy:_ Pricing power lever; raising ADR lifts RevPU without more assets.\
   &#xNAN;_&#x42;enchmark:_ U.S. hotel ADR $155.62 (2023); upscale segments far higher.
6. **EBIT Margin %**\
   &#xNAN;_&#x45;N:_ Operating profit (pre-interest/taxes) as % of revenue.\
   &#xNAN;_&#x50;seudo:_ `EBIT / Revenue * 100`\
   &#xNAN;_&#x57;hy:_ Captures structural profitability after maintenance, overhead.\
   &#xNAN;_&#x42;enchmark:_ Car rental majors often post 10–15% EBIT; asset-light hotel franchisors can exceed 30%.
7. **Maintenance & Depreciation Ratio %**\
   &#xNAN;_&#x45;N:_ Maintenance plus depreciation cost share of revenue.\
   &#xNAN;_&#x50;seudo:_ `(Maintenance + Depreciation) / Revenue * 100`\
   &#xNAN;_&#x57;hy:_ Assets wear out; keeps margin honest. Too low risks quality, too high erodes profits.\
   &#xNAN;_&#x42;enchmark:_ Fleet-heavy rentals \~9–12%; hotels allocate \~5–8% of revenue to property maintenance/capex.
8. **Contract / Lease Renewal %**\
   &#xNAN;_&#x45;N:_ Portion of expiring long-term leases/contracts that renew.\
   &#xNAN;_&#x50;seudo:_ `Renewed / Expiring * 100`\
   &#xNAN;_&#x57;hy:_ Stickiness metric; lowers selling cost and smooths cash flows.\
   &#xNAN;_&#x42;enchmark:_ Commercial leases 75–90% renewal; equipment leases 60–80%+ depending on term.
9. **Total Capacity (Units \* Time)**\
   &#xNAN;_&#x45;N:_ Theoretical rentable supply (rooms × nights, cars × days).\
   &#xNAN;_&#x50;seudo:_ `Units * Available_Time`\
   &#xNAN;_&#x57;hy:_ Sets denominator for utilization/RevPU; critical for planning expansion or retirements.
10. **Occupied / Rented Units**\
    &#xNAN;_&#x45;N:_ Actual unit-time rented in period.\
    &#xNAN;_&#x50;seudo:_ `Σ rented_unit_time`\
    &#xNAN;_&#x57;hy:_ Raw volume driver for utilization and revenue; track by segment to see mix shifts.
11. **Avg Rental Duration**\
    &#xNAN;_&#x45;N:_ Mean length of each rental/booking.\
    &#xNAN;_&#x50;seudo:_ `Total_Rented_Time / #Contracts`\
    &#xNAN;_&#x57;hy:_ Impacts ops (turn costs), pricing, and forecasting.\
    &#xNAN;_&#x42;enchmark:_ Cars 3–7 days; equipment months; hotels 1–3 nights average.
12. **Yield Management Uplift %**\
    &#xNAN;_&#x45;N:_ Incremental revenue vs flat pricing.\
    &#xNAN;_&#x50;seudo:_ `(Actual_Rev − FlatRate_Rev) / FlatRate_Rev * 100`\
    &#xNAN;_&#x57;hy:_ Quantifies value of RM/dynamic pricing systems.\
    &#xNAN;_&#x42;enchmark:_ Airlines/hotels typically claim +3–7% uplift from RM algorithms.
13. **Dynamic Pricing Hit Rate %**\
    &#xNAN;_&#x45;N:_ % of price changes that improved RevPU.\
    &#xNAN;_&#x50;seudo:_ `#Positive_Changes / Total_Changes * 100`\
    &#xNAN;_&#x57;hy:_ Ensures pricing AI is actually adding value, not noise.\
    &#xNAN;_&#x42;enchmark:_ Internal metric—teams target quarter-over-quarter improvement.

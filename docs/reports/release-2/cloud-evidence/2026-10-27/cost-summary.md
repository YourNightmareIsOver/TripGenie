# Observed Azure cost: 27 October 2026

Read-only Azure Cost Management query (`2023-11-01`, ActualCost, daily
granularity, grouped by ServiceName). Scope: `rg-tripgenie` only. Query window:
1-27 October 2026 UTC. This is incurred usage reported so far, not a forecast.

| Usage date (UTC) | Container Apps (AUD) | Container Registry (AUD) | Total (AUD) |
| --- | ---: | ---: | ---: |
| 2026-10-19 | 0.0287 | 0.1430 | 0.1716 |
| 2026-10-20 | 4.1057 | 0.2373 | 4.3430 |
| 2026-10-21 | 6.6573 | 0.2373 | 6.8946 |
| 2026-10-22 | 4.7799 | 0.2373 | 5.0172 |
| 2026-10-23 | 4.5376 | 0.2373 | 4.7749 |
| 2026-10-24 | 4.4708 | 0.2373 | 4.7082 |
| 2026-10-25 | 4.4431 | 0.2373 | 4.6805 |
| 2026-10-26 | 4.4426 | 0.2373 | 4.6799 |
| 2026-10-27 (partial) | 0.4154 | 0.0297 | 0.4451 |

**Total returned: AUD 35.72.** Bandwidth, Log Analytics and Storage rows
returned zero. No rows before 19 October were returned.

Billing data lags usage; the 27 October row is partial and is not the final
cost of deployment 40476984860. This is not a monthly projection or a total
for the subscription. The separate identity resource group was not included
in this query. The [21 October cost snapshot](../cost-2026-10-21.md) is retained
as historical evidence, not the current cost figure.

[Original returned columns and rows](cost-results.json).

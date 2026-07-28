# Portfolio

Current holdings. The source of truth for what you actually own.

**Base currency:** EUR <!-- reporting currency only: aggregate weights, cost basis, and cash are expressed in EUR. Individual positions trade and are priced in their listing currency (see "Listing ccy" column) — e.g. NKE/ADBE in USD — and get converted at the transaction-date FX rate. -->

**Total portfolio value (incl. cash):** — (as of: —) <!-- updated by decision-log on every transaction and by portfolio-review weekly -->
**Last reviewed:** never — positions backfilled 2026-07-17 during system audit; first `portfolio-review` pending trade details

---

## Active positions

| Ticker | Sector | Initiated | Shares | Listing ccy | Avg cost/share | Cost basis (base ccy) | Current weight | Conviction (1-5) | Thesis status |
|---|---|---|---|---|---|---|---|---|---|
| NKE | branded-athletic-footwear-and-apparel | TBD (May-Jul 2026) | TBD | USD | TBD | TBD | TBD | 3 | MONITOR (earnings-debrief 2026-07-17) |
| ADBE | creative-and-design-software | TBD (May-Jul 2026) | TBD | USD | TBD | TBD | TBD | 4 (under review) | FLAGGED — thesis-check required (kill switch triggered 2026-07-17) |

> **TBD fields:** both positions were confirmed by Francesco on 2026-07-17 but the trades were never logged at the time — see `journal/2026-07-17-decision.md` (backfilled entries). Fill shares / price / date from brokerage records; until then, weight and concentration metrics cannot be computed.

Column semantics:

- **Shares** — actual share count. This is the ground truth; weights are derived, never stored as primary data.
- **Avg cost/share** — in the listing currency, averaged across BUY/ADD lots.
- **Cost basis (base ccy)** — total invested, converted to base currency at each transaction date's FX rate (written by `decision-log`).
- **Current weight** — shares × current price ÷ total portfolio value, in base currency. **Computed by `portfolio-review` at each sweep** (dated by "Last reviewed" above) — treat as stale between sweeps; never hand-maintain.
- **Thesis status** — most recent `thesis-check`/`earnings-debrief` verdict, updated whenever those skills run.

## Cash / dry powder

- **Cash:** — ( —% of portfolio, as of: — ) <!-- updated by decision-log on every BUY/ADD/TRIM/SELL/EXIT, and correctable by hand after deposits/withdrawals -->
- **Target deployment / waiting for:** —

## Concentration check

Computed by `portfolio-review` at each sweep — the numbers below carry the sweep date:

- Top 5 positions as % of portfolio: — (as of: —)
- Sector concentration (any single sector > 35%?): — (as of: —)
- Geographic concentration: — (as of: —)
- Currency exposure (any single non-base currency > 30%?): — (as of: —)

## Notes

Anything that doesn't fit the table above. Pending trims, names you're considering adding to, etc.

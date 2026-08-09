---
name: 0.11.6-understand-supplier_contract_negotiation
description: [0.11.6] formal agreements with vendors on pricing, terms, and exclusivity
---

# understand-supplier_contract_negotiation

**CALL NUMBER:** `supply_chain_and_inventory.supplier_contract_negotiation`
**DEFINITION:** formal agreements with vendors on pricing, terms, and exclusivity

Invoke this skill to understand `supplier_contract_negotiation` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `supply_chain_and_inventory`
- **supplier_price_fluctuation_tracking** (d1): monitoring changes in vendor pricing over time
- **vendor_credit_terms** (d1): negotiated payment schedules such as net_30 or net_60
- **volume_discount_agreements** (d1): contracted price breaks for purchasing specified quantities
- **commodity_market_price_awareness** (d2): tracking broader market prices for beef, produce, grains, etc.
- **vendor_payment_processing** (d2): managing invoices and payments to suppliers
- **bulk_purchasing_decisions** (d2): buying larger quantities to secure lower per-unit costs
- **currency_exchange_rate_impact** (d3): effect of exchange rates on imported ingredient costs
- **seasonal_price_variance_accounting** (d3): budgeting for predictable price changes during seasons
- **implied_accounting_payable_systems** (d3): implied connection to financial and payment processing infrastructure
- **carrying_cost_of_inventory** (d3): expense of storing and maintaining inventory over time
- **implied_supply_chain_financial_planning** (d4): implied connection to budgeting and financial forecasting
- **storage_cost_allocation** (d4): assigning space costs to inventory items

## CONSUMERS (what needs this)
`meat_supplier_relationships`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_

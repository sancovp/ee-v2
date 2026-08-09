---
name: 0.11.3-understand-receiving_inspection_protocol
description: [0.11.3] checking delivered goods against order for quality and accuracy
---

# understand-receiving_inspection_protocol

**CALL NUMBER:** `supply_chain_and_inventory.receiving_inspection_protocol`
**DEFINITION:** checking delivered goods against order for quality and accuracy

Invoke this skill to understand `receiving_inspection_protocol` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `supply_chain_and_inventory`
- **bill_of_lading_verification** (d1): matching delivery documents to purchase orders
- **case_lot_inspection** (d1): examining outer packaging for damage or contamination signs
- **temperature_of_delivered_goods** (d1): verifying proper cold chain maintenance during delivery
- **weight_verification_receiving** (d1): confirming delivered weight matches invoiced quantities
- **implied_refrigeration_equipment** (d2): implied relationship to commercial refrigeration systems

## CONSUMERS (what needs this)
`delivery_dock_operations`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_

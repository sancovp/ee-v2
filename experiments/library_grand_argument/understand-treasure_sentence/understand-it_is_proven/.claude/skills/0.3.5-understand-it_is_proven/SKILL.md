---
name: 0.3.5-understand-it_is_proven
description: [0.3.5] Premise computable via vault plus cert ladders plus S3 as external adjudicator
---

# understand-it_is_proven

**CALL NUMBER:** `treasure_sentence.it_is_proven : premise_receipts(2)`
**DEFINITION:** Premise computable via vault plus cert ladders plus S3 as external adjudicator

Invoke this skill to understand `it_is_proven` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `?`
- **cert_ladders** (d1): Tiered validation structures that make proven claims computable and auditable at each level of the system
- **s3_adjudication** (d2): Independent verification implemented via S3 that provides objective proof of claims; the external adjudicator that makes proven computable
- **s3_verification** (d2): The technical mechanism by which S3 serves as external adjudicator; verification of vault contents and cert ladder compliance
- **proven_is_computable** (d3): The verification architecture where 'proven' status is achieved through vault plus cert ladders plus S3 as external adjudicator; a computable proof chain

### from `premise_receipts`
- **external_adjudicator** (d1): an independent third-party verifier, implemented as S3, that provides objective proof of claims
- **the_vault** (d1): The immutable storage layer where proven assets are archived on S3

### from `treasure_sentence`
- **cert_ladder** (d1): Certification hierarchy that elevates assets from draft to proven status across levels
- **s3_adjudicator** (d1): External storage adjudicator that serves as the independent proof layer
- **vault** (d1): The storage layer where proven typed assets are recorded; SOMA implementation vaulted equals proven
- **soma** (d2): The storage system that implements vault semantics; implemented assets get vaulted

## CONSUMERS (what needs this)
`depth_1_deploy`, `grand_argument`, `it_is_one_system`

---
*Projected from the `the grand argument (draft kernel v0)` KB (260 concepts / 330 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_

---
name: 0.1.6-understand-receipt_scene
description: [0.1.6] A scene that functions as proof; the GAS instantiation of a premise that carries its own evidence attached to 
---

# understand-receipt_scene

**CALL NUMBER:** `?.receipt_scene : treasure_sentence(1), premise_receipts(1)`
**DEFINITION:** A scene that functions as proof; the GAS instantiation of a premise that carries its own evidence attached to the proven asset

Invoke this skill to understand `receipt_scene` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `?`
- **vault_to_receipt** (d1): «undefined»
- **s3_adjudication** (d4): Independent verification implemented via S3 that provides objective proof of claims; the external adjudicator that makes proven computable
- **s3_verification** (d4): The technical mechanism by which S3 serves as external adjudicator; verification of vault contents and cert ladder compliance
- **proven_is_computable** (d5): The verification architecture where 'proven' status is achieved through vault plus cert ladders plus S3 as external adjudicator; a computable proof chain

### from `premise_receipts`
- **external_adjudicator** (d3): an independent third-party verifier, implemented as S3, that provides objective proof of claims

### from `treasure_sentence`
- **cert_ladder** (d2): Certification hierarchy that elevates assets from draft to proven status across levels

## CONSUMERS (what needs this)
`post_receipt`, `scene`, `scene_as_receipt`, `testimony`

---
*Projected from the `the grand argument (draft kernel v0)` KB (260 concepts / 330 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_

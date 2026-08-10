---
name: 0.2.2-understand-external_adjudicator
description: [0.2.2] an independent third-party verifier, implemented as S3, that provides objective proof of claims
---

# understand-external_adjudicator

**CALL NUMBER:** `premise_receipts.external_adjudicator`
**DEFINITION:** an independent third-party verifier, implemented as S3, that provides objective proof of claims

Invoke this skill to understand `external_adjudicator` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `?`
- **s3_adjudication** (d1): Independent verification implemented via S3 that provides objective proof of claims; the external adjudicator that makes proven computable
- **s3_verification** (d1): The technical mechanism by which S3 serves as external adjudicator; verification of vault contents and cert ladder compliance
- **proven_is_computable** (d2): The verification architecture where 'proven' status is achieved through vault plus cert ladders plus S3 as external adjudicator; a computable proof chain

## CONSUMERS (what needs this)
`cert_ladder`, `it_is_proven`

---
*Projected from the `the grand argument (draft kernel v0)` KB (260 concepts / 330 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_

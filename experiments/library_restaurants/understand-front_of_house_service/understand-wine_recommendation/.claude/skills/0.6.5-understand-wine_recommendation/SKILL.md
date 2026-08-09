---
name: 0.6.5-understand-wine_recommendation
description: [0.6.5] Suggesting wine pairings based on menu selections
---

# understand-wine_recommendation

**CALL NUMBER:** `front_of_house_service.wine_recommendation`
**DEFINITION:** Suggesting wine pairings based on menu selections

Invoke this skill to understand `wine_recommendation` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `?`
- **wine_pairing_expertise** (d2): «undefined»

### from `front_of_house_service`
- **sommelier_visits_table** (d1): Wine expert consulting on selections and pours
- **wine_decanting** (d1): Allowing wine to breathe by transferring to decanter
- **wine_pouring** (d1): Proper technique for decanting and pouring wine service
- **wine_temperature_check** (d1): Verifying wine is served at appropriate temperature
- **wine_list_presentation** (d2): Offering and explaining wine selection options

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_

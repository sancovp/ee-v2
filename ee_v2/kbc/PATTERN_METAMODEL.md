# Pattern geometry metamodel (research synthesis wf_cfad6a31)

## 1. The substrate a Prolog gate needs (before the invariants)

Roles are **types**, not instances. When an LLM fills a geometry it produces a set of concrete architecture elements, each tagged with the role it plays, plus the concrete typed edges it observed. So the Prolog domain has exactly four fact shapes:

```prolog
role(Pattern, RoleName).                 % the geometry's vocabulary of roles
maps_to(Element, RoleName).              % the LLM's filling: element plays role
edge(Src, RelType, Dst).                 % an observed structural edge in the real system
% invariants are declared, not observed:
inv_required(RelType, RoleA, RoleB, Quant).
inv_forbidden(RelType, RoleA, RoleB).
```

Every invariant below is checked at the **element level** (over `edge/3` after resolving `maps_to/2`) but declared at the **role level**. That gap — role-declared, element-checked — is why every invariant is implicitly quantified over all elements of a role, and why residue can name a concrete offending element/pair.

---

## 2. Canonical controlled vocabulary (union of all six, deduped — 13 edge types)

| edge | meaning (one line) |
|---|---|
| `implements` | source provides a concrete realization that satisfies target's interface/contract |
| `extends` | source is a subclass/specialization of target (inheritance from a concrete/base type) |
| `composes` | source owns/holds target as a part (has-a; lifecycle/aggregation), normally by the target's abstraction |
| `depends_on` | source's definition requires knowledge of target — the generic directional source/compile-time coupling edge |
| `delegates_to` | source forwards a responsibility to target at runtime (hands the work off) |
| `calls` | source invokes an operation on target (runtime control transfer) |
| `references` | source names/mentions target in its signature or body — weaker "knows-about" than `depends_on` |
| `creates` | source instantiates/constructs target (factory responsibility) |
| `notifies` | source pushes events/updates to target (one-to-many broadcast / publish) |
| `routes_to` | source hands its output stream to target (dataflow connection) |
| `adapts` | source translates target's interface into a different contract |
| `persists` | source stores/retrieves target's state to durable storage |
| `exposes` | source publishes target (an operation/port/interface) as a callable surface |

Two natural clusters a builder should keep in mind, because invariants trade on them:
- **Coupling/knowledge edges** (`depends_on`, `references`, `calls`, `creates`, `composes`) — these are what "forbidden" invariants almost always police (they encode *illegitimate knowledge*).
- **Contract edges** (`implements`, `extends`, `adapts`) — these are what "required" invariants almost always demand (they encode *substitutability*).

---

## 3. The invariant forms

Across all six patterns, **every declared invariant is a required-edge or a forbidden-edge over a role pair.** No third syntactic form actually appears. But the *quantification* varies, and two patterns declare a family of edges that is really a single higher-order constraint enumerated by hand. The complete form catalog a builder should implement:

**Form A — FORBIDDEN edge** (the workhorse; every pattern uses it).
Declared `forbidden RelType(RoleA -> RoleB)`. Semantics: *no* pair of elements witnesses it.
```prolog
violation(forbidden(R,A,B), edge(S,R,D)) :-
    inv_forbidden(R,A,B), maps_to(S,A), maps_to(D,B), edge(S,R,D).
```
Residue = the concrete offending edge. Examples: `forbidden depends_on(context->concrete_strategy)`, `forbidden depends_on(domain->infrastructure)`, `forbidden references(subject->concrete_observer)`.

**Form A′ — FORBIDDEN self-edge** (Pipes & Filters). Same as A with `RoleA == RoleB`; the check must accept `S = D` (self-loops) *and* `S ≠ D` (peer-to-peer) — both are the violation. `forbidden routes_to(filter->filter)`, `…references(filter->filter)`, `…calls(filter->filter)`, `…depends_on(filter->filter)` are one idea ("filters never touch filters; only pipes connect them") declared once per edge type. A builder may want sugar: `forbidden_any({routes_to,references,calls,depends_on}, filter, filter)`.

**Form B — REQUIRED edge, ∀-source** (the default required form).
Declared `required RelType(RoleA -> RoleB)`. Semantics: *every* element playing RoleA has the edge to *some* element playing RoleB.
```prolog
violation(required(R,A,B,forall_src), missing(S,R,B)) :-
    inv_required(R,A,B,forall_src), maps_to(S,A),
    \+ ( maps_to(D,B), edge(S,R,D) ).
```
Residue = the concrete RoleA element that lacks the edge. Examples: `required implements(concrete_strategy->strategy)`, `required implements(concrete_repository->repository_interface)`, `required depends_on(presentation->application)`.

**Form B′ — REQUIRED edge, ∀-target** (the "required-implements-for-all-of-a-role" form the brief anticipated).
Semantics: *every* element playing RoleB is covered by the edge from *some* RoleA. Use this when the point is "no target left dangling" rather than "no source left unbound" — e.g. every `driven_port` must be implemented by some `driven_adapter`; every `subject` abstraction extended by some `concrete_subject`. The two required readings are distinct and both are legitimate; a builder should carry a quantifier tag (`forall_src` | `forall_tgt`) on `inv_required/4` rather than pick one globally. Most single-abstraction cases (Strategy's lone `strategy` role) collapse the two, which is why the source geometries didn't need to disambiguate — but Hexagonal (`composes(domain_core->driven_port)` with several ports) and Observer genuinely want ∀-target.

That is the whole checkable core: **A, A′, B, B′.** Everything in the six patterns reduces to these.

---

## 4. Invariants that are NOT a single simple edge fact — the closure/typed-set cases

Two patterns declare invariants that are *currently written as an enumeration of Form-A edges* but whose true intent is a higher-order structural constraint. A builder should implement these as first-class invariant kinds, because the enumeration is lossy.

**(i) Hexagonal — "the core depends only on ports" = a CLOSED-TARGET-SET constraint.**
The geometry lists three hand-picked forbidden targets: `forbidden depends_on(domain_core->driven_adapter | external_system | driving_adapter)`. The real rule is universal over the *complement*: *every* outgoing `depends_on` edge from `domain_core` must land in `{driving_port, driven_port}`. Implement as a new form:
```prolog
% required: all outgoing R edges from RoleA target only roles in AllowedSet
violation(closed_targets(R,A,Allowed), edge(S,R,D)) :-
    inv_closed_targets(R,A,Allowed), maps_to(S,A), edge(S,R,D),
    maps_to(D,B), \+ member(B,Allowed).
```
This catches drift the enumeration misses (a core that depends on some *newly introduced* concrete role nobody forbade by name). The same shape expresses Layered's closed-layer intent and Repository's "domain_client depends only on repository_interface."

**(ii) Layered — "no upward dependency" = a TRANSITIVE-CLOSURE constraint.**
The geometry enumerates direct forbidden pairs (`forbidden depends_on(domain->presentation)`, `…(presentation->infrastructure)`, etc.). Those Form-A edges correctly forbid **direct skip-layer and direct upward** edges. But the architectural law is stronger: *no `depends_on` path of any length* may run upward through the layer order. A closed-layer stack `presentation → application → domain` legitimately lets presentation *transitively* reach domain, so you cannot just forbid the direct edge for adjacency; you must reason over the transitive closure to forbid upward *paths* while allowing downward ones. Implement with a layer ordering plus closure:
```prolog
layer_rank(presentation,4). layer_rank(application,3).
layer_rank(domain,2).       layer_rank(infrastructure,1).  % (seam handled by inv_required implements)
reaches(X,Y) :- edge(X,depends_on,Y).
reaches(X,Y) :- edge(X,depends_on,Z), reaches(Z,Y).
violation(no_upward_dep, path(X,Y)) :-
    reaches(X,Y), maps_to(X,Rx), maps_to(Y,Ry),
    layer_rank(Rx,Nx), layer_rank(Ry,Ny), Ny > Nx.
```

**Patterns flagged as needing transitive/closure reasoning:**
- **Layered Architecture** — YES: upward-dependency is a closure property; the enumerated direct forbiddens are a sound-but-incomplete approximation of it.
- **Hexagonal** — PARTIAL: "core depends only on ports" is a closed-target-set (typed complement) constraint, not plain closure; but if you want to *guarantee* the core cannot transitively reach an external system, that too is a closure check over `depends_on`. In practice dependency-inversion makes the core's out-edges point only inward/at ports, so the closed-target-set check on direct edges is usually sufficient.
- **Repository** — MILD: "domain_client depends only on repository_interface, never on concrete_repository or persistence_mechanism" is the same closed-target-set shape as Hexagonal (i), expressed here as two enumerated forbiddens.
- **Strategy, Observer, Pipes & Filters** — NO closure needed: all their invariants are pure Form A/A′/B/B′ over direct edges. (Pipes & Filters' `filter↛filter` plus `filter→pipe→filter` gives a linear dataflow, but conformance is checked edge-locally, not by path.)

---

## 5. Residue contract (what "DRIFTED OUT" returns)

The gate should return, per failed invariant, a structured residue naming **the invariant kind, the role-level rule, and the concrete witness**:
- Forbidden (A/A′): `drifted(forbidden, R, A→B, witness=edge(S,R,D))` — "element S (role A) illegitimately R's element D (role B)."
- Required ∀-source (B): `drifted(required_src, R, A→B, witness=element S)` — "S plays A but has no R edge into B."
- Required ∀-target (B′): `drifted(required_tgt, R, A→B, witness=element D)` — "D plays B but nothing in A R's it."
- Closed-target-set (i): `drifted(open_target, R, A, allowed=Set, witness=edge(S,R,D))` — "S (role A) R's D whose role is outside the allowed set."
- Transitive-forbidden (ii): `drifted(upward_path, depends_on, witness=path(X…Y))` — "a dependency path runs from a lower layer up to a higher one."

**STAYS IN PATTERN** ⇔ every declared invariant yields zero violations. The design keeps the vocabulary of relations closed (13 types), the vocabulary of invariant *kinds* closed (A, A′, B, B′, closed-target-set, transitive-forbidden), and pushes all pattern-specificity into the declared `inv_*` facts + role list — so adding a seventh pattern is data, not code.
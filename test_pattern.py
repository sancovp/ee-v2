#!/usr/bin/env python3
"""ee_pattern — THE CONFORMANCE GATE, deterministic proof (real SWI-Prolog).

Pattern-as-geometry-as-gate: fill a geometry with a real architecture mapping,
prove it STAYS IN PATTERN or get residue NAMING the drift.

Asserted:
  T1 Strategy, conformant fill → IN PATTERN
  T2 Strategy, drift (context references a concrete strategy directly) →
     OUT, residue names the forbidden edge
  T3 Strategy, drift (a concrete strategy does NOT implement the interface) →
     OUT, residue names the missing required edge
  T4 Layered, conformant (only downward deps) → IN PATTERN
  T5 Layered, drift (infrastructure depends on presentation, transitively) →
     OUT, forbidden_transitive path named
  T6 malformed: a binding onto a role the geometry never declared → named
  T7 geometry_from_kb rejects a role that isn't a KB concept
"""
import sys

sys.path.insert(0, "/home/ceo/repo/ee-v2")

from ee_v2.kbc.pattern import conformance, geometry_from_kb, drift_report  # noqa: E402

# ── the STRATEGY geometry ────────────────────────────────────────────────────
STRATEGY = {
    "roles": ["context", "strategy_interface", "concrete_strategy"],
    "invariants": [
        {"id": "impl", "inv": "required", "relation": "implements",
         "source_role": "concrete_strategy", "target_role": "strategy_interface"},
        {"id": "delegate", "inv": "required", "relation": "delegates_to",
         "source_role": "context", "target_role": "strategy_interface"},
        {"id": "no_direct", "inv": "forbidden", "relation": "references",
         "source_role": "context", "target_role": "concrete_strategy"},
    ],
}

# ── the LAYERED geometry (transitive: no upward dependency) ───────────────────
LAYERED = {
    "roles": ["presentation", "domain", "infrastructure"],
    "invariants": [
        {"id": "no_up_pd", "inv": "forbidden_transitive", "relation": "depends_on",
         "source_role": "infrastructure", "target_role": "presentation"},
        {"id": "no_up_di", "inv": "forbidden_transitive", "relation": "depends_on",
         "source_role": "domain", "target_role": "presentation"},
    ],
}


def main():
    # T1 — conformant Strategy
    v = conformance(STRATEGY, {
        "bindings": [("PaymentContext", "context"),
                     ("PaymentMethod", "strategy_interface"),
                     ("CreditCard", "concrete_strategy"),
                     ("Paypal", "concrete_strategy")],
        "edges": [("delegates_to", "PaymentContext", "PaymentMethod"),
                  ("implements", "CreditCard", "PaymentMethod"),
                  ("implements", "Paypal", "PaymentMethod")],
    }, subject="strategy_ok")
    assert v["in_pattern"], v
    print("  T1 Strategy conformant → IN PATTERN ✓")

    # T2 — drift: context references a concrete strategy directly
    v = conformance(STRATEGY, {
        "bindings": [("PaymentContext", "context"),
                     ("PaymentMethod", "strategy_interface"),
                     ("CreditCard", "concrete_strategy")],
        "edges": [("delegates_to", "PaymentContext", "PaymentMethod"),
                  ("implements", "CreditCard", "PaymentMethod"),
                  ("references", "PaymentContext", "CreditCard")],   # DRIFT
    }, subject="strategy_direct")
    assert not v["in_pattern"]
    assert ("no_direct", "PaymentContext", "CreditCard") in v["drift"]["forbidden"]
    print(f"  T2 Strategy direct-reference drift → OUT; "
          f"{drift_report(v).splitlines()[1].strip()} ✓")

    # T3 — drift: a concrete strategy doesn't implement the interface
    v = conformance(STRATEGY, {
        "bindings": [("PaymentContext", "context"),
                     ("PaymentMethod", "strategy_interface"),
                     ("CreditCard", "concrete_strategy"),
                     ("Wire", "concrete_strategy")],
        "edges": [("delegates_to", "PaymentContext", "PaymentMethod"),
                  ("implements", "CreditCard", "PaymentMethod")],  # Wire missing
    }, subject="strategy_missing")
    assert not v["in_pattern"]
    assert ("impl", "Wire") in v["drift"]["missing"], v["drift"]
    print("  T3 Strategy missing-implements drift → OUT; residue names Wire ✓")

    # T4 — conformant layered (only downward deps)
    v = conformance(LAYERED, {
        "bindings": [("WebUI", "presentation"), ("OrderSvc", "domain"),
                     ("PgRepo", "infrastructure")],
        "edges": [("depends_on", "WebUI", "OrderSvc"),
                  ("depends_on", "OrderSvc", "PgRepo")],
    }, subject="layered_ok")
    assert v["in_pattern"], v
    print("  T4 Layered downward-only → IN PATTERN ✓")

    # T5 — drift: infra depends on presentation TRANSITIVELY (via domain)
    v = conformance(LAYERED, {
        "bindings": [("WebUI", "presentation"), ("OrderSvc", "domain"),
                     ("PgRepo", "infrastructure")],
        "edges": [("depends_on", "WebUI", "OrderSvc"),
                  ("depends_on", "PgRepo", "OrderSvc"),
                  ("depends_on", "OrderSvc", "WebUI")],   # upward → cycle path
    }, subject="layered_up")
    assert not v["in_pattern"]
    paths = v["drift"]["forbidden_path"]
    assert any(f == "PgRepo" and t == "WebUI" for _i, f, t in paths), paths
    print("  T5 Layered transitive upward-dep → OUT; forbidden PATH named ✓")

    # T6 — malformed: binding onto an undeclared role
    v = conformance(STRATEGY, {
        "bindings": [("X", "context"), ("Y", "phantom_role")],
        "edges": [],
    }, subject="strategy_malformed")
    assert not v["in_pattern"]
    assert "phantom_role" in v["drift"]["malformed"], v["drift"]
    print("  T6 malformed role binding → named ✓")

    # T7 — geometry_from_kb guards role membership
    class _KB:
        concepts = {"context": "", "strategy_interface": ""}
    try:
        geometry_from_kb(_KB(), ["context", "not_a_concept"], [])
        raise AssertionError("should have rejected non-KB role")
    except ValueError as e:
        assert "not_a_concept" in str(e)
    print("  T7 geometry_from_kb rejects a non-KB role ✓")


if __name__ == "__main__":
    main()
    print("PATTERN PASS — a filled geometry is proven IN PATTERN, or the "
          "residue NAMES exactly which invariant drifted (forbidden edge, "
          "forbidden path, missing required edge, malformed binding).")

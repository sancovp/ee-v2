% ee_pattern gate — PATTERN-AS-GEOMETRY-AS-GATE (Isaac 2026-08-11: "a KB of
% code patterns so LLMs can fill out the geometries and figure out if they are
% staying in pattern or not for different archis").
%
% A pattern's GEOMETRY = roles + structural INVARIANTS (required / forbidden
% edges over roles), taken from the certified pattern KB. An LLM FILLS the
% geometry: binds real architecture elements to roles + declares the real
% edges between them. This gate proves the filled geometry STAYS IN PATTERN,
% or emits RESIDUE naming exactly which invariant DRIFTED:
%   drift_forbidden(Inv, From, To)  a forbidden edge is actually present
%   drift_missing(Inv, From)        a required edge is absent for an element
% forbidden_transitive additionally forbids a PATH (layered "no upward dep",
% hexagonal "core reaches only ports"): residue drift_forbidden_path(Inv,F,T).
%
% candidate_* = the seat's claims (the geometry it read + the mapping it filled)
% source_* = the journey engine's witness that the mapping pass completed.

:- dynamic map_subject/2.
:- dynamic map_kappa_domain/2.
:- dynamic map_kappa_invariant/2.
:- dynamic candidate_role/2.               % candidate_role(S, RoleId)
:- dynamic candidate_pattern_inv/6.        % (S, Kind, RelType, FromRole, ToRole, InvId)
:- dynamic candidate_bind/3.               % candidate_bind(S, Element, RoleId)
:- dynamic candidate_edge/4.               % candidate_edge(S, RelType, FromEl, ToEl)
:- dynamic source_pass_complete/1.

map_domain_target_kind(ee_pattern).
map_domain_target_subject(ee_pattern, Subject) :-
    map_subject(ee_pattern, Subject).

pattern_kappa_complete(S) :-
    map_kappa_domain(S, ee_conformance),
    map_kappa_invariant(S, stays_in_pattern).

% every bind names a declared role (a mapping onto a phantom role is malformed)
unbound_role(S, RoleId) :-
    candidate_bind(S, _, RoleId),
    \+ candidate_role(S, RoleId).

% FORBIDDEN — a real edge of the forbidden type exists between bound elements
% of the two roles
forbidden_hit(S, Inv, From, To) :-
    candidate_pattern_inv(S, forbidden, RelType, FromRole, ToRole, Inv),
    candidate_bind(S, From, FromRole),
    candidate_bind(S, To, ToRole),
    candidate_edge(S, RelType, From, To).

% FORBIDDEN_TRANSITIVE — a PATH of RelType edges from a FromRole element to a
% ToRole element (visited-list bounded; terminates on any finite graph)
reach(S, RelType, X, Y, _) :- candidate_edge(S, RelType, X, Y).
reach(S, RelType, X, Y, V) :-
    candidate_edge(S, RelType, X, Z), \+ memberchk(Z, V),
    reach(S, RelType, Z, Y, [Z|V]).
forbidden_path_hit(S, Inv, From, To) :-
    candidate_pattern_inv(S, forbidden_transitive, RelType, FromRole, ToRole, Inv),
    candidate_bind(S, From, FromRole),
    candidate_bind(S, To, ToRole),
    reach(S, RelType, From, To, [From]).

% REQUIRED — some element in FromRole has NO edge of RelType to ANY element in
% ToRole (the required structural fact is missing for that element)
required_missing(S, Inv, From) :-
    candidate_pattern_inv(S, required, RelType, FromRole, ToRole, Inv),
    candidate_bind(S, From, FromRole),
    \+ ( candidate_bind(S, To, ToRole),
         candidate_edge(S, RelType, From, To) ).

pattern_well_formed(S) :- source_pass_complete(S), \+ unbound_role(S, _).
no_forbidden(S)  :- source_pass_complete(S), \+ forbidden_hit(S, _, _, _).
no_forbidden_path(S) :- source_pass_complete(S), \+ forbidden_path_hit(S, _, _, _).
all_required(S)  :- source_pass_complete(S), \+ required_missing(S, _, _).

ee_pattern_proof(S, stays_in_pattern) :-
    pattern_kappa_complete(S),
    pattern_well_formed(S),
    no_forbidden(S),
    no_forbidden_path(S),
    all_required(S).

map_domain_target_status(S, ee_pattern, compiled) :-
    ee_pattern_proof(S, stays_in_pattern), !.
map_domain_target_status(S, ee_pattern, partial) :-
    map_subject(ee_pattern, S).

map_domain_target_obligation(_S, ee_pattern, kappa_domain(ee_conformance)).
map_domain_target_obligation(_S, ee_pattern, kappa_invariant(stays_in_pattern)).
map_domain_target_obligation(S, ee_pattern, well_formed_mapping) :-
    map_subject(ee_pattern, S).
map_domain_target_obligation(S, ee_pattern, no_forbidden_edges) :-
    map_subject(ee_pattern, S).
map_domain_target_obligation(S, ee_pattern, required_edges_present) :-
    map_subject(ee_pattern, S).

map_domain_target_obligation_status(S, ee_pattern, kappa_domain(ee_conformance), compiled) :-
    map_kappa_domain(S, ee_conformance), !.
map_domain_target_obligation_status(S, ee_pattern, kappa_domain(ee_conformance), partial) :-
    \+ map_kappa_domain(S, ee_conformance).
map_domain_target_obligation_status(S, ee_pattern, kappa_invariant(stays_in_pattern), compiled) :-
    map_kappa_invariant(S, stays_in_pattern), !.
map_domain_target_obligation_status(S, ee_pattern, kappa_invariant(stays_in_pattern), partial) :-
    \+ map_kappa_invariant(S, stays_in_pattern).
map_domain_target_obligation_status(S, ee_pattern, well_formed_mapping, compiled) :-
    pattern_well_formed(S), !.
map_domain_target_obligation_status(S, ee_pattern, well_formed_mapping, partial) :-
    map_subject(ee_pattern, S), \+ pattern_well_formed(S).
map_domain_target_obligation_status(S, ee_pattern, no_forbidden_edges, compiled) :-
    no_forbidden(S), no_forbidden_path(S), !.
map_domain_target_obligation_status(S, ee_pattern, no_forbidden_edges, partial) :-
    map_subject(ee_pattern, S), (\+ no_forbidden(S) ; \+ no_forbidden_path(S)).
map_domain_target_obligation_status(S, ee_pattern, required_edges_present, compiled) :-
    all_required(S), !.
map_domain_target_obligation_status(S, ee_pattern, required_edges_present, partial) :-
    map_subject(ee_pattern, S), \+ all_required(S).

% THE RESIDUE — extension terms NAME every drift (the "you left the pattern
% HERE" signal an LLM can act on directly)
map_domain_target_extension_term(frontier, S, ee_pattern, malformed_role(R)) :-
    unbound_role(S, R).
map_domain_target_extension_term(frontier, S, ee_pattern, drift_forbidden(Inv, From, To)) :-
    forbidden_hit(S, Inv, From, To).
map_domain_target_extension_term(frontier, S, ee_pattern, drift_forbidden_path(Inv, From, To)) :-
    forbidden_path_hit(S, Inv, From, To).
map_domain_target_extension_term(frontier, S, ee_pattern, drift_missing(Inv, From)) :-
    required_missing(S, Inv, From).
map_domain_target_extension_term(outputs, S, ee_pattern, ee_pattern_conformant(S)) :-
    ee_pattern_proof(S, stays_in_pattern).

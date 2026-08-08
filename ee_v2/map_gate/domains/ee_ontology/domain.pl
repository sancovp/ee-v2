% EE ontology gate — P1's claimed ontology must be CLOSED and CONNECTED.
% candidate_* = the seat's claims; source_* = the journey engine's witness.
% SOUP residue names each dangling reference / orphan concept — the retry
% signal an LLM can act on directly.

:- dynamic map_subject/2.
:- dynamic map_kappa_domain/2.
:- dynamic map_kappa_invariant/2.
:- dynamic candidate_concept/2.
:- dynamic candidate_relation/4.
:- dynamic source_pass_complete/1.

map_domain_target_kind(ee_ontology).
map_domain_target_subject(ee_ontology, Subject) :-
    map_subject(ee_ontology, Subject).

ee_kappa_complete(Subject) :-
    map_kappa_domain(Subject, ee_conceptualization),
    map_kappa_invariant(Subject, ontology_coherence).

% a relation endpoint that names no declared concept = DANGLING
dangling_ref(Subject, Rel, Endpoint) :-
    candidate_relation(Subject, Rel, Endpoint, _),
    \+ candidate_concept(Subject, Endpoint).
dangling_ref(Subject, Rel, Endpoint) :-
    candidate_relation(Subject, Rel, _, Endpoint),
    \+ candidate_concept(Subject, Endpoint).

% a concept no relation touches = ORPHAN
orphan_concept(Subject, C) :-
    candidate_concept(Subject, C),
    \+ candidate_relation(Subject, _, C, _),
    \+ candidate_relation(Subject, _, _, C).

ontology_closed(Subject) :-
    source_pass_complete(Subject),
    \+ dangling_ref(Subject, _, _).

ontology_connected(Subject) :-
    source_pass_complete(Subject),
    \+ orphan_concept(Subject, _).

ee_ontology_proof(Subject, ontology_coherence) :-
    ee_kappa_complete(Subject),
    ontology_closed(Subject),
    ontology_connected(Subject).

map_domain_target_status(Subject, ee_ontology, compiled) :-
    ee_ontology_proof(Subject, ontology_coherence),
    !.
map_domain_target_status(Subject, ee_ontology, partial) :-
    map_subject(ee_ontology, Subject).

map_domain_target_obligation(_S, ee_ontology, kappa_domain(ee_conceptualization)).
map_domain_target_obligation(_S, ee_ontology, kappa_invariant(ontology_coherence)).
map_domain_target_obligation(Subject, ee_ontology, closed_ontology) :-
    map_subject(ee_ontology, Subject).
map_domain_target_obligation(Subject, ee_ontology, connected_ontology) :-
    map_subject(ee_ontology, Subject).

map_domain_target_obligation_status(S, ee_ontology, kappa_domain(ee_conceptualization), compiled) :-
    map_kappa_domain(S, ee_conceptualization), !.
map_domain_target_obligation_status(S, ee_ontology, kappa_domain(ee_conceptualization), partial) :-
    \+ map_kappa_domain(S, ee_conceptualization).
map_domain_target_obligation_status(S, ee_ontology, kappa_invariant(ontology_coherence), compiled) :-
    map_kappa_invariant(S, ontology_coherence), !.
map_domain_target_obligation_status(S, ee_ontology, kappa_invariant(ontology_coherence), partial) :-
    \+ map_kappa_invariant(S, ontology_coherence).
map_domain_target_obligation_status(S, ee_ontology, closed_ontology, compiled) :-
    ontology_closed(S), !.
map_domain_target_obligation_status(S, ee_ontology, closed_ontology, partial) :-
    map_subject(ee_ontology, S), \+ ontology_closed(S).
map_domain_target_obligation_status(S, ee_ontology, connected_ontology, compiled) :-
    ontology_connected(S), !.
map_domain_target_obligation_status(S, ee_ontology, connected_ontology, partial) :-
    map_subject(ee_ontology, S), \+ ontology_connected(S).

% THE RESIDUE — extension terms NAME every violation (the retry prompt)
map_domain_target_extension_term(frontier, Subject, ee_ontology,
                                 dangling(Rel, Endpoint)) :-
    dangling_ref(Subject, Rel, Endpoint).
map_domain_target_extension_term(frontier, Subject, ee_ontology,
                                 orphan(C)) :-
    orphan_concept(Subject, C).
map_domain_target_extension_term(outputs, Subject, ee_ontology,
                                 ee_ontology_proof(Subject, ontology_coherence)) :-
    ee_ontology_proof(Subject, ontology_coherence).

% EE skill gate — P2's steps must GROUND in P1's CERTIFIED concepts.
% candidate_* = the seat's claimed skill; source_concept = the engine's
% authority (lowered from P1's stored ONT certificate). The frontier NAMES
% every ungrounded use — the retry signal.

:- dynamic map_subject/2.
:- dynamic map_kappa_domain/2.
:- dynamic map_kappa_invariant/2.
:- dynamic candidate_step/2.
:- dynamic candidate_use/3.
:- dynamic source_concept/2.
:- dynamic source_pass_complete/1.

map_domain_target_kind(ee_skill).
map_domain_target_subject(ee_skill, Subject) :-
    map_subject(ee_skill, Subject).

ee_skill_kappa_complete(Subject) :-
    map_kappa_domain(Subject, ee_generalization),
    map_kappa_invariant(Subject, skill_grounding).

ungrounded_use(Subject, Step, Concept) :-
    candidate_use(Subject, Step, Concept),
    \+ source_concept(Subject, Concept).

skill_grounded(Subject) :-
    source_pass_complete(Subject),
    candidate_step(Subject, _),
    \+ ungrounded_use(Subject, _, _).

ee_skill_proof(Subject, skill_grounding) :-
    ee_skill_kappa_complete(Subject),
    skill_grounded(Subject).

map_domain_target_status(Subject, ee_skill, compiled) :-
    ee_skill_proof(Subject, skill_grounding),
    !.
map_domain_target_status(Subject, ee_skill, partial) :-
    map_subject(ee_skill, Subject).

map_domain_target_obligation(_S, ee_skill, kappa_domain(ee_generalization)).
map_domain_target_obligation(_S, ee_skill, kappa_invariant(skill_grounding)).
map_domain_target_obligation(Subject, ee_skill, grounded_steps) :-
    map_subject(ee_skill, Subject).

map_domain_target_obligation_status(S, ee_skill, kappa_domain(ee_generalization), compiled) :-
    map_kappa_domain(S, ee_generalization), !.
map_domain_target_obligation_status(S, ee_skill, kappa_domain(ee_generalization), partial) :-
    \+ map_kappa_domain(S, ee_generalization).
map_domain_target_obligation_status(S, ee_skill, kappa_invariant(skill_grounding), compiled) :-
    map_kappa_invariant(S, skill_grounding), !.
map_domain_target_obligation_status(S, ee_skill, kappa_invariant(skill_grounding), partial) :-
    \+ map_kappa_invariant(S, skill_grounding).
map_domain_target_obligation_status(S, ee_skill, grounded_steps, compiled) :-
    skill_grounded(S), !.
map_domain_target_obligation_status(S, ee_skill, grounded_steps, partial) :-
    map_subject(ee_skill, S), \+ skill_grounded(S).

map_domain_target_extension_term(frontier, Subject, ee_skill,
                                 ungrounded(Step, Concept)) :-
    ungrounded_use(Subject, Step, Concept).
map_domain_target_extension_term(outputs, Subject, ee_skill,
                                 ee_skill_proof(Subject, skill_grounding)) :-
    ee_skill_proof(Subject, skill_grounding).

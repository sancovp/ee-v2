% EE argument gate — §24c THE ALGEBRA OF ARTICULATION.
% A claim held only as a hyperedge (unordered proven set) is knowledge
% without language; the minted skeleton — a DAG of operator edges over the
% hyperedge — makes it walkable. This domain proves the skeleton is:
%   GROUNDED   every endpoint is a certified atom (the witness's authority)
%   ROOTED     the root claim is actually argued (an outgoing because/explains)
%   ACYCLIC    an order, not a knot — sentences are walks
%   WARRANTED  every `because` discharges: its ground carries a since /
%              together_fit support edge (the canonical template "X because
%              is-a Y since parts together fit pattern Y", v1-flattened)
% Residue NAMES the unfilled slot: ungrounded / unrooted / cyclic /
% unwarranted. Deeper mereology (parts verified against the KB's own
% part-of edges) is the next tightening — declared, not silently skipped.

:- dynamic map_subject/2.
:- dynamic map_kappa_domain/2.
:- dynamic map_kappa_invariant/2.
:- dynamic candidate_root/2.
:- dynamic candidate_arg/5.
:- dynamic source_concept/2.
:- dynamic source_pass_complete/1.

map_domain_target_kind(ee_argument).
map_domain_target_subject(ee_argument, Subject) :-
    map_subject(ee_argument, Subject).

arg_kappa_complete(Subject) :-
    map_kappa_domain(Subject, ee_articulation),
    map_kappa_invariant(Subject, argument_walkable).

arg_edge(S, X, Y) :- candidate_arg(S, _, _, X, Y).

% GROUNDED — an endpoint no certificate vouches for
ungrounded(S, X) :-
    (arg_edge(S, X, _) ; arg_edge(S, _, X)),
    \+ source_concept(S, X).

% ROOTED — the root claim never argued
unrooted(S, R) :-
    candidate_root(S, R),
    \+ candidate_arg(S, _, because, R, _),
    \+ candidate_arg(S, _, explains, R, _).

% ACYCLIC — visited-list reachability (terminates on any finite skeleton)
arg_reach(S, X, Y, _) :- arg_edge(S, X, Y).
arg_reach(S, X, Y, V) :-
    arg_edge(S, X, Z), \+ memberchk(Z, V), arg_reach(S, Z, Y, [Z|V]).
cyclic_node(S, X) :- arg_edge(S, X, Z), arg_reach(S, Z, X, [Z]).

% WARRANTED — a `because` whose ground carries no support edge is asserted
% without its templated subgraph; the seat must warrant it or weaken to `since`
unwarranted(S, E) :-
    candidate_arg(S, _, because, _, E),
    \+ candidate_arg(S, _, since, E, _),
    \+ candidate_arg(S, _, together_fit, E, _).

skeleton_grounded(S)  :- source_pass_complete(S), \+ ungrounded(S, _).
skeleton_rooted(S)    :- source_pass_complete(S), \+ unrooted(S, _).
skeleton_acyclic(S)   :- source_pass_complete(S), \+ cyclic_node(S, _).
skeleton_warranted(S) :- source_pass_complete(S), \+ unwarranted(S, _).

ee_argument_proof(S, argument_walkable) :-
    arg_kappa_complete(S),
    skeleton_grounded(S),
    skeleton_rooted(S),
    skeleton_acyclic(S),
    skeleton_warranted(S).

map_domain_target_status(S, ee_argument, compiled) :-
    ee_argument_proof(S, argument_walkable),
    !.
map_domain_target_status(S, ee_argument, partial) :-
    map_subject(ee_argument, S).

map_domain_target_obligation(_S, ee_argument, kappa_domain(ee_articulation)).
map_domain_target_obligation(_S, ee_argument, kappa_invariant(argument_walkable)).
map_domain_target_obligation(S, ee_argument, grounded_skeleton) :-
    map_subject(ee_argument, S).
map_domain_target_obligation(S, ee_argument, rooted_skeleton) :-
    map_subject(ee_argument, S).
map_domain_target_obligation(S, ee_argument, acyclic_skeleton) :-
    map_subject(ee_argument, S).
map_domain_target_obligation(S, ee_argument, warranted_skeleton) :-
    map_subject(ee_argument, S).

map_domain_target_obligation_status(S, ee_argument, kappa_domain(ee_articulation), compiled) :-
    map_kappa_domain(S, ee_articulation), !.
map_domain_target_obligation_status(S, ee_argument, kappa_domain(ee_articulation), partial) :-
    \+ map_kappa_domain(S, ee_articulation).
map_domain_target_obligation_status(S, ee_argument, kappa_invariant(argument_walkable), compiled) :-
    map_kappa_invariant(S, argument_walkable), !.
map_domain_target_obligation_status(S, ee_argument, kappa_invariant(argument_walkable), partial) :-
    \+ map_kappa_invariant(S, argument_walkable).
map_domain_target_obligation_status(S, ee_argument, grounded_skeleton, compiled) :-
    skeleton_grounded(S), !.
map_domain_target_obligation_status(S, ee_argument, grounded_skeleton, partial) :-
    map_subject(ee_argument, S), \+ skeleton_grounded(S).
map_domain_target_obligation_status(S, ee_argument, rooted_skeleton, compiled) :-
    skeleton_rooted(S), !.
map_domain_target_obligation_status(S, ee_argument, rooted_skeleton, partial) :-
    map_subject(ee_argument, S), \+ skeleton_rooted(S).
map_domain_target_obligation_status(S, ee_argument, acyclic_skeleton, compiled) :-
    skeleton_acyclic(S), !.
map_domain_target_obligation_status(S, ee_argument, acyclic_skeleton, partial) :-
    map_subject(ee_argument, S), \+ skeleton_acyclic(S).
map_domain_target_obligation_status(S, ee_argument, warranted_skeleton, compiled) :-
    skeleton_warranted(S), !.
map_domain_target_obligation_status(S, ee_argument, warranted_skeleton, partial) :-
    map_subject(ee_argument, S), \+ skeleton_warranted(S).

% THE RESIDUE — extension terms NAME every unfilled slot (the retry prompt)
map_domain_target_extension_term(frontier, S, ee_argument, ungrounded(X)) :-
    ungrounded(S, X).
map_domain_target_extension_term(frontier, S, ee_argument, unrooted(R)) :-
    unrooted(S, R).
map_domain_target_extension_term(frontier, S, ee_argument, cyclic(X)) :-
    cyclic_node(S, X).
map_domain_target_extension_term(frontier, S, ee_argument, unwarranted(E)) :-
    unwarranted(S, E).
map_domain_target_extension_term(outputs, S, ee_argument,
                                 ee_argument_proof(S, argument_walkable)) :-
    ee_argument_proof(S, argument_walkable).

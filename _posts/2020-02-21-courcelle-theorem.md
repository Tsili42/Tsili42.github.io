---
layout: post
title:  "Courcelle's theorem"
date: 2020-02-21
---

# Courcelle's theorems

During a class I took a couple semesters ago on Advanced Algorithmic Techniques, while covering the area of Parameterized Complexity, the professor mentioned a theorem known as "Courcelle's Theorem", which ties together the decidability of a property of a graph with a parameter of the graph, known as *treewidth* (a measure of how much said graph resembles a tree). In particular, the theorem states that **any** graph property that can be expressed in a fragment of the second order logic, known as *Monadic Second Order Logic ($\text{MS0}_2$)*, can be solved in linear time on graphs with bounded treewidth.
The theorem immediately fascinated me, as it promised a long-wished-for tool inside Combinatorial Optimization which I haven't seen before; a way to describe in formal language problems that are solvable effectively. At first, the theorem felt as magic and out of reach. How can the syntactic expression of a property guarantee that there is an algorithm to solve it? How can one be sure about any $\text{MS0}_2$ formula, no matter how long or complex that might be (although, I now feel that younger-Nikos should have guessed something about **spoiler** Automata)? And what about the linear time algorithm? What is the dependence on the constants that the asymptotic notation hides (e.g the length of the formula)? How does the obscure notion of treewidth fit in the picture? When a professor in another theoretical class told us we need to find a topic to present from the areas of Mathematics, Logic and Computer Science, I didn't need to look any further.
Briefly, the proof of the theorem starts by computing a tree decomposition of the graph and then transforming that into a parse tree (namely, a tree of symbols from a specific alphabet) which encodes in a compact way the initial graph. The parse tree is then fed as input to a *Tree Automaton* (similar to a DFA, but its input must be a tree), which accepts if and only if the parse tree has the desired property. Since we promised the decidability of each property described in $\text{MS0}_2$, we rely on the graph-theoretic analog of Myhill-Nerode theorem for proving that a large class of automata recognizes the class of bounded-treewidth graphs.
See more [here](https://github.com/Tsili42/courcelles_theorem/blob/master/Logic_II_Project.pdf) and if you feel you need more details (and happen to be able to read greek), see my project [report](https://github.com/Tsili42/courcelles_theorem/blob/master/report.pdf).

### Existence of a Hamilton cycle in a graph $G = (V, E)$ expressed in $\text{MSO}_2$

$$\text{Hamiltonicity} \equiv \exists R \subseteq E (\text{conn}(R) \land \forall v \in V \text{deg2}(v, R)),$$

where:
* $\text{conn}(R) \equiv \forall Y \subseteq V [(\exists u \in V (u \in Y) \land  \exists v \in V (v \notin Y)) \to (\exists e \in R, u \in Y, v \notin Y (\text{inc}(u,e) \land \text{inc}(u,e)))]$
* $\text{deg2}(u, R) \equiv \exists e_1, e_2 \in R [(e_1 \neq e_2 \land \text{inc}(e_1,u) \land \text{inc}(e_2, u) \land (\forall e_3 \in R(\text{inc}(e_3,u) \to (e_3=e_1 \lor e_3=e_2)))]$

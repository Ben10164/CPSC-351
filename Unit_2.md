# CPSC 351 <!-- omit from toc -->

* [DPDA's](#dpdas)
* [Turing Machines](#turing-machines)
* [Church-Turing Hypothesis](#church-turing-hypothesis)
  * [Formal Definition of Turing Machine](#formal-definition-of-turing-machine)
* [Configuration of a TM](#configuration-of-a-tm)
* [Turing-Recognizable Languages](#turing-recognizable-languages)
  * [Deciders](#deciders)

## DPDA's

Deterministic Push Down Automata

* A PDA with all the transition functions altered, so they go to a non-null state
* The class of deterministic context free languages is closed under complementation

Here is a context free language:

$A = \{a^i b^k c^k | i \neq j \text{ or } j \neq k, k \ge 0\}$  
$A_c = \{a^i b^i c^i | i \ge 0\}$

## Turing Machines

Alan Turing: *On Computable Numbers*

TM:

* Controller
* Read/Write head
* Infinite tape
  * Stores 1s and 0s
* Essentially a bunch of if statements inside a for loop

## Church-Turing Hypothesis

* There is no more powerful computational device than a Turing machine
* Anything that may be computed, may be computed on a Turing machine
* Everything can be reduced to a Turing machine

Turing Complete:

* Loop
* Conditional
* Assignment
* Executed in sequence

$B = \{w # w | w \in \{0, 1\}^*\}$

> Accept: `01010#01010`
> Reject: `00010#01010`

Algorithm

1. Zig/Zag back and forth crossing out pairs
2. If
   1. pair not equal, reject
   2. RHS > LHS
   3. RHS < LHS

### Formal Definition of Turing Machine

A Turing Machine is a 7-tuple

$(Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}})

* $Q$
* $\Sigma$
  * The input alphabet
  * Does **NOT** contain the blank character ($\sqcup$)
* $\Gamma$
  * The tape alphabet
  * $\sqcup \in \Gamma, \Sigma \subseteq \Gamma$
* $\delta$
  * $\delta: Q \times \Gamma \rarr Q \times \Gamma \times \{L, R\}$
  * Action
    * halt in accept
    * halt in reject
    * loop forever
* $q_0$
* $q_{\text{accept}}$
* $q_{\text{reject}})$

## Configuration of a TM

* State
* Tape Contents
* Head Location

Yields:

"Configuration $c_1$ yields configuration $c_2$"

ex.

* $a,b,c \in \Gamma$  
* $u, v \in \Gamma^*$  
* $q_1, q_1 \in Q$

So:

* $c_1 = u a q_i b v$  
* $c_2 = u q_j a c v$

$u a q_i b v$ yields $u q_j a c v$

* Read b
* Written c
* moved left

Can be written as:

$\delta(q_i, b) \rarr (q_j,c, L)$

* If in state $q_i$ with character $b$ on the tape, then it yields $q_j$ (a new state), while overwriting $b$ with $c$, and then move left

TM, $m$, accepts input, $w$, if there are a sequence of configurations:

$$c_1, c_2, ..., c_k$$

S.T.

1. $c_1$ is a start start for input $w$
2. Each $c_i$ yields $c_{i+1}$
3. $c_k$ is designated accept state

$L(m)$ is the langauge of $m$ (set of strings that $m$ accepts)

## Turing-Recognizable Languages

Def:

A language is turing-recognizable (recursively enumerable) if some TM recognizes (accepts) it

Turing Machines

* Accept
* Reject
* Loop
  * uh oh, this could be infinite
  * this means calculating this can be a bit of an issue

### Deciders

Subset of Turing Machines

* These TMs make a decision to either accept or rejects and input, rather than loop

Turing-Decidable:

A language is TD (decidable) if some Decider decides it (accepts or rejects it)
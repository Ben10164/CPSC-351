# CPSC 351 <!-- omit from toc -->

* [DPDA's](#dpdas)
* [Turing Machines](#turing-machines)
* [Church-Turing Hypothesis](#church-turing-hypothesis)
  * [Formal Definition of Turing Machine](#formal-definition-of-turing-machine)
* [Configuration of a TM](#configuration-of-a-tm)
* [Turing-Recognizable Languages](#turing-recognizable-languages)
  * [Recognizer](#recognizer)
  * [Deciders](#deciders)
    * [Decider example](#decider-example)
  * [Elementary Distinctiveness Problem](#elementary-distinctiveness-problem)
* [The Acceptance Problem](#the-acceptance-problem)
* [The Halting Problem](#the-halting-problem)

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

$B = \{w \# w | w \in \{0, 1\}^*\}$

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

$(Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}})$

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

Ex.

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

### Recognizer

The term for a normal Turing machine that can Accept, Reject, and Loop (unlike deciders which cannot loop)

### Deciders

Subset of Turing Machines

* These TMs make a decision to either accept or rejects and input, rather than loop

Turing-Decidable:

A language is TD (decidable) if some Decider decides it (accepts or rejects it)

Anything that is computable on a modern computer is computable on a Turing Machine - Church-Turing hypothesis

#### Decider example

$A = \{0^{2^n} | n \ge 0\}$ ($2^n$ amount of zeros)  
if $w \in A$, then |w|$ is a power of $2$.  

* $0$
* $00$
* $0000$
* etc.

if it contains 1 zero, it is an accept state

![Image 39](images/Image-39.png)

$M_2$ = “On input string w:

1. Sweep left to right across the tape, crossing off every other 0.
2. If in stage 1 the tape contained a single 0, accept.
3. If in stage 1 the tape contained more than a single 0 and the
number of 0s was odd, reject.
4. Return the head to the left-hand end of the tape.
5. Go to stage 1.”

Each iteration of stage 1 cuts the number of 0s in half. As the machine sweeps across the tape in stage 1, it keeps track of whether the number of 0s seen is even or odd. If that number is odd and greater than 1, the original number of 0s in the input could not have been a power of 2. Therefore, the machine rejects in this instance. However, if the number of 0s seen is 1, the original number must have been a power of 2. So in this case, the machine accepts.

Now we give the formal description of M2 = (Q, $\Gamma$, $\Gamma$, $\delta$, $q_1$, $q_{\text{accept}}$, $q_{\text{reject}}$):

* $Q=\{q_1,q_2,q_3,q_4,q_5,q_{\text{accept}},q_{\text{reject}}\}$
* $\Sigma=\{0\}$
* $\Gamma=\{0,x,\sqcup\}$
* We describe $\delta$ with a state diagram (See above image)
* The start, accept,and reject states are $q_1$, $q_{\text{accept}}$, and $q_{\text{reject}}$, respectively

$S \in A = 0000$  
$q_1 0000|\sqcup$  
$\sqcup q_2 000|\sqcup$  
$\sqcup x q_3 00|\sqcup$  
$\sqcup x 0 q_4 0|\sqcup$  
$\sqcup x 0 x q_3 | \sqcup$  
$\sqcup x 0 q_5 x | \sqcup$  
$\sqcup x q_5 0 x | \sqcup$  
$\sqcup q_5 x 0 x | \sqcup$  
etc.

![Image 40](images/Image-40.png)

Ex 2.

$B = \{ w \# w | w \in \{0, 1\}^* \}$ (this is the zig zag example)

![Image 41](images/Image-41.png)

### Elementary Distinctiveness Problem

$E = \{ \# x_1 \# x_2 ... \# x_l$ Each $x_i \in \{0 ,1\}^*$ and $x_i \ne x_j$ for each $i \ne j\}$

* #010#111#011 - accept
* #010#111#010 - reject

$A, B, E$ decidable

1. Since a Decidable Language are TR, $A, B, E$ are Turing Reconizable
2. Showing that some language $L$ is turing recongizable, but not Turing Decider is harder

The halting problem:

it is impossible to determine if a progarm will hault or not without running it

Turing machines can:

* Accept (enter q_acc)
* Reject w by halting (enter q_rej)
* Reject w by looping (running forever)

Theorem Reviews

* A is turing recognizable if A = L(M) for some TM M
* A is turing decidable if A = L(M) for some TM decider M. (halts on all inputs)

Multitape Machines in Sipser Land

As always: the secret is in the transition function\
Changed to allow RW head moving on some or all tapes simulatneously

* Formally: $\delta: Q \times \Gamma^k \rarr Q \times \Gamma^k \times \{L, R, S\}^k$
  * Where k is the number of tapes.
  * S is (stay in the same place)

Hilbert's 10th Problem

* An international congress of mathematicians
* Paris 1900
* Davild Hilbert presented 23 unsolved problems in mathematics
* for us #10 is important:
  * Is there a process by which it can be determined by a finite number of operations if a given polynomial has an integer root"

Alonzo Church invented Lambda Calculus: "An unsolvable problem in elementary number theory"

The two definitioins have been showed to be equivalent:

* "Hilbert's problem asked for a process according to which somthing can be determined in a precise number of steps."

The Church_Turing Thesis resolves Hilbert's informal noton of a process into what we now call an algorithm.

In 1970, it was shown that no algorithm exists for determining wheter ha polynomial has integral roots.

D = {all p | p is a polynomial with an integral root}

Hilbert's 10th problem asked if D is decidable

Corollarty 3.19: A language is decidible iff some non-deterministic turing machine decides it

> Narrow D to D'
> > D' = {all p | p is a polynomial over x with an integral root}
> > Make a TM for this:
> > M' = "On input (p), where p is a polynomial over x:
> > > while(there are integers to be tested)
> > > > set x to 0, 1, -1, 2, -2, ...
> > > > if p(x) == 0, accept"
> Extend M' so that it assigns values from the generation of possible values to all varaibles in p
> > M = "On input (p), where p is a polynomial over x:
> > > for each variable, v,
> > > > for each dandidate value, y,
> > > > > set v to y
> > > > > if p evaluates to 0, accept"
> Yuri Matijasevic showed that it is not possible to calculate such bounds for multivariable poilynomials.
> M is not a decider. D is Turing-Recognizable but not Turing-Decidable

## The Acceptance Problem

Testing whetehr a particular DFA accepts a given string may be expressed as a language,
$A_{\text{DFA}}$  
$\text{Let} A = \{ < B, w > | B \text{ is a DFA that accepts the string } w\}$  
$A_{\text{DFA}}$ is the set of all encodings of all DFAs along with the string that 

Prove ${A_\text{DFA}}$ is a decidable languages

Build a TM that decides $A_{\text{DFA}}$

M = "On input <B, w>, where B is a DFA and w is a string:

1. Simulat B on input, w
2. If the simulation ends in an accep tstate, accept. If it ends in a non-accepting state, reject"

Informal proof:

1. Imageine you have a program p that upon the input of an integer, prints Y if the integer is prime, N ptherwise
2. Write a program P that allows P and the integer as input
   * P' checks to see if P is in proper format. If not, go to reject state. You do this all the time. A compiuler chekc sP and creates P'. P' simulates running the underlying machine on w.
   * P' simulates P.

## The Halting Problem

Simple Proof:

* We assume that we do have a program that correctly determins if a program halts or not: lets call it `H`
* Now lets create `D`, a bigger program that encompasses `H`
* D returns the opposite of `H`, by running H and returning the opposite
* What happens when we give `D` its own program
* If `H` determines halt, `D` will actually run forever
* If `H` determines forever, `D` will actually halt
* This contradicts our assumption

This is a problem that cannot be algorithmically solved

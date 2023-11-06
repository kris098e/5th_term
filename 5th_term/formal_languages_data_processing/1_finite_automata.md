# language
## Definition
Languages are sets of strings

Strings of symbols from some alphabet
Can be infinite
### Examples
language = `Z={a,b,c}`
`Z={0,1}`
`Z={010101,011,0111}`

# Regular languages
Languages, L,  are regular if there exists a finite automata, that recognizes L
## Examples
### Not regular
`Z={a, aba, aabaa, aaabaaa, ...}`
### Regular

# Finite automata
double rings are final/accepting state
languages are defined by the way of the arrows

## Terms
states
accept/final state
transition, from one state to another
start state

## Definition and example
$\epsilon$ means the empty string
![[Pasted image 20230904085445.png]]
![[Pasted image 20230904090122.png]]

## Definition, language of an automata
![[Pasted image 20230904092112.png]]

`L(M)` is the language for the automata

In addition to the empty string, this machine accepts any string ending with a 0. Here,
`L(M 3 ) = {w| w is the empty string ε or ends in a 0}`

# Regular operations (These operations on two languages will result in another closed language)
![[Pasted image 20230904093816.png]]
**Concatenation**. Take a string from the first language and then a string from the other language and then put them right after each other
**Star**. All of the strings belong to the language which is stared.

examples
[[Introduction to the theory of computation_third edition - Michael Sipser.pdf#page=68]]

## Union
Have to keep track of both automatas, and if **one of them accepts, then accept**
Can also combine the automata introducing multiple states in each state

# Nondetermination
It may take in a $\epsilon$ at each of the arrows, meaning it will take no input and just proceed. Here can also create branches
means that there exists two or more arrows for a given input
![[Pasted image 20230906142026.png]]
When a branch is met, it duplicates itself, running each of the automaton. If any of the branched succeed then the NFA accepts the input

Any NFA can be turned into an equivalent DFA. This means that if a NFA recognises a language it must be regular.
The procedure can be seen just after `corollary 1.40`. 
![[Pasted image 20230906142356.png]]
![[Pasted image 20230906150538.png]]

## NFAs are closed under union, intersection and star
![[Pasted image 20230906154920.png]]
![[Pasted image 20230906154905.png]]
![[Pasted image 20230906155119.png]]
Notice that we cannot just add the start the initial state to accept state as this would accept undeseriable language additions. Fx adding ø to the set
# Regular expressions
some operators have higher precedence than others

union has the weakest precedence
concatenation is stronger
star is the strongest
## Definion
![[Pasted image 20230911123758.png]]
Means that we are allowed to use syntax in regular expressions
## Shorthands
allowed to write $\sum$ _and then some syntax_ for indicating a regular language, which is just the language
$R^+$  is $R\ concat\ R^*$
$R^k$ is $R\ concat\ R\ concat\ R\dots$
can also omit the concat

R vs L(R) is
R=regular expression
L(R)=the actual language of R

## Special cases
$R\ concat\ ø=ø$

in the arithmetic 
* ø acts like a 0
* union acts like a +
* epsilon acts like a 1

## Goal, prove this theorem
![[Pasted image 20230911124903.png]]

### Prove we can make a DFA from a regular expression
**uses**
![[Pasted image 20230911125004.png]]

![[Pasted image 20230911125320.png]]
ø recognises nothing, since the language is empty

Proof **1.54** via structural proof


Proof this is a regular language (ab ∪ a)∗
![[Pasted image 20230911131357.png]]

Here the concatination symbol is omitted
![[Pasted image 20230911131533.png]]

### Prove we can make a regular expression from a DFA
**look in the book from page 69**
![[Pasted image 20230911132111.png]]

Steps -> 
1. have DFA
2. make generalised NFA
3. make new GNFA
4. ...
5. until reach regular expression


do this via making regular expressions be the transitions

requirement: all states has transitions to all other states, except
1. start state has no transitions in
2. the accept state has no transitions out
start state and accept state are **unique**

#### Making of the generalised NFA
**look in the book from page 69**
start by making a new accept state, remove the other accept states and do _epsilon_ to the new accept state from the other accept states

from the ones which does not accept we make a transition to the new accept state, writing Ø as the regular expression to the accept state. This will never be accepted anyways

...

##### Examples
![[Pasted image 20230911134758.png]]
1. The DFA
2. adding a transition from all of the states to the others and also adding the start state and a new end state
3. remove state 2, concatenate it with state 1
4. remove state 1 and concatenate it with start state



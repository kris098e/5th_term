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
It make take in a $\epsilon$ at each of the arrows, meaning it will take no input and just proceed. Here can also create branches
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

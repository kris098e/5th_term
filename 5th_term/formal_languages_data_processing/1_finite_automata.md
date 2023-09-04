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

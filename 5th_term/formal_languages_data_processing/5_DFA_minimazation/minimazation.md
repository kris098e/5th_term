[[DFA_minimazation.pdf]]
- cannot have two minimal DFAs that recognize the same language
# Algorithm to compute the DFA
## Computing reachable states for the DFA
- all states has to be reachable
	- get rid of all unreachable states

first reachable state is `q0`
$\sum$ is here the alphabet

## Minimization algorithm
- p stands for partition, takes the states in the dfa and split them into disjoint sets. States that ought to be the same will be in the same partition
### Example
starts at page 6

- `F` is the accepting states.
- see in `W` we can just work on the smaller one.
- remember u have to take the one that goes to the state. So you have to look back, not forward.

# Can use this in fx type equivalence checking
- If using structural equivalence, the types will have exactly the same structure in the DFA and states.
- can be also fx via linked lists

## How the algorithm is used
if we have two types which are hard to see if they are the same via structual equivalence, we can run the minimization algorithm on both, and see if we get the same `unique` DFA


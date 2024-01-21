# Finite Automota, regular expressions and closed under certain operations
## Take an extra look at
- reducing an NFA to a regular expression
- reducing a regular expression to NFA
- reducing NFA to DFA
## DFA and NFA
- The complement of a language is just the accepting DFA for the language, and then swapping the accept states. That is $F=Q \backslash F$.
- The intersection between two languages is following states in both DFAs and accepting when both of the DFAs accept.
- NFAs making union of two languages is easy, same with intersection, and star.
## Defining regular expressions
some operators have higher precedence than others

union has the weakest precedence
concatenation is stronger
star is the strongest
### Definion
![[Pasted image 20230911123758.png]]
Means that we are allowed to use syntax in regular expressions
### Shorthands
allowed to write $\sum$ _and then some syntax_ for indicating a regular language, which is just the language
$R^+$  is $R\ concat\ R^*$
$R^k$ is $R\ concat\ R\ concat\ R\dots$
can also omit the concat

R vs L(R) is
R=regular expression
L(R)=the actual language of R

### Special cases
$R\ concat\ ø=ø$

in the arithmetic 
* ø acts like a 0
* union acts like a +
* epsilon acts like a 1

### Goal, prove this theorem
![[Pasted image 20230911124903.png]]

## NFA basics
- Remember that we dont have to define paths for all letters from each state in NFAs
	- As the walkthrough of the NFA can just stop the branch if it finds itself in a state where it cannot get further 
### Making NFAs from regular expressions
pretty easy when you think about it

![[Pasted image 20230918133959.png]]
b.
![[1-19b.excalidraw]]
![[Pasted image 20230919110233.png]]

## Making a DFA into a regular expression
- Remember to add epsilon transitions from all accept states to the new accept state. Else it just `Ø`.
- Just a matter of thinking about how we can get to the other states still, and when we have this removed, how can we get to the other states
### In class
#### Prove we can make a regular expression from a DFA
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

##### Making of the generalised NFA
**look in the book from page 69**
start by making a new accept state, remove the other accept states and do _epsilon_ to the new accept state from the other accept states

from the ones which does not accept we make a transition to the new accept state, writing Ø as the regular expression to the accept state. This will never be accepted anyways

...

###### Examples
![[Pasted image 20230911134758.png]]
1. The DFA
2. adding a transition from all of the states to the others and also adding the start state and a new end state
3. remove state 2, concatenate it with state 1
4. remove state 1 and concatenate it with start state
### Good exercise showing it all

![[Pasted image 20230918135652.png]]
make a new start state and accept state, all the previous accept states gets an empty string transition to the new accept state
and need to make all possible arrows to all states. Can use the empty set.

Sequentially remove the states one by one by `ripping` them out
![[NFA_to_regex.png]]




## Good exercise for proving that some language is closed under the operation
![[Pasted image 20230913130609.png]]
Have two boxes in which we have removed the accept states in the first, and when we meet the symbol we want to skip, we have epsilon to the box which has accept states. This way we **have** to jump if we want to accept the string.
![[Pasted image 20230915122431.png]]

In the formal proof we have
![[Pasted image 20230915124033.png]]
So what is stated in the transition function is that, when we are in the state `(q,b)` and we read in `c` then we should use the transition function on the input. I.e $\delta_{A} (q,c)$ and then keep being in the state `b`. Else we change the `b` to a `1`.

`states`: Q x {0,1} indicating whether we are in the first box or the accepting box.
`transition function`: 
1. When the read symbol is not epsilon we just take the transition function and we stay in the same state. 
2. When the symbol is epsilon we have a state for each of the ways of taking the path for `c` and




## Reducing NFA to a DFA

![[Pasted image 20230918122418.png]]
a. NFA which for each machine allows for going to the machines on the empty strings and allows to go back as we can repeat as many times we want

Remember that the empty set is part of every set
**We dont need to take into consideration all of the possibilites as each of the languages are described with an NFA, meaning we dont need to know what fx state 2 does on a 1 as it does not have to be deterministic**
Just make them go all the back to the first state, as this has an epsilon transition.
![[NFA_union.excalidraw]]

b.
`all about first seeing which states we can go to on an epsilon transition. Then we for this state look at each of the states that we can get to for` $\forall x \in Z$ `and draw the DFA transition`
Start of by calculating how many states you can reach from the start state with epsilon transisitions
{1,2,3,6,10}
Next we need to check what each of the states does on a {0,1, $\epsilon$}

When we have converged we add accept states to all of the states that were accept states
Remember to follow the epsilon and add them to each state
See that `5, 9, 13` are redundant accept state since state `2` accepts
![[Pasted image 20230919104827.png]]
![[NFA_1.17b]]

# 2 CLI & data formats
![[Pasted image 20240119144557.png]]
## Tabular Data
- There are likely some rules which are made for these, to make it easier to work with
[[04.pdf#page=10]]
## CLI
### GREP
- careful for character encoding [[04.pdf#page=page=21]]
- examples of special operators in GREP for `NOT` [[04.pdf#page=34]]
### Other tools
[[05.pdf]] has examples
- uniq
	- Used after sorting as it is inefficient
- tr
	- translates characters into another character. Is not line oriented
	- can also delete specific characters
- cut
	- cut out some columns
- paste
	- Merge lines of files, i.e using 2 or more files
- join
	- join lines on common field in 2 files
	- Like natural join in databases
- head/tail
	- output first/last lines in file
#### Chatten
You're absolutely right. Providing sample text and expected output makes these examples much clearer and more useful. Let's improve the examples with sample input and expected output for each command:

1. **sed (Stream Editor)**:
   - **Task**: Fix a spelling error.
   - **Sample Input**: "This is an iether example."
   - **Command**: `sed -E 's/iether/either/g'`
   - **Expected Output**: "This is an either example."

2. **awk (Pattern Scanning and Processing Language)**:
   - **Task**: Print the line number and the product of the second and third fields.
   - **Sample Input**: 
     ```
     a 2 3
     b 4 5
     ```
   - **Command**: `awk '{ print NR, $2 * $3 }'`
   - **Expected Output**: 
     ```
     1 6
     2 20
     ```

3. **sort and uniq**:
   - **Task**: Sort numerically and remove duplicates ignoring the first field.
   - **Sample Input**: 
     ```
     1 4
     2 3
     3 4
     ```
   - **Command**: `sort -n | uniq -f1`
   - **Expected Output**: 
     ```
     1 4
     2 3
     ```

4. **tr (Translate Characters)**:
   - **Task**: Change 'F' to 'f' and delete digits.
   - **Sample Input**: "Forty 40"
   - **Command**: `echo "Forty 40" | tr 'F' 'f' | tr -d '0-9'`
   - **Expected Output**: "forty "

5. **join (Join Lines of Two Files on a Common Field)**:
   - **Task**: Join lines on a common field.
   - **Sample Input**:
     - File1: 
       ```
       1 A
       2 B
       ```
     - File2: 
       ```
       1 X
       2 Y
       ```
   - **Command**: `join file1 file2`
   - **Expected Output**: 
     ```
     1 A X
     2 B Y
     ```

6. **cut and paste**:
   - **Task**: Change input/output delimiters and keep columns 2 and 3.
   - **Sample Input**: "x:41:one y:42:two"
   - **Command**: `echo "x:41:one y:42:two" | cut -d ':' --output-delimiter=' ' -f2,3`
   - **Expected Output**: "41 one 42 two"

These revised examples with sample input and expected output should give a clearer understanding of how each command-line tool functions and can be applied in real-world scenarios.

7. **paste**
```
41
42

forty - one
forty - two

paste -d ’ ’ myfile1 myfile2
41 forty - one
42 forty - two
```
### SED you didnt remember them all
[[05.pdf#page=13]]
### AWK (dont bother)

![[Pasted image 20230910070747.png]]
[[DFA.excalidraw]]
# I
![[Pasted image 20230912110453.png]]
![[Pasted image 20230912110439.png]]

![[Pasted image 20230910104621.png]]
a. since we accept exactly this language, we must, when swapping the accept state accept everything that is not that language. Since we have a finite automata, it will still be a regular language. 



b. .
![[NFA_Complement.excalidraw]]
If we take the complement we still recognise 0, so it does not necesarrily produce the complement of the languange

As an NFA can always be made to a DFA, it is still closed under this operation

![[Pasted image 20230910105014.png]]
Just means that we go from one letter in a to the next in b, then to the next in a and then to the next in b, and so on ...

![[Pasted image 20230912114336.png]]
C is the token, i.e which machine we are to go to next.

![[Pasted image 20230910105721.png]]



![[Pasted image 20230913112159.png]]
![[Pasted image 20230913112214.png]]
even number of as's
[[DFA_even_a.excalidraw]], **This is a horrible solution, as we can end up with just 2 states, basicly removing 2\*8 states**
[[1or2Bs.excalidraw]]

The approach is that we follow each transition from the two DFAs, we start til `q00` meaning we are in state 0 in the first DFA and 0 in the 2nd. If we get an `a` then we will see which state we are in the 1st DFA and the 2nd. If the 1st will lead to state `1` and the 2nd in `3` then we have the state `q13`. 

We only accept when both of the machines are in an accept state. 

answer
[[IntersectionDFA.excalidraw]]

![[Pasted image 20230913112228.png]]
![[Pasted image 20230913112237.png]]
The language contains epsilon, and all strings which starts with any amount of a's and then any amount of b's. We cannot accept any a's after taking any b's

the DFA:
![[DFAab.excalidraw]]
The complement would then be the empty set, meaning not accept state.

![[Pasted image 20230913130349.png]]
easy: 
![[Pasted image 20230913130440.png]]

![[Pasted image 20230913130456.png]]
easy: ![[Pasted image 20230913130521.png]]


![[Pasted image 20230913130556.png]]
The language contains any combination of a string in A with a string in B. Since the empty string is also in this, as we use star, we can start in B as well. But we cannot just jump around in the strings in the two language, we have to follow them sequentially.

![[Pasted image 20230915121508.png]]

The states will be the product of the two states
the transition function, we can just choose if we want to use the one in A or in B. If we take the one in A we move forward in A else we move forward in B.

The accept states are gonna be the product of the two accept states, as both has to accept, i.e we have to be done with both strings.
![[Pasted image 20230915121634.png]]
In the transition function we can see that either we continue in A or in B, and we still keep track of the state in the other language

![[Pasted image 20230913130609.png]]
Have two boxes in which we have removed the accept states in the first, and when we meet the symbol we want to skip, we have epsilon to the box which has accept states. This way we **have** to jump if we want to accept the string.
![[Pasted image 20230915122431.png]]

In the formal proof we have
![[Pasted image 20230915124033.png]]
`states`: Q x {0,1} indicating whether we are in the first box or the accepting box.
`transition function`: 
1. When the read symbol is not epsilon we just take the transition function and we stay in the same state. 
2. When the symbol is epsilon we have a state for each of the ways of taking the path for `c` and

![[Pasted image 20230918122418.png]]
a. NFA which for each machine allows for going to the machines on the empty strings and allows to go back as we can repeat as many times we want
![[NFA_union.excalidraw]]

b.

![[Pasted image 20230918124408.png]]
![[Pasted image 20230918124434.png]]
a. \^10
b. (0|1)\*111\[01\]*
c. \[01\]\*0101\[01\]\*
d. \[01\]{2}\0\[01\]\*
e. 0(\[01\]{2})\*|1
f.\[01\]\*(^(110))\[01\]\*
g. (^(\[01\]{6,}))
h. 


![[Pasted image 20230918133959.png]]
b.
![[1-19b.excalidraw]]

![[Pasted image 20230918135351.png]]
h.
- accept
	- a
	- ba
- decline
	- ø
	- $\epsilon$

![[Pasted image 20230918135652.png]]
\[ab\]a\*(ulige antal b | lige antal b med a*, når møder b igen skal bruge ulige)\*a

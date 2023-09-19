# counting rules
## Product rule
![[Pasted image 20230901093129.png]]
![[Pasted image 20230901093143.png]]

## Sum rule
![[Pasted image 20230901093219.png]]
![[Pasted image 20230901093228.png]]

## Subtraction rule
![[Pasted image 20230901103037.png]]

## Division rule
![[Pasted image 20230901110151.png]]
![[Pasted image 20230901110157.png]]

## Tree diagrams
![[Pasted image 20230901110555.png]]


# Pigeon hole principle
In these problems it all comes down to identifying what are the "pigeons" and what are the "pigeon holes"
![[Pasted image 20230903152857.png]]

Can prove that lossless compression is not possible. Fx here we have $2^n$ inputs and $2^m$ outputs, there are a lot more inputs than outputs, meaning that two inputs must match a given output, and therefore the output cannot cover all of the $2^n$ inputs.
![[Pasted image 20230907083937.png]]

![[Pasted image 20230907085335.png]]


## Covered examples
**Ramseys theorem**

# Permutations & combinations

## Permutations
Ordered set of a given set. Can also be a r-permutation meaning that we are interresed in a paring of the set but only with `r` of the members
Has mostly to do with `!` i.e **factorial**
## Combinations
Unordered set of a given set
![[Pasted image 20230907094046.png]]

![[Pasted image 20230907094729.png]]
The reason this is true is because if we look at the formula, when doing the computation, only the placement of the two factorials in the denominator changes,

example: `C(7,3) = C(7,4)`
`C(7,3)=7/(3!*4!)`
`C(7,4)=7/(4!*3!)`
### Binomial coefficients
https://www.youtube.com/watch?v=Pcgvv6T_bD8
It follows the coeefficients of the calculations of $(x+y)^n$ as seen in the video
It is based on how many ways there are to choose the specific combination, fx choosing $n=4$ there are 6 ways to choose the combination $x^2y^2$

![[Pasted image 20230908114847.png]]

![[Pasted image 20230907111031.png]]


### Vandermonde
![[Pasted image 20230907112542.png]]
Think about it as we want exactly r, and if we chose `k` from `n` then we need only chose `r-k` in m. We iterate over the combinations where we fx choose more from `m` than `n`

## Generalized Permutations and combinations
### permutations with repetitions
https://www.youtube.com/watch?v=1Uy2E2ncazg
When you have repetitions you can just divide by the number of ways to arrange the duplicates, as you want to get rid of all the arrangements you cannot tell apart. I.e when we fx have 3L's, we have to divide by the number of ways to arrange these L's as we cannot tell them apart.Because these are the number of ways to arrange them when they are together. Meaning, we know there are 3 possible Ls to the first L and 2 for the next and 1 for the next, we remove these permutations where the Ls are in the same place in the permutation, since we do not know which is which. fx we remove 1 of these `KLELLY, KLELLY` since we dont know which Ls are which
![[Pasted image 20230908173440.png]]

### Combinations with repetition
https://www.youtube.com/watch?v=ZcSSI6VY1kM
![[Pasted image 20230910120729.png]]
What we are doing is that when we take an item into the list, we put it back in. Meaning that we will actually, in the case where we choose the same object `r`-times, we end up with having `n+r-1` objects to choose from instead. `r-1` since the first time we take it, it is already contained inside of `n`.

In the following example this means that we have `n=3` since we can chose from x1, x2, x3. We can then choose up to 7 objects, i.e we at max can choose from `3+6=n+r-1`. This is because we have 3 objects, and if we fx choose to use x1 7 times, we will have 7x `x1` and `x2,x3` are unchosen but they are still possible to be selected in another pick.
![[Pasted image 20230910143805.png]]

# Objects into boxes
Different ways to prove permutations with repetitions & comibinations with repetition
![[Pasted image 20230912124110.png]]


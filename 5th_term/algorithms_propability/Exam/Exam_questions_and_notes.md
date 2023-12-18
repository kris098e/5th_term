[[exspmjan24.pdf]]
# remember
you can choose exercises from the assignments or from class.

# 1. Basic counting problems (pigeon hole principle, generalized permutations and combinations etc)
- the different counting rules
- Pigeon hole principle
	- could show the thing with $n^2+1$ distinct element then increasing or decreasing of size $n+1$?
	- look at the first exercise with proving something with the pigeon hole principle

- **ramseys theorem** the example on page 425.

- group of 6 people, each pair of individuals contains 2 enemies or 2 friends, there are now 3 mutual friends or 3 mutual enemies, when we pick a person out. This follows from the generalized pigeon hole principle $\lceil \frac{n}{\groups}\rceil=\lceil \frac{5}{2}\rceil=3$. Meaning that there must be at least 4 friends or 4 enemies.

- permutations, combinations
	- with repetition

> Permutation with repetition:
> quite self explanatory. It is just permutation formula where we want to remove each permutation of the repeated character.

> Combinations with repetition
> stars and bars ![[Pasted image 20231215083843.png]]
- pascals triangle
	- ![[Pasted image 20230907111031.png]]

- Vandermonde
	- ![[Pasted image 20230907112542.png]]

- $${2n\choose{2}} = {n \choose 2}+n^2$$
- Find the exercise with how many permutations of people we can seat around a table.
# 2. Inclusion-exclusion with applications(derivation of the general formula, number of onto-functions, the hatcheck problem)
- start by drawing the Venn-diagram, and showing the formula
![[Pasted image 20230928061536.png]]
## Generalized formula
![[Pasted image 20231216064334.png]]
The binomial theorem states that

$$(x+y)^n=\sum_{k=0}^{n}{n\choose k}x^{n-k}y^k$$

In Corollary 2, $1^{n-k}=1$ so it does not matter that we multiply the other part with this. 
![[Pasted image 20230928110002.png]]
### Notes to the proof
- See first that, in the `2nd step`, we used the corollary, which let us rewrite the expression so that it will be equal to `0`. 
- Next we isolate the `C(r,0)` which ends up concluding that the `1st` equation is `=1`.
- Do keep an eye out for the $(-1)^{r}$ and $(-1)^{r+1}$, as these are used differently in the different equations. 
This concludes that each element `a` is counted once, which means that all elements are counted once by the equation.
## number of onto functions
![[Pasted image 20230928164329.png]]
The number of functions in this example is $3^6$ since, for each of the elements being mapped via the function, i.e the x's in `f(x)`, can each go to 3 options. Meaning we have $3^6$ functions.
- S1: we have $2^6$ options, and we can choose the element which is not mapped to in  $3\choose 1$ ways.
- S2: we have $1^6$ options, and we can choose the elements to exclude in $3\choose 2$ ways.

Fluently you can quickly prove the generalisation of this, arguing that there is a pattern that how many options in the codomain we map to is falling linearly with how many elements in the codomain we exclude.
![[Pasted image 20230928165006.png]]
## Hatcheck
![[Pasted image 20230928174050.png]]
- This is similar to the number of onto functions, but just now it is factorial instead of power. 
- The intuition is that, we look at the entire space $10!$, and remove the once that does not meet the predicate. So we remove ${10 \choose 1}9!$ since we here select 1 of the coats to be the correct, and then we do not care about the rest. We have not subtracted too many, so we add this. We then end up with
- $\sum_{k=0}^{n} (-1)^{k}{n \choose k}(n-k)! \approx \frac{n!}{e}$ as the number of scenarios where no people get the correct coat.

# 3. Discrete probability, random variables and bounds (expected value, variance, Bayes formula, Markov's inequality, Chebyshev's inequality and Chernoff bounds)
## Comment
Maybe do more examples instead of doing the basics
## Introduction
- start by drawing a diagram for the probabilities
![[probability.excalidraw]]
$$P(E)=\frac{|E|}{|S|}$$
$$P(E|F)=\frac{P(E\cap F)}{P(F)}$$
If E and F are independent
$$P(E\cap F)=P(E)\cdot P(F)$$
since both events has to happen, and there are no common event in their space.
$$P(!E)=1-P(E)$$
## Union bound
point to the Venn-diagram, have a look at fx event F, E.  less elements in the union than when we overcount. However looking at F, D, then the union bound will be equal to the right side of the bound.
$$P(E_{1}\cup E_{2}\cup \dots E_{i})\leq \sum_{i=0}^{n}P(E_{i})$$
## Random variables
Mapping of event to number in the reals.
$$E(X)=\sum_{s\in S} p(s)X(s)$$
Slow to do it one by one, cluster the values which are equal.
$$E(X)=\sum_{r\in X(S)}P(X=r)r$$
deviation of X at s
$$X(s)-E(X)$$
Linearity of expectation. Can prove it works for `n+1` via induction.
![[Pasted image 20231216093753.png]]
Bernolli trials, probability of `k` out of `n` is success is
$$C(n,k)p^{k}q^{n-k}$$
as we can choose these `k` successes in $C(n,k)$ ways, and the probability of success is `p`, and the rest should be failures. Using linearity of expectation we can show that this is simply
$$E(X)=np$$
Where $X_{j}(s)=1$ iff the `jth` try is a success, else 0. Therefore
$$E(X_{j})=1 \cdot p(X_{j}=1) + 0\cdot p(X_{j}=0)=1\cdot p\cdot+0=p$$
This means that if we take the sum of all random indicator variables we get
$$E(\sum_{i=0}^{n} X_{i})=\sum_{i=0}^{n}E(X_{i})=np$$
**could quickly run over hatcheck**
## Variance
Describes how much the random variable deviates from its expected value.
$$V(X)=\sum_{s \in S}(X(s)-E(X))^2p(s)$$
Expand
$$V(X)=\sum_{s\in S}(X(s)^2-2X(s)E(X)+E(X)^2)p(s)$$
multiply $p(s)$ into the parentheses
$$V(X)=\sum_{s \in S}X(s)^2p(s)-2X(s)E(X)p(s)+E(X)^{2}p(s)$$
split the sum
$$V(X)=\sum_{s \in S} X(s)^{2}p(s)-2E(X)\sum_{s \in S}X(s)p(s)+E(X)^2\sum_{s \in S}p(s)$$
now as $E(X)=\sum_{s \in S}X(s)p(s)$ and $\sum_{s \in S}p(s)=1$ 
$$V(X)=E(X^2)-2E(X)E(X)+E(X)^2=E(X^2)-2E(X)^2+E(X)^2$$
$$V(X)=E(X^2)-E(X)^2$$
If X is a random indicator variable, then 
$$V(X)=p-p^2=p(1-p)$$
Note also that
$$V(X)=E((X-E(X))^2)=\sum_{s \in S}p(s)(X(s)-E(X))^2$$
## Geometric distributions
When we may try infinitely many times before succeding. Fx throwing a fair coin until we get tails 
$E(X)=\frac{1}{p}$
Where $p$ is the chance of success.
## Markov
![[Pasted image 20230929080613.png]]
![[Pasted image 20231009085242.png]]
$$p(X(s)\geq a)\leq \frac{E(X)}{a}$$
proof
$$A=\{s|X(s)\geq a\}$$
$$!A=S\A$$
$$E(X)=\sum_{s \in S} p(s)X(s)$$
$$=\sum_{s\in A}p(s)X(s)+\sum_{s\in !A}p(s)X(s)$$
$$\geq \sum_{s\in A}p(s)a+0$$
$$=a\left( \sum_{s \in A}p(s) \right)=a \cdotp(X(s)\geq a)$$
ending notes:
$$E(x) \geq a \cdot p(X(s)\geq a)\implies p(X(s) \geq a)\leq \frac{E(X)}{a}$$
## Chebyshev
$$p(|X(s)-E(X)|\geq r)\leq \frac{V(X)}{r^2}$$
proof:

$$V(X)=\sum_{s \in S}p(s)(X(s)-E(X))^2$$
now let
$$A=\{s\mid \left|X(s)-E(X)\right|\geq r \}$$
$$V(X)=\sum_{s \in A} p(s)(X(S)-E(X))^2+\sum_{s\in !A}p(s)(X(S)-E(X))^2$$
The 2nd term will all be nonnegative, adding value to the variance. the 1st term
$$(X(S)-E(X))^{2} \geq r^2$$
due to the condition of $A$. Therefore
$$V(X)\geq\sum_{s \in A} p(s)(X(S)-E(X))^2$$
$$\geq r^2\sum_{s\in A}p(s)$$
$$=r^2p(A)$$
$$=r^2p(\mid X(s)-E(X)\mid \geq r)$$
putting it together:
$$\frac{V(X)}{r^{2}}\geq p(\mid X(s)-E(X)\mid \geq r)$$
## Notes to take with into the exam
- basics (Venn-diagram)
- Linearity of expectation
- Bernolli trials (regular and with random indicator variables)
- Variance
- Union bound
- Chebyshev: $p(|X(s)-E(X)|\geq r)\leq \frac{V(X)}{r^2}$
- Markov: $p(X(s)\geq a)\leq \frac{E(X)}{a}$

# 4. Randomized algorithms (Quicksort, median finding and selection, min-cut in graphs, generating a random permutation, majority element, and more!!!)
## Median finding
![[Pasted image 20231031062454.png]]
Select(S,k) = Select(the set, the size of half the set)
![[Pasted image 20231031062421.png]]
![[Pasted image 20231031063442.png]]
- Want to remove at least some constant $\times$ n, in each iteration of `select(S,k)`.
- The reason why the last step shows it is $\leq$ is because it starts from $i=0$
- **IMPORTANT** that you remember the rule for deriving
	- $\sum_{i=0}^{\infty}(1-\epsilon)^i=\frac{1}{1-(1-\epsilon)}$
	- this is because $\sum_{i=0}^{\infty}ar^i=\frac{a}{1-r}$
	- where in our case $r=(1-\epsilon)$
![[Pasted image 20231031065338.png]]
Probability of picking something in the middel is $\frac{1}{2}$. We then work on $\frac{3}{4}n$ the next time. 
![[Pasted image 20231031065940.png]]
We now go with phases, so how big the set will be in the next phase. The set we are working on is $\mid S'\mid$, which if we were unlucky we only removed $\frac{3}{4}$ of the `n` elements in the last phase. This happens when the splitter is picked as the last or first element of `central`.
![[Pasted image 20231031070301.png]]
as it follows geometric distrubition, expected number of times before we get a central splitter is
$$\frac{1}{p}=\frac{1}{\frac{1}{2}}=2$$
How much time do we spend in each phase?
![[Pasted image 20231031070607.png]]
- How much work we do, at most what is stated since we may be lucky to not always choose the worst splitter (first or last element) in central. 
`remember` each random variable is the number of steps done by the algorithm. We can now work out the expected work in each step.
![[Pasted image 20231031071634.png]]
- Note: we do not put upper bound, since we dont know how many phases we will do.
- We use $\leq$ since we may not do $2$ steps in each phase, `i.e:` because the expected value of $E(X_{j})$ is specified as an upper bound.
## Quicksort
![[Pasted image 20231031072355.png]]
We now look how many subproblems there are, which is based on the splitter: i.e running quicksort on $S^{-}$ and $S^+$.
![[Pasted image 20231217120635.png]]
### Prove how many problems we end up with.
**Remember** that the set `S` has type `j` if the following holds
$$n\cdot \left( \frac{3}{4} \right)^{j+1}<\mid S'\mid \leq n\cdot \left( \frac{3}{4} \right)^j$$
I.e for each of the rounds, how much work is done in each recursive call, and how many recursive calls are there.
![[Pasted image 20231031072940.png]]
It says they are all `disjoint`. This means that when we split $S$ we will create a subproblems of type $j$  The main point is that they are `disjoint`.
![[Pasted image 20231031073116.png]]
- The total number of subproblems of type `j` is exactly what is stated. Think about if we have 5 elements and we split in the middel then we have 2 subproblems.
- so there are at most $\frac{n}{n\cdot \left( \frac{3}{4} \right)^{j+1}}$ subproblems of type `j`
	- for each of these subproblems, we do at most $n\cdot \left( \frac{3}{4} \right)^j$ work, as this is the largest split we can make, if you choose an unlucky splitter. These cancel out, meaning the expected amount of work on each subproblem is $O(n)$
![[Pasted image 20231031073245.png]]
- How many times can we divide n by $\frac{4}{3}$ before we go down to 1? That is, the largest possible set side after $\frac{n}{\frac{4}{3}}=\frac{3}{4}n$. 
- There are at most $\log_{\frac{4}{3}}n$ different types, `j`, and as we do $O(n)$ on each subproblem, we will do a total amount of work $O(n \log n)$
## Notes to take with into the exam
- The split picture
- select(S, k)
- randselect
	- central splitter
	- prove linear runtime
	- phases
	- probability of good splitter, expected #times before finding a good splitter
	- sum of all random variables
- RandQsort
	- Splits are disjoint (back to split picture)
	- how many subproblems are at most created of type `j`
	- how much work for each
	- total types of `j`
# 5. Probabilistic analysis (using (indicator) random variables, coupon collector, expected running time of quicksort and selection, randomized approximation for max k-SAT)
## Quicksort and selection
Look at the problem above.
# 6. Examples of applications of indicator random variables (find some yourselves in the pensum, there are many!)
Universal hashing, perfect hashing

# 7. Universal hashing (universal hash functions, perfect hashing (also called 2-level hashing), count-min sketch)
Look at Overleaf
https://www.overleaf.com/project/653b925960e85f96d2a551aa


# 8. String matching (naive algorithm, The Rabin-Karp algorithm, Finite automaton based string matching).



# 9. Maximum flows (Definitions, Ford Fulkerson algorithm, Max-Flow- Min-Cut theorem, Edmonds-Karp Algorithm, bipartite matching, integrality theorem)

  

# 10. The min-cut problem (randomized algorithm, solution via flows, solution via max-back orderings)


[[exspmjan24.pdf]]
# remember
you can choose exercises from the assignments or from class.
## Look at again
- waiting to find a good assignment with K-sat
# Try again
- Flows went like shit
- String matching is still shit
# 1. Basic counting problems (pigeon hole principle, generalized permutations and combinations etc)
- the different counting rules
- Pigeon hole principle
	- could show the thing with $n^2+1$ distinct element then increasing or decreasing of size $n+1$?
we do this by proof by contradiction.
Vi opstiller elementerne i en række
$$x_{1},x_{2}, \dots, x_{i}, \dots x_{j}, \dots x_{n+1}$$
- Lad os først tilknytte en 2-tuple med hvert element, $(I_{i},D_{i})$ som er den længste stigende sekvens op til og med element $x_{i}$ og den længste decreasing sekvens op til og med.
- Antag nu som contradiction at den største værdi i en af de her værdier er $n$. For tuplen er der $n \cdot n=n^{2}$ mulige tupler, pr. produkt-reglen.
- ved brug af pigeon hole principle $\lceil \frac{k}{N}\rceil$, hvor `k=antal entries`, `N=antal muligheder for hvor entries kan være`.
	- her har vi $k=n^{2}+1$
	- $N=n\cdot n=n^{2}$
	- Dermed $\lceil \frac{n^{2}+1}{n^{2}}\rceil = 2$, hvilket vil sige at to har den samme tuple.
- dette kan ikke være muligt da hvis vi kigger på $x_{i},x_{j}$ hvor $j$ står længere henne i rækken så har vi to scenarier, da disse ikke kan være lig hinanden
	- $x_{i}<x_{j}\implies$ $I_{j} \geq I_{i}+1$
	- $x_{i}> x_{j}\implies$ $D_{j} \geq D_{i}+1$
- dermed er der ikke to tupler der er ens, hvilket medfører at der må være en en tuple som har $>n$ på en af sin tuples værdier.

- **ramseys theorem** the example on page 425.
- group of 6 people, each pair of individuals contains 2 enemies or 2 friends, there are now 3 mutual friends or 3 mutual enemies, when we pick a person out. This follows from the generalized pigeon hole principle $\lceil \frac{n}{\groups}\rceil=\lceil \frac{5}{2}\rceil=3$. Meaning that there must be at least 4 friends or 4 enemies.
	- simply stated. We pick a person out. Now he is either friends with or enemies with the other person `i` for all persons $i \in \{1,2,3,4,5\}$, and these are put into boxes. Then one box must have $\lceil \frac{5}{2} \rceil =3$ inside. Therefore $3+the\ guy=3+1=4$ friends or enemies.

- permutations, combinations
	- with repetition

> Permutation with repetition:
> quite self explanatory. It is just permutation formula where we want to remove each permutation of the repeated character.

> Combinations with repetition
> stars and bars ![[Pasted image 20231215083843.png]]
> **Its about placing 7 objects, but adding (3-1) bars such that we can distinct the different kinds of objects from each other**
> In this example we have `n=3`, which means we will only `2` separators, bars, to distinguish between these. We have to choose `7` objects, but to distinguish between what is what in this we will need `2` separators. This means we effectively have to pick `9 objects`.
- pascals triangle
	- ![[Pasted image 20230907111031.png]]
![[Pasted image 20231215082721.png]]
- Vandermonde
	- ![[Pasted image 20230907112542.png]]

- $${2n\choose{2}} = {n \choose 2}+n^2$$
- Find the exercise with how many permutations of people we can seat around a table.

## Notes to proofs
- remember pigeon hole principle is a contradiction proof, remember to use example, `n=10`
- Counting with repetition, write up the `x1+x2+x3=7`, then `xxxxxxx=7`, but we also want to distinguish these from each other. Therefore we want `n-1` bars.
- ${n\choose r}=\frac{n!}{r!\cdot (n-r)!}$
	- Since $n-r$ is the number of elements we cannot permute further on from the original set
## Notes for the exam
- Pigeon hole principle ($n^{2}+1$)
	- proof with the example
	- Cases for person $j < k$
- Counting with repetition
	- stars and bars
- Permutations with repetitions
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
The reason why for sum in 1 set is $C(r,1)$ is because we have `r-sets the element is in`, now how many ways can we choose the two distinct sets, fx choose $r_1,r_2$ with each other and $r_{1,}r_3$, this we can do in $C(r,2)$ ways. ...
- First we state what the summation will look like
- The 2nd equation is not dependant on the first. We simply state that using the corollary, this is equation is `= 0`
- Since the 2nd equation is using a `-` where it should be `+` in the 1st equation, then we can fix this by moving these terms to the right-hand side of the equation, and we get exactly the first equation on the right-hand side.
	- Now we can see that this is equal to $C(r,0)=1$
	
remember it is $\dots (-1)^{r+1}$ but this can be seen by the fact that the first first choose $C(r,1)$ is positive, i.e $r=1$
## number of onto functions
![[Pasted image 20230928164329.png]]
The number of functions in this example is $3^6$ since, for each of the elements being mapped via the function, i.e the x's in `f(x)`, can each go to 3 options. Meaning we have $3^6$ functions.
- S1: we have $2^6$ options, and we can choose the element which is not mapped to in  $3\choose 1$ ways.
- S2: we have $1^6$ options, and we can choose the elements to exclude in $3\choose 2$ ways.

Fluently you can quickly prove the generalisation of this, arguing that there is a pattern that how many options in the codomain we map to is falling linearly with how many elements in the codomain we exclude.

**Notice that there is a `mistake`. it is supposed to be** $$\sum\limits_{k=0}^{n} (-1)^{k} { n \choose k} (n-k)^m$$
![[Pasted image 20230928165006.png]]
## Hatcheck
![[Pasted image 20230928174050.png]]
- This is similar to the number of onto functions, but just now it is factorial instead of power. 
- The intuition is that, we look at the entire space $10!$, and remove the once that does not meet the predicate. So we remove ${10 \choose 1}9!$ since we here select 1 of the coats to be the correct, and then we do not care about the rest. We have not subtracted too many, so we add this. We then end up with
- $\sum_{k=0}^{n} (-1)^{k}{n \choose k}(n-k)! \approx \frac{n!}{e}$ as the number of scenarios where no people get the correct coat.

## Remember 
- The formula for finding how many elements are in the sets, **remember** to write it is $|A_{1}\cup A_{2}\cup \dots \cup A_{n}|=...$ . I.e remember to say that this is what it calculated
- Remember that we want each elements to be counted only once.
## Exam Notes
- Generalized formula for inclusion-exclusion (venn-diagram)
- Prove each element is counted only once
	- Focus in on specific element `a`
	- Uses binomial theorem $(x+y)^{n}=\sum\limits_{k=0}^{n}{n \choose k}x^{k} y^{n-k}$, 
- Number of onto functions
	- Connect seen pattern with a generalized formula
- Hatcheck derangements
	- Similar with last function, now it is just permutations
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
$$p(|X(S)-E(X)|\geq r)\leq \frac{V(X)}{r^2}$$
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
## Hatcheck with bounds
Probability that more than 10 people get their hat back in the hatcheck problem, bounded by chebyshev:
$$p(|X(S)-E(X)| \geq r) \leq \frac{V(X)}{r^2}$$
$$p(|X(S)-E(X)| \geq 10) \leq \frac{V(X)}{10}$$
we define some random variables, let $X_{i}=1$ iff person `i` get their hat correctly back, else 0.
$$E(X_{i})=\sum\limits_{s \in S} p(s)X_i(s)=\frac{1}{n}1+\left( 1-\frac{1}{n} \right)0=\frac{1}{n}$$
there are `n` people, we have 
$$X=X_{1},X_{2}, \dots, X_{n}$$
so 
$$E(X)=E\left( \sum\limits_{i=1}^{n}X_{i} \right)=\sum\limits_{i=1}^{n}E(X_{i})=n\cdot \frac{1}{n}=1$$
as
$$V(X)=E(X^{2})-E(X)^{2}$$
we can now instantly calculate
$$E(X)^{2}=1^{2}=1$$
We can calculate
$$E(X^{2})=E\left((X_{1},X_{2}, \dots, X_{n})^{2}\right)=E\left( \sum\limits_{i=0}^{n}X_{i}^{2} \right)+E\left(\sum\limits_{1\leq j <k\leq n} X_{j}X_{k}\right)$$
$$=n \frac{1}{n} + n(n-1)\left( \frac{1}{n\cdot n-1} \right)=2$$
since $X_{i}^{2}=\frac{1}{n}$ as $1^{2}=1$
There are $n^2$ options to match the random variables, therefore we have $n(n-1)$ options left after having summed over `n` possibilities. For these, having both success for `j` and `k`, is $\frac{1}{n}$ for `j` and $\frac{1}{n-1}$ for `k`, as it increases the probability for `k` that `j` got his/her hat correctly back.

we can now insert into the formula:
$$p(|X(S)-E(X)| \geq 10) \leq \frac{2-1}{10^2}=\frac{1}{100}$$
## Notes to take with into the exam
- Chebyshevs inequality
- Probability that more than 10 people get their hat back
	- bounded by Chebyshevs inequality
- Markovs inequality
- Prove variance formula
# 4. Randomized algorithms (Quicksort, median finding and selection, min-cut in graphs, generating a random permutation, majority element, and more!!!)
**Use less time on not-randselect / select** just handwave it, showcasing it is $O(n^2)$
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
- Note: we do not put upper bound, since we need to know how many phases we will do.
- We use $\leq$ since we may not do $2$ steps in each phase, `i.e:` because the expected value of $E(X_{j})$ is specified as an upper bound.

$$E(X_{j}) \leq 2cn\left( \frac{3}{4} \right)^j$$
X=sum all random variables
$$E(X)=E\left( \sum_{j} X_{j}\right)$$
$$=\sum_{j}(E(X_{j}))$$
$$\leq 2cn \sum_{j}\left( \frac{3}{4} \right)^j$$
$$\leq 2cn \sum_{j=0}^{\infty}\left( \frac{3}{4} \right)^{j}= 2cn \frac{1}{1-\left( \frac{3}{4} \right)}=8cn$$
constant time.
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
- The total number of subproblems of type `j` is exactly what is stated. Think about if we have 5 elements and we split in the middle then we have 2 subproblems.
- so there are at most $\frac{n}{n\cdot \left( \frac{3}{4} \right)^{j+1}}$ subproblems of type `j`
	- for each of these subproblems, we do at most $n\cdot \left( \frac{3}{4} \right)^j$ work to find the good splitter / median, as this is the largest split we can make, if you choose an unlucky splitter. These cancel out, meaning the expected amount of work on each subproblem is $O(n)$
![[Pasted image 20231031073245.png]]
- How many times can we divide n by $\frac{4}{3}$ before we go down to 1? That is, the largest possible set size after $\frac{n}{\frac{4}{3}}=\frac{3}{4}n$. 
- There are at most $\log_{\frac{4}{3}}n$ different types, `j`, and as we do $O(n)$ on each subproblem, we will do a total amount of work $O(n \log n)$
## RandQSort by Rosen
### Starting notes
- It is all about looking at the chance of comparing two specific elements, and all of the possible ways to do so. As summing up the expectation of each element being compared, will give the total expectated number of elements being compared
- Remember that we look at how the sorted array is looking all the way, to make sure we can analyze if we pick something smaller than both the elements, larger or in-between.
### Proof
We look at the sorted set
$z_{1}<z_{2}<z_{3}<z_{4}<\dots <z_{n}$
Define random variable $Z_{i,j}=1$ iff $z_{i}$ is compared with $z_{j}$. These are `only` compared when these are chosen as the pivot. Look at the set
$$Z[i,j]=\{z_{i}<z_{i+1}< \dots < z_{j}\}$$
obvious to see that in the same round for qsort, `i` and `j` are compared only if these are the pivots. Since if we choose some $z_{x}< z_{i}$ as the pivot, then all these elements ends up in $S^{+}$. same if larger than $z_{j}$, if between $z_{i},z_{j}$ then these are never compared. Since we use random median finding that means the probability of either of these being chosen must be the
$$E(Z_{i,j})=p(Z_{i,j}=1)=\frac{2}{j-i+1}$$
As only choosing $z_{i},z_{j}$ will work, and there are $j-i+1$ elements in the set. Since this is a random indicator variable we can calculate the expected value/running-time of the algorithm
$$E(Z)=E(\sum\limits_{i=1}^{n-1}\sum\limits_{j=i+1}^{n}Z_{i,j})$$
use linearity of expectation
$$=\sum\limits_{i=1}^{n-1}\sum\limits_{j=i+1}^{n}E(Z_{i,j})$$
$$=\sum\limits_{i=1}^{n-1}\sum\limits_{j=i+1}^{n} \frac{2}{j-i+1}$$
make variable shift, let `k=j-i`
$$=\sum\limits_{i=1}^{n-1}\sum\limits_{j=i+1}^{n} \frac{2}{k+1}$$
$$=2\sum\limits_{i=1}^{n-1}\sum\limits_{j=i+1}^{n} \frac{1}{k+1}$$
$$< 2\sum\limits_{i=1}^{n-1}\sum\limits_{j=i+1}^{n} \frac{1}{k}$$
$$< 2\sum\limits_{i=1}^{n-1} H(n)$$
$$<2 nH(n)=2n \cdot ln (n)$$
i.e algorithm is
$$O(n \cdot ln(n))$$

## Notes to take with into the exam
- The split picture
- Select(S, k) / median finding
- Randselect
	- Central splitter
	- Prove linear runtime
	- Phases
	- Probability of good splitter, expected #times before finding a good splitter
	- Expected value of all random variables.
- RandQsort
	- Splits are disjoint (back to split picture)
	- How many subproblems are at most created of type `j`
	- How much work for each, the median finding time
	- Total types of `j`
# 5. Probabilistic analysis (using (indicator) random variables, coupon collector, expected running time of quicksort and selection, randomized approximation for max k-SAT)
## Quicksort and selection
Look at the problem above.
# 6. Examples of applications of indicator random variables (find some yourselves in the pensum, there are many!)
## Hatcheck with bounds
Probability that more than 10 people get their hat back in the hatcheck problem, bounded by chebyshev:
$$p(|X(S)-E(X)| \geq r) \leq \frac{V(X)}{r^2}$$
$$p(|X(S)-E(X)| \geq 10) \leq \frac{V(X)}{10^{2}}$$
we define some random variables, let $X_{i}=1$ iff person `i` get their hat correctly back, else 0.
$$E(X_{i})=\sum\limits_{s \in S} p(s)X_i(s)=\frac{1}{n}1+\left( 1-\frac{1}{n} \right)0=\frac{1}{n}$$
there are `n` people, we have 
$$X=X_{1},X_{2}, \dots, X_{n}$$
so
$$E(X)=E\left( \sum\limits_{i=1}^{n}X_{i} \right)=\sum\limits_{i=1}^{n}E(X_{i})=n\cdot \frac{1}{n}=1$$
as
$$V(X)=E(X^{2})-E(X)^{2}$$
we can now instantly calculate
$$E(X)^{2}=1^{2}=1$$
We can calculate
$$E(X^{2})=E\left((X_{1},X_{2}, \dots, X_{n})^{2}\right)=E\left( \sum\limits_{i=0}^{n}X_{i}^{2} \right)+E\left(\sum\limits_{1\leq j <k\leq n} X_{j}X_{k}\right)$$
$$=n \frac{1}{n} + n(n-1)\left( \frac{1}{n\cdot n-1} \right)=2$$
since $X_{i}^{2}=\frac{1}{n}$ as $1^{2}=1$
There are $n^2$ options to match the random variables, therefore we have $n(n-1)$ options left after having summed over `n` possibilities. For these, having both success for `j` and `k`, is $\frac{1}{n}$ for `j` and $\frac{1}{n-1}$ for `k`, as it increases the probability for `k` that `j` got his/her hat correctly back.

we can now insert into the formula:
$$p(|X(S)-E(X)| \geq 10) \leq \frac{2-1}{10^2}=\frac{1}{100}$$
## K-Sat
- Har clauses med `k` literaler, på formen $C_{i}=(k_{1}\vee k_{2}\vee \dots \vee k_{k})$
- Vi har `m` af de her klausuler seperet med and-operator: $C_{1}\wedge C_{2}\wedge \dots \wedge C_{m}$
- Sandsynligheden for at vi satisfier $C_{i}$ er $p(C_{i})=1-p(!C_{i})=1-\left( \frac{1}{2^{k}} \right)=\frac{2^{k}-1}{2^{k}}$
- laver indicator random variables, $X_{i}$ er 1 hviss klausus $C_{i}$ er satisfied, ellers 0
	- $E(X_{i})=p(X_{i}=1)1+p(X_{i}=0)0=p(X_{i}=1)=p(C_{i})=\frac{2^{k}-1}{2^{k}}$
- Lad $X=\sum\limits_{i=1}^{n}X_{i}\implies E(X)=E\left( \sum\limits_{i=1}^{n}X_{i} \right)=\sum\limits_{i=1}^{n}E(X_{i})=\sum\limits_{i=1}^{n} \frac{2^{k}-1}{2^{k}}=n\frac{2^{k}-1}{2^{k}}$
	- Forventer at satisfy præcis så mange. Vi ved der findes en truth assignment til alle `k` literaler som tilfredstiller mindst så mange, ellers ville `X` forventede værdi være mindre end dette. I.e. `X` vil tage den forventede værdi, ellers ville den forventede værdi være mindre.
- Vil nu vise hvor mange klausuler vi forventer at tilfredstille baseret på `n`
	- lad $I_{i}$ være 1 hvis klausul $C_{i}$ ikke er satisfied, ellers 0
	- $E(I_{i})=p(I_{i}=1)1+p(I_{i})0=\frac{1}{2^{k}}$
	- lad $I=\sum\limits_{i=1}^{n}I_{i} \implies E\left( \sum\limits_{i=1}^{n}I_{i} \right)=\sum\limits_{i=1}^{n}E(I_{i})=n \frac{1}{2^{k}}$
		- Det betyder altså, så længe at $n <2^{k}$ er det forventet antal ikke-tilfredstillet klausuler $< 1$.
## Notes for the exam
- (Chebyshev) Probability that more than 10 people get their hat back
- k-sat
# 7. Universal hashing (universal hash functions, perfect hashing (also called 2-level hashing), count-min sketch)
## Making the family of universal hash functions
![[Pasted image 20240108120426.png]]
- choose a prime, which is $p \geq |U|$ and let $|U| \subseteq \{0,1,2, \dots , p-1\}$. That is, we map the universe to maximally p different elements, that is, we associate the universe elements with p different options
- let the set $a=\{0,1,2,\dots, p-1\}$ and $b=\{1,2,3,\dots, p\}$
	- choose a uniformly random input entry in `a` and `b`, and let your hash function be $h_{a,b}(k)=((ak+b)\mod \ p)\ mod \ m$
## Universal hashing
- Choose a random universal hashfunction independent of the keys.
The probability that two keys hash to the same index should be $\frac{1}{|S|}$, i.e.
$$p(h(k)=h(l))\leq \frac{1}{m}$$

given that
$$h: U \to [m]_{0}$$
i.e it has to use all spots `m`, for all input keys in the universe `U`
- We handle all collisions with chaining
	- what is the length of the linked list at index `i` in the hash table?
say we hash some collection of elements $S$ where $|S| = n$.
- we now wish to hash. a new element `k`
	- if $k \notin S$, then we want $E(n_{h(k)})$ of the linked list at any index to be $\leq \frac{n}{m}=\alpha$
	- if $k \in S$ then we want $E(n_{h(k)})$ at any index to be $\leq \frac{n}{m}+1=\alpha + 1$
define random indicator variable for `k`, $\forall l \in U \ define\ X_{k,l}, \ where \ k \neq l \ is =1$ iff $h(k)=h(l)$ else 0.
now since we have fixed our element `k`. Now we can calculate the expected value of the random variable
$$E(X_{k,l})=p \cdot 1 +(1-p)0=p \implies E(X_{k,l})\leq \frac{1}{m}$$
we can now analyze the length of the linked list at a given index.
$$X=\sum\limits_{l \in S}X_{k,l}$$
$$E(X)=E\left( \sum\limits_{l \in S}X_{k,l} \right)=\sum\limits_{l \in S}E(X_{k,l}) \leq \frac{n}{m}=\alpha$$
now if $k\in S$, then we are guaranteed that we will have an extra element in the index, when we hash the same element again, `and also, since $k\in S$ then we will have 1 random indicator variable less generated, therefore we only have n-1 random indicator variables`, therefore this would be $E(X)=\frac{n-1}{m}+1 \leq \alpha +1$

**In conclusion**
- if $k \notin S$, then we want $E(n_{h(k)})$ of the linked list at any index to be $\leq \frac{n}{m}=\alpha$
- if $k \in S$ then we want $E(n_{h(k)})$ at any index to be $\leq \frac{n}{m}+1=\alpha + 1$

**Therefore** if we make $O(m)$ insert operations, fx $S\in O(m)=10m$, then the `search, insert, delete, ...` operations will be constant time $O(1)$.
## Perfect hashing
The probability that we have any collisions when we use a universal hash function into a table of size $n^2$ where $n=\mid S\mid$ is $\frac{1}{2}$.
Define random indicator variable, $Z_{k,l}=1$ iff $h(k)=h(l)$ else 0. We have ${n \choose 2}$ ways for collision
![[Pasted image 20231218160804.png]]
probability of collision is $\frac{1}{n^2}$.  there are ${ n \choose 2}$ ways to collide. Therefore, the expected number of collisions is: $\frac{{n \choose 2}}{n^{2}}< \frac{1}{2}$. Bound this by Markovs inequality
$$p(Z \geq 1) \leq \frac{E(Z)}{1}=E(Z)<\frac{1}{2}$$
probability of no collision $p(Z=0)=1-p(Z=1)\implies p(Z=0)\geq \frac{1}{2}$.
Expected number of times we run the algorithm $\frac{1}{p}=\frac{1}{\frac{1}{2}}<2$.
But we now still use $n^2$ memory.

Use $n^2$ in the 2nd level of hash table.

let
$$n_{j}=\forall x\in n\mid \{ x \mid h(x)=j\}\mid$$
And use table size of
$$n_{j}^2$$
for storage in this 2nd hash table. This means that $n_{j}$ is the number of elements hashed to the j'th index. We will then need to store the hash function for the table, and this much storage for each. Let us look at the expected value of storage in all the 2nd hash tables
$$E\left( \sum_{i=0}^{n-1} n_{j}^{2}\right)$$
Note that it does make sense to take the expected value of this, as $n_{j}$ depends on the random hash function.
we use that
$n^{2}=n+2 {n\choose 2}=n+n(n-1)$
$$\begin{align}
E\left( \sum_{i=0}^{n-1} n_{i}^2 \right)=E\left(\sum_{i=0}^{n-1}n_{i}+2 {n_{i}\choose 2}\right) \\
= E(\sum_{i=0}^{n-1}n_{i})+E\left(\sum_{i=0}^{n-1}2 {n_{i}\choose 2}\right) \\
=E(n)+2E\left(\sum_{i=0}^{n-1} {n_{i} \choose 2}\right) \\
=n+2E(r)
\end{align}
$$
the `n` comes from the fact we sum up all that is mapped to the `i'th` position. Iterating over all indexes will end up giving all of the elements, which is just `n`.
$\sum_{i=0}^{n-1} {n_{i} \choose 2}$ is simply the total number of collisions. I.e we sum up all the collisions.
$$E(r)={n\choose 2}\cdot \frac{1}{n} = \frac{n-1}{2}$$
$$E\left(\sum_{i=0}^{n-1} n_{i}^{2}\right)=n+2\frac{n-1}{2}\lt 2n$$
We can then bound the probability that the expected value is more than 4n:
$$p\left( \sum_{i=0}^{n-1}n_{i}^2 >4n\right)\leq \frac{E\left( \sum_{i=0}^{n-1}n_{i}^2 \right)}{4n}=\frac{2n}{4n}=\frac{1}{2}$$
This means the probability that we have to use more than $4n$ space is $\frac{1}{2}$.
## Count min sketch
Bruges til at finde heavy hitters i et uendeligt langt input. Lav en $l \times b$ matrix **M**. Hver row har sin egen hash function, som er randomly valgt ud fra en familie af universelle hashfunctions $U \to [b]$. Flow er så når man møder et input, kører man hashfunktionen på alle rækker og addere til counteren hvor dette input bliver hashet til.\\
**Eksempel?**\\
Anerkend at selvom man har et uendeligt input, så bruger man altid den samme mængde plads. Altid $l \times b$. Der kommer til at være clashes i counterne, så counterne i cellerne er kun en upper bound for hvor mange gange input bliver mødt. \\
Vi vil nu kigge på, at bruge en probabalistic approach, kigge på hvad den forventede mængde clashes vi har er. Definer random indicator variable $I_{i,x}(y)$ som er $1$ hviss $h_{i}(x)=h_{i}(y)$ ellers 0. Hvor $h_{i}$ er den universelle hashfunktion $i$ ved række $i$. Da vi bruger en universal hashfunction, er sandsynligheden for to forskellige input clasher $p(I_{i,x}(y)=1)\leq \frac{1}{b}$. Det betyder at counteren i celle $i$ er
$$Z_{i,x}=f_{x}+\sum_{y \in S_n \mid y \neq x} f_y \cdot I_{i,x}(y) \geq f_{x}$$
Hvor $S_n$ er de første $n$ elementer i $S$. Da $Z_{i,x}$ er en random variable, kan vi kigge på dens expected value. Hvor vi bruger at $\sum_{y \in S_n}f_{y}=n=\mid S_n\mid$ som estimation.
$$E(Z_{i,x})=E(f_x+\sum_{y \in S_{n} \mid x \neq y} f_{y} \cdot I_{i,x}(y))$$
Linearity of expectation og at $f_x$ er en konstant.
$$=E(f_{x})+E\left(\sum_{y \in S_{n} \mid x \neq y} f_{y} \cdot I_{i,x}(y)\right)$$
Da $\sum_{y \in S_{n} \mid x \neq y} f_{y}$ alle sammen er konstanter.
$$=f_{x}+\sum_{y \in S_{n} \mid x \neq y} f_{y} \cdot E(I_{i,x}(y))$$
Da expected value af en random incidator variable er $p$.
$$\leq f_{x}+\sum_{y \in S_{n} \mid x \neq y} f_{y} \cdot \frac{1}{b}$$
$$\leq f_{x} + \frac{1}{b} \sum_{y \in S_{n}} f_{y}$$
$$=f_{x}+\frac{n}{b}$$
her er antal collisions afhængig af $n$ hvilket vil sige vi forventer at have mange collisions. Vi kan bruge **markovs inequality** hvor vi isloere antal collisions med **x**, og kigge på om et er mere end $2\cdot \frac{n}{b}$
$$p(Z_{i,x}-f_{x} \geq \frac{2n}{b})=\frac{E(Z_{i,x}-f_{x})}{\frac{2n}{b}}=\frac{\frac{n}{b}}{\frac{2n}{b}}=\frac{1}{2}$$
Da dette er for alle rækker $i$, kan vi se på sandsynligheden for elementer der clasher med **x** i alle rækker **i**. Derfor kan vi nu kigge på minimum af $\hat{f_x}=Z_{i,x}$, baseret på at alle universelle hashfunktioner er independent, så sandsynlighed for at alle $Z_{i,x}$ værdier er mere end $\frac{2n}{b}$ er dem alle gange sammen:
$$p(\hat{f}_x-f_x\geq \frac{2n}{b})\leq \frac{1}{2^{l}}$$
Nu vil vi gerne kunne finde værdierne til **b** og **l**, således at vi kan bounde den her probability for at antallet af gange **x** gentager sig, er mere end et specific sandsynlighed.\\
Vi får givet **$\epsilon$, $\delta$** således at
$$p(\hat{f}_x-f_x\geq \epsilon \cdot n)\leq \delta$$
Hvis vi vælger $b=\frac{2}{\epsilon}$ and $l=\log_{2} \left(\frac{1}{\delta} \right)$ deraf:
$$p(\hat{f}_{x}-f_{x}\geq \epsilon n)= p(\hat{f}_{x}-f_{x}\geq \frac{2}{b} n) \leq 2^{-l}=2^{-\log_2 (\frac{1}{\delta})}=\frac{1}{\frac{1}{\delta}}=\delta$$
Nu kan vi bruge
$$b \times l = \frac{2}{\epsilon} \cdot \log(\frac{1}{\delta})$$
som er uafhængig af **n**, længden af input. \\

Eksempel: Vil vise alle elementer som viser sig mindst 100 gange, i.e $\frac{n}{100}$, med nøjagtigheden skal være $1\%$ fra det rigtige, er væk fra sin rigtige værdi med sandsynlighedehn $\frac{1}{1000}$. Derfor skal 
$$\epsilon=\frac{1}{100} 1\%=\frac{1}{10^4}=10^{-4}$$
og
$$\delta = \frac{1}{1000} = 10^{-3}$$
deraf:
$$p(\hat{f}_x-f_x\geq 10^{-4} n) \leq 10^{-3}$$
Tænk på det i den her rækkefølge: først siger vi at estimatet skal være at $\frac{n}{100}$ væk fra den rigtige værdi. Yderligerer vælger vi at forstærke det med at differencen skal være $1\&$ af $\frac{n}{100}$ væk fra det rigtige. Slutteligt så vil gerne have at chancen for at differencen er $\frac{n}{10000}$ væk fra sin rigtige værdi, skal være $0.1\%$.\\

Det betyder at 
$$b=\frac{2}{\epsilon}=\frac{2}{10^{-4}}=20,000$$ 
og 
$$l=\log_{2} (\frac{1}{\delta})=\log_2 \frac{1}{10^{-3}}=\log_2 10^3 \approx 10$$
så med 200,000 counteres kan vi give et estimat på at counteren er mere end $1\%$ væk fra sin reelle værdi, for elementer som viser sig mere end 100 gange, med en sandsynlighed på $0.1\%$. Det er altså ikke sandsynligt at counteren er mere end $1\%$ væk fra sin reelle værdi.
## Exam notes
- Perfect hashing
	- Solution with $n^2$ in 1st table
	- Random indicator variable
	- Bound by Markov
	- Expected number of trials before perfect
	- Solution with $n^2$ in 2nd table
	- Bound by Markov, more than `4n`
- Universal hashing
	- Drawing
	- Hash collection `S`, `|S|=n`
	- Random indicator variable, fix on `k`
# 8. String matching (naive algorithm, The Rabin-Karp algorithm, Finite-automaton-based string matching).
**Dont define the basics before we know what we will need them for**
## Basics
prefix $w[ x\implies x=wy$
suffix $w]x \implies x=yw$
shift $S=5$ means the string from $T[6\to 6+x]$
![[Pasted image 20231209091652.png]]
Want to find
$$P]T_{S+m}=T[1\dots S+m]$$
Where $m=|p|$ for all `S`.

- Naive implementation will be to simply check all of the possible `S` values. we will use `O(m)` as the running time for finding the pattern and we do this for each `n` elements up to $n-m$, so `O(m(n-m))`. 
- Problem is we dont use the information from the previous trial. for every new `n`.
Solution is we will for each character assign a number. Lets use `base 10` for ease. 
$p=2341$
shift $S$ has value $2341$ they are a match.
We can write $2341$ by Horners rule
$2341=1+10(4+10(3+10 \cdot2))$
which is less expensive to calculate than calculating the powers of 10 over and over again like
$$2341=2\cdot 10^{3}+3\cdot 10^{2}+4\cdot 10^{1}+1$$
We can then calculate the next shifts value in constant time once we have the first shifts value by 
$$t_{S+1}=10(t_{S}-10^{m-1}T[S+1])+T[S+m+1]$$
In this way, we use the information from the previous calculation as well.
## Rabin karp
- utilizes this. So, first calculate $t_{0}$ and then we can calculate all the other $S={1,2,3\dots n-m}$ in constant time. So this will take $\Theta(m)$ for calculating $t_{0}$ and then $\Theta(n-m)$ for calculating the rest.
- But this is too good to be true, as we cannot assume we can compare two very large numbers in constant time. **solution** use `modulo`. That is, we do `mod q` on the pattern `p` and on all the $t_{S}$, and compare these instead.
- When we want to calculate the next $t_{S+1}$ we will do the calculation, where `d` is the base. ![[Pasted image 20231228100311.png]]
- But now if `p mod q` matches with $t_{S} \% q$ then we will have to compare the two original numbers, since they may not actually be equal.
- we want to choose $q\le 10\cdot size \ of \ computer \ word$ since then we can compare the two numbers `mod q` in constant time, as the two numbers can fit into one computer word.  That means we always expect $10[0\dots q-1]$, i.e 10 times something between $0$ and $q-1$. So $0\dots 9+10[0\dots q-1]$ can fit into a computer word, **this is such that we can do the calculation above, i.e $t_{s+1}$ in constant time**
	- That is, look at the fact that $h=d^{m-1}\ mod\  q$, it is downscaled such that we dont exceed a computer word.
	- Therefore we can still keep a processing time of $O(m+n-m)=n$
	- We still can compare elements of in constant time as well, as all $t_{s}$ are downscaled to fit into a computer word.
### At the exam
- But now if `p mod q` matches with $t_{S} \% q$ then we will have to compare the two original numbers, since they may not actually be equal.
- `q` should have a value such that `10q < computer word`, as then we can can make sure that when we calculate the previous value, and we do the calculation $10(t_{s})$, then we will maximally multiply $10(q-1)$, and add `x` where $0 \leq x < 10$, such that this $t_{s+1}$ can again fit inside a computer word.
- **dont try to show the formula** just say that we can still calculate the previous based on modulo calculation. That is, we can `still` calculate $t_{s+1}$ from $t_{s}$
### Expected spurries hits
- Have to test all the matches whether they are actually equal. So in the worst case we still have running time $\Theta(m(n-m))$. However, if we can prove that all of the values from $0\to q$ are equally likely, that is all $Z^{*}: [0,q)$ then the probability of a collision is $\frac{1}{q}$ for a match that was not actually a match. That means we have $E(\#hits)=\frac{O(n)}{q} \leq \frac{n}{q}$
### Final analysis
The expected matching time will be
$$O(n)+O\left( m\left( v+\frac{n}{q} \right) \right)$$
where `v=#actual hits` and $\frac{n}{q}$ is `spurries hits`. and we assume $q\ge m$, or just argue that $O\left( \frac{m}{q} \right)=O(1) \implies O\left( \frac{m}{q} n\right)=O(n)$ and we expect `v` is $O(1)$, then $O\left( m\left( v+\frac{n}{q} \right) \right)=O(n)$ so the expected time for matching is $O(n)$ as $n\ge m$. So the total running time is
$$O(matching + preprocessing)=O(m+n)=O(n)$$
Dont think this is entirely correct. This is the actual runtime of the algorithm: go over `n` elements, match on the last expression: $O(n)+O\left( m\left( v+\frac{n}{q} \right) \right)=O(n)+O(n)=O(n)$ 
Preprocessing is `O(n)`. So preprocessing + matching is $O(n)+O(n)=O(n)$.
## DFA
### Starting notes
All about the suffix function and how we just always want to find the longest prefix of `p` with length `k`, which is a suffix of the input string `x`
That is $\sigma(x)=max\{k | p_{k}\ ]\ x\}$
Also having the final state function $\Phi(x)$ is the state we are in the DFA after reading in the string `x`.
- we want to have the transition function as $\delta(q,a)=\sigma(p_{q}a)$. See the subsection `Proof that we can make DFA without looking at input T`
	- just draw the illustration
### Good example
as the picture
![[string_matching.excalidraw]]
We can first show we can construct `p` without looking at `T`. Then we can show an example, that if we read in some of `T`, then we dont have to remember what we have read. We only care about the state that we are in after reading in some of the characters. Therefore the suffix function is equal to the state we are in after reading in the string `x`
### intro
we have a graph $M=(Q,q_{0},A,\Sigma,\delta)$
- Q is the states
- $q_{0}$ is the start state
- A is the accept states $A\subseteq Q$
- $\Sigma$ is the alphabet
- $\delta:Q\times \Sigma \to Q$ is the transition function.
We now make a function, $\Phi$ which is the `final state function`, where if `M` accepts $w$ then $\Phi(w)\in A$. So $\delta(wa)=\delta(\Phi(w)a)$ since we know the state from the `final state function` and then we just follow the arc `a`.

We want to construct $M=M(p)$ independently of the input text, such that we always have a DFA for the pattern $p$ over the alphabet.
### Suffix function
$$\sigma(x)=max\{k|\ p_{k}\ ]\ x\}$$
which simply means, the longest prefix of `p` (the length is `k`), which is a suffix of `x`.
- The suffix function implies $\forall x\in \Sigma^{*} \implies \sigma(xa) \le \sigma(x) + 1$ since the new character `a` may just give a smaller prefix of `p` which is a suffix of `x`.
We now want to define the DFA as having 
- $Q=\{0,1,2\dots m\}$
- $A=\{m\}$
- $q_{0}=0$
- $\delta(q,a)=\sigma(p_{q}a)$, since $p_{q}$ is the longest suffix of $T_{q}$ which forms a prefix of `p`, and then we transition to the new state when we have read `a`.
This will ensure we don't have to construct the DFA  from the input text `T` which is the goal.
### Proof that we can make DFA without looking at input T
let $q=\Phi(T_{i})$ be the state we are in after reading $T_{i}$, then $p_{q}$ is the longest prefix of `p` which is a suffix of $T_{i}$. Then when we read $a=T[i+1]$, we want to make the transition to $\delta(q,a)=\sigma(T_{i}a)=\sigma(p_{q}a)$ i.e we dont have to look at `T`, we only care about the state we are in. This can be seen from this picture
![[string_matching.excalidraw]]
when we look at $T_{i}$ we have moved to some state in the DFA, **but the DFA is constructed to only accept suffixes of T which are of length of `m`, i.e `p` is a suffix of `T`**. Therefore, when we have read $T_{i}$ we are in the state corresponding to if we had only read $p_{q}$. 

Looking at the longest prefix of `p` which is also a suffix of $T_{i}$, is the same as looking at the first `q` (which corresponds to the state we are in the DFA) letters of `p` and then the transition when we add $a$.
### Final proof of the state we are in after reading $T[i+1]$
## Notes for the exam
- (briefly)Showcase naive algorithm
- Shifts and their requirements
- Rabin-Karp with Horners rule
- modulo (10q)
- $p(hit)=\frac{1}{q}$
- Expected match time
# 9. Maximum flows (Definitions, Ford Fulkerson algorithm, Max-Flow- Min-Cut theorem, Edmonds-Karp Algorithm, bipartite matching, integrality theorem)
## Figuring out if your flow is actually maximal
![[Pasted image 20231230120835.png]]
The flow of the `(S,T)` network will always be $\mid f\mid=f(S,T)-f(T,S)$ which means that it will always be what flows from the S side to the T side, minus what goes back. This is due to the flow value being $\sum_{v \in S} b_{f}(s)$.
This can easily be seen from the next picture:
![[Pasted image 20231230121229.png]]
What is inside of S will always have $\forall v\in S:  b_{f}(v)=0$ except for little `s`. That means the only flow which can contribute positively is the arcs going out of `S` and negatively is the arcs that go back into `S`. 
![[Pasted image 20231230121506.png]]
This is true since we can maximally send out the capacity of the arcs coming from `S` into `T`, and what comes back may be `0`, that is $f(T,S)\geq 0$ so we can make some bound. So if we have a cut, and $\mid f\mid = c(S,T)$ then the flow we have found is maximum. 
**rewrite**: The only flow that can contribute positively is the flow coming out of `S`, therefore this is bounded by the smallest capacity of what we can send out of `S`, which are the bottleneck-arcs. If we find some cut that is larger than some other cut, then this means that these can only get flow from the bottleneck arcs, so the `|f|` must be smaller, i.e we cannot fill all of the arcs on in this cut with their maximum capacity.
## Residual networks
![[Pasted image 20231230123551.png]]
This is just as you have worked with before, we start off with just the regular network, and as we augment the paths with flow, we will start having the capacities backward instead. We can then take any path in the residual network from `s` to `t`, and increase the flow on the forward arcs and decrease the flow on the backward arcs, which will preserve the `S, T` conditions, where all vertices in between will have $b_{f}(v)=0$, and so on. 
**Get better understanding of why this works?**
![[Pasted image 20231230125459.png]]
Do note that during real world examples, we regularly cancel out flows `cancelling out what we have already given of flow` to find a better flow-value.
This gives rise to the `Ford-folkerson` algorithm, finding augmenting paths until no more can be found. If we cannot find new augmenting paths, then we have a maximum flow. 

This depends very much on the fact that during this augmentation in `N`, all the vertices have flow conservation still. We will find the smallest $\delta$, and on the backwards arcs in `N` we will decrease by $\delta$ while on the forward arcs, we will increase by $\delta$. 

**During the exam** just like Mads has said, we only need to describe the residual network in brief, so it is enough to say that the balance of all other than the vertices `s, t` will still be 0, and we augment with the minimum increase in the residual network.
## Ford-Folkerson
The algorithm will stop eventually, since when we can find an augmenting `S,T` path, the flow is increased by $\delta$-units. And if we look at
![[Pasted image 20231230131221.png]]
we see that the sum of capacities on all arcs from `S` is an upper bound of the flow, which we proved first, and since we increase the flow `f` by at least `1` each time, then it will terminate, assuming that no infinite capacity path exists from `s` to `t`.
## Max flow, min capacity cut (proving the found network by Ford-Folkerson is actually maximum)
min capacity means that since $|f| \leq c(S,T)$ then when we have found the flow that is equal to the capacity of some cut, then the capacity cut must be the minimum, as we may be able to find some capacity cut that is larger, but it is not the minimum

We have to prove the following
1. `f` is a maximum valued flow in the `S,T` flow for `N=(V, E, c)`
2. There are no more augmenting paths in $N_{f}$
3. `|f|=c(S,T)` for some cut `S,T` cut
Now of course, if we find a capacity (a minimum capacity) of a cut that has the value of the flow, then this is the maximum flow, as we have already proven.
- Clearly, 1 implies 2, as $!2 \implies !1$ therefore, there is an augmenting path, then the flow is not a maximum. That is, we can increase by at least `1`, then the flow is clearly not maximum.
- 3 implies 1, as $\mid f\mid \leq c(S,T)$, so if we can find a cut in which $\mid f\mid=c(S,T)$ then this is a max flow.
- 2 implies 3, as when we have no more augmenting paths in the residual network, that must mean that we cannot get to `T` from `S` anymore in $N_{f}$. This means that we can make the set `S` with arcs going to `T` in such a way that the capacity of all these arcs are maxed out with flow. Thereby we have no way to get to `T` in the residual network, when we define the arcs by how we actually made the residual network. 
![[Pasted image 20231230134546.png]]
This must also mean that `N` looks like 
![[Pasted image 20231230135327.png]]
Since if we had flow going from `T to S`, then we would be able to cancel it out in $N_{f}$, but as $N_{f}$ has no arcs from `S to T` then the flow must be `0` on all the arcs going from `T to S`. now as
$$|f|=f(S,T)-f(T,S)$$
$$|f|=f(S,T)-0=c(S,T)$$
And since 3 implies 1, then the found flow is maximum.

### Running time
Now we may only increase the flow by `1` in each iteration, and if there are augmenting paths which augment by more than this we are of course unlucky to have chosen this exact path. But we may always be unlucky, meaning we end up with the running time of 
$$O(|f| \cdot |E|)$$
Since we may find the path in linear time in regards to the number of edges $E$.
### Solution to bad running time: Edmonds-Karp
![[Pasted image 20231230142426.png]]
The main point is that when we use `breadth-first-search` the previous augmenting paths length was the shortest path, but in then next iteration, the shortest path will always be the same OR longer. **the IMPORTANT observation is that as we augment along the algorithm, we cannot get a shorter path than the previous shortest path.** That is 
let $n_{i-1}=$ shortest path in step $i-1$ of the algorithm, then $n_{i-1}\leq n_{i}$. This is because when we use an augmenting path, then we remove an arc (by making an arc backwards), removing the same path from the shortest paths. So we are forced to try other paths now.
So we cannot end up in a situation where we always choose the same bad path. 
#### Running time
![[Pasted image 20231230144806.png]]
- The paths will be at least of length 1
- A path may only use the same vertex once, therefore the path may only be $n-1$ long as we ignore the first
- at most $|E|$ paths in the `breadth-first-search` which has the same length, as we flip at least 1 arc for each augmentation.
- As we at most can make $|E|$ paths of the same length, and the shortest path may be up to $|V|-1$ long, we have this many augmenting paths.
	- **note that we dont care about the length of each path**, we just care about how many augmenting paths there are.
	- This is clear from the fact that for each length of an augmenting path $1,2, \dots , |V|-1$ there are maximally $|E|$ augmenting paths with this length.
- we use `BFS`
- obvious that each time we find a new augmenting path, we have to again find the shortest BFS-path, as we have to recreate the residual network.
	- so for each time we augment, and there may be $(|V|-1)\cdot|E|$ augmenting paths in total, we run `BFS` again, which runs in $|V|+|E|$.
## Residual network example
Show first how it looks in `N`, then show that you are allowed to cancel it in `N_G`.
![[residual.excalidraw]]

## Notes for the exam
- (briefly) network definition
- Residual networks (**just show example**)
- (brief) Ford-Folkerson
- Max flow, min (capacity) cut
- Runtime
- Edmonds-Karp
# 10. The min-cut problem (randomized algorithm, solution via flows, solution via max-back orderings)
## IMPORTATNT
- is to understand the fact that having these anti-parallel edges, having flow of `1` on the arc, means that there is an edge present. Therefore when we have found the min-cut, we have found the minimum number of edges we have to remove before the graph is disconnected
- What the hardest for you to understand why it is true that we can simply fix some `x` and iterate over all the different possible `y` choices.
	- This is all about thinking it is every possible way to seperate into two partitions where `x` is disconnected from `y` for all `y`.  
- **Remember** that $\lambda(G)=min\{\lambda(s,t) |y \in V\backslash \{x\}\}$ `is actually` the minimum of all the flows in the corresponding networks.
	- Now we have to prove why the corresponding flow-value of the different `s, t` networks is the minimum of the number of edges we have to remove before the original graph is disconnected. 
		- This means we have to prove the max-flow min-cut theorem, `remember that edmond carp is guranteed to find the maximum flow, and this is equal to a minimum cut`, so we prove that this flow is equal to a minimum cut, where filling with flow to the capacity of the arc means we are using it. And the flow is `1` thereby, the summation of all the capacities means we are summing up `1` for each edge we are using. Therefore $|f|=\#min \ edges$.
## Formulate the problem as a min-cut flow problem
- We start by defining the fact that $\lambda (G)$ is the minimum edge connectivity. 
- $\lambda(G)=min\{\lambda(x,y) | x,y \in V\ and \ x\neq y\}$, since this is a combination of `x, y`, when we find the minimum amount of edges that connect these two, we are done.
- Now we can find the minimum by $\lambda(G)=min\{\lambda(x,y) |y \in V\backslash \{x\}\}$ since
	- This is simply because it is every possible way to separate the graph into two `partitions`, since for a graph to be connected there must be a way from every vertex to another. If we try all options to disconnect a fixed `x` from `y`, then we have effectively tried all possible ways to disconnect the graph into two components. As, this makes all the vertices not able to reach `x` either.
- This means we have to run the algorithm $|V|-1$ times.
## Quickly summarize how we would make the undirected graph to a directed one
- We can start by taking the undirected graph, and make it into a directed graph, by making unparalleled edges from $(u,v), (v,u) \ |\  \forall v\ and \ u, u\neq v$ all with capacities of 1, simplifying into the fact that the flow can go both ways.
	- This means there can be `0-1` flow on each arc, signifying that there is an edge here when the flow is `1` or else when it is `0` the edge is not there.
- Now we can try all pairs of $(s,t)=(x,y)\ |\ y \in V \backslash \{x\}$, run Edmonds-Karp on all these possible S,T-Networks, and take the minimum of all these flow values, bounded by the minimum capacity cuts. 
- This is because the flow is bounded by the capacity going towards the other partition where the sink `t` is. Now, as the flow is bounded by the minimum capacity of the edges going toward the other partition, and the capacity of `1` on all edges signifies that there is an edge between the two partitions, the minimum capacity **is** the minimum number of edges going towards the other partition.
- Does this work in ?????$O(\mid V\mid \cdot (\mid V\mid + \mid E\mid))$ ?????????

### Chatten
Your summary and understanding of how to determine the edge connectivity �(�)λ(G) of an undirected graph using flow algorithms are largely correct. Here's a breakdown of the key points:

1. **Anti-parallel Edges and Flows**: The transformation of an undirected graph into a directed one by replacing each undirected edge with a pair of anti-parallel directed edges, each with a capacity of 1, allows you to use flow algorithms. The presence of a flow of 1 in either direction signifies that the original undirected edge is present. Thus, finding a minimum cut in this flow network corresponds to finding the minimum set of edges whose removal would disconnect the graph.
    
2. **Fixing Vertex x and Iterating Over y**: By fixing a vertex �x and iterating over all other vertices �y, you are indeed trying all possible ways to separate the graph into two partitions. This is because a graph is connected if and only if there is a path between every pair of vertices. So, by finding the minimum cut that disconnects �x from �y, you are considering all such partitions. Since you do this for all vertices �y, you effectively consider every possible disconnection scenario, ensuring that you find the true edge connectivity.
    
3. **Minimum Edge Connectivity**: The minimum edge connectivity �(�)λ(G) is the smallest number of edges that, when removed, disconnects the graph. Your formula �(�)=min⁡{�(�,�)∣�∈�∖{�}}λ(G)=min{λ(x,y)∣y∈V∖{x}} is correct. It reflects that you only need to consider disconnecting a fixed vertex �x from every other vertex �y, rather than considering every possible pair of vertices.
    
4. **Directed Graph Construction**: Your description of converting the undirected graph to a directed one is correct. You replace each undirected edge with two directed edges with capacities of 1, which allows the flow to go in both directions, reflecting the undirected nature of the original graph.
    
5. **Edmonds-Karp and Min-Cuts**: Running the Edmonds-Karp algorithm (or any other max-flow algorithm) for all pairs (�,�)(x,y) where �y is every other vertex except �x, and then taking the minimum of these flow values will give you the edge connectivity of the graph.
    
6. **Runtime Complexity**: The complexity of �(∣�∣⋅(∣�∣+∣�∣))O(∣V∣⋅(∣V∣+∣E∣)) mentioned at the end is incorrect if it's supposed to reflect the use of the Edmonds-Karp algorithm, which has a runtime of �(∣�∣⋅∣�∣2)O(∣V∣⋅∣E∣2) for each max-flow computation. Since you perform ∣�∣−1∣V∣−1 max-flow computations, the total runtime would be �(∣�∣2⋅∣�∣2)O(∣V∣2⋅∣E∣2). If using more efficient max-flow algorithms like Dinic's algorithm, the complexity could be �(∣�∣3⋅∣�∣)O(∣V∣3⋅∣E∣).
    

So in summary, your understanding of the method is correct, but there's a need to correct the runtime complexity based on the max-flow algorithm used. For Edmonds-Karp, the complexity is �(∣�∣2⋅∣�∣2)O(∣V∣2⋅∣E∣2), and for more efficient algorithms, it could be �(∣�∣3⋅∣�∣)O(∣V∣3⋅∣E∣).
## Proving max-flow min-cut theorem

## Exam notes
- Natural to discuss edge-connectivity
- Try all possible options
- Fix specific vertex
- undirected graph ---> network
	- `flow = 1` on ark -> we use the underlying undirected edge.
- Max-flow min-cut
	- **Remember** that $\lambda(G)=min\{\lambda(s,t) |y \in V\backslash \{x\}\}$ `is actually` the minimum of all the flows in the corresponding networks. (see #remember part of this question for explanation)
- prove max-flow min-cut.
	1. `f` is a maximum valued flow in the `S,T` flow for `N=(V, E, c)`
	2. There are no more augmenting paths in $N_{f}$
	3. `|f|=c(S,T)` for some `S,T` cut

## min cut algorithm
probability of contracting edge $e_{i}$ which does not cross the minimal cut `C`, for all contractions is
$$p(E_{1}\cap E_{2} \cap \dots \cap E_{n-2})=p(E_{1})\cdot p(E_{2}|E_{1})\cdot p(E_{3}|E_{1} \cap E_{2})\cdot \dots p(E_{n-2}|E_{1} \cap E_{2} \cap \dots \cap E_{n-3})$$
It goes up to $n-2$ as when we have contracted this many edges, then we will have only two vertices left.
lets focus on a specific cut
$$p(E_{j}|E_{1} \cap E_{2} \cap \dots \cap E_{j-1})=1-p(not \ E_{j}| E_{1} \cap E_{2} \cap \dots \cap E_{j-1})$$
I.e `1 - (the event that we choose to contract one of the edges in the minimum cut)`
$$p(not \ E_{j}| E_{1} \cap E_{2} \cap \dots \cap E_{j-1}) = \frac{\#edges \ in\ min-cut}{\#edges \ left\ after \ j-1 \ contractions}$$
now `#edges left after j-1 contractions` can be bounded by
$$\#edges \ left\ after \ j-1 \ contractions\geq |V|-j+1 \cdot \frac{min\{edge\ degree\}}{2}$$
$$\geq |V|-j+1 \cdot \frac{\#num \ edges\ in\ min-cut}{2}$$
thereby (insert what we just found out in the original equation)
$$p(not \ E_{j}| E_{1} \cap E_{2} \cap \dots \cap E_{j-1}) \leq \frac{2}{|V|-j+1}$$
$$1-\frac{2}{|V|-j+1}=\frac{|V|-j-1}{|V|-j+1}$$
therefore 
$$1-p(not \ E_{j}| E_{1} \cap E_{2} \cap \dots \cap E_{j-1}) \geq \frac{|V|-j-1}{|V|-j+1}$$
This all ends up with
![[Pasted image 20240103190806.png]]


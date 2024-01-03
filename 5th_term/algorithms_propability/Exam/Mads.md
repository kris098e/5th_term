Good presentation of basic material is better than covering hard material poorly.

## Examples of things to do
A = harder
B = easier
### 1 - Counting
A: Prove the sequence of $n^2 +1$ distinct numbers, there is a strictly increasing or decreasing subsequence of length n. Derive formula for the number of subsets with repetition.

B: Derive formulas for the number of permutations and combinations
### 2 - Inclusion - Exclusion
A: Derive inclusion exclusion principle. Derive formula for the number of derangements or onto-functions

B: Derive formula for the number of onto-functions
### 3 discrete probability, random variables and bound
A: Prove Markov's inequality and/or Chebyshev's inequality. Use Chebyshev's inequality to bound probability of some amount (say 10) people getting their hat back in the hat-check problem.

B: Define (indicator) random variables. Use linearity of expectation to show that the expected number of people getting their hat back in the hat-check problem is 1

### 4 - Randomized algorithms
A: Derive the probability that the randomized min-cut algorithm finds a min-cut. MAX-k-SAT algorithm is also an option

B: Analyze randomized majority element algorithm. MAX-3-SAT

### 5 - Probabilistic analysis
A: Expected number of coupons in the coupon-collector problem. MAX-k-SAT

B: Show that the expected number of people to get their hat in the hat-check problem is 1.

### 6 - Examples of applications of indicator random variables
A: Show that any graph G(V,E) has a spanning bipartite subgraph with at least $\frac{|E|}{2}$ edges.
Show that for any 3-SAT instance it is possible to satisfy at least $\frac{7}{8}$ of clauses

B: Show that the number of times we expect to find a new largest element when scanning a random permutation of n distinct numbers is H_n (O(log n))
Show that the expected number of people to get their hat in the hat-check problem is 1.


### 7 - Universal hashing: 
A: Let U be a set of keys, $S \subseteq U, n=|S|$ and let h be chosen uniformly at random from a universal set of hash functions from U to |m|. Shows that the expected number of keys $k' \in S - \{k\}$ ("-" is "\\") such that h(k') = h(k) is at most n/m

B: Define a universal set of hash function (pick one shown in the course and show that it is universal)

### 8 - String Matching
A: Explain the idea behind Rabin-Karp algorithm
Explain how to construct DFA for string matching

B: Explain the naive algorithm and explain in broad terms what the Rabin-Karp algortihm does better.

### 9 - Maximum flows
A: Briefly define a network and residual network (briefly!). Then prove the Max-flow Min-cut theorem.

B: Define a network and residual network and explain the idea behind the Ford Fulkerson method.

### 10 -  The Min-cut problem
A:  Analyse the randomized algorithm for finding a min-cut.
Formulate it as a max-flow problem and use the Max-Flow Min-Cut theorem to prove that the answer is correct.
Prove the max-flow min-cut theorem

B: Analyze the randomized algorithm. Formulate it as a max-flow problem.
let $X_{i}$ = 1 iff we hire the `i'th` candidate, else 0. Since these candidates come in a random order, that means the probability that the `i'th` candidate is better than the `i` options in total is $\frac{1}{i}$. Now we can sum up over all indicator random variables
Then
$$E(X_{i})=p\cdot 1 +(1-p)0=p=\frac{1}{i}$$
since
$$p(X=1)=\frac{1}{i}$$

$$E(X)=E\left( \sum\limits_{i=1}^{n}X_{i} \right)=\sum\limits_{i=1}^{n} \frac{1}{i}=H(n)=ln (n)$$
# generating random permutation
using $n^3$ in permutation by sorting

p: $A_{i,j}$, where `i, j` are distinct elements are given same priority is $\frac{1}{n^{3}}$
$$p\left(\sum\limits_{0\leq i < j<n}A_{i,j}\right)=\forall i,j: p(\cup A_{ij})\leq \sum\limits_{0 \leq i < j < n}p(A_{i,j})$$
$$=\sum\limits_{0 \leq i < j < n} \frac{1}{n^{3}}= \frac{{n \choose 2}}{n^{3}} < \frac{1}{n}$$
since ${ n \choose 2} < n^{2}$

so the probability of collision is $< \frac{1}{n}$ meaning the probability of no collision is $\geq 1- \frac{1}{n}=\frac{n-1}{n}$

![[Pasted image 20240107164313.png]]
**remember** that it is simply based on the fact that we have the intersection of all the events. 
$$p(X_{1})=\frac{1}{n}$$
as out of the `n` elements, this has to be the smallest. Now we look at the probability that $p(X_{2})$ is the 2nd smallest, that is, out of $n-1$ elements, this has to be the smallest. Therefore $\frac{1}{n-1}$

![[Pasted image 20240107172036.png]]
Easy to see that for `i=1`, each element can be at index 1. If we move onto the next, there `n-1` possibilites left, and since we have a random choosing, each element has $\frac{1}{n-1}$ chance of being at this position in the array after we are finished.  

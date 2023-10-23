Start of by calculating total number of assignments, where we don't have the meet the condition of having at least 1 woman and man in each of the committees, then remove the ones where we don't match the condition, which should bring us down to what we want to prove.

First, we will define a random assignment of men and women to the skills, each skill can be assigned to a man or a woman with the probability of $1/2$ \\
Now we can define a random variable as X the number of committees where there is at least one man and one woman in the committee. With this, we can calculate the expected value of X, which is the average of the number of committees where there is at least one man and one woman.\\
The probability that we have committees of size $k$ where there are either only men or women are then $(\frac{1}{2})^k$, since we then have to choose the same gender $k$ times uniformly randomly, where the probability of picking the man or woman (where we fixed on picking either only men or women) is $\frac{1}{2}$ for each drawing of the man or woman from the set of men or women. We then want to take the compliment of the scenarios, meaning we have the probability $1-(\frac{1}{2})^k$ of picking committees with at least one woman and one man. 

We now use random indicator variables, where the random indicator variable $X_i=1$ iff the committee \textit{i} satisfies the condition, else it takes the value $0$. This means that $E(X_i)=1\cdot (1-(\frac{1}{2})^k)$, since the probability of the \textit{i'th} committee is satisfied is $1-(\frac{1}{2})^k$, and the random indicator variable is equal to $1$ when its satisfied, else its 0. We then do this for all of the $m$ committees, i.e have random indicator variables for all $1\leq i \leq m$, and use \textbf{linearity of expectation} which results in the calculation
$$E(X)=E(\sum_{i=1}^m X_i)=\sum_{i=1}^{m} 1-(\frac{1}{2})^k=m \cdot (1-(\frac{1}{2})^k)$$

Now we show that the expected value of $X$ is less than $m$, since if we can prove this, then we know that if we only pick the expected value of $X$-committees or less, then there will always be a combination of the $m$ committees, where we have satisfied the condition of picking at least one man and one woman.\\
We can rewrite $$1-(\frac{1}{2})^k$$
To its alternate form: $$2^{-k}(2^k-1)=\frac{2^k-1}{2^k}$$
We now have, that the number of committees that satisfy the condition is $$m(\frac{2^k-1}{2^k})$$\\
From this we that, if $$m=2^k$$ then only $2^k-1$ of the clauses in the committee is expected to satisfy the condition. This means that, if we choose $m=2^k-1$, then the expected number of satisfied committees will be equal to $2^k-1$. This is because if we fx. satisfy the condition in $7.1$ committees, then one of the random indicator variables will have to have satisfied more than the $7.1$ committees, fx. $8$ committees. This means the number of satisfied committees is actually calculated as $$\lceil m(\frac{2^k-1}{2^k})\rceil$$. This means if $$m\geq2^k$$then we expect to satisfy the condition in only $2^k-1$ of the committees. This means that there must exist a choosing from the $m$ created committees, where we choose only $2^k-1$ of the committees which satisfies, that at least 1 woman and at least 1 man is in the committee. This also implies that, since $k\geq 2$ then $2^{k-1}$ committees are also satisfied, since this is a smaller number of expected committees that satisfies the condition than what we have proved to be the number of committees satisfied, then we have also proved that it works for the case where we only have to satisfy $2^{k-1}$


# Solution
As a committee has have at least 1 woman and 1 man to be correct, we see that if we have to form a committee with \textit{k} people (which implies \textit{k} skills). This means that picking the first person out of the \textbf{k} people, can never cause the committee to not meet the condition. However, when we have picked the first person, either a woman or a man, then the next person we can pick has a $\frac{1}{2}$ chance of making the committee satisfy the condition. This holds for the leftover $k-1$ people we have to choose. The probability of a committee being satisfied is then $1-\left( \frac{1}{2} \right)^{k-1}$

We now use random indicator variables, where the random indicator variable $X_i=1$ iff the committee \textit{i} satisfies the condition, else it takes the value $0$. This means that $E(X_i)=1\cdot (1-(\frac{1}{2})^{k-1})$, since the probability of the \textit{i'th} committee is satisfied is $1-(\frac{1}{2})^{k-1}$, and the random indicator variable is equal to $1$ when its satisfied, else its 0. We then do this for all of the $m$ committees, i.e have random indicator variables for all $1\leq i \leq m$, and use \textbf{linearity of expectation} which results in the calculation
$$E(X)=E(\sum_{i=1}^m X_i)=\sum_{i=1}^{m} 1-(\frac{1}{2})^{k-1}=m \cdot (1-(\frac{1}{2})^{k-1})$$
Now we show that the expected value of $X$ is less than $m$, since if we can prove this, then we know that if we only pick the expected value of $X$-committees or less, then there will always be a combination of the $m$ committees, where we have satisfied the condition of picking at least one man and one woman.\\
We can rewrite $$1-(\frac{1}{2})^{k-1}$$
To its alternate form: $$2^{-k-1}(2^{k-1}-1)=\frac{2^{k-1}-1}{2^{k-1}}$$
We now have, that the number of committees that satisfy the condition is $$m(\frac{2^{k-1}-1}{2^{k-1}})$$then we expect to satisfy the condition in less than $2^{k-1}$ of the committees. This means that there must exist a choosing from the $m$ created committees, where we choose less than $2^{k-1}$ of the committees which then satisfies, that at least 1 woman and at least 1 man is in the committee.



# Comments
- % using the stars and bars method / choosing with repetition
- % Why can we use the sum rule?
- % should specify why we only calculate the probability of R, E, N and also why we multiply them together. I.e why we use the product rule (they are independant)
- % Should specify why it is so, i.e it is (#number of ways we get 1) / (#all ways)
- % should add some more information to this
- % add that box1 means that box1 is satisfied?
- % should we add explanation to why?
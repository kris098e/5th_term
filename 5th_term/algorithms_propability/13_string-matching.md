# Intro
![[Pasted image 20231213091043.png]]
- This is the string from $T_{1}$ to $T_{i}$ which is just noted as $T_{i}$. 
- the last two letters $ab$ form a suffix of $T_{i}$. This suffix of $T_{i}$ is a prefix of the pattern `p`. We want to find the maximal length of this suffix, which is also the maximal prefix of `p`.
# Video
![[Pasted image 20231209091617.png]]
![[Pasted image 20231209091652.png]]
This means that the shift = 5 is valid, since `S` has to be 5 before can begin seeing the pattern we are looking for.
![[Pasted image 20231209091908.png]]

![[Pasted image 20231209093543.png]]
Remember that we are looking at the entire word after adding the suffix or prefix. We are not just looking at the prefix and suffix parts.
![[Pasted image 20231209093631.png]]
This means that the `p` is actually what we have added to the string `T` from `S`. So `p` is the last `m` characters.
![[Pasted image 20231209094141.png]]
![[Pasted image 20231209094301.png]]
![[Pasted image 20231209094506.png]]
![[Pasted image 20231209094642.png]]
![[Pasted image 20231209094739.png]]
![[Pasted image 20231209094911.png]]
![[Pasted image 20231209095215.png]]
It is much more efficient to calculate the number using the lowest calculation. Since we do not have to have all of the large numbers $10^{4},10^3,\dots$ since we can just do it by multiplying by 10 multiple times.

> 17 min inde

![[Pasted image 20231209135443.png]]
- To calculate $t_{s+1}$ we have to remove the most significant number from $t_{s}$ which was calculated by $10^{m-1}T[s+1]$. We now want to make all of the other numbers count for $10\cdot number$ more, i.e. multiply all expressions in $t_{s}$ by 10, since the 2nd most significant number before is now the most significant and need to be `multiplied by 10`.  Lastly we want to ass the least significant number again.
- If we have already caclulated $10^{m-1}$ it is constant time, else it is what stated below on the picture.
![[Pasted image 20231209140259.png]]

![[Pasted image 20231209140530.png]]
If `p` is very large then we cannot compare `t` to `p` in constant time. That is, if our architecture has a low word-size, then constant time is unrealistic. Jørgen mentioned something about if the word is 10-20 then it is still realistic to expect this, else it is unrealistic.
![[Pasted image 20231209140854.png]]
What is meant here is that to calculate $p \%q$ we have to calculate `p` in exactly $\Theta(m)$ as p is calculated in $\Theta(m)$ and mod operation is constant time. The same with $t_{0}$ and the rest. 

![[Pasted image 20231209141824.png]]
We want it to be `10q` as then the calculation below can be done in `1` computer word. If _look at the calculation in the picture below this_, it is $1\dots 9+10(q)$. That means we always expect $10[0\dots q-1]$, i.e 10 times something between $0$ and $q-1$. So $10[0\dots q-1]$ can fit into a computer word, and we only have to use one computer word for this.
- the `red box`: since $t_{s}$ is mod q, $h$ is mod q, and $T[s+1]$ is less than q, then it can all be done in a single computer word.
![[Pasted image 20231209141804.png]]
![[Pasted image 20231209142243.png]]
If we have a hit, we must actually test if they are a true match. This means in the worst case, we still have the same running time as before, since we have to calculate the true values of the hits.
![[Pasted image 20231209155025.png]]
- Assume that each of the $0,1,2\dots q-1$ values is equally likely.
![[Pasted image 20231209155237.png]]
- as written, this is preprocessing + matches, preprocessing is $\Theta(m)+\Theta(n-m+1)$ to calculate all of the $t$-values.
![[Pasted image 20231209155851.png]]
![[Pasted image 20231209155902.png]]
![[Pasted image 20231209160051.png]]
![[Pasted image 20231209160559.png]]
![[Pasted image 20231209160902.png]]
![[Pasted image 20231209161117.png]]
- This simply means that `x` last character is the last of `p`, 2nd last is also matching the one in `p` and so on. I.e we give it a string, and it will return the max of `k`, where `k` is the largest suffix.
- ![[Pasted image 20231209170519.png]]

![[Pasted image 20231209172010.png]]
This means that the transition function will now be:
- $p_{q}$ is the largest prefix of `p`
- $p_{q}a$ is then the largest prefix of `p` followed by an `a`.
the `red box` explains it quite clearly.
- $p_{q}]T_{i}$ means that $p_{q}$ is a suffix of $T_{i}$, and here $p_{q}$ is a prefix of `p`. Then `q` is the longest suffix of $T_{i}$.
- **for the exam just try drawing the picture below to explain it?**
	- For this, explain a long the way, that if we fx see a `b` in state `0`, then the longest prefix of `p` when we include some character (here b) that we can be formed from the suffix of $T_{i}$, is of length `0` as we cannot make a prefix of `p` when we include that `b` which is not part of `p`.

![[Pasted image 20231209172225.png]]
![[Pasted image 20231209173049.png]]
![[Pasted image 20231209173407.png]]
$P_{q}$ is the longest prefix of `P`. This means that we are currently in the state `q`, however as this is not the entire `P` then $P_{q}$ is a prefix of `P`. And $T_{i}+P$ is a suffix of $T_{i}$, where some of `P` may be in $P_{q}$.
![[Pasted image 20231209174015.png]]
![[Pasted image 20231209174056.png]]
- This statement is what is tying it all together.
	- instead of looking at the longest suffix $p_{q}$ which is the longest prefix of `p` in the text `x`, we can simply look for the same in the string $p_{q}a$, so we can omit the `x` all together.
	- Jørgen says it would be easier to make a drawing and see it. So you could use the one in the DFA example.
	- ![[string_matching.excalidraw]] Only the green part matters, as we are looking for something which is also a prefix of `p`, therefore we should only look at maximally the last `len(p)` elements, as only this can form a prefix of `p`. If the first characters in the `green area` does not from a prefix of `p` then we should also omit looking at these.
- see for instance from minute `56` for explanation
- In this example it is important to notice that $p\ ]\ p_{q}a$, so adding `a` to the current position will actually move us one step closer to finalizing.
- What is stated is that when $p_{q}]x$ and we add `a` to the text `x` then what was read in $x+p_{q}$ as $p_{q}$ is a suffix of `x` then when we read in `a` , this must also be a suffix. **remember that $p_{q}$ is not the entire `p`**.  
![[Pasted image 20231209180136.png]]
- Here it is stated that the longest suffix of $T_{i}$ is the longest prefix of $p$, for all $T_{i}$, where `p` is a suffix of $T_{i}$ when in state $m$.
![[Pasted image 20231209180620.png]]
![[Pasted image 20231209180721.png]]

![[Pasted image 20231209181011.png]]
![[Pasted image 20231209181333.png]]

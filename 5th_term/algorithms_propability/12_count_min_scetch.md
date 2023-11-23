![[Pasted image 20231122064751.png]]
A matter of we want to find the majority element without saving all of the elements, since `we dont have that much memory, and it may be slow`. 
![[Pasted image 20231122064928.png]]
This will in fact return the majority element, when it occurs more than twice the times
![[Pasted image 20231122065146.png]]
We use $\log m$ space as this is the maximal the counter can be in bits, if the stream only contained `m` repeats of the same elements. And $\log n$ bits for the largest $x_{i}$.
![[Pasted image 20231122065728.png]]
![[Pasted image 20231122072040.png]]
![[Pasted image 20231122073155.png]]
![[Pasted image 20231122073413.png]]
![[Pasted image 20231122073553.png]]
![[Pasted image 20231122074131.png]]

![[Pasted image 20231122074503.png]]
`2nd bullet point:` We only decrement all of the counters by 1, whenever we dont hold the element that we are currently looking at. We only decrement $\frac{m}{k}$ times. 
- **Important** to notice that it is `all` that are decremented, thats why we have the upperbound of decrementing $\frac{m}{k}$ times.
![[Pasted image 20231122080658.png]]
space use is $\frac{1}{\epsilon}$ since this is the amount of counters we store.
# More important
![[Pasted image 20231122081544.png]]
![[Pasted image 20231122081605.png]]

![[Pasted image 20231122081747.png]]
What we do is that we have a hashfunction for each of the `l` rows. We then go through all of the `l` rows, hashing `x` via `h` i.e $h_{l}(x)$ and increment the counter, which started at 0, in each of the rows. Therefore each of the rows has exactly `1` of the counters incremented with each entry.
![[Pasted image 20231122082053.png]]
![[Pasted image 20231122082345.png]]
- What we see is that we only use $b \cdot l$ counters, for an infinite input. I.e it does not matter if the input has the size of fx `100` or `1,000,000` we still use the same counters
- The cells will give us the upper bound of the frequencies of the inputs. This is because we cannot be sure that we have a cell with no collisions, i.e where two values hash to the same cell, but it does gives us an upper bound of the amount of times the element occurs.
![[Pasted image 20231122083553.png]]
- $M_{i, h_{i}(x)}$ is simply row `i` and the column which is the hash value of x.
- This is just stating that we may have collisions, therefore it is an upperbound and not an exact frequency
![[Pasted image 20231122083741.png]]
![[Pasted image 20231122084047.png]]
![[Pasted image 20231122084059.png]]
![[Pasted image 20231122084218.png]]
![[Pasted image 20231122084447.png]]
![[Pasted image 20231122084522.png]]
- The expected value of the cell `i,h_i(x)` is off by at most $\frac{n}{b}$
- We have to depend on `n` as we only have `b` entries in the hashtable, so we expect to have many collisions. 

But we can do better.
![[Pasted image 20231122085211.png]]
We use markovs inequality (where we have isolated $\frac{n}{b}$ in the previous expression), to bound the probability that we will be off by $2 \cdot \frac{n}{b}$, i.e 2 times the expected value. Which is $\frac{1}{2}$
![[Pasted image 20231122085421.png]]
- If we `only` look at the smallest upper bound, i.e the smallest value of all of the hashtables we made for the frequencies, then we will get a `much` smaller amount that we will be off by from the real frequency.
	- note that it states $\leq \frac{1}{2^l}$ not $2^e$.
	- This is because the probability that we are off by $2 \frac{n}{b}=\frac{1}{2}$ (look at the picture above this) so if we do it $l$ times then the probability will become $\frac{1}{2^l}$. 
![[Pasted image 20231122090001.png]]
- This means that we choose $b=\frac{2}{\epsilon}$ many columns for each row, or b is the size of the hashtables
- $\delta$ will be the number of hashfucntions, i.e the number of rows.
![[Pasted image 20231122091050.png]]
This is just what was stated before, how many counters we have.
- again, the number of counters does not depend of `n`.
![[Pasted image 20231122091416.png]]
- the probability that the lowest upperbound (lowest frequency in the cells which the value was hashed to) is more than $0.1\%$ of all `n` values, is less than $1\%$. Which is a very good estimate.
	- We can calculate $b$ from this, as $b=\frac{2}{\epsilon}$ and $l=\log\left( \frac{1}{\delta} \right)$


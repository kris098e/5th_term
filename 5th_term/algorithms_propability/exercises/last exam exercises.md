[[NB_NOT_THIS_YEARS_EXAM_PROBLEMS_exopg22.1.pdf]]
# 1
- Use the pigeon hole principle
- associate two numbers with each house ($F_{i}, D_{i}$). If one of the are 6, then we have proved it
		- assume $D_{i}, I_{i} \leq 5\ for\ i=1,2,3\dots 26$ This we can then prove D by contradiction
			- because 5\*5 < 26:
	- there must exist an $i,j$ where $i\neq j,\ D_{i}=D_{j}$ and $I_{i}=I_{j}$
	- assume $i<j$ 
Either one of the sequences must be at least 6,

# Problem 2
a. ${12\choose 6}{8\choose 4}$
may have to divide by 2?
b. Arrangements: $8\choose 4$, we then have 4 people to arrange which is $4!$ ways but we have to divide by 4 at is 4 rotation options around the table. We also have to do this for the other table, i.e we have $\left( \frac{4!}{3!} \right)^2$. As we can distuingish the two tables from eachother we divide by two $\frac{{8\choose 4}}{2}$. To this $\left( \frac{4!}{3!} \right)^2$ we have to add $\left( \frac{4!}{3!*2} \right)^2$ as the 2 will ensure that we dont just have any vertical/horizontal flips
We end up with $$\frac{{8\choose 4}}{2}\left( \frac{4!}{4*2} \right)^2$$
c.
stars and bars, fix 4 men as one man has to sit between 2 women. What we have left to choose is 2, and this is out of 5, as we have $n=4-1+2$ 3 bars as the seperators. We do this for each of the tables, so to the power of 2
![[Pasted image 20231002144809.png]]

# problem 3
a. we dont care about the letters which are not in both of the words. Because this is 0 chance of getting it.
probability for E: $\frac{2}{17}* \frac{3}{10}$
For N" $\frac{1}{17} * \frac{1}{10}$ we plus them together

it is basically the fact that we have two independent events, so we multiply the probabilities together. Since they are disjoint, we can add the probability for the others to get the entire summation

b.
$\frac{17!}{2!2!2!2!2!3!}$
# Problem 4
![[Pasted image 20231002150558.png]]
$\sum_{i=1}^{6}\sum_{j=1}^6$
# Problem 8
![[Pasted image 20231002153854.png]]
A. when does an edge come inside of the edge-mængde
If two knots have the same same coloring, if one of them just arrives, the probability that it gets the same coloring as the other 1 is $\frac{1}{k}$. The probability that they dont get the same coloring is the $1-\frac{1}{k}$. Meaning it is precisely $\frac{k-1}{k}$

B. 
p(X=1)=$\frac{k-1}{k}$
$E(X_{e})=1p(X_{e}=1)0p(X_{e}=0)=\frac{k-1}{k}$
C. 

D. ss 
E. comes down to proving that if we take all of the instances in the space, then it does not make sense than none of these instances live up to the average. Because this would mean that the average would be lower
![[Pasted image 20231002154909.png]]

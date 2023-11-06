# Random variables and K-sat
![[Pasted image 20231103081417.png]]
The probability of satisfying a clause with just a single variable is $\frac{1}{2}$. The probability of satisfying a clause with 2 variables i $1-\left( \frac{1}{2} \right)^2=\frac{3}{4}$. Just will just continue to increase, up to the maximum size of $k=n$ meaning the probability of satisfying the biggest clause with `k` variables will be $1-\left( \frac{1}{2} \right)^k=\frac{2^k-1}{2^k}$. Thereby we see that the probability of satisfying a clause with only 1 variable will have the smallest probability.
Since we have `k` clauses and can use a random indicator variable, being `1` if the clause $i\in\{1,2\dots k\}$ is satisfied. We use linerarity of expectation and get
$$E(X)=E\left(\sum_{i=1}^kX_{i} \right)=\sum_{i=1}^n(X_{i})=\sum_{i=1}^{n}{\frac{1}{2}}=\frac{k}{2}$$
example: $x_{1}\cap!x_{1}$ can only satisfy half
![[Pasted image 20231103081427.png]]
![[Pasted image 20231103081437.png]]
- if $x_{i}$ appear alone, then the probability of the variable being true is $p=\frac{6}{10}$ if $x_{i}$ is a clause. Also if it were negated, we would set it to false with the probability $p=\frac{6}{10}$
$E(x_{i})=\frac{6}{10}$ if $l_{i}=1$ i.e how many variables are inside the clause
the worst thing that can happen is that we have the negated form in the same clauses. fx $x_{1}\cap x_{2}\cap(!x_{1}\cup !x_{2})$
therefore the $E(x_{i})=\frac{6}{10}=1-\left( \frac{4}{10} \right)^{l_{i}}>0.6$.
![[Pasted image 20231103081446.png]]

# Rekursionsligninger
![[Pasted image 20231103082914.png]]
## a
![[Pasted image 20231012130335.png]]
have the equation $$r^n=6r^{n-1}-8r^{n-2}$$
divide by $r^{n-2}$
$$r^2=6r^1-8$$
$$r^2-6r^1+8=0$$
solve: 
$$r=7.123105626, -1.123105626$$
so 
$$a_{n}=\alpha_{1}7.12^n+\alpha_{2}(-1.12)^n$$
Now we find alpha
$$\alpha_{1}=\frac{24-4 \cdot(-1.12)}{7.12-(-1.12)}=3.456$$
$$\alpha_{2}=\frac{24-4 \cdot 7.12}{-1.12-7.12}=0.544$$
thereby
$$a_{n}=3.456 \cdot 7.12^{n}+0.544 \cdot (-1.12)^n$$
## b
LISTEN CAREFULLY, dont know how to solve
# Rekursionsligninger

![[Pasted image 20231103090018.png]]
$$r^n=2r^{n-1}+3r^{n-2}$$
divide by $r^{n-2}$
$$r^2=2r^1+3$$
set equation = 0
$$r^2-2r-3=0$$
solve
$$r_{1}=3, r_{2}=-1$$
have the equation
$$a_{n}=\alpha_{1}3^n+\alpha_{2}(-1)^n$$
solve the alphas
$$\alpha_{1} =\frac{1-1 \cdot (-1)}{3-(-1)}=\frac{2}{4}=\frac{1}{2}$$
$$\alpha_{2}=\frac{1-1 \cdot 3}{-1-3}=\frac{-2}{-4}=\frac{1}{2}$$
therefore
$$a_{n}=\frac{3^n}{2}+\frac{(-1)^n}{2}$$

![[Pasted image 20231103091834.png]]
have the equation
$$r^n=4r^{n-1}-4r^{n-2}$$
divide by $r^{n-2}$ and set equal to 0
$$r^2-4r^{1}+4=0$$
$$r_{1},r_{2}=2$$
have the equation
$$a_{n}=\alpha_{1}2^n+\alpha_{2}+2^n$$
but since the root is `2`, when solving for alpha, we will end up dividing by 0.
![[Pasted image 20231103102625.png]]
$\alpha_{1}=C_{0}=1$
$C_{1}=1 \cdot 2+2 \cdot \alpha_{2}=4$
$\alpha_{2}=\frac{2}{2}=1$
the equation is then
$$a_{n}=2^{n}+n \cdot 2^n$$


![[Pasted image 20231103092414.png]]
**Listen closely**

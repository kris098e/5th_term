$$V(X)=\sum\limits_{s \in S}p(s)(X(s)-E(X))^2$$
$$V(X)=\sum\limits_{s \in S} X(s)^{2}p(s)-2E(X)\sum\limits_{s \in S}X(s)p(s)+E(X) \sum\limits_{s \in S}p(s)$$
$$V(X)=E(X^{2})-2E(X)E(X)+E(X)=E(X^{2})-E(X)^{2}$$

# prove markov
$$\frac{E(X)}{a} \geq p(X(s) \geq a)$$
$$E(X)= \sum\limits_{s \in S}p(s)X(s)$$
let $A=\{s | \ X(s) \geq a\}$
$$E(X)=\sum\limits_{s \in A} p(s)X(s) + \sum\limits_{s \notin A}p(s) X(s)$$
$$\geq \sum\limits_{s \in A} p(s)a + 0=p(A)a$$
$$\frac{E(X)}{a}\geq p(A)=p(X(s \geq a))$$

# Prove Chebyshev
$$p(|X(s)-E(X)|\geq r)\leq \frac{V(X)}{r^2}$$
$$V(X)=\sum\limits_{s \in S} p(s)(X(s)-E(X))^2$$
let $A=\{s| |X(s)-E(X)|\geq r \}$
$$V(X)= \sum\limits_{s \in A}p(s)(X(s)-E(X))^{2}+\sum\limits_{s \notin A} p(s)(X(s)-E(X))^{2}$$
$$(X(s)-E(X))^{2} \geq r^{2}$$
$$V(X)\geq r^{2}\sum\limits_{s \in A}p(s)=r^{2}p(A)=r^{2}p(|X(s)-E(X)| \geq r) \implies \frac{V(X)}{r^{2}} \geq p(|X(s)-E(X)| \geq r)$$


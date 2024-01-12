Bruges til at finde heavy hitters i et uendeligt langt input. Lav en $l \times b$ matrix **M**. Hver row har sin egen hash function, som er randomly valgt ud fra en familie af universelle hashfunctions $U \to [b]$. Flow er så når man møder et input, kører man hashfunktionen på alle rækker og addere til counteren hvor dette input bliver hashet til.\\
**Eksempel?**\\
Anerkend at selvom man har et uendeligt input, så bruger man altid den samme mængde plads. Altid $l \times b$. Der kommer til at være clashes i counterne, så counterne i cellerne er kun en upper bound for hvor mange gange input bliver mødt. \\
Vi kigger vil nu, ved at bruge en probabalistic approach, kigge på hvad den forventede mængde clashes vi har er. Definer random indicator variable $I_{i,x}(y)$ som er $1$ hviss $h_{i}(x)=h_{i}(y)$ ellers 0. Hvor $h_{i}$ er den universelle hashfunktion $i$ ved række $i$. Da vi bruger en universal hashfunction, er sandsynligheden for to forskellige input clasher $p(I_{i,x}(y)=1)\leq \frac{1}{b}$. Det betyder at counteren i celle $i$ er
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

$$p(X > (1+\delta)\mu) < \left( \frac{e^{\delta}}{(1+\delta)^{1+\delta}} \right)^{\mu}$$
$$p(X < (1-\delta)\mu ) < e^{\frac{1}{2} \mu \delta^2}$$



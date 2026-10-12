# Section 1.3: Efficient quantum algorithms [PDF Pages 5-6]

<!-- ============================================================ -->
<!-- Source: chap1.pdf, Physical Pages: 5-6                       -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 5 -->
## 1.3 Efficient quantum algorithms

Given that quantum information has many unusual properties, it might have been expected that quantum theory would have a profound impact on our understanding of computation. That this is spectacularly true came to many of us as a bolt from the blue unleashed by Peter Shor (an AT&T computer scientist and a former Caltech undergraduate) in April, 1994. Shor demonstrated that, at least in principle, a quantum computer can *factor* a large number efficiently.

Factoring (finding the prime factors of a composite number) is an example of an *intractable* problem with the property:

- The solution can be *easily verified*, once found.
- But the solution is *hard* to find.

That is, if $p$ and $q$ are large prime numbers, the product $n = pq$ can be computed quickly (the number of elementary bit operations required is about $\log_2 p \cdot \log_2 q$). But given $n$, it is *hard* to find $p$ and $q$.

The time required to find the factors is strongly believed (though this has never been proved) to be *superpolynomial* in $\log(n)$. That is, as $n$ increases, the time needed in the worst case grows faster than any power of $\log(n)$. The

<!-- Page 6 -->
best known factoring algorithm (the “number field sieve”) requires
$$
\text{time} \simeq \exp[c(\ln n)^{1/3}(\ln\ln n)^{2/3}]
$$ {#eq-1.3}
where $c = (64/9)^{1/3} \sim 1.9$. The current state of the art is that the 65 digit factors of a 130 digit number can be found in the order of one month by a network of hundreds of work stations. Using this to estimate the prefactor in Eq. 1.3, we can estimate that factoring a 400 digit number would take about $10^{10}$ years, the age of the universe. So even with vast improvements in technology, factoring a 400 digit number will be out of reach for a while.

The factoring problem is interesting from the perspective of complexity theory, as an example of a problem presumed to be intractable; that is, a problem that can’t be solved in a time bounded by a polynomial in the size of the input, in this case $\log n$. But it is also of practical importance, because the difficulty of factoring is the basis of schemes for public key cryptography, such as the widely used RSA scheme.

The exciting new result that Shor found is that a quantum computer can factor in polynomial time, e.g., in time $O[(\ln n)^3]$. So if we had a quantum computer that could factor a 130 digit number in one month (of course we don’t, at least not yet!), running Shor’s algorithm it could factor that 400 digit number in less than 3 years. The harder the problem, the greater the advantage enjoyed by the quantum computer.

Shor’s result spurred my own interest in quantum information (were it not for Shor, I don’t suppose I would be teaching this course). It’s fascinating to contemplate the implications for complexity theory, for quantum theory, for technology.

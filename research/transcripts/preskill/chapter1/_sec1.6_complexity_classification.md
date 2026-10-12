# Section 1.6: A new classification of complexity [PDF Pages 13-15]

<!-- ============================================================ -->
<!-- Source: chap1.pdf, Physical Pages: 13-15                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 13 -->
## 1.6 A new classification of complexity

The computer on your desktop is not a quantum computer, but still it is a remarkable device: in principle, it is capable of performing any conceivable computation. In practice there are computations that you can’t do — you either run out of time or you run out of memory. But if you provide an unlimited amount of memory, and you are willing to wait as long as it takes, then anything that deserves to be called a computation can be done by your little PC. We say, therefore, that it is a “universal computer.”

Classical complexity theory is the study of which problems are hard and which ones are easy. Usually, “hard” and “easy” are defined in terms of how much time and/or memory are needed. But how can we make meaningful

<!-- Page 14 -->
distinctions between hard and easy without specifying the hardware we will be using? A problem might be hard on the PC, but perhaps I could design a special purpose machine that could solve that problem much faster. Or maybe in the future a much better general purpose computer will be available that solves the problem far more efficiently. Truly meaningful distinctions between hard and easy should be *universal* — they ought not to depend on which machine we are using.

Much of complexity theory focuses on the distinction between “polynomial time” and “exponential time” algorithms. For any algorithm $A$, which can act on an input of variable length, we may associate a *complexity function* $T_A(N)$, where $N$ is the length of the input in bits. $T_A(N)$ is the longest “time” (that is, number of elementary steps) it takes for the algorithm to run to completion, for any $N$-bit input. (For example, if $A$ is a factoring algorithm, $T_A(N)$ is the time needed to factor an $N$-bit number in the worst possible case.) We say that $A$ is polynomial time if
$$
T_A(N) \le \text{Poly}(N),
$$ {#eq-1.16}
where $\text{Poly}(N)$ denotes a polynomial of $N$. Hence, polynomial time means that the time needed to solve the problem does not grow faster than a power of the number of input bits.

If the problem is not polynomial time, we say it is exponential time (though this is really a misnomer, because of course that are superpolynomial functions like $N^{\log N}$ that actually increase much more slowly than an exponential). This is a reasonable way to draw the line between easy and hard. But the truly compelling reason to make the distinction this way is that it is machine-independent: it does not matter what computer we are using. The universality of the distinction between polynomial and exponential follows from one of the central results of computer science: one universal (classical) computer can simulate another with at worst “polynomial overhead.” This means that if an algorithm runs on your computer in polynomial time, then I can always run it on my computer in polynomial time. If I can’t think of a better way to do it, I can always have my computer emulate how yours operates; the cost of running the emulation is only polynomial time. Similarly, your computer can emulate mine, so we will always agree on which algorithms are polynomial time.[^3]

[^3]: To make this statement precise, we need to be a little careful. For example, we should exclude certain kinds of “unreasonable” machines, like a parallel computer with an unlimited number of nodes.

<!-- Page 15 -->
Now it is true that information and computation in the physical world are fundamentally quantum mechanical, but this insight, however dear to physicists, would not be of great interest (at least from the viewpoint of complexity theory) were it possible to simulate a quantum computer on a classical computer with polynomial overhead. Quantum algorithms might prove to be of technological interest, but perhaps no more so than future advances in classical algorithms that might speed up the solution of certain problems.

But if, as is indicated (but not proved!) by Shor’s algorithm, no polynomial-time simulation of a quantum computer is possible, that changes everything. Thirty years of work on complexity theory will still stand as mathematical truth, as theorems characterizing the capabilities of classical universal computers. But it may fall as physical truth, because a classical Turing machine is not an appropriate model of the computations that can really be performed in the physical world.

If the quantum classification of complexity is indeed different than the classical classification (as is suspected but not proved), then this result will shake the foundations of computer science. In the long term, it may also strongly impact technology. But what is its significance for physics?

I’m not sure. But perhaps it is telling that no conceivable classical computation can accurately predict the behavior of even a modest number of qubits (of order 100). This may suggest that relatively small quantum systems have greater potential than we suspected to surprise, baffle, and delight us.

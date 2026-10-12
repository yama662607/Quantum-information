# Section 5.1: Classical Circuits [PDF Pages 3-13]

<!-- ============================================================ -->
<!-- Source: chap5.pdf, Physical Pages: 3-13                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 3 -->
# 5 Classical and quantum circuits

## 5.1 Classical Circuits

The concept of a quantum computer was introduced in Chapter 1. Here we will specify our model of quantum computation more precisely, and we will point out some basic properties of the model; later we will investigate the power of the model. But before we explain what a quantum computer does, we should say what a classical computer does.

### 5.1.1 Universal gates

A (deterministic) classical computer evaluates a function: given $n$-bits of input it produces $m$-bits of output that are uniquely determined by the input; that is, it finds the value of the function
$$
f : \{0, 1\}^n \to \{0, 1\}^m,
$$ {#eq-5.1}
for a particular specified $n$-bit argument $x$. A function with an $m$-bit output is equivalent to $m$ functions, each with a one-bit output, so we may just as well say that the basic task performed by a computer is the evaluation of
$$
f : \{0, 1\}^n \to \{0, 1\}.
$$ {#eq-5.2}
A function taking an $n$-bit input to a one-bit output is called a Boolean function. We may think of such a function as a binary string of length $2^n$, where each bit of the string is the output $f(x)$ for one of the $2^n$ possible values of the input $x$. Evidently, there are $2^{2^n}$ such strings; that's a lot of functions! Already for $n = 5$ there are $2^{32} \approx 4.3 \times 10^9$ Boolean functions — you've encountered only a tiny fraction of these in your lifetime.

<!-- Page 4 -->
It is sometimes useful to regard a Boolean function as a subset $\Sigma$ of the $n$-bit strings containing those values of the input $x$ such that $f(x) = 1$; we say these strings are "accepted" by $f$. The complementary set $\bar{\Sigma}$ contains values of $x$ such that $f(x) = 0$, which we say are "rejected" by $f$.

The evaluation of a Boolean function $f$ can be reduced to a sequence of simple logical operations. To see how, denote the $n$-bit strings accepted by $f$ as $\Sigma = \{x^{(1)}, x^{(2)}, x^{(3)}, \dots\}$ and note that for each $x^{(a)}$ we can define a function $f^{(a)} : \{0, 1\}^n \to \{0, 1\}$ such that
$$
f^{(a)}(x) = \begin{cases} 1 & x = x^{(a)} \\ 0 & \text{otherwise} \end{cases}
$$ {#eq-5.3}
Then $f$ can be expressed as
$$
f(x) = f^{(1)}(x) \vee f^{(2)}(x) \vee f^{(3)}(x) \vee \dots,
$$ {#eq-5.4}
the logical OR ($\vee$) of all the $f^{(a)}$'s. In binary arithmetic the $\vee$ operation of two bits may be represented
$$
x \vee y = x + y - x \cdot y;
$$ {#eq-5.5}
it has the value 0 if $x$ and $y$ are both zero, and the value 1 otherwise.

Now consider the evaluation of $f^{(a)}$. We express the $n$-bit string $x$ as
$$
x = x_{n-1} x_{n-2} \dots x_2 x_1 x_0.
$$ {#eq-5.6}
In the case where $x^{(a)} = 11\dots 111$, we may write
$$
f^{(a)}(x) = x_{n-1} \wedge x_{n-2} \wedge \dots \wedge x_2 \wedge x_1 \wedge x_0;
$$ {#eq-5.7}
it is the logical AND ($\wedge$) of all $n$ bits. In binary arithmetic, the AND is the product
$$
x \wedge y = x \cdot y.
$$ {#eq-5.8}
For any other $x^{(a)}$, $f^{(a)}$ is again obtained as the AND of $n$ bits, but where the NOT ($\neg$) operation is first applied to each $x_i$ such that $x_i^{(a)} = 0$; for example
$$
f^{(a)}(x) = \dots (\neg x_3) \wedge x_2 \wedge x_1 \wedge (\neg x_0)
$$ {#eq-5.9}
if
$$
x^{(a)} = \dots 0110.
$$ {#eq-5.10}
The NOT operation is represented in binary arithmetic as
$$
\neg x = 1 - x.
$$ {#eq-5.11}

We have now constructed the function $f(x)$ from three elementary logical connectives: NOT, AND, OR. The expression we obtained is called the "disjunctive normal form" (DNF) of $f(x)$. We have also implicitly used another operation $\text{INPUT}(x_i)$, which inputs the $i$th bit of $x$.

<!-- Page 5 -->
These considerations motivate the circuit model of computation. A computer has a few basic components that can perform elementary operations on bits or pairs of bits, such as NOT, AND, OR. It can also input a variable bit or prepare a constant bit. A computation is a finite sequence of such operations, a *circuit*, applied to a specified string of input bits. Each operation is called a *gate*. The result of the computation is the final value of all remaining bits, after all the elementary operations have been executed. For a Boolean function (with a one-bit output), if there are multiple bits still remaining at the end of the computation, one is designated as the output bit. A circuit can be regarded as a directed acyclic graph, where each vertex in the graph is a gate, and the directed edges indicate the flow of bits through the circuit, with the direction specifying the order in which gates are applied. By acyclic we mean that no directed closed loops are permitted.

We say that the gate set $\{\text{NOT}, \text{AND}, \text{OR}, \text{INPUT}\}$ is "universal," meaning that any function can be evaluated by building a circuit from these components. It is a remarkable fact about the world that an arbitrary computation can be performed using such simple building blocks.

### 5.1.2 Most functions require large circuits

Our DNF construction shows that any Boolean function with an $n$-bit input can be evaluated using no more than $2^n$ OR gates, $n 2^n$ AND gates, $n 2^n$ NOT gates, and $n 2^n$ INPUT gates, a total of $(3n + 1)2^n$ gates. Of course, some functions can be computed using much smaller circuits, but for *most* Boolean functions the smallest circuit that evaluates the function really does have an exponentially large (in $n$) number of gates. The point is that if the circuit size (i.e., number of gates) is subexponential in $n$, then there are many, many more functions than circuits.

How many circuits are there with $G$ gates acting on an $n$-bit input? Consider the gate set from which we constructed the DNF, where we will also allow inputting of a constant bit (either 0 or 1) in case we want to use some scratch space when we compute. Then there are $n + 5$ different gates: NOT, AND, OR, $\text{INPUT}(0)$, $\text{INPUT}(1)$, and $\text{INPUT}(x_i)$ for $i = 0, 1, 2, \dots n - 1$. Each two-qubit gate acts on a pair of bits which are outputs from preceding gates; this pair can be chosen in fewer than $G^2$ ways. Therefore the total number of size-$G$ circuits can be bounded as
$$
N_{\text{circuit}}(G) \le \left((n + 5)G^2\right)^G.
$$ {#eq-5.12}

<!-- Page 6 -->
If $G = c\frac{2^n}{2n}$, where $c$ is a constant independent of $n$, then
$$
\begin{aligned}
\log_2 N_{\text{circuit}}(G) &\le G (\log_2(n + 5) + 2\log_2 G) \\
&= c 2^n \left(1 + \frac{1}{2n}\log_2\left(\frac{c^2(n + 5)}{4n^2}\right)\right) \le c 2^n,
\end{aligned}
$$ {#eq-5.13}
where the second inequality holds for $n$ sufficiently large. Comparing with the number of Boolean functions, $N_{\text{function}}(n) = 2^{2^n}$, we find
$$
\log_2\left(\frac{N_{\text{circuit}}(G)}{N_{\text{function}}(n)}\right) \le (c - 1)2^n
$$ {#eq-5.14}
for $n$ sufficiently large. Therefore, for any $c < 1$, the number of circuits is smaller than the number of functions by a huge factor. We did this analysis for one particular universal gate set, but the counting would not have been substantially different if we had used a different gate set instead.

We conclude that for any positive $\varepsilon$, then, most Boolean functions require circuits with at least $(1 - \varepsilon)\frac{2^n}{2n}$ gates. The circuit size is so large because most functions have no structure that can be exploited to construct a more compact circuit. We can't do much better than consulting a "look-up table" that stores a list of all accepted strings, which is essentially what the DNF does.

### 5.1.3 Circuit complexity

So far, we have only considered a computation that acts on an input with a fixed ($n$-bit) size, but we may also consider *families* of circuits that act on inputs of variable size. Circuit families provide a useful scheme for analyzing and classifying the *complexity* of computations, a scheme that will have a natural generalization when we turn to quantum computation.

Boolean functions arise naturally in the study of complexity. A Boolean function $f$ may be said to encode a solution to a "decision problem" — the function examines the input and issues a YES or NO answer. Often, what might not be stated colloquially as a question with a YES/NO answer can be "repackaged" as a decision problem. For example, the function that defines the FACTORING problem is:
$$
f(x, y) = \begin{cases} 1 & \text{if integer } x \text{ has a divisor } z \text{ such that } 1 < z < y, \\ 0 & \text{otherwise}; \end{cases}
$$ {#eq-5.15}
knowing $f(x, y)$ for all $y < x$ is equivalent to knowing the *least* nontrivial factor of $x$ (if there is one).

<!-- Page 7 -->
Another example of a decision problem is the HAMILTONIAN PATH problem: let the input be an $\ell$-vertex graph, represented by an $\ell \times \ell$ adjacency matrix ( a 1 in the $ij$ entry means there is an edge linking vertices $i$ and $j$); the function is
$$
f(x) = \begin{cases} 1 & \text{if graph } x \text{ has a Hamiltonian path}, \\ 0 & \text{otherwise}. \end{cases}
$$ {#eq-5.16}
A path on the graph is Hamiltonian if it visits each vertex exactly once.

For the FACTORING problem the size of the input is the number of bits needed to specify $x$ and $y$, while for the HAMILTONIAN PATH problem the size of the input is the number of bits needed to specify the graph. Thus each problem really defines a family of Boolean functions with variable input size. We denote such a function family as
$$
f : \{0, 1\}^* \to \{0, 1\},
$$ {#eq-5.17}
where the $*$ indicates that the input size is variable. When $x$ is an $n$-bit string, by writing $f(x)$ we mean the Boolean function in the family which acts on an $n$-bit input is evaluated for input $x$. The set $L$ of strings accepted by a function family
$$
L = \{x \in \{0, 1\}^* : f(x) = 1\}
$$ {#eq-5.18}
is called a *language*.

We can quantify the hardness of a problem by stating how the computational resources needed to solve the problem scale with the input size $n$. In the circuit model of computation, it is natural to use the circuit *size* (number of gates) to characterize the required resources. Alternatively, we might be interested in how much *time* it takes to do the computation if many gates can be executed in parallel; the *depth* of a circuit is the number of time steps required, assuming that gates acting on distinct bits can operate simultaneously (that is, the depth is the maximum length of a directed path from the input to the output of the circuit). The *width* of a circuit, the maximum number of gates (including identity gates acting on "resting" bits) that act in any one time step, quantifies the storage space used to execute the computation.

We would like to divide the decision problems into two classes: easy and hard. But where should we draw the line? For this purpose, we consider decision problems with variable input size, where the number of bits of input is $n$, and examine how the size of the circuit that solves the problem scales with $n$.

If we use the scaling behavior of a circuit family to characterize the difficulty of a problem, there is a subtlety. It would be cheating to hide the difficulty of the problem in the *design* of the circuit. Therefore, we should

<!-- Page 8 -->
restrict attention to circuit families that have acceptable "uniformity" properties — it must be "easy" to build the circuit with $n + 1$ bits of input once we have constructed the circuit with an $n$-bit input.

Associated with a family of functions $\{f_n\}$ (where $f_n$ has $n$-bit input) are circuits $\{C_n\}$ that compute the functions. We say that a circuit family $\{C_n\}$ is "polynomial size" if the size $|C_n|$ of $C_n$ grows with $n$ no faster than a power of $n$,
$$
\text{size }(C_n) \le \text{poly}(n),
$$ {#eq-5.19}
where poly denotes a polynomial. Then we define:
$$
\text{P} = \{\text{decision problems solved by polynomial-size uniform circuit families}\}
$$
(P for "polynomial time"). Decision problems in P are "easy." The rest are "hard." Notice that $C_n$ computes $f_n(x)$ for every possible $n$-bit input, and therefore, if a decision problem is in P we can find the answer even for the "worst-case" input using a circuit of size no greater than $\text{poly}(n)$. As already noted, we implicitly assume that the circuit family is "uniform" so that the *design* of the circuit can itself be solved by a polynomial-time algorithm. Under this assumption, solvability in polynomial time by a circuit family is equivalent to solvability in polynomial time by a universal Turing machine.

Of course, to determine the size of a circuit that computes $f_n$, we must know what the elementary components of the circuit are. Fortunately, though, whether a problem lies in P does not depend on what gate set we choose, as long as the gates are universal, the gate set is finite, and each gate acts on a constant number of bits. One universal gate set can *simulate* another efficiently.

The way of distinguishing easy and hard problems may seem rather arbitrary. If $|C_n| \sim n^{1000}$ we might consider the problem to be intractable in practice, even though the scaling is "polynomial," and if $|C_n| \sim n^{\log \log \log n}$ we might consider the problem to be easy in practice, even though the scaling is "superpolynomial." Furthermore, even if $|C_n|$ scales like a modest power of $n$, the constants in the polynomial could be very large. Such pathological cases seem to be uncommon, however. Usually polynomial scaling is a reliable indicator that solving the problem is feasible.

Of particular interest are decision problems that can be answered by exhibiting an example that is easy to verify. For example, given $x$ and $y < x$, it is hard (in the worst case) to determine if $x$ has a factor less than $y$. But if someone kindly provides a $z < y$ that divides $x$, it is easy for us to check that $z$ is indeed a factor of $x$. Similarly, it is hard to determine if a graph has a Hamiltonian path, but if someone kindly provides a path, it is easy to verify that the path really is Hamiltonian.

<!-- Page 9 -->
This concept that a problem may be hard to solve, but that a solution can be easily verified once found, can be formalized. The complexity class of decision problems for which the answer can be checked efficiently, called NP, is defined as

**Definition. NP.** *A language $L$ is in NP iff there is a polynomial-size verifier $V(x, y)$ such that*
*If $x \in L$, then there exists $y$ such that $V(x, y) = 1$ (completeness),*
*If $x \notin L$, then, for all $y$, $V(x, y) = 0$ (soundness).*

The verifier $V$ is the uniform circuit family that checks the answer. Completeness means that for each input in the language (for which the answer is YES), there is an appropriate "witness" such that the verifier accepts the input if that witness is provided. Soundness means that for each input not in the language (for which the answer is NO) the verifier rejects the input no matter what witness is provided. It is implicit that the witness is of polynomial length, $|y| = \text{poly}(|x|)$; since the verifier has a polynomial number of gates, including input gates, it cannot make use of more than a polynomial number of bits of the witness. NP stands for "nondeterministic polynomial time;" this name is used for historical reasons, but it is a bit confusing since the verifier is actually a deterministic circuit (evaluates a function).

It is obvious that $\text{P} \subseteq \text{NP}$; if the problem is in P then the polynomial-time verifier can decide whether to accept $x$ on its own, without any help from the witness. But some problems in NP seem to be hard, and are believed not to be in P. Much of complexity theory is built on a fundamental conjecture:
$$
\text{Conjecture : } \text{P} \neq \text{NP}.
$$ {#eq-5.20}
Proving or refuting this conjecture is the most important open problem in computer science, and one of the most important problems in mathematics.

Why should we believe $\text{P} \neq \text{NP}$? If $\text{P} = \text{NP}$ that would mean we could easily find the solution to any problem whose solution is easy to check. In effect, then, we could automate creativity; in particular, computers would be able to discover all the mathematical theorems which have short proofs. The conjecture $\text{P} \neq \text{NP}$ asserts that our machines will never achieve such awesome power — that the mere existence of a succinct proof of a statement does not ensure that we can find the proof by any systematic procedure in any reasonable amount of time.

An important example of a problem in NP is CIRCUIT-SAT. In this case the input is a Boolean circuit $C$, and the problem is to determine

<!-- Page 10 -->
whether any input $x$ is accepted by $C$. The function to be evaluated is
$$
f(C) = \begin{cases} 1 & \text{if there exists } x \text{ with } C(x) = 1, \\ 0 & \text{otherwise}. \end{cases}
$$ {#eq-5.21}
This problem is in NP because if the circuit $C$ has polynomial size, then if we are provided with an input $x$ accepted by $C$ it is easy to check that $C(x) = 1$.

The problem CIRCUIT-SAT is particularly interesting because it has a remarkable property — if we have a machine that solves CIRCUIT-SAT we can use it to solve any other problem in NP. We say that every problem in NP is (efficiently) *reducible* to CIRCUIT-SAT. More generally, we say that problem $B$ reduces to problem $A$ if a machine that solves $A$ can be used to solve $B$ as well.

That is, if $A$ and $B$ are Boolean function families, then "$B$ reduces to $A$" means there is a function family $R$, computed by poly-size circuits, such that $B(x) = A(R(x))$. Thus $B$ accepts $x$ iff $A$ accepts $R(x)$. In particular, then, if we have a poly-size circuit family that solves $A$, we can hook $A$ up with $R$ to obtain a poly-size circuit family that solves $B$.

A problem $B$ in NP reduces to CIRCUIT-SAT because problem $B$ has a poly-size verifier $V(x, y)$, such that $B$ accepts $x$ iff there exists some witness $y$ such that $V$ accepts $(x, y)$. For each fixed $x$, asking whether such a witness $y$ exists is an instance of CIRCUIT-SAT. So a poly-size circuit family that solves CIRCUIT-SAT can also be used to solve problem $B$.

We say a problem $A$ in NP is *NP-complete* if every problem in NP is reducible to $A$. Hence, CIRCUIT-SAT is NP-complete. The NP-complete problems are the "hardest" problems in NP, in the sense that if we can solve any NP-complete problem then we can solve every NP problem. Furthermore, to show that problem $A$ is NP-complete, it is enough to show that $B$ reduces to $A$ where $B$ is NP-complete. If $C$ is any problem in NP and $B$ is NP-complete then there is a poly-size reduction $R$ such that $C(x) = B(R(x))$, and if $B$ is reducible to $A$ then there is another poly-size reduction $R'$ such that $B(y) = A(R'(y))$. Hence $C(x) = A(R'(R(x)))$, and since the composition $R' \circ R$ of two poly-size reductions is also poly-size, we see that an arbitrary problem $C$ in NP reduces to $A$, and therefore $A$ is NP-complete. NP-completeness is a useful concept because hundreds of "natural" computational problems turn out to be NP-complete. For example, one can exhibit a polynomial reduction of CIRCUIT-SAT to HAMILTONIAN PATH, and it follows that HAMILTONIAN PATH is also NP-complete.

Another noteworthy complexity class is called co-NP. While NP problems can be decided by exhibiting an *example* if the answer is YES, co-NP

<!-- Page 11 -->
problems can be answered by exhibiting a *counter-example* if the answer is NO. More formally:

**Definition. co-NP.** *A language $L$ is in co-NP iff there is a polynomial-size verifier $\bar{V}(x, y)$ such that*
*If $x \notin L$, then there exists $y$ such that $\bar{V}(x, y) = 1$,*
*If $x \in L$, then, for all $y$, $\bar{V}(x, y) = 0$.*

For NP the witness $y$ testifies that $x$ is in the language while for co-NP the witness testifies that $x$ is *not* in the language. Thus if language $L$ is in NP, then its complement $\bar{L}$ is in co-NP and vice-versa. We see that whether we consider a problem to be in NP or in co-NP depends on how we choose to frame the question — while "Is there a Hamiltonian path?" is in NP, the complementary question "Is there no Hamiltonian path?" is in co-NP.

Though the distinction between NP and co-NP may seem arbitrary, it is nevertheless interesting to ask whether a problem is in *both* NP and co-NP. If so, then we can easily verify the answer (once a suitable witness is in hand) regardless of whether the answer is YES or NO. It is believed (though not proved) that $\text{NP} \neq \text{co-NP}$. For example, we can show that a graph has a Hamiltonian path by exhibiting an example, but we don't know how to show that it has *no* Hamiltonian path that way!

If we assume that $\text{P} \neq \text{NP}$, it is known that there exist problems in NP of intermediate difficulty (the class NPI), which are neither in P nor NP-complete. Furthermore, assuming that $\text{NP} \neq \text{co-NP}$, it is known that no co-NP problems are NP-complete. Therefore, problems in the intersection of NP and co-NP, if not in P, are good candidates for inclusion in NPI.

In fact, a problem in $\text{NP} \cap \text{co-NP}$ believed not to be in P is the FACTORING problem. As already noted, FACTORING is in NP because, if we are offered a factor of $x$, we can easily check its validity. But it is also in co-NP, because it is known that if we are given a prime number we can efficiently verify its primality. Thus, if someone tells us the prime factors of $x$, we can efficiently check that the prime factorization is right, and can *exclude* that any integer less than $y$ is a divisor of $x$. Therefore, it seems likely that FACTORING is in NPI.

We are led to a crude (conjectured) picture of the structure of $\text{NP} \cup \text{co-NP}$. NP and co-NP do not coincide, but they have a nontrivial intersection. P lies in $\text{NP} \cap \text{co-NP}$ but the intersection also contains problems not in P (like FACTORING). No NP-complete or co-NP-complete problems lie in $\text{NP} \cap \text{co-NP}$.

<!-- Page 12 -->
### 5.1.4 Randomized computation

It is sometimes useful to consider *probabilistic* circuits that have access to a random number generator. For example, a gate in a probabilistic circuit might act in either one of two ways, and flip a fair coin to decide which action to execute. Such a circuit, for a single fixed input, can sample many possible computational paths. An algorithm performed by a probabilistic circuit is said to be "randomized."

If we run a randomized computation many times on the same input, we won't get the same answer every time; rather there is a probability distribution of outputs. But the computation is useful if the probability of getting the right answer is high enough. For a decision problem, we would like a randomized computation to accept an input $x$ which is in the language $L$ with probability at least $\frac{1}{2} + \delta$, and to accept an input $x$ which is not in the language with probability no greater than $\frac{1}{2} - \delta$, where $\delta > 0$ is a constant independent of the input size. In that case we can *amplify* the probability of success by performing the computation many times and taking a majority vote on the outcomes. For $x \in L$, if we run the computation $N$ times, the probability of rejecting in more than half the runs is no more than $e^{-2N\delta^2}$ (the *Chernoff bound*). Likewise, for $x \notin L$, the probability of accepting in the majority of $N$ runs is no more than $e^{-2N\delta^2}$.

Why? There are all together $2^N$ possible sequences of outcomes in the $N$ trials, and the probability of any particular sequence with $N_W$ wrong answers is
$$
\left(\frac{1}{2} - \delta\right)^{N_W} \left(\frac{1}{2} + \delta\right)^{N - N_W}.
$$ {#eq-5.22}
The majority is wrong only if $N_W \ge N/2$, so the probability of any sequence with an incorrect majority is no larger than
$$
\left(\frac{1}{2} - \delta\right)^{N/2} \left(\frac{1}{2} + \delta\right)^{N/2} = \frac{1}{2^N}\left(1 - 4\delta^2\right)^{N/2}.
$$ {#eq-5.23}
Using $1 - x \le e^{-x}$ and multiplying by the total number of sequences $2^N$, we obtain the Chernoff bound:
$$
\text{Prob}(\text{wrong majority}) \le \left(1 - 4\delta^2\right)^{N/2} \le e^{-2N\delta^2}.
$$ {#eq-5.24}
If we are willing to accept a probability of error no larger than $\varepsilon$, then, it suffices to run the computation a number of times
$$
N \ge \frac{1}{2\delta^2}\ln(1/\varepsilon).
$$ {#eq-5.25}

<!-- Page 13 -->
Because we can make the error probability very small by repeating a randomized computation a modest number of times, the value of the constant $\delta$ does not really matter for the purpose of classifying complexity, as long as it is positive and independent of the input size. The standard convention is to specify $\delta = 1/6$, so that $x \in L$ is accepted with probability at least $2/3$ and $x \notin L$ is accepted with probability no more than $1/3$. This criterion defines the class BPP ("bounded-error probabilistic polynomial time") containing decision problems solved by polynomial-size randomized uniform circuit families.

It is clear that BPP contains P, since a deterministic computation is a special case of a randomized computation, in which we never consult the source of randomness. It is widely believed that BPP=P, that randomness does not enhance our computational power, but this has not been proven. It is not even known whether BPP is contained in NP.

We may define a randomized class analogous to NP, called MA ("Merlin-Arthur"), containing languages that can be checked when a randomized verifier is provided with a suitable witness:

**Definition. MA.** *A language $L$ is in MA iff there is a polynomial-size randomized verifier $V(x, y)$ such that*
*If $x \in L$, then there exists $y$ such that $\text{Prob}(V(x, y) = 1) \ge 2/3$,*
*If $x \notin L$, then, for all $y$, $\text{Prob}(V(x, y) = 1) \le 1/3$.*

The colorful name evokes a scenario in which the all-powerful Merlin uses his magical powers to conjure the witness, allowing the mortal Arthur, limited to polynomial time computation, to check the answer. Obviously BPP is contained in MA, but we expect $\text{BPP} \neq \text{MA}$ just as we expect $\text{P} \neq \text{NP}$.

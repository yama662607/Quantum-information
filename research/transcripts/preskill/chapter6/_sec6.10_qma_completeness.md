# Section 6.10: QMA-completeness of the local Hamiltonian problem

## Transcript (English Original)

### 6.10 QMA-completeness of the local Hamiltonian problem [chap6.pdf#page=52]

As we have discussed, we expect that quantum computers can compute the ground state energy of local Hamiltonians in cases where the problem is hard classically; this may be an important application for quantum computers. On the other hand, we believe that in some cases computing the ground state energy of a local Hamiltonian is still hard even for quantum computers. Let us try to understand more deeply the reason for this belief.

Physicists are often interested in translation-invariant geometrically local Hamiltonians, in which all qubits interact in the same way with their neighbors (except for the qubits at the boundary of the sample), because such Hamiltonians provide good models of some real materials. But Hamiltonians that are not translationally invariant are also useful in physics (for example, when modeling a material with "disorder" due to dirt and other imperfections in the sample). If the Hamiltonian is not translation invariant, then we can formulate an instance of an $n$-qubit local Hamiltonian problem by specifying how the Hamiltonian varies from site to site in the system. Physicists sometimes refer to such (not translationally-invariant) systems as spin glasses. Even in the classical case, where the variable at each site is a bit rather than a qubit, finding the ground state energy of a spin glass to constant accuracy can be an NP-hard problem. Therefore, we don't expect classical or quantum computers to be able to solve the problem in general (unless NP is contained in BQP, which seems unlikely).

Let's first understand why the classical spin-glass problem can be NP-hard. Then we'll discuss the hardness of the quantum problem. We'll see that in the quantum case finding the ground state energy of a local Hamiltonian is QMA-hard. (Recall that QMA is the [chap6.pdf#page=53] quantum analogue of NP: the class of problems such that the solution can be verified efficiently with a quantum computer if a suitable "quantum witness" is provided.)

For the classical case, we'll recall the notion of a "reduction" of one computational problem to another ($B$ reduces to $A$ if a machine that solves $A$ can be used to solve $B$), and then we'll consider this sequence of reductions:

1. Any problem in NP reduces to CIRCUIT-SAT (already discussed previously); i.e., CIRCUIT-SAT is NP-complete.
2. CIRCUIT-SAT reduces to 3-SAT (3-SAT is NP-complete).
3. 3-SAT can be formulated as the problem of finding the ground state energy of a classical 3-local Hamiltonian to constant accuracy.
4. MAX 2-SAT is also NP-hard and can be formulated as the problem of finding the ground state energy of a classical 2-local Hamiltonian to constant accuracy.
5. The classical 2-local Hamiltonian problem is still hard in the case where the Hamiltonian is geometrically local, in three or even in two dimensions (cases of interest for describing real spin glasses).

(5) implies that a spin glass will not be able to relax to its ground state efficiently in any realistic physical process (which is part of what physicists mean by the word "glass").

#### 6.10.1 3-SAT is NP-complete [chap6.pdf#page=53]

**Language:** Recall (as discussed earlier) that if $f$ is a uniform family of Boolean functions with variable input size, $f : \{0, 1\}^* \to \{0, 1\}$, then the set of input strings accepted by $f$ is called a language:
$$
L = \{x \in \{0, 1\}^* : f(x) = 1\}
$$ (6.232)

**NP:** We say that a language is in NP if there is a polynomial-size uniform classical circuit family (the verifier $V(x, y)$) such that:
- If $x \in L$, then there exists a witness $y$ such that $V(x, y) = 1$ (completeness).
- If $x \notin L$, then, for all $y$, $V(x, y) = 0$ (soundness).

**Reduction:** We say that $B$ reduces to $A$ if there is a polynomial-size uniform classical circuit family $R$ mapping $x$ to $R(x)$ such that $B$ accepts $x$ if and only if $A$ accepts $R(x)$. This means we can hook up $R$ to a machine that solves $A$ to construct a machine that solves $B$.

An important problem in NP is CIRCUIT-SAT. The input to the problem is a Boolean circuit $C$ (with an $n$-bit input and $G = \mathrm{poly}(n)$ gates), and we are to evaluate the Boolean function $f(C)$, where $f(C) = 1$ if there is an input $x$ such that $C(x) = 1$, $f(C) = 0$ otherwise. CIRCUIT-SAT is in NP because we can simulate the circuit $C$. Given as a witness the value of $x$ that $C$ accepts, we can verify efficiently that $C(x) = 1$. Furthermore, CIRCUIT-SAT is NP-complete (any problem in NP reduces to CIRCUIT-SAT), as we discussed previously. If $V(x, \cdot)$ is the verifier for an NP problem with a fixed instance $x$, we may think of $V(x, \cdot)$ as a circuit whose input is the witness $y$. Solving the CIRCUIT-SAT problem for this Boolean circuit tells us whether there exists a witness that the verifier accepts, and therefore solves the NP problem.

Now we come to a further reduction that we did not discuss previously: CIRCUIT-SAT reduces to 3-SAT, and therefore 3-SAT, too, is an NP-complete problem (the Cook-Levin theorem). For the SAT problem, the input is a "Boolean formula" with $n$ variables, where [chap6.pdf#page=54] each variable is a bit. The formula is a conjunction of clauses, and the formula is true if and only if every clause is true. In the $k$-SAT problem, each clause depends on at most $k$ of the variables, where $k$ is a constant. (In some formulations of $k$-SAT, each clause is required to be a disjunction of $k$ literals (variables or their negations), but that is not an important requirement, since any formula, and in particular any $k$-bit formula, can be expressed in conjunctive normal form.). If $f$ is a Boolean formula, the SAT function is:
$$
\begin{aligned}
\mathrm{SAT}(f) &= 1 \quad \text{if there exists } x \text{ such that } f(x) = 1, \\
\mathrm{SAT}(f) &= 0 \quad \text{otherwise}.
\end{aligned}
$$ (6.233)

Now we'll show that CIRCUIT-SAT reduces to 3-SAT. For a given circuit $C$ (the input to CIRCUIT-SAT), how do we construct the corresponding Boolean formula $R(C)$ (the input to 3-SAT)?

Suppose that the gates in the circuit $C$ are chosen from the universal set (AND, OR, NOT), or any other gate set such that each gate has at most two input bits and one output bit. We introduce a variable for the output of each gate, and we include in the formula $R(C)$ a clause corresponding to each gate.

Here the three-variable clause $C_g(x, y, z)$ is true iff $z$ is a valid output of the gate $g$ when the inputs are $(x, y)$. The circuit may also have inputs that are constants rather than variables. Then, e.g. a gate with two input bits, one of which is a constant, becomes a two-variable clause, determined by the gate and the value of the constant. Or equivalently, we can regard input of a constant as a gate with a one-bit output; the corresponding one-bit clause is true if $x$ has the right value. The circuit also has an answer bit, which becomes a 1-bit clause $C_g(x)$ which is true iff $x = 1$ (that is, if and only if the answer is YES).

The formula $R(C)$ has as variables the input $x$ to the circuit $C$, and also additional variables corresponding to the outputs of all gates in the circuit $C$. $R(C)$ has been constructed so that an assignment that satisfies every clause in $C$ corresponds to a valid history of the computation of the circuit $C$ acting on input $x$, where the input is accepted. If there is an input $x$ that is accepted by the circuit $C$, then there will be a satisfying assignment for the 3-SAT formula $R(C)$, and conversely if there is no input that $C$ accepts, then there will be no satisfying assignment for $R(C)$. Thus we have obtained the desired reduction of CIRCUIT-SAT to 3-SAT.

The key idea we have exploited to reduce CIRCUIT-SAT to 3-SAT is that the witness for 3-SAT is a valid history of the whole computation $C$ that accepts the input $x$. We can check the history efficiently because the circuit $C$ has polynomial size and it is easy to check each of the $\mathrm{poly}(n)$ gates in the execution of the circuit. Later on, we will extend this idea — that a valid history of the computation is an efficiently checkable witness — to the quantum setting.

Notice that we may think of the clauses in the formula $f$ as the terms in a 3-local classical Hamiltonian
$$
H(x) = \sum_c H_c(x_{c1}, x_{c2}, x_{c3});
$$ (6.234)
here the sum is over the clauses in the formula, where
$$
H_c(x_{c1}, x_{c2}, x_{c3}) = \begin{cases}
0 & \text{if clause } c \text{ is true for assignment } x_{c1}, x_{c2}, x_{c3}, \\
1 & \text{otherwise}
\end{cases}
$$ (6.235)

[chap6.pdf#page=55]
Then $\min_x H(x) = 0$ if there is an assignment that satisfies every clause, while $\min_x H(x) \ge 1$ if there is no satisfying assignment (the number of violated clauses is $\ge 1$ for any assignment). We conclude that finding the minimum value of a 3-local classical Hamiltonian is NP-hard: if we could do it we could solve 3-SAT, and hence any problem in NP. This conclusion implies, as asserted earlier, that finding the ground state energy of a 3-local classical Hamiltonian to constant accuracy must be hard in general for quantum computers, too, unless $\mathrm{NP} \subseteq \mathrm{BQP}$.

#### 6.10.2 Frustrated spin glasses [chap6.pdf#page=55]

In fact, finding the ground state energy to constant accuracy is NP-hard even for a 2-local classical Hamiltonian
$$
H(x) = \sum_c H_c(x_{c1}, x_{c2}).
$$ (6.236)
Although 2-SAT (deciding whether a 2-SAT formula can be satisfied) is easy (there is a poly-time algorithm), MAX-2SAT is an NP-hard problem. MAX-2SAT is the problem of finding the minimum number of violated clauses for any assignment, which is equivalent to minimizing the Hamiltonian function $H$.

Furthermore, we can make the 2-local Hamiltonian geometrically local without losing hardness. An example is the Ising spin-glass model in three dimensions. Suppose the binary variables are spins sitting at the sites of a cubic lattice, taking values $Z_i \in \{\pm 1\}$ at site $i$ in the lattice. Consider the Hamiltonian
$$
H = -\sum_{\langle ij\rangle} J_{ij} Z_i Z_j.
$$ (6.237)
Here $\langle ij\rangle$ labels the edge in the lattice that connects two nearest-neighbor sites with labels $i$ and $j$.

$J_{ij} \in \{\pm 1\}$ encodes the instance of the problem. If $J_{ij} = +1$, then we say the edge $\langle ij\rangle$ is ferromagnetic; it is energetically favorable for the neighboring spins to align (both $+1$ or both $-1$). If $J_{ij} = -1$, then we say the edge $\langle ij\rangle$ is anti-ferromagnetic; it is energetically favorable for the neighboring spins to anti-align (either $+1$ and $-1$ or $-1$ and $+1$). If all edges were ferromagnetic, it would be easy to minimize the energy — all spins would align. But anti-ferromagnetic edges can generate frustration. This means it is not possible to minimize $-J_{ij}Z_i Z_j$ for all edges simultaneously.

For purposes of visualization, it is convenient to represent spins by lattice cells — i.e. by squares on the 2D square lattices or by cubes in the 3D cubic lattice. There is a $-J_{ij}Z_i Z_j$ term coupling neighboring spins associated with each edge where two squares meet in 2D on each face where two cubes meet in 3D.

Consider a site in 2D where 4 edges meet. If one of these edges is antiferromagnetic and the other three are ferromagnetic, then there must be an odd number of excited edges meeting at this site. More generally, if the number of antiferromagnetic edges is odd, then there must be an odd number of excited edges and if the number of antiferromagnetic edges is even, then there must be an even number of excited edges. If the number of $J = -1$ edges meeting at a site is odd, we say that there is an Ising vortex at that site. For any spin configuration, there are domain walls of excited edges, where the walls end on Ising vortices.

Minimizing the energy, then, is equivalent in 2D to finding the minimum "chain" of [chap6.pdf#page=56] excited edges with boundary points at the positions of the Ising vortices. There is a poly-time classical algorithm that finds the minimal chain. In 3D, there is an Ising vortex on an edge if there are an odd number of $J = -1$ faces that meet at that edge. These vortices form closed loops, and each spin configuration has a domain wall of excited faces bounded by the vortex loops. To minimize the energy, then, we find the minimum area surface with a specified 1D boundary; this problem is NP-hard. Finding the minimum energy configuration is hard because there are many ways for the domain walls to be "pinned" — stuck at local minima in the energy, such that many spins need to flip at once to find a lower energy configuration. Local searching for the global energy minimum fails.

In fact, there are also NP-hard spin glass problems in 2D, if we introduce local magnetic field terms in $H$ as well as antiferromagnetic terms. For example, on a square lattice consider
$$
H = -\sum_{\langle ij\rangle} J_{ij} Z_i Z_j - \sum_i h_i Z_i
$$ (6.238)
where $J_{ij} \in \{1, 0, -1\}$ and $h_i \in \{1, 0, -1\}$. The local magnetic field $\{h_i\}$ compounds the frustration: Each spin wants to align with the local field, but by doing so the edge connecting the spins might become excited.

So we see that minimizing the energy of a geometrically 2-local classical Hamiltonian can be NP-hard because of frustration — there is no way to satisfy all the clauses and there are many local minima of the energy that are not global minima. In the quantum local Hamiltonian problem, we have $H = \sum_a H_a$ where the $\{H_a\}$ might not be mutually commuting; hence we might expect the problem to be even harder — that the $H_a$'s cannot be simultaneously diagonalized compounds the frustration even further. Indeed the ground state could be highly entangled, with no succinct classical description. Let's try to characterize the hardness of the quantum problem.

#### 6.10.3 The quantum k-local Hamiltonian problem [chap6.pdf#page=56]

Let $H = \sum_a H_a$ be an $n$-qubit Hamiltonian that is $k$-local — each $H_a$ acts nontrivially on at most $k$ qubits, where $k$ is a constant, and $\|H_a\| \le h = \text{constant}$. The $2^k \times 2^k$ matrix $H_a$ is specified to $\mathrm{poly}(n)$ bits of precision.

We are promised that the ground state energy $E_0$, the lowest eigenvalue of $H$, satisfies either
1. $E_0 \le E_{\mathrm{low}}$, or
2. $E_0 > E_{\mathrm{high}}$,
where $E_{\mathrm{high}} - E_{\mathrm{low}} > \frac{1}{\mathrm{poly}(n)}$.

We are to output:
$$
f(H) = \begin{cases}
1 & \text{if } E_0 \le E_{\mathrm{low}}, \\
0 & \text{if } E_0 > E_{\mathrm{high}}.
\end{cases}
$$ (6.239)
Note that in the formulation of the problem, there is a promise gap so that we can answer the YES/NO question by determining $E_0$ to $1/\mathrm{poly}(n)$ accuracy.

We already know that this problem is NP-hard, even in the special case where $H$ is classical (all $H_a$ commute). Also recall there is a class analogous to NP for randomized computation (MA) and quantum computation (QMA): A language $L$ is in QMA if there [chap6.pdf#page=57] exists a poly-size uniform quantum circuit family (the verifier $V$) and a single-qubit measurement $\{\Pi_0, \Pi_1\}$ such that:

1. If $x \in L$ there is a witness $|\psi_x\rangle$ such that:
$$
\langle\Psi|\Pi_1|\Psi\rangle \ge 2/3 \quad \text{where} \quad |\Psi\rangle = V(|\psi_x\rangle \otimes |x\rangle \otimes |0\rangle^*).
$$ (6.240)
2. If $x \notin L$, then $\langle\Psi|\Pi_1|\Psi\rangle \le 1/3$ for all $|\psi_x\rangle$.

We claim: the $k$-local Hamiltonian problem is QMA-complete for $k \ge 5$ (famously proved by Kitaev: see Chap. 14 of KSV). The result can be improved to geometrically 2-local $H$ in 2D (for qubits) or geometrically 2-local $H$ in 1D (for higher dimensional qudits, with the local dimension $d$ sufficiently large).

To verify this claim, we need to show:
1. The $k$-local Hamiltonian problem is in QMA.
2. Any problem in QMA is reducible to the $k$-local Hamiltonian problem. We'll show this for $k = 5$ and without geometrical constraints, as in Kitaev's original discovery.

We have already shown part (1). We have seen that if the ground state $|\psi_0\rangle$ is provided as a witness, then we can compute $E_0$ to $1/\mathrm{poly}(n)$ accuracy using a circuit of size $\mathrm{poly}(n)$ that performs the phase estimation algorithm. But how to achieve the reduction (2)?

For the reduction, we'll follow the strategy used to show that 3-SAT is NP-complete: For any problem in QMA, we'll construct a witness that encodes the whole history of the computation performed by the verifier, and a Hamiltonian $H$ such that computing the ground state energy of $H$ amounts to checking that each step in the computation is valid.

For a given problem in QMA, suppose that the verifier circuit $V_T$ has $T$ gates: $U_1, U_2, \dots U_T$ chosen from a universal set, where each $U_t$ acts on at most two qubits. For the corresponding $k$-local Hamiltonian problem, we'll suppose that Merlin provides the history state encoding the computation performed by the verifier:
$$
|\eta\rangle = \frac{1}{\sqrt{T+1}}\sum_{t=0}^T |\psi(t)\rangle \otimes |t\rangle,
$$ (6.241)
where $|\psi(t)\rangle = (U_t U_{t-1} \dots U_1)|\psi_{\mathrm{initial}}\rangle$; here $|\psi_{\mathrm{initial}}\rangle = |x\rangle \otimes |0\rangle^* \otimes |\psi_x\rangle$, where $|x\rangle$ specifies the instance of the QMA problem, $|0\rangle^*$ is the initial state of scratch space used by the verifier, $|\psi_x\rangle$ is the quantum witness testifying that $x$ should be accepted, and $|\psi(t)\rangle$ is state of the quantum computer obtained after the first $t$ steps of the verifier circuit have been executed. The state $|t\rangle$ is the state of a clock register that records the time $t \in \{0, 1, \dots, T\}$; since $\langle t|s\rangle = \delta_{ts}$, the $T + 1$ states appearing in superposition in state $|\eta\rangle$ are mutually orthogonal, so $|\eta\rangle$ is properly normalized: $\langle\eta|\eta\rangle = 1$.

#### 6.10.4 Constructing and analyzing the Hamiltonian [chap6.pdf#page=57]

Now we want to choose our Hamiltonian $H$ so that it locally "checks" the history encoded in $|\eta\rangle$; that is, $H$ will impose an energetic penalty if a step in the circuit is invalid, or if the input is not accepted.

We will choose $H$ to be of the form
$$
H = H_{\mathrm{in}} + H_{\mathrm{out}} + H_{\mathrm{prop}} + H_{\mathrm{clock}}.
$$ (6.242)

The purpose of $H_{\mathrm{in}}$ is to enforce that the verifier circuit's input qubits (other than the [chap6.pdf#page=58] witness itself) are set to the right initial values. E.g. for each scratch qubit labeled $j$ that should be in the state $|0\rangle$ at time $t = 0$, we include in $H_{\mathrm{in}}$ the term
$$
H_{\mathrm{in}}^{(j)} = (|1\rangle\langle 1|)^{(j)} \otimes I^{(\mathrm{else})} \otimes (|0\rangle\langle 0|)^{(\mathrm{clock})}.
$$ (6.243)
There is an energy penalty of 1 if the scratch qubit is set to $|1\rangle$ rather than $|0\rangle$ as the execution of the verifier circuit begins (time $t = 0$). Similar terms in $H_{\mathrm{in}}$ enforce that the input register is set to the desired value $x$. The purpose of $H_{\mathrm{out}}$ is to impose a penalty if the verifier circuit for the QMA problem fails to accept:
$$
H_{\mathrm{out}} = (|0\rangle\langle 0|)^{(\mathrm{output})} \otimes I^{(\mathrm{else})} \otimes (|T\rangle\langle T|)^{(\mathrm{clock})}.
$$ (6.244)
There is an energy cost of 1 if the output qubit has the value $|0\rangle$ rather than $|1\rangle$ after the verifier circuit is fully executed (time $t = T$). The purpose of $H_{\mathrm{clock}}$ is to impose a penalty if the clock register is not properly encoded (we'll return to this issue later).

The purpose of $H_{\mathrm{prop}}$ is to impose a penalty if the state $|\psi(t)\rangle$ does not have the form $U_t |\psi(t-1)\rangle$; i.e., was not obtained by faithfully executing step $t$ of the verifier circuit. Hence we write:
$$
H_{\mathrm{prop}} = \sum_{t=1}^T H_{\mathrm{prop}}(t),
$$ (6.245)
where
$$
H_{\mathrm{prop}}(t) = \frac{1}{2}\left(I \otimes |t\rangle\langle t| + I \otimes |t-1\rangle\langle t-1| - U_t \otimes |t\rangle\langle t-1| - U_t^\dagger \otimes |t-1\rangle\langle t|\right).
$$ (6.246)
The action of $H_{\mathrm{prop}}(t)$ on the relevant part of the valid history state $|\eta\rangle$ is
$$
\begin{aligned}
|\psi(t-1)\rangle \otimes |t-1\rangle &\mapsto \frac{1}{2}\left(|\psi(t-1)\rangle \otimes |t-1\rangle - U_t|\psi(t-1)\rangle \otimes |t\rangle + \dots\right), \\
|\psi(t)\rangle \otimes |t\rangle &\mapsto \frac{1}{2}\left(|\psi(t)\rangle \otimes |t\rangle - U_t^\dagger|\psi(t)\rangle \otimes |t-1\rangle + \dots\right).
\end{aligned}
$$ (6.247)
Acting on $|\eta\rangle$, the terms $I \otimes |t\rangle\langle t|$ and $-U_t \otimes |t\rangle\langle t-1|$ in $H_{\mathrm{prop}}$ give canceling contributions. Hence
$$
H_{\mathrm{prop}}|\eta\rangle = 0 \quad \text{if } |\eta\rangle \text{ is a valid history state}.
$$ (6.248)
Therefore, a valid history state (where the state at time $t$ is obtained from the state at time $t-1$ by applying the proper gate), such that the initial state is also valid, is a null vector of both $H_{\mathrm{prop}}$ and $H_{\mathrm{in}}$. Furthermore, if the quantum verifier accepts the input with probability $1 - \epsilon$, then
$$
E_0 \le \langle\eta|H_{\mathrm{out}}|\eta\rangle = \frac{\epsilon}{T+1}.
$$ (6.249)
(If the history is valid, the only term in the Hamiltonian that makes a nonzero contribution to $\langle H\rangle$ is the term that penalizes an incorrect final readout.) Note also that it is possible to amplify the success probability by repeating the verification of multiple copies of the witness. Actually, the amplification is a little bit subtle: Merlin might try to fool Arthur: Instead of sending a product state $|\psi_x\rangle^{\otimes m}$ ($m$ copies of the witness) he might send an entangled state instead. But the amplification still works even in that case. Each copy sent by Merlin may be a mixed state (obtained from the partial trace over the other copies), a mixture of a state the verifier accepts with probability $\ge 2/3$ [chap6.pdf#page=59] and of another state that it might reject. But Merlin cannot fool Arthur into accepting after many trials unless there is some state occurring in the ensemble of pure states that is accepted with high probability in each trial.

So now we have seen that for a problem in QMA such that the verifier accepts with high probability, the corresponding Hamiltonian $H$ has an eigenvector with eigenvalue close to zero. There are two things left to show:

- If the verifier rejects with high probability, then
$$
E_0 \ge 1/\mathrm{poly}(n)
$$ (6.250)
(then we can choose the promise gap of size $1/\mathrm{poly}(n)$, such that $E_0 \le E_{\mathrm{low}}$ for a YES answer and $E_0 > E_{\mathrm{high}}$ for a NO answer)
- So far $H_{\mathrm{prop}}$ is not local! It acts on the clock register, which is a $(T+1)$-dimensional system, and $T = \mathrm{poly}(n)$. We need to show we can encode the clock using qubits such that $H_{\mathrm{prop}} + H_{\mathrm{clock}}$ is $k$-local.

We'll come back to the issue of encoding the clock later. First let's try to understand better the spectrum of $H = H_{\mathrm{in}} + H_{\mathrm{out}} + H_{\mathrm{prop}}$.

#### Diagonalizing $H_{\mathrm{prop}}$ [chap6.pdf#page=59]

Let's start by considering $H_{\mathrm{prop}}$. We've seen that a valid history state is a null vector of $H_{\mathrm{prop}}$ (has eigenvalue zero). What are the other eigenspaces and eigenvalues of $H_{\mathrm{prop}}$?

It's easier to compute the spectrum of $H_{\mathrm{prop}}$ by transforming to a rotating frame basis that freezes the motion of the state $|\psi(t)\rangle$. That is, let
$$
V_t = U_t U_{t-1} \dots U_1
$$ (6.251)
(the unitary applied after the first $t$ steps of the circuit). And consider $V = \sum_{t=0}^T V_t \otimes |t\rangle\langle t|$. Then the history state $|\eta\rangle = \frac{1}{\sqrt{T+1}}\sum_{t=0}^T V_t|\psi(0)\rangle \otimes |t\rangle$ is mapped by $V^\dagger$ to the "history" state for the case where $|\psi(t)\rangle$ does not depend on $t$ at all:
$$
V^\dagger|\eta\rangle = \frac{1}{\sqrt{T+1}}\sum_{t=0}^T V_t^\dagger V_t |\psi(0)\rangle \otimes |t\rangle = |\psi(0)\rangle \otimes \frac{1}{\sqrt{T+1}}\sum_{t=0}^T |t\rangle.
$$ (6.252)
Under this basis change, the Hamiltonian transforms as
$$
\begin{aligned}
H'_{\mathrm{prop}} = V^\dagger H_{\mathrm{prop}} V &= \sum_{t=1}^T \frac{1}{2}(I \otimes |t\rangle\langle t| + I \otimes |t-1\rangle\langle t-1|) \\
&\quad - \sum_{t=1}^T \frac{1}{2}(V_t^\dagger U_t V_{t-1} \otimes |t\rangle\langle t-1| + V_{t-1}^\dagger U_t^\dagger V_t \otimes |t-1\rangle\langle t|) \\
&= \sum_{t=1}^T \frac{1}{2}(|t\rangle\langle t| + |t-1\rangle\langle t-1| - |t\rangle\langle t-1| - |t-1\rangle\langle t|).
\end{aligned}
$$ (6.253)
This transformed Hamiltonian $H'_{\mathrm{prop}}$ acts nontrivially only on the clock register. It is a sum of overlapping $2 \times 2$ blocks:
$$
H'_{\mathrm{prop}} = \sum_{t=1}^T \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ -\frac{1}{2} & \frac{1}{2} \end{pmatrix}_{t-1, t},
$$ (6.254)
where the subscript means the matrix acts on the space spanned by $\{|t-1\rangle, |t\rangle\}$. Because [chap6.pdf#page=60] of the overlaps, $H'_{\mathrm{prop}}$ is actually $\begin{pmatrix} 1 & -\frac{1}{2} \\ -\frac{1}{2} & 1 \end{pmatrix}$ in each block, except in the spaces spanned by $\{|0\rangle, |1\rangle\}$ and $\{|T-1\rangle, |T\rangle\}$, where it is
$$
\begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ -\frac{1}{2} & 1 \end{pmatrix}_{0, 1} \quad \text{and} \quad \begin{pmatrix} 1 & -\frac{1}{2} \\ -\frac{1}{2} & \frac{1}{2} \end{pmatrix}_{T-1, T}.
$$ (6.255)
That is, $H'_{\mathrm{prop}}$ acts on the clock as a $(T+1) \times (T+1)$ matrix
$$
H'_{\mathrm{prop}} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} & 0 & \dots & & \\
-\frac{1}{2} & 1 & -\frac{1}{2} & 0 & \dots & \\
0 & -\frac{1}{2} & 1 & -\frac{1}{2} & 0 & \dots \\
& & \ddots & & & \\
& & & \ddots & & \\
& \dots & 0 & -\frac{1}{2} & 1 & -\frac{1}{2} \\
& & \dots & 0 & -\frac{1}{2} & \frac{1}{2}
\end{pmatrix};
$$ (6.256)
its entries are $(-\frac{1}{2}, -\frac{1}{2}, \dots, -\frac{1}{2})$ just above and below the diagonal, $(\frac{1}{2}, 1, 1, \dots, 1, \frac{1}{2})$ on the diagonal, and 0 elsewhere.

We may express it as $H'_{\mathrm{prop}} = I - \frac{1}{2}M$, where
$$
M = \begin{pmatrix}
1 & 1 & 0 & \dots & & \\
1 & 0 & 1 & 0 & \dots & \\
0 & 1 & 0 & 1 & 0 & \dots \\
& & \ddots & & & \\
& & & \ddots & & \\
& \dots & 0 & 1 & 0 & 1 \\
& & \dots & 0 & 1 & 1
\end{pmatrix}.
$$ (6.257)
That is,
$$
\begin{aligned}
M &: |t\rangle \mapsto |t+1\rangle + |t-1\rangle, \quad t \in \{1, 2, \dots, T-1\}, \\
M &: |0\rangle \mapsto |0\rangle + |1\rangle, \\
M &: |T\rangle \mapsto |T-1\rangle + |T\rangle.
\end{aligned}
$$ (6.258)
Diagonalizing $M$ also diagonalizes $H'_{\mathrm{prop}}$.

We can diagonalize $M$ by Fourier transforming. The eigenvectors have the form
$$
|\omega\rangle = \sum_{t=0}^T e^{i\omega t} |t\rangle.
$$ (6.259)
In the expansion of $M|\omega\rangle$, the coefficient of |t⟩ for $t \in \{1, 2, \dots, T-1\}$ is
$$
\begin{aligned}
e^{i\omega(t-1)} + e^{i\omega(t+1)} &= (e^{i\omega} + e^{-i\omega})e^{i\omega t} \\
&= (2\cos\omega)e^{i\omega t}.
\end{aligned}
$$ (6.260), (6.261)
Thus the action on $|t\rangle$ is multiplication by $2\cos\omega$, which does not depend on the sign of $\omega$. To construct an eigenstate of $M$, then, we may consider a linear combination of $|\omega\rangle$ and $|-\omega\rangle$, where the value of $|\omega\rangle$ is chosen so that $M$ acts properly on the states at the boundary — i.e. on $|t = 0\rangle$ and $|t = T\rangle$.

[chap6.pdf#page=61]
The coefficient of $|0\rangle$ in $M|\omega\rangle$ is $1 + e^{i\omega}$; therefore, the coefficient of $|0\rangle$ in $M(e^{i\omega/2}|\omega\rangle + e^{-i\omega/2}|-\omega\rangle)$ is
$$
\begin{aligned}
e^{i\omega/2}(1 + e^{i\omega}) + e^{-i\omega/2}(1 + e^{-i\omega}) &= (e^{i\omega} + e^{-i\omega})(e^{i\omega/2} + e^{-i\omega/2}) \\
&= 2\cos\omega(e^{i\omega/2} + e^{-i\omega/2}).
\end{aligned}
$$ (6.262)
It follows that the "boundary condition" at $t = 0$ is consistent, for any value of $\omega$, with an eigenvalue of $2\cos\omega$ for the vectors $e^{i\omega/2}|\omega\rangle + e^{-i\omega/2}|-\omega\rangle$.

But we must also consider the other boundary, at $t = T$. The coefficient of $|T\rangle$ in $e^{i\omega/2}|\omega\rangle + e^{-i\omega/2}|-\omega\rangle$ is $e^{i\omega/2}e^{i\omega T} + e^{-i\omega/2}e^{-i\omega T}$, while the coefficient of $|T\rangle$ in $M(e^{i\omega/2}|\omega\rangle + e^{-i\omega/2}|-\omega\rangle)$ is
$$
(1 + e^{-i\omega})e^{i\omega/2}e^{i\omega T} + (1 + e^{i\omega})e^{-i\omega/2}e^{-i\omega T}.
$$ (6.263)
We are to choose $\omega$ so that
$$
(1 + e^{-i\omega})e^{i\omega/2}e^{i\omega T} + (1 + e^{i\omega})e^{-i\omega/2}e^{-i\omega T} = (e^{i\omega} + e^{-i\omega})(e^{i\omega/2}e^{i\omega T} + e^{-i\omega/2}e^{-i\omega T}).
$$ (6.264)
After some cancellations, this condition becomes
$$
\begin{aligned}
e^{i\omega/2}e^{i\omega T} + e^{-i\omega/2}e^{-i\omega T} &= e^{3i\omega/2}e^{i\omega T} + e^{-3i\omega/2}e^{-i\omega T} \\
\implies \cos\left(\omega\left(T + \frac{1}{2}\right)\right) &= \cos\left(\omega\left(T + \frac{3}{2}\right)\right).
\end{aligned}
$$ (6.265), (6.266)
This condition is satisfied provided that
$$
\omega(T + 1) = \pi k \quad \text{where} \quad k = \text{integer}.
$$ (6.267)
We have therefore established that $\{2\cos\omega_k\}$ are $T + 1$ distinct eigenvalues of $M$ where $\omega_k = \frac{\pi}{T+1}k$ for $k \in \{0, 1, 2, \dots, T\}$, and that the corresponding eigenvectors (up to normalization) are
$$
|\psi_k\rangle = \sum_{t=0}^T \cos\left(\omega_k\left(t + \frac{1}{2}\right)\right)|t\rangle;
$$ (6.268)
hence the eigenvalues of $H'_{\mathrm{prop}}$ are $E_k = 1 - \cos\omega_k = 2\sin^2\frac{\omega_k}{2}$. These $T + 1$ eigenstates are a complete basis, and the two smallest eigenvalues are:
$$
E_0 = 0,
$$ (6.269)
$$
E_1 = 2\sin^2\left(\frac{\pi}{2(T+1)}\right) \approx \frac{\pi^2}{2(T+1)^2}.
$$ (6.270)
If $T = \mathrm{poly}(n)$, then, the eigenvalue gap for $H_{\mathrm{prop}}$ is $E_1 - E_0 \ge \frac{1}{\mathrm{poly}(n)}$.

#### Lower bound on the energy when the witness is rejected [chap6.pdf#page=61]

But we want to consider the spectrum for the full Hamiltonian $H = H_{\mathrm{in}} + H_{\mathrm{out}} + H_{\mathrm{prop}}$ (ignoring $H_{\mathrm{clock}}$ for now). For $H_{\mathrm{in}} + H_{\mathrm{out}}$, the null space is spanned by all vectors that have a valid input at $t = 0$ and answer YES (are accepted) at $t = T$:
$$
(H_{\mathrm{in}} + H_{\mathrm{out}})|\text{valid input, accepted output}\rangle = 0,
$$ (6.271)
while $\langle H_{\mathrm{in}} + H_{\mathrm{out}}\rangle \ge 1$ for all vectors orthogonal to this null space. Thus $H_{\mathrm{in}} + H_{\mathrm{out}}$ has eigenvalue $\text{gap} = 1$. Now, if the verifier accepts the input with probability one, then [chap6.pdf#page=62] there is a simultaneous null eigenvector of $H_{\mathrm{prop}}$ and of $H_{\mathrm{in}} + H_{\mathrm{out}}$. That is, there is a valid history with a valid input where the output is accepted. But if the acceptance probability is small, that means the angle between these two null spaces cannot be too small, since there is no vector that comes close to lying within both null spaces. We can relate this angle to the ground state energy of the full Hamiltonian $H = H_{\mathrm{in}} + H_{\mathrm{out}} + H_{\mathrm{prop}}$.

In general, suppose that $H_1$ and $H_2$ are two Hermitian operators, each with lowest eigenvalue zero, and eigenvalue gap at least $\Delta$. Then
$$
\begin{aligned}
H_1 &\ge \Delta(I - \Pi_1) \quad \text{where } \Pi_1 \text{ is projection onto null space of } H_1, \\
H_2 &\ge \Delta(I - \Pi_2) \quad \text{where } \Pi_2 \text{ is projection onto null space of } H_2.
\end{aligned}
$$ (6.272), (6.273)
Thus $H_1 + H_2 \ge \Delta(2I - \Pi_1 - \Pi_2)$ and $\langle H_1 + H_2\rangle \ge 2\Delta - \Delta\langle\Pi_1 + \Pi_2\rangle$. Now suppose $|\psi_1\rangle$ and $|\psi_2\rangle$ are two vectors such that $|\langle\psi_1|\psi_2\rangle| = \cos\theta$ for $0 \le \theta \le \pi/2$. With suitable phase conventions we may choose a basis in the two-dimensional space spanned by $|\psi_1\rangle$ and $|\psi_2\rangle$ such that
$$
\begin{aligned}
|\psi_1\rangle &= \begin{pmatrix} \cos\theta/2 \\ \sin\theta/2 \end{pmatrix}, \quad |\psi_2\rangle = \begin{pmatrix} \cos\theta/2 \\ -\sin\theta/2 \end{pmatrix} \implies \\
|\psi_1\rangle\langle\psi_1| + |\psi_2\rangle\langle\psi_2| &= \begin{pmatrix} 2\cos^2\theta/2 & 0 \\ 0 & 2\sin^2\theta/2 \end{pmatrix},
\end{aligned}
$$ (6.274), (6.275)
and therefore, in any state
$$
\langle |\psi_1\rangle\langle\psi_1| + |\psi_2\rangle\langle\psi_2| \rangle \le 2\cos^2\theta/2 = 1 + \cos\theta.
$$ (6.276)
It follows that, if $\Pi_1$ and $\Pi_2$ are projectors, where the maximum overlap between spaces projected by $\Pi_1$ and $\Pi_2$ is $|\langle\psi_1|\psi_2\rangle| = \cos\theta$, then $\langle\Pi_1 + \Pi_2\rangle \le 1 + \cos\theta$. Thus
$$
\begin{aligned}
\langle H_1 + H_2\rangle &\ge 2\Delta - \Delta\langle\Pi_1 + \Pi_2\rangle \\
&\ge \Delta(1 - \cos\theta) = 2\Delta\sin^2\theta/2.
\end{aligned}
$$ (6.277), (6.278)

Having related the expectation value of a sum of nonnegative Hermitian operators to the angle between their null spaces, we now need to estimate the angle between null spaces of $H_1 = H_{\mathrm{in}} + H_{\mathrm{out}}$ and $H_2 = H_{\mathrm{prop}}$. That is, we want to find
$$
\begin{aligned}
\cos^2\theta &= \max |\langle\eta_1|\eta_2\rangle|^2 \\
&= \max \langle\eta_2|\Pi_1|\eta_2\rangle
\end{aligned}
$$ (6.279), (6.280)
where we maximize over $\eta_1$ in the null space of $H_1$ and $\eta_2$ in the null space of $H_2$, and $\Pi_1$ is the projector onto the null space of $H_1$.

A vector in the null space of $H_2 = H_{\mathrm{prop}}$ is a valid history state $|\eta_2\rangle = \frac{1}{\sqrt{T+1}}\sum_{t=0}^T |\psi(t)\rangle \otimes |t\rangle$. The projector onto null space of $H_1$ acts trivially on states with $t \in \{1, 2, \dots, T-1\}$ so after transforming to the rotating frame
$$
\langle\eta'_2|\Pi_1|\eta'_2\rangle = \frac{T-1}{T+1} + \frac{1}{T+1}\langle\tilde{\eta}_2|\Pi_{\mathrm{in}} + \Pi'_{\mathrm{out}}|\tilde{\eta}_2\rangle,
$$ (6.281)
where $\tilde{\eta}_2$ is a state of the non-clock variables, $\Pi_{\mathrm{in}}$ projects onto a valid input state, and $\Pi'_{\mathrm{out}}$ projects onto
$$
V_T^\dagger (|1\rangle_{\mathrm{out}}\langle 1| \otimes I_{\mathrm{else}}) V_T
$$ (6.282)
(because we have transformed to the rotating frame, and the history state is valid). We know that $\langle\tilde{\eta}_2|\Pi_{\mathrm{in}} + \Pi'_{\mathrm{out}}|\tilde{\eta}_2\rangle \le (1 + \cos\phi)$ where $\phi$ is the angle between the spaces that [chap6.pdf#page=63] $\Pi_{\mathrm{in}}$ and $\Pi'_{\mathrm{out}}$ project onto, as we showed above. This angle $\phi$ is given by $\cos^2\phi = \epsilon$ where $\epsilon$ is the max. acceptance probability — that is, if the input is valid (in the support of $\Pi_{\mathrm{in}}$) and the history is valid, then the probability of $|1\rangle_{\mathrm{out}}$ is at most $\epsilon$.

Via eq.(6.281), this upper bound $\langle\tilde{\eta}_2|\Pi_{\mathrm{in}} + \Pi'_{\mathrm{out}}|\tilde{\eta}_2\rangle \le 1 + \sqrt{\epsilon}$ provides an upper bound on the expectation value of $\Pi_1$ in a valid history state, and hence a lower bound on the angle $\theta$ between the $H_1$ and $H_2$ null eigenspaces:
$$
\cos^2\theta \le \frac{T-1}{T+1} + \frac{1}{T+1}(1 + \sqrt{\epsilon}) = 1 - \frac{1-\sqrt{\epsilon}}{T+1},
$$ (6.283)
where $\epsilon$ is the maximum acceptance probability. Now, $\Delta = 2\sin^2\left(\frac{\pi}{2(T+1)}\right)$ is a lower bound for the gap of $H_1$ or $H_2$ and $\langle H_1 + H_2\rangle \ge 2\Delta\sin^2\frac{\theta}{2}$, where $\sin^2\theta = 1 - \cos^2\theta \ge \frac{1-\sqrt{\epsilon}}{T+1}$. Using $\sin^2\frac{\theta}{2} = \frac{\sin^2\theta}{4\cos^2\frac{\theta}{2}} \ge \frac{1}{4}\sin^2\theta$, we have
$$
\begin{aligned}
E_0 &\ge 4\sin^2\left(\frac{\pi}{2(T+1)}\right) \times \frac{1}{4}\left(\frac{1-\sqrt{\epsilon}}{T+1}\right) \ge \sin^2\left(\frac{\pi}{2(T+1)}\right) \times \left(\frac{1-\sqrt{\epsilon}}{T+1}\right) \\
&\ge \mathrm{constant} \times \frac{1-\sqrt{\epsilon}}{(T+1)^3} = \frac{1-\sqrt{\epsilon}}{\mathrm{poly}(n)}.
\end{aligned}
$$ (6.284)

To summarize, we have shown that if the acceptance probability is $\ge 1 - \epsilon$, then $E_0 \le \frac{\epsilon}{T+1}$, and if acceptance probability is $\le \epsilon$, then $E_0 \ge \mathrm{constant} \times \frac{1-\sqrt{\epsilon}}{(T+1)^3}$. With suitable amplification to make $\epsilon$ small (compared to $1/(T+1)^3$) in the case where the answer is YES, we have reduced the QMA problem to an instance of the local Hamiltonian problem.

#### Encoding the clock [chap6.pdf#page=63]

Except . . . we still need to see that the Hamiltonian can be made local. We'd like to encode the clock register using qubits. One way is to use a unary encoding with $T$ qubits labeled by $i = \{1, 2, 3, \dots, T\}$, where
$$
\begin{aligned}
|t = 0\rangle &= |000\dots 0\rangle \\
|t = 1\rangle &= |100\dots 0\rangle \\
|t = 2\rangle &= |110\dots 0\rangle \\
&\dots \\
|t = T\rangle &= |111\dots 1\rangle
\end{aligned}
$$ (6.285)

We can add a term to the Hamiltonian that imposes an energy penalty on the clock if its state is not validly encoded. The encoding is valid if a 0 is never followed by a 1. Therefore we choose
$$
H_{\mathrm{clock}} = \sum_{i=1}^{T-1} (|01\rangle\langle 01|)_{i, i+1},
$$ (6.286)
so that the only null vectors of $H_{\mathrm{clock}}$ are valid clock states.

The term $H_{\mathrm{prop}}$ in the Hamiltonian contains operators $|t\rangle\langle t|$, $|t\rangle\langle t-1|$, $|t-1\rangle\langle t|$ acting on the clock register. If only validly encoded clock states are allowed, we can project onto the state $|t\rangle$ by acting on just two neighboring qubits:
$$
|t\rangle\langle t| = (|10\rangle\langle 10|)_{t, t+1}
$$ (6.287)
for $t = 1, 2, 3, \dots, T-1$, and acting on only a single qubit suffices for $t = 0$ or $t = T$.

[chap6.pdf#page=64]
The operators that advance or retard the time act on three adjacent qubits:
$$
\begin{aligned}
|t\rangle\langle t-1| &= (|110\rangle\langle 100|)_{t-1, t, t+1}, \\
|t-1\rangle\langle t| &= (|100\rangle\langle 110|)_{t-1, t, t+1}
\end{aligned}
$$ (6.288)
(for $1 \le t \le T-1$). Acting on three qubits suffices to locate the position of the "domain wall" between the 0's and 1's in the bit string, and to move the wall one position to the left or to the right; for $t = 0$ action on just two qubits suffices to move the wall one step to the right, and for $t = T$ action on two qubits suffices to move the wall one step to the left. Since these clock terms act on at most three qubits, the term $U_t \otimes |t\rangle\langle t-1|$ acts on at most 5 qubits, if $U_t$ is a 2-qubit gate. Thus with this clock encoding, the Hamiltonian
$$
H = H_{\mathrm{in}} + H_{\mathrm{out}} + H_{\mathrm{prop}} + H_{\mathrm{clock}}
$$ (6.289)
is 5-local. Because the clock Hamiltonian annihilates validly encoded clock states, it trivially commutes with the rest of the terms in the Hamiltonian $H$, and has an energy gap of 1. Therefore, our previous analysis of the ground state energy of $H$ still stands.

This completes the demonstration that any QMA problem is reducible to the problem of estimating the ground state energy (with a $1/\mathrm{poly}(n)$ promise gap) of a 5-local Hamiltonian.

#### Comments [chap6.pdf#page=64]

Thus we have shown that the 5-local Hamiltonian problem is a "natural" QMA-complete problem, much as 3-SAT is a natural NP-complete problem. But while in the classical case many practical problems have been shown to be NP-complete, the family of problems that have been shown to be QMA-complete is still rather small, and the problems seem relatively "artificial." In any case, it's interesting to see that quantum local Hamiltonian problems seem to be harder than classical ones (if $\mathrm{QMA} \ne \mathrm{NP}$).

I won't discuss the tricks for reducing the QMA-complete problem to $k = 2$ (which involves clever use of perturbation theory) or for making $H$ geometrically local (which involves encoding the clock more cleverly, among other things).

Another interesting direction to pursue using these ideas is to show that any problem in BQP can be solved using adiabatic quantum computing. The idea is to replace
$$
H_{\mathrm{prop}} \to H_{\mathrm{prop}}(s) = (1 - s)H_{\mathrm{clock-init}} + s H_{\mathrm{prop}}
$$ (6.290)
where the null space of $H_{\mathrm{clock-init}}$ fixes the clock at $|t = 0\rangle$ and $s$ varies in $[0, 1]$. Then the ground state of $H(s = 0)$ is easy to construct, and the ground state of $H(s = 1)$ is the valid history state. The eigenvalue gap of $H(s)$ stays $> 1/\mathrm{poly}(n)$ for $s \in [0, 1]$, so the history state can be prepared in polynomial time by adiabatically varying $s$. Once we have prepared the history state, we can measure the clock, projecting out $|t = T\rangle$ with probability $1/(T + 1) = 1/\mathrm{poly}(n)$. And once we have $|\psi(T)\rangle$ we can measure the output qubit to find out if the circuit accepts. At a modest additional cost, we can substantially improve the probability of preparing $|\psi(T)\rangle$, by adding a long "runway" after time $t = T$, so that the state of the computer remains fixed for $S$ additional time steps; then measuring the clock prepares $|\psi(T)\rangle$ with probability $(S + 1)/(S + T + 1)$.

# Section 4.1: Nonseparability of EPR pairs [PDF Pages 4-9]

<!-- ============================================================ -->
<!-- Source: chap4.pdf, Physical Pages: 4-9                       -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 4 -->
# 4 Quantum Entanglement

## 4.1 Nonseparability of EPR pairs

### 4.1.1 Hidden quantum information

The deep ways that quantum information differs from classical information involve the properties, implications, and uses of *quantum entanglement*. Recall from §2.4.1 that a bipartite pure state is *entangled* if its Schmidt number is greater than one. Entangled states are interesting because they exhibit correlations that have no classical analog. We will study these correlations in this chapter.

Recall, for example, the *maximally entangled* state of two qubits (or *EPR pair*) defined in §3.4.1:

$$
|\phi^+\rangle_{AB} = \frac{1}{\sqrt{2}} (|00\rangle_{AB} + |11\rangle_{AB}).
$$ {#eq-4.1}

"Maximally entangled" means that when we trace over qubit $B$ to find the density operator $\boldsymbol{\rho}_A$ of qubit $A$, we obtain a multiple of the identity operator

$$
\boldsymbol{\rho}_A = \mathrm{tr}_B(|\phi^+\rangle\langle\phi^+|) = \frac{1}{2}\boldsymbol{I}_A,
$$ {#eq-4.2}

(and similarly $\boldsymbol{\rho}_B = \frac{1}{2}\boldsymbol{I}_B$). This means that if we measure spin $A$ along *any* axis, the result is completely random --- we find spin up with probability $1/2$ and spin down with probability $1/2$. Therefore, if we perform any local measurement of $A$ or $B$, we acquire no information about the preparation of the state, instead we merely generate a random bit. This situation contrasts sharply with case of a single qubit in a pure state; there we can store a bit by preparing, say, either $|\uparrow_{\hat{n}}\rangle$ or $|\downarrow_{\hat{n}}\rangle$, and we can recover that bit reliably by measuring along the $\hat{n}$-axis. With two

<!-- Page 5 -->
qubits, we ought to be able to store two bits, but in the state $|\phi^+\rangle_{AB}$ this information is *hidden*; at least, we can't acquire it by measuring $A$ or $B$.

In fact, $|\phi^+\rangle$ is one member of a basis of four mutually orthogonal states for the two qubits, all of which are maximally entangled --- the basis

$$
\begin{aligned}
|\phi^\pm\rangle &= \frac{1}{\sqrt{2}}(|00\rangle \pm |11\rangle), \\
|\psi^\pm\rangle &= \frac{1}{\sqrt{2}}(|01\rangle \pm |10\rangle),
\end{aligned}
$$ {#eq-4.3}

introduced in §3.4.1. Imagine that Alice and Bob play a game with Charlie. Charlie prepares one of these four states, thus encoding two bits in the state of the two-qubit system. One bit is the *parity* bit ($|\phi\rangle$ or $|\psi\rangle$): are the two spins aligned or antialigned? The other is the *phase* bit ($+$ or $-$): what superposition was chosen of the two states of like parity. Then Charlie sends qubit $A$ to Alice and qubit $B$ to Bob. To win the game, Alice (or Bob) has to identify which of the four states Charlie prepared.

Of course, if Alice and Bob bring their qubits together, they can identify the state by performing an orthogonal measurement that projects onto the $\{|\phi^+\rangle, |\phi^-\rangle, |\psi^+\rangle, |\psi^-\rangle\}$ basis. But suppose that Alice and Bob are in different cities, and that they are unable to communicate at all. Acting locally, neither Alice nor Bob can collect any information about the identity of the state.

What they *can* do locally is *manipulate* this information. Alice may apply $\boldsymbol{\sigma}_3$ to qubit $A$, flipping the relative phase of $|0\rangle_A$ and $|1\rangle_A$. This action flips the phase bit stored in the entangled state:

$$
\begin{aligned}
|\phi^+\rangle &\leftrightarrow |\phi^-\rangle, \\
|\psi^+\rangle &\leftrightarrow |\psi^-\rangle.
\end{aligned}
$$ {#eq-4.4}

On the other hand, she can apply $\boldsymbol{\sigma}_1$, which flips her spin ($|0\rangle_A \leftrightarrow |1\rangle_A$), and also flips the parity bit of the entangled state:

$$
\begin{aligned}
|\phi^+\rangle &\leftrightarrow |\psi^+\rangle, \\
|\phi^-\rangle &\leftrightarrow -|\psi^-\rangle.
\end{aligned}
$$ {#eq-4.5}

Bob can manipulate the entangled state similarly. In fact, as we discussed in §2.4, either Alice or Bob can perform a local unitary transformation that changes one maximally entangled state to any other maximally entangled state.* What their local unitary transformations *cannot* do is alter

---
\* But of course, this does not suffice to perform an arbitrary unitary transformation on the four-dimensional space $\mathcal{H}_A \otimes \mathcal{H}_B$, which contains states that are not maximally entangled. The maximally entangled states are *not* a subspace --- a superposition of maximally entangled states typically is *not* maximally entangled.

<!-- Page 6 -->
$\boldsymbol{\rho}_A = \boldsymbol{\rho}_B = \frac{1}{2}\boldsymbol{I}$ --- the information they are manipulating is information that neither one can read.

But now suppose that Alice and Bob are able to exchange (classical) messages about their measurement outcomes; together, then, they can learn about how their measurements are correlated. The entangled basis states are conveniently characterized as the simultaneous eigenstates of two commuting observables:

$$
\begin{aligned}
&\boldsymbol{\sigma}_1^{(A)} \otimes \boldsymbol{\sigma}_1^{(B)}, \\
&\boldsymbol{\sigma}_3^{(A)} \otimes \boldsymbol{\sigma}_3^{(B)};
\end{aligned}
$$ {#eq-4.6}

the eigenvalue of $\boldsymbol{\sigma}_3^{(A)} \otimes \boldsymbol{\sigma}_3^{(B)}$ is the parity bit, and the eigenvalue of $\boldsymbol{\sigma}_1^{(A)} \otimes \boldsymbol{\sigma}_1^{(B)}$ is the phase bit. Since these operators commute, they can in principle be measured simultaneously. But they cannot be measured simultaneously if Alice and Bob perform localized measurements. Alice and Bob could both choose to measure their spins along the $z$-axis, preparing a simultaneous eigenstate of $\boldsymbol{\sigma}_3^{(A)}$ and $\boldsymbol{\sigma}_3^{(B)}$. Since $\boldsymbol{\sigma}_3^{(A)}$ and $\boldsymbol{\sigma}_3^{(B)}$ both commute with the parity operator $\boldsymbol{\sigma}_3^{(A)} \otimes \boldsymbol{\sigma}_3^{(B)}$, their orthogonal measurements do not disturb the parity bit, and they can combine their results to infer the parity bit. But $\boldsymbol{\sigma}_3^{(A)}$ and $\boldsymbol{\sigma}_3^{(B)}$ *do not* commute with phase operator $\boldsymbol{\sigma}_1^{(A)} \otimes \boldsymbol{\sigma}_1^{(B)}$, so their measurement disturbs the phase bit. On the other hand, they could both choose to measure their spins along the $x$-axis; then they would learn the phase bit at the cost of disturbing the parity bit. But they can't have it both ways. To have hope of acquiring the parity bit without disturbing the phase bit, they would need to learn about the product $\boldsymbol{\sigma}_3^{(A)} \otimes \boldsymbol{\sigma}_3^{(B)}$ without finding out anything about $\boldsymbol{\sigma}_3^{(A)}$ and $\boldsymbol{\sigma}_3^{(B)}$ separately. That cannot be done locally.

Now let us bring Alice and Bob together, so that they can operate on their qubits jointly. How might they acquire both the parity bit and the phase bit of their pair? By applying an appropriate unitary transformation, they can rotate the entangled basis $\{|\phi^\pm\rangle, |\psi^\pm\rangle\}$ to the unentangled basis $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$. Then they can measure qubits $A$ and $B$ separately to acquire the bits they seek. How is this transformation constructed?

This is a good time to introduce notation that will be used heavily in later chapters, the quantum circuit notation. Qubits are denoted by horizontal lines, and the single-qubit unitary transformation $\boldsymbol{U}$ is denoted:

```
──────[ U ]──────
```

<!-- Page 7 -->
A particular single-qubit unitary we will find useful is the *Hadamard transform*

$$
\boldsymbol{H} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{\sqrt{2}}(\boldsymbol{\sigma}_1 + \boldsymbol{\sigma}_3),
$$ {#eq-4.7}

which has the properties

$$
\boldsymbol{H}^2 = \boldsymbol{I},
$$ {#eq-4.8}

and

$$
\begin{aligned}
\boldsymbol{H}\boldsymbol{\sigma}_1\boldsymbol{H} &= \boldsymbol{\sigma}_3, \\
\boldsymbol{H}\boldsymbol{\sigma}_3\boldsymbol{H} &= \boldsymbol{\sigma}_1.
\end{aligned}
$$ {#eq-4.9}

(We can envision $\boldsymbol{H}$ (up to an overall phase) as a $\theta = \pi$ rotation about the axis $\hat{n} = \frac{1}{\sqrt{2}}(\hat{n}_1 + \hat{n}_3)$ that rotates $\hat{x}$ to $\hat{z}$ and vice-versa; we have

$$
\boldsymbol{U}(\hat{n}, \theta) = \boldsymbol{I}\cos\frac{\theta}{2} + i\hat{n}\cdot\vec{\boldsymbol{\sigma}}\sin\frac{\theta}{2} = i\frac{1}{\sqrt{2}}(\boldsymbol{\sigma}_1 + \boldsymbol{\sigma}_3) = i\boldsymbol{H}.)
$$ {#eq-4.10}

Also useful is the two-qubit transformation known as the reversible XOR or *controlled-NOT* transformation; it acts as

$$
\text{CNOT} : |a, b\rangle \to |a, a \oplus b\rangle,
$$ {#eq-4.11}

on the basis states $a, b = 0, 1$, where $a \oplus b$ denotes addition modulo 2. The CNOT is denoted:

```
a ──────●────── a
        │
b ──────⊕────── a ⊕ b
```

Thus this transformation flips the second bit if the first is 1, and acts trivially if the first bit is 0; it has the property

$$
(\text{CNOT})^2 = \boldsymbol{I} \otimes \boldsymbol{I}.
$$ {#eq-4.12}

We call $a$ the *control* (or source) bit of the CNOT, and $b$ the *target* bit.

By composing these "primitive" transformations, or quantum *gates*, we can build other unitary transformations. For example, the "circuit"

```
──────[ H ]──────●──────
                 │
─────────────────⊕──────
```

<!-- Page 8 -->
(to be read from left to right) represents the product of $\boldsymbol{H}$ applied to the first qubit followed by CNOT with the first bit as the source and the second bit as the target. It is straightforward to see that this circuit transforms the standard basis to the entangled basis,

$$
\begin{aligned}
|00\rangle &\to \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)|0\rangle \to |\phi^+\rangle, \\
|01\rangle &\to \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)|1\rangle \to |\psi^+\rangle, \\
|10\rangle &\to \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)|0\rangle \to |\phi^-\rangle, \\
|11\rangle &\to \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)|1\rangle \to |\psi^-\rangle,
\end{aligned}
$$ {#eq-4.13}

so that the first bit becomes the phase bit in the entangled basis, and the second bit becomes the parity bit.

Similarly, we can invert the transformation by running the circuit backwards (since both CNOT and $\boldsymbol{H}$ square to the identity): if we apply the inverted circuit to an entangled state, and then measure both bits, we can learn the value of both the phase bit and the parity bit.

Of course, $\boldsymbol{H}$ acts on only one of the qubits; the "nonlocal" part of our circuit is the controlled-NOT gate --- this is the operation that establishes or removes entanglement. If we could only perform an "interstellar CNOT," we would be able to create entanglement among distantly separated pairs, or extract the information encoded in entanglement. But we can't. To do its job, the CNOT gate must act on its target without revealing the value of its source. Local operations and classical communication will not suffice.

### 4.1.2 Einstein locality and hidden variables

Einstein was disturbed by quantum entanglement. Eventually, he along with Podolsky and Rosen (EPR) sharpened their discomfort into what they regarded as a paradox. As later reinterpreted by Bohm, the situation they described is really the same as that discussed in §2.5.3. Given a maximally entangled state of two qubits shared by Alice and Bob, Alice can choose one of several possible measurements to perform on her spin that will realize different possible ensemble interpretations of Bob's density matrix; for example, she can prepare either $\boldsymbol{\sigma}_1$ or $\boldsymbol{\sigma}_3$ eigenstates.

We have seen that Alice and Bob are unable to exploit this phenomenon for faster-than-light communication. Einstein knew this but he was still dissatisfied. He felt that in order to be considered a *complete* description of physical reality a theory should meet a stronger criterion, that might be called *Einstein locality* (also sometimes known as *local realism*):

<!-- Page 9 -->
> Suppose that $A$ and $B$ are spacelike separated systems. Then in a *complete* description of physical reality an action performed on system $A$ must not modify the description of system $B$.

But if $A$ and $B$ are entangled, a measurement of $A$ is performed and a *particular* outcome is known to have been obtained, then the density matrix of $B$ *does* change. Therefore, by Einstein's criterion, the description of a quantum system by a wavefunction or density operator cannot be considered complete.

Einstein seemed to envision a more complete description that would remove the indeterminacy of quantum mechanics. A class of theories with this feature are called *local hidden-variable theories*. In a hidden-variable theory, measurement is actually fundamentally deterministic, but appears to be probabilistic because some degrees of freedom are not precisely known. For example, perhaps when a spin is prepared in what quantum theory would describe as the pure state $|\uparrow_{\hat{z}}\rangle$, there is actually a deeper theory in which the state prepared is parametrized as $(\hat{z}, \lambda)$ where $\lambda$ ($0 \le \lambda \le 1$) is the hidden variable. Suppose that with present-day experimental technique, we have no control over $\lambda$, so when we prepare the spin state, $\lambda$ might take any value --- the probability distribution governing its value is uniform on the unit interval.

Now suppose that when we measure the spin along an axis $\hat{n}$ rotated by $\theta$ from the $\hat{z}$ axis, the outcome will be

$$
\begin{aligned}
|\uparrow_{\hat{n}}\rangle, &\quad \text{for } 0 \le \lambda \le \cos^2\frac{\theta}{2}, \\
|\downarrow_{\hat{n}}\rangle, &\quad \text{for } \cos^2\frac{\theta}{2} < \lambda \le 1.
\end{aligned}
$$ {#eq-4.14}

If we know $\lambda$, the outcome is deterministic, but if $\lambda$ is completely unknown, then the probability distribution governing the measurement will agree with the predictions of quantum theory. In a hidden-variable theory, the randomness of the measurement outcome is not intrinsic; rather, it results from ignorance --- our description of the system is not the most complete possible description.

Now, what about entangled states? When we say that a hidden-variable theory is *local*, we mean that it satisfies the Einstein locality constraint. A measurement of $A$ does not modify the values of the variables that govern the measurements of $B$. Rather, when Alice measures her half of an entangled state that she shares with Bob, she gains information about the values of the hidden variables, sharpening her ability to predict what Bob will find when he measures the other half. This seems to be what Einstein had in mind when he envisioned a more complete description.

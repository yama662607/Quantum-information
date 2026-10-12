# Section 7.5: Failure probability [PDF Pages 21-24]

<!-- ============================================================ -->
<!-- Source: chap7.pdf, Physical Pages: 21-24                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 21 -->
## 7.5 Failure probability

### 7.5.1 Fidelity bound

If the support of the error map contains only the Pauli operators in the set $\mathcal{E}$ that we know how to correct, then we can recover the encoded quantum information with perfect fidelity. But in a realistic error model, there will be a small but nonzero amplitude for errors that are not in $\mathcal{E}$, so that the recovered state will not be perfect. What can we say about the fidelity of the recovered state?

The Pauli operator expansion of the error map can be divided into a sum over the “good” operators (those in $\mathcal{E}$), and the “bad” ones (those not in $\mathcal{E}$), so that it acts on a state $|\psi\rangle$ in the code subspace according to

$$
\begin{aligned}
|\psi\rangle &\mapsto \sum_a \boldsymbol{E}_a|\psi\rangle \otimes |\varphi_a\rangle_E \\
&= \sum_{\boldsymbol{E}_a \in \mathcal{E}} \boldsymbol{E}_a|\psi\rangle \otimes |\varphi_a\rangle_E + \sum_{\boldsymbol{E}_b \notin \mathcal{E}} \boldsymbol{E}_b|\psi\rangle \otimes |\varphi_b\rangle_E \\
&:= |\text{GOOD}\rangle + |\text{BAD}\rangle.
\end{aligned}
$$ {#eq-7.55}

The recovery operation then maps $|\text{GOOD}\rangle$ to a state $|\text{GOOD}'\rangle$ of data, environment, and ancilla, and $|\text{BAD}\rangle$ to a state $|\text{BAD}'\rangle$, so that after recovery we obtain the state

$$
|\text{GOOD}'\rangle + |\text{BAD}'\rangle;
$$ {#eq-7.56}

<!-- Page 22 -->
here (since recovery works perfectly acting on the good state)

$$
|\text{GOOD}'\rangle = |\psi\rangle \otimes |\chi\rangle_{EA},
$$ {#eq-7.57}

where $|\chi\rangle_{EA}$ is some (unnormalized) state of the environment and ancilla.

Suppose that the states $|\text{GOOD}\rangle$ and $|\text{BAD}\rangle$ are orthogonal. This would hold if, for example, all of the “good” states of the environment are orthogonal to all of the “bad” states; that is, if

$$
\langle\varphi_a|\varphi_b\rangle = 0 \quad \text{for} \quad \boldsymbol{E}_a \in \mathcal{E}, \boldsymbol{E}_b \notin \mathcal{E}.
$$ {#eq-7.58}

Let $\boldsymbol{\rho}'$ denote the density matrix of the recovered state, obtained by tracing out the environment and ancilla, and let

$$
F = \langle\psi|\boldsymbol{\rho}'|\psi\rangle
$$ {#eq-7.59}

be its fidelity with the initial code state. Because the recovery map is an isometry, the states $|\text{BAD}'\rangle$ and $|\text{GOOD}'\rangle$ are also orthogonal (that is, $|\text{BAD}'\rangle$ has no component along $|\psi\rangle \otimes |\chi\rangle_{EA}$). Therefore the fidelity is

$$
F = \langle\psi|\boldsymbol{\rho}_{\text{GOOD}'}|\psi\rangle + \langle\psi|\boldsymbol{\rho}_{\text{BAD}'}|\psi\rangle,
$$ {#eq-7.60}

where

$$
\boldsymbol{\rho}_{\text{GOOD}'} = \text{tr}_{EA}(|\text{GOOD}'\rangle\langle\text{GOOD}'|), \quad \boldsymbol{\rho}_{\text{BAD}'} = \text{tr}_{EA}(|\text{BAD}'\rangle\langle\text{BAD}'|),
$$ {#eq-7.61}

and hence

$$
F \ge \langle\psi|\boldsymbol{\rho}_{\text{GOOD}'}|\psi\rangle = \||\chi\rangle_{EA}\|^2 = \||\text{GOOD}'\rangle\|^2.
$$ {#eq-7.62}

Furthermore, since the recovery operation is an isometry, we have $\||\text{GOOD}'\rangle\| = \||\text{GOOD}\rangle\|$, and hence

$$
F \ge \||\text{GOOD}\rangle\|^2 = \left\|\sum_{\boldsymbol{E}_a \in \mathcal{E}} \boldsymbol{E}_a|\psi\rangle \otimes |\varphi_a\rangle_E\right\|^2.
$$ {#eq-7.63}

In general, though, $|\text{BAD}\rangle$ need not be orthogonal to $|\text{GOOD}\rangle$, so that $|\text{BAD}'\rangle$ need not be orthogonal to $|\text{GOOD}'\rangle$. Then $|\text{BAD}'\rangle$ might have a component along $|\text{GOOD}'\rangle$ that interferes destructively with $|\text{GOOD}'\rangle$ and so reduces the fidelity. We can still obtain a lower bound on the fidelity in this more general case by resolving $|\text{BAD}'\rangle$ into a component along $|\text{GOOD}'\rangle$ and an orthogonal component, as

$$
|\text{BAD}'\rangle = |\text{BAD}'_\|\rangle + |\text{BAD}'_\perp\rangle.
$$ {#eq-7.64}

Then reasoning just as above we obtain

$$
F \ge \||\text{GOOD}'\rangle + |\text{BAD}'_\|\rangle\|^2.
$$ {#eq-7.65}

Of course, since both the error operation and the recovery operation are isometries, the complete state $|\text{GOOD}'\rangle + |\text{BAD}'\rangle$ is normalized, or

$$
\||\text{GOOD}'\rangle + |\text{BAD}'_\|\rangle\|^2 + \||\text{BAD}'_\perp\rangle\|^2 = 1,
$$ {#eq-7.66}

and eq. (7.65) becomes

$$
F \ge 1 - \||\text{BAD}'_\perp\rangle\|^2.
$$ {#eq-7.67}

<!-- Page 23 -->
Finally, the norm of $|\text{BAD}'_\perp\rangle$ cannot exceed the norm of $|\text{BAD}'\rangle$, so we conclude that

$$
1 - F \le \||\text{BAD}'\rangle\|^2 = \||\text{BAD}\rangle\|^2 \equiv \left\|\sum_{\boldsymbol{E}_b \notin \mathcal{E}} \boldsymbol{E}_b|\psi\rangle \otimes |\varphi_b\rangle_E\right\|^2.
$$ {#eq-7.68}

This is our general bound on the “failure probability” of the recovery operation. The result eq.(7.63) can be recovered from eq.(7.68) in the special case where $|\text{GOOD}\rangle$ and $|\text{BAD}\rangle$ are orthogonal states.

### 7.5.2 Uncorrelated noise

Let's now consider some implications of these results for the case where errors acting on distinct qubits are completely uncorrelated. In that case, the error channel is a tensor product of single-qubit channels. If the noise acts on all the qubits in the same way, then the noise acting on the $n$ qubits in the code block is $\mathcal{N}^{\otimes n}$, where the single-qubit channel $\mathcal{N}$ has the dilation

$$
|\psi\rangle \mapsto |\psi\rangle \otimes |\varphi_I\rangle_E + \boldsymbol{X}|\psi\rangle \otimes |\varphi_X\rangle_E + \boldsymbol{Y}|\psi\rangle \otimes |\varphi_Y\rangle_E + \boldsymbol{Z}|\psi\rangle \otimes |\varphi_Z\rangle_E.
$$ {#eq-7.69}

The effect of the noise on encoded information is especially easy to analyze if we suppose further that each of the three states of the environment $|\varphi_{X,Y,Z}\rangle$ is orthogonal to the state $|\varphi_I\rangle$. In that case, a record of whether or not an error occurred for each qubit is permanently imprinted on the environment, and it is sensible to speak of a probability of error $\varepsilon$ for each qubit, where

$$
\langle\varphi_I|\varphi_I\rangle = 1 - \varepsilon.
$$ {#eq-7.70}

If our quantum code can correct $t$ errors, then the “good” Pauli operators have weight up to $t$, and the “bad” Pauli operators have weight greater than $t$; recovery is certain to succeed unless at least $t + 1$ qubits are subjected to errors. It follows that the fidelity obeys the bound

$$
1 - F \le \sum_{s=t+1}^n \binom{n}{s} \varepsilon^s (1 - \varepsilon)^{n-s} \le \binom{n}{t+1} \varepsilon^{t+1}.
$$ {#eq-7.71}

(For each of the $\binom{n}{t+1}$ ways of choosing $t+1$ locations, the probability that errors occur at every one of those locations is $\varepsilon^{t+1}$, where we disregard whether additional errors occur at the remaining $n - t - 1$ locations. Therefore, the final expression in eq. (7.71) is an upper bound on the probability that at least $t + 1$ errors occur in the block of $n$ qubits.) For $\varepsilon$ small and $t$ large, the fidelity of the encoded data is a substantial improvement over the fidelity $F = 1 - O(\varepsilon)$ maintained by an unprotected qubit.

For a general noise map acting on a single qubit, there is no clear notion of an “error probability;” the state of the qubit and its environment obtained when the Pauli operator $\boldsymbol{I}$ acts is not orthogonal to (and so cannot be perfectly distinguished from) the state obtained when the Pauli operators $\boldsymbol{X}$, $\boldsymbol{Y}$, and $\boldsymbol{Z}$ act. In the extreme case where there is no entanglement with the environment at all, the errors arise because unknown unitary transformations act on the qubits.

<!-- Page 24 -->
Consider uncorrelated unitary errors acting on the $n$ qubits in the code block, each of the form (up to an irrelevant phase)

$$
\boldsymbol{U}^{(1)} = \sqrt{1 - \varepsilon}\boldsymbol{I} + i\sqrt{\varepsilon} \boldsymbol{W},
$$ {#eq-7.72}

where $\boldsymbol{W}$ is a (traceless, Hermitian) linear combination of $\boldsymbol{X}, \boldsymbol{Y}$, and $\boldsymbol{Z}$, satisfying $\boldsymbol{W}^2 = \boldsymbol{I}$. If the state $|\psi\rangle$ of the qubit is prepared, and then the unitary error eq. (7.72) occurs, the fidelity of the resulting damaged state with the initial state is

$$
F = |\langle\psi|\boldsymbol{U}^{(1)}|\psi\rangle|^2 = 1 - \varepsilon\left(1 - (\langle\psi|\boldsymbol{W}|\psi\rangle)^2\right) \ge 1 - \varepsilon.
$$ {#eq-7.73}

If a unitary error of the form eq. (7.72) acts on each of the $n$ qubits in the code block, and the resulting state is expanded in terms of Pauli operators as in eq. (7.55), then the state $|\text{BAD}\rangle$ (which arises from terms in which $\boldsymbol{W}$ acts on at least $t + 1$ qubits) has a norm of order $(\sqrt{\varepsilon})^{t+1}$, and eq. (7.68) becomes

$$
1 - F = O(\varepsilon^{t+1}).
$$ {#eq-7.74}

We see that coding provides an improvement in fidelity of the same order irrespective of whether the uncorrelated errors are due to decoherence or due to unknown unitary transformations.

To avoid confusion, let us emphasize the meaning of “uncorrelated” for the purpose of the above discussion. We consider a unitary error acting on $n$ qubits to be “uncorrelated” if it is a tensor product of single-qubit unitary transformations, irrespective of how the unitaries acting on distinct qubits might be related to one another. For example, an “error” whereby all qubits rotate by the same angle $\theta \ll 1$ about a common axis is effectively dealt with by quantum error correction; after recovery the fidelity will be $F = 1 - O(\theta^{2(t+1)})$, if the code can protect against $t$ errors. In contrast, an $n$-qubit unitary error that would cause more trouble is one of the form $\boldsymbol{U}^{(n)} \sim \boldsymbol{I} + i\theta\boldsymbol{E}_{\text{bad}}^{(n)}$, where $\boldsymbol{E}_{\text{bad}}^{(n)}$ is an $n$-qubit Pauli operator whose weight is greater than $t$. Then $|\text{BAD}\rangle$ has a norm of order $\theta$, and the typical fidelity after recovery will be $F = 1 - O(\theta^2)$.

We should also note another important difference between unitary errors and decoherence errors. As discussed in Chapter 3, when decoherence is described by a Markovian master equation, errors are due to “quantum jumps” which occur at a constant rate $\Gamma$ per unit time, and the probability $\varepsilon = \Gamma\tau$ that an error occurs during a time interval of length $\tau$ increases linearly with $\tau$. In contrast, unitary errors due to imperfect control of the system Hamiltonian cause the quantum state to rotate by an angle $\theta$ which accumulates linearly in $\tau$, so that the corresponding infidelity $\sim \theta^2$ increases quadratically with $\tau$. We'll return to this distinction when we discuss fault-tolerant quantum computing in Chapter 8.

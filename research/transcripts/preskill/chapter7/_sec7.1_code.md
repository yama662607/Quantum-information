# Section 7.1: A Quantum error-correcting code [PDF Pages 7-10]

<!-- ============================================================ -->
<!-- Source: chap7.pdf, Physical Pages: 7-10                       -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 7 -->
# 7 Quantum Error Correction

## 7.1 A Quantum error-correcting code

In our study of quantum algorithms, we have found persuasive evidence that a quantum computer would have extraordinary power. But will quantum computers really work? Will we ever be able to build and operate them?

To do so, we must rise to the challenge of protecting quantum information from errors. As we have already noted in Chapter 1, there are several aspects to this challenge. A quantum computer will inevitably interact with its surroundings, resulting in decoherence and hence in the decay of the quantum information stored in the device. Unless we can successfully combat decoherence, our computer is sure to fail. And even if we were able to prevent decoherence by perfectly isolating the computer from the environment, errors would still pose grave difficulties. Quantum gates (in contrast to classical gates) are unitary transformations chosen from a continuum of possible values. Thus quantum gates cannot be implemented with perfect accuracy; the effects of small imperfections in the gates will accumulate, eventually leading to a serious failure in the computation. Any effective strategem to prevent errors in a quantum computer must protect against small unitary errors in a quantum circuit, as well as against decoherence.

In this and the next chapter we will see how clever encoding of quantum information can protect against errors (in principle). This chapter will present the theory of quantum error-correcting codes. We will learn that quantum information, suitably encoded, can be deposited in a quantum memory, exposed to the ravages of a noisy environment, and recovered without damage (if the noise is not too severe). Then in Chapter 8, we will extend the theory in two important ways. We will see that the recovery procedure can work effectively even if occasional errors occur during recovery. And we will learn how to process encoded information, so that a quantum computation can be executed successfully despite the debilitating effects of decoherence and faulty quantum gates.

A quantum error-correcting code (QECC) can be viewed as a mapping of $k$ qubits (a Hilbert space of dimension $2^k$) into $n$ qubits (a Hilbert space of dimension $2^n$), where $n > k$. The $k$ qubits are the "logical qubits" or "encoded qubits" that we wish to protect from error. The additional $n-k$ qubits allow us to store the $k$ logical qubits in a redundant fashion, so that the encoded information is not easily damaged.

We can better understand the concept of a QECC by revisiting an example that was introduced in Chapter 1, Shor's code with $n = 9$ and $k = 1$. We can characterize the code by specifying two basis states for the code subspace; we will refer to these basis

<!-- Page 8 -->
states as $|\bar{0}\rangle$, the "logical zero" and $|\bar{1}\rangle$, the "logical one." They are

$$
\begin{aligned}
|\bar{0}\rangle &= \left[\frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)\right]^{\otimes 3}, \\
|\bar{1}\rangle &= \left[\frac{1}{\sqrt{2}}(|000\rangle - |111\rangle)\right]^{\otimes 3};
\end{aligned}
$$ {#eq-7.1}

each basis state is a 3-qubit cat state, repeated three times. As you will recall from the discussion of cat states in Chapter 4, the two basis states can be distinguished by the 3-qubit observable $\boldsymbol{\sigma}_x^{(1)} \otimes \boldsymbol{\sigma}_x^{(2)} \otimes \boldsymbol{\sigma}_x^{(3)}$ (where $\boldsymbol{\sigma}_x^{(i)}$ denotes the Pauli matrix $\boldsymbol{\sigma}_x$ acting on the $i$th qubit); we will use the notation $\boldsymbol{X}_1\boldsymbol{X}_2\boldsymbol{X}_3$ for this operator. (There is an implicit $\boldsymbol{I}\otimes\boldsymbol{I}\otimes\cdots\otimes\boldsymbol{I}$ acting on the remaining qubits that is suppressed in this notation.) The states $|\bar{0}\rangle$ and $|\bar{1}\rangle$ are eigenstates of $\boldsymbol{X}_1\boldsymbol{X}_2\boldsymbol{X}_3$ with eigenvalues $+1$ and $-1$ respectively. But there is no way to distinguish $|\bar{0}\rangle$ from $|\bar{1}\rangle$ (to gather any information about the value of the logical qubit) by observing any one or two of the qubits in the block of nine. In this sense, the logical qubit is encoded *nonlocally*; it is written in the nature of the entanglement among the qubits in the block. This nonlocal property of the encoded information provides protection against noise, if we assume that the noise is local (that it acts independently, or nearly so, on the different qubits in the block).

Suppose that an unknown quantum state has been prepared and encoded as $a|\bar{0}\rangle + b|\bar{1}\rangle$. Now an error occurs; we are to diagnose the error and reverse it. How do we proceed? Let us suppose, to begin with, that a single bit flip occurs acting on one of the first three qubits. Then, as discussed in Chapter 1, the location of the bit flip can be determined by measuring the two-qubit operators

$$
\boldsymbol{Z}_1\boldsymbol{Z}_2, \quad \boldsymbol{Z}_2\boldsymbol{Z}_3.
$$ {#eq-7.2}

The logical basis states $|\bar{0}\rangle$ and $|\bar{1}\rangle$ are eigenstates of these operators with eigenvalue 1. But flipping any of the three qubits changes these eigenvalues. For example, if $\boldsymbol{Z}_1\boldsymbol{Z}_2 = -1$ and $\boldsymbol{Z}_2\boldsymbol{Z}_3 = 1$, then we infer that the first qubit has flipped relative to the other two. We may recover from the error by flipping that qubit back.

It is crucial that our measurement to diagnose the bit flip is a collective measurement on two qubits at once — we learn the value of $\boldsymbol{Z}_1\boldsymbol{Z}_2$, but we must not find out about the separate values of $\boldsymbol{Z}_1$ and $\boldsymbol{Z}_2$, for to do so would damage the encoded state. How can such a collective measurement be performed? In fact we can carry out collective measurements if we have a quantum computer that can execute controlled-NOT gates. We first introduce an additional "ancilla" qubit prepared in the state $|0\rangle$, then execute the quantum circuit

– Figure –

and finally measure the ancilla qubit. If the qubits 1 and 2 are in a state with $\boldsymbol{Z}_1\boldsymbol{Z}_2 = -1$ (either $|0\rangle_1|1\rangle_2$ or $|1\rangle_1|0\rangle_2$), then the ancilla qubit will flip once and the measurement outcome will be $|1\rangle$. But if qubits 1 and 2 are in a state with $\boldsymbol{Z}_1\boldsymbol{Z}_2 = 1$ (either $|0\rangle_1|0\rangle_2$ or $|1\rangle_1|1\rangle_2$), then the ancilla qubit will flip either twice or not at all, and the measurement

<!-- Page 9 -->
outcome will be $|0\rangle$. Similarly, the two-qubit operators

$$
\begin{aligned}
\boldsymbol{Z}_4\boldsymbol{Z}_5, &\quad \boldsymbol{Z}_7\boldsymbol{Z}_8, \\
\boldsymbol{Z}_5\boldsymbol{Z}_6, &\quad \boldsymbol{Z}_8\boldsymbol{Z}_9,
\end{aligned}
$$ {#eq-7.3}

can be measured to diagnose bit flip errors in the other two clusters of three qubits.

A three-qubit code would suffice to protect against a single bit flip. The reason the 3-qubit clusters are repeated three times is to protect against phase errors as well. Suppose now that a phase error

$$
|\psi\rangle \to \boldsymbol{Z}_i|\psi\rangle
$$ {#eq-7.4}

occurs acting on one of the nine qubits. We can diagnose in which cluster the phase error occurred by measuring the two six-qubit observables

$$
\begin{aligned}
&\boldsymbol{X}_1\boldsymbol{X}_2\boldsymbol{X}_3\boldsymbol{X}_4\boldsymbol{X}_5\boldsymbol{X}_6, \\
&\boldsymbol{X}_4\boldsymbol{X}_5\boldsymbol{X}_6\boldsymbol{X}_7\boldsymbol{X}_8\boldsymbol{X}_9.
\end{aligned}
$$ {#eq-7.5}

The logical basis states $|\bar{0}\rangle$ and $|\bar{1}\rangle$ are both eigenstates with eigenvalue one of these observables. A phase error acting on any one of the qubits in a particular cluster will change the value of $\boldsymbol{X}\boldsymbol{X}\boldsymbol{X}$ in that cluster relative to the other two; the location of the change can be identified by measuring the observables in eq.(7.5). Once the affected cluster is identified, we can reverse the error by applying $\boldsymbol{Z}$ to any one of the qubits in that cluster.

How do we measure the six-qubit observable $\boldsymbol{X}_1\boldsymbol{X}_2\boldsymbol{X}_3\boldsymbol{X}_4\boldsymbol{X}_5\boldsymbol{X}_6$? Notice that if its control qubit is initially in the state $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$, and its target is an eigenstate of $\boldsymbol{X}$ (that is, NOT) then a controlled-NOT acts according to

$$
\text{CNOT} : \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes |x\rangle \to \frac{1}{\sqrt{2}}(|0\rangle + (-1)^x|1\rangle) \otimes |x\rangle;
$$ {#eq-7.6}

it acts trivially if the target is the $\boldsymbol{X} = 1$ ($x=0$) state, and it flips the control if the target is the $\boldsymbol{X} = -1$ ($x=1$) state. To measure a product of $\boldsymbol{X}$'s, then, we execute the circuit

– Figure –

and then measure the ancilla in the $\frac{1}{\sqrt{2}}(|0\rangle \pm |1\rangle)$ basis.

We see that a single error acting on any one of the nine qubits in the block will cause no irrevocable damage. But if two bit flips occur in a single cluster of three qubits, then the encoded information *will* be damaged. For example, if the first two qubits in a cluster both flip, we will misdiagnose the error and attempt to recover by flipping the third. In all, the errors, together with our mistaken recovery attempt, apply the operator $\boldsymbol{X}_1\boldsymbol{X}_2\boldsymbol{X}_3$ to the code block. Since $|\bar{0}\rangle$ and $|\bar{1}\rangle$ are eigenstates of $\boldsymbol{X}_1\boldsymbol{X}_2\boldsymbol{X}_3$ with distinct eigenvalues, the effect of two bit flips in a single cluster is a *phase error* in the encoded qubit:

$$
\boldsymbol{X}_1\boldsymbol{X}_2\boldsymbol{X}_3 : a|\bar{0}\rangle + b|\bar{1}\rangle \to a|\bar{0}\rangle - b|\bar{1}\rangle.
$$ {#eq-7.7}

The encoded information will also be damaged if phase errors occur in two different

<!-- Page 10 -->
clusters. Then we will introduce a phase error into the third cluster in our misguided attempt at recovery, so that altogether $\boldsymbol{Z}_1\boldsymbol{Z}_4\boldsymbol{Z}_7$ will have been applied, which flips the encoded qubit:

$$
\boldsymbol{Z}_1\boldsymbol{Z}_4\boldsymbol{Z}_7 : a|\bar{0}\rangle + b|\bar{1}\rangle \to a|\bar{1}\rangle + b|\bar{0}\rangle.
$$ {#eq-7.8}

If the likelihood of an error is small enough, and if the errors acting on distinct qubits are not strongly correlated, then using the nine-qubit code will allow us to preserve our unknown qubit more reliably than if we had not bothered to encode it at all. Suppose, for example, that the environment acts on each of the nine qubits, independently subjecting it to the depolarizing channel described in Chapter 3, with error probability $p$. Then a bit flip occurs with probability $\frac{2}{3}p$, and a phase flip with probability $\frac{2}{3}p$. (The probability that both occur is $\frac{1}{3}p$). We can see that the probability of a phase error affecting the logical qubit is bounded above by $3 \cdot \binom{3}{2} \cdot (\frac{2}{3}p)^2 = 4p^2$, and the probability of a bit flip error is bounded above by $3 \cdot 3 \cdot \binom{3}{2} \cdot (\frac{2}{3}p)^2 = 4p^2 = 12p^2$. The total error probability is no worse than $16p^2$; this is an improvement over the error probability $p$ for an unprotected qubit, provided that $p < 1/16$. (As we'll see in §??, the asymmetry between $\boldsymbol{X}$ and $\boldsymbol{Z}$ errors is actually illusory; the code provides equally good protection against both.)

Of course, in this analysis we have implicitly assumed that encoding, decoding, error syndrome measurement, and recovery are all performed flawlessly. In Chapter 8 we will examine the more realistic case in which errors occur during these operations.

# Section 10.8: Quantum Protocols [PDF Pages 66-74]

<!-- ============================================================ -->
<!-- Source: chap10.pdf, Physical Pages: 66-74                     -->
<!-- Transcribed: 2026-10-12                                       -->
<!-- ============================================================ -->

<!-- Page 66 -->
## 10.8 Quantum Protocols

Using the decoupling principle in an i.i.d. setting, we can prove achievable rates for two fundamental quantum protocols. These are fondly known as the *father* and *mother* protocols, so named because each spawns a brood of interesting corollaries. We will formulate these protocols and discuss some of their "children" in this section, postponing the proofs until §10.9.

### 10.8.1 Father: Entanglement-assisted quantum communication

The father protocol is a scheme for entanglement-assisted quantum communication. Through many uses of a noisy quantum channel $\mathcal{N}^{A \to B}$, this protocol sends quantum information with high fidelity from Alice to Bob, while also consuming some previously prepared quantum entanglement shared by Alice and Bob. The task performed by the protocol is summarized by the *father resource inequality*
$$
\langle\mathcal{N}^{A \to B} : \boldsymbol{\rho}_A\rangle + \frac{1}{2}I(R; E)[qq] \ge \frac{1}{2}I(R; B)[q \to q],
$$ {#eq-10.317}
where the resources on the left-hand side can be used to achieve the result on the right-hand side, in an asymptotic i.i.d. setting. That is, the quantum channel $\mathcal{N}$ may be used $n$ times to transmit $\frac{n}{2} I(R; B) - o(n)$ qubits with fidelity $F \ge 1 - o(1)$, while consuming $\frac{n}{2} I(R; E) + o(n)$ ebits of entanglement shared between sender and receiver. These entropic quantities are evaluated in a tripartite pure state $\phi_{RBE}$, obtained by applying the Stinespring dilation $\boldsymbol{U}^{A \to BE}$ of $\mathcal{N}^{A \to B}$ to the purification $\psi_{RA}$ of the input density operator $\boldsymbol{\rho}_A$. Eq.(10.317) means that for any input density operator $\boldsymbol{\rho}_A$, there exists a coding procedure that achieves the quantum communication at the specified rate by consuming entanglement at the specified rate.

To remember the father resource inequality, it helps to keep in mind that $I(R; B)$

<!-- Page 67 -->
quantifies something good, the correlation with the reference system which survives transmission through the channel, while $I(R; E)$ quantifies something bad, the correlation between the reference system $R$ and the channel's environment $E$, which causes the transmitted information to decohere. The larger the good quantity $I(R; B)$, the higher the rate of quantum communication. The larger the bad quantity $I(R; E)$, the more entanglement we need to consume to overcome the noise in the channel. To remember the factor of $\frac{1}{2}$ in front of $I(R; B)$, consider the case of a noiseless quantum channel, where $\psi_{RA}$ is maximally entangled; in that case there is no environment,
$$
\phi_{RB} = \frac{1}{\sqrt{d}} \sum_{x=0}^{d-1} |x\rangle_R \otimes |x\rangle_B,
$$ {#eq-10.318}
and $\frac{1}{2}I(R; B) = H(R) = H(B) = \log_2 d$ is just the number of qubits in $A$. To remember the factor of $\frac{1}{2}$ in front of $I(R; E)$, consider the case of a noiseless classical channel (what we called the completely dephasing channel in §10.7.3), where the quantum information completely decoheres in a preferred basis; in that case
$$
\phi_{RBE} = \frac{1}{\sqrt{d}} \sum_{x=0}^{d-1} |x\rangle_R \otimes |x\rangle_B \otimes |x\rangle_E,
$$ {#eq-10.319}
and $I(R; B) = I(R; E) = H(R) = H(B) = \log_2 d$. Then the father inequality merely expresses the power of quantum teleportation: we can transmit $\frac{n}{2}$ qubits by consuming $\frac{n}{2}$ ebits and sending $n$ bits through the noiseless classical channel.

Before proving the father resource inequality, we will first discuss a few of its interesting consequences.

*Entanglement-assisted classical communication.*
Suppose Alice wants to send classical information to Bob, rather than quantum information. Then we can use superdense coding to turn the quantum communication achieved by the father protocol into classical communication, at the cost of consuming some additional entanglement. By invoking the superdense coding resource inequality
$$
\mathrm{SD} : [q \to q] + [qq] \ge 2[c \to c]
$$ {#eq-10.320}
$\frac{n}{2} I(R; B)$ times, and combining with the father resource inequality, we obtain $I(R; B)$ bits of classical communication per use of the channel while consuming a number of ebits
$$
\frac{1}{2}I(R; E) + \frac{1}{2}I(R; B) = H(R)
$$ {#eq-10.321}
per channel use. Thus we obtain an achievable rate for entanglement-assisted classical communication through the noisy quantum channel:
$$
\langle\mathcal{N}^{A \to B} : \boldsymbol{\rho}_A\rangle + H(R)[qq] \ge I(R; B)[c \to c].
$$ {#eq-10.322}
We may define the *entanglement-assisted classical capacity* $C_E(\mathcal{N})$ as the supremum over achievable rates of classical communication per channel use, assuming that an unlimited amount of entanglement is available at no cost. Then the resource inequality eq.(10.322) implies
$$
C_E(\mathcal{N}) \ge \max_A I(R; B).
$$ {#eq-10.323}

<!-- Page 68 -->
In this case there is a matching upper bound, so eq.(10.323) is really an equality, and hence a single-letter formula for the entanglement-assisted classical capacity. Furthermore, eq.(10.322) tells us a rate of entanglement consumption which suffices to achieve the capacity. If we disregard the cost of entanglement, the father protocol shows that a rate can be achieved for entanglement-assisted quantum communication which is half the entanglement-assisted classical capacity $C_E(\mathcal{N})$ of the noisy channel $\mathcal{N}$. That's clearly true, since by consuming entanglement we can use teleportation to convert $n$ bits of classical communication into $n/2$ qubits of quantum communication.

We also note that for the case where $\mathcal{N}$ is a noisy classical channel, eq.(10.323) matches Shannon's classical capacity. In that case, eq.(10.322) asserts that Shannon's classical communication rate is achievable by consuming some entanglement, but it turns out that no consumption of entanglement is actually necessary.

*Quantum channel capacity.*
It may be that Alice wants to send quantum information to Bob, but Alice and Bob are not so fortunate as to have pre-existing entanglement at their disposal. They can still make use of the father protocol, if we are willing to loan them some entanglement, which they are later required to repay. In this case we say that the entanglement *catalyzes* the quantum communication. Entanglement is needed to activate the process to begin with, but at the conclusion of the process no net entanglement has been consumed.

In this catalytic setting, Alice and Bob borrow $\frac{1}{2}I(R; E)$ ebits of entanglement per use of the channel to get started, execute the father protocol, and then sacrifice some of the quantum communication they have generated to replace the borrowed entanglement via the resource inequality
$$
[q \to q] \ge [qq].
$$ {#eq-10.324}
After repaying their debt, Alice and Bob retain a number of qubits of quantum communication per channel use
$$
\frac{1}{2}I(R; B) - \frac{1}{2}I(R; E) = H(B) - H(E) = I_c(R \rangle B),
$$ {#eq-10.325}
the channel's coherent information from $R$ to $B$. We therefore obtain the achievable rate for quantum communication
$$
\langle\mathcal{N}^{A \to B} : \boldsymbol{\rho}_A\rangle \ge I_c(R \rangle B)[q \to q],
$$ {#eq-10.326}
albeit in the catalyzed setting. It can actually be shown that this same rate is achievable without invoking catalysis (see §10.9.4). As already discussed in §10.7.1, though, because of the superadditivity of coherent information this resource inequality does not yield a general single-letter formula for the quantum channel capacity $Q(\mathcal{N})$.

### 10.8.2 Mother: Quantum state transfer

In the mother protocol, Alice, Bob, and Eve initially share a tripartite pure state $\phi_{ABE}$; thus Alice and Bob together hold the purification of Eve's system $E$. Alice wants to send her share of this purification to Bob, using as few qubits of noiseless quantum communication as possible. Therefore, Alice divides her system $A$ into two subsystems $A_1$ and $A_2$, where $A_1$ is as small as possible and $A_2$ is uncorrelated with $E$. She keeps $A_2$ and sends $A_1$ to Bob. After receiving $A_1$, Bob divides $A_1 B$ into two subsystems $B_1$

<!-- Page 69 -->
and $B_2$, where $B_1$ purifies $E$ and $B_2$ purifies $A_2$. Thus, at the conclusion of the protocol, Bob holds the purification of $E$ in $B_1$, and in addition Alice and Bob share a bipartite pure state in $A_2 B_2$. The protocol is portrayed in the following diagram:

```
  +---+         +---+        +----+----+         +---+        +----+              +----+----+
  | A | ------- | B |        | A1 | A2 |         | B |        | A2 |              | B2 | B1 |
  +---+         +---+        +----+----+         +---+        +----+              +----+----+
    \   phi_ABE   /    ===>         \             /     ===>    \                    /    /
     \           /                   \           /               \                  /    /
      \         /                     \         /                 \                /    /
       \       /                       \       /                   \              /    /
         +---+                           +---+                       \           /   +---+
         | E |                           | E |                        +---------+    | E |
         +---+                           +---+                                       +---+
```

In the i.i.d. version of the mother protocol, the initial state is $\phi_{ABE}^{\otimes n}$, and the task achieved by the protocol is summarized by the *mother resource inequality*
$$
\langle\phi_{ABE}\rangle + \frac{1}{2}I(A; E)[q \to q] \ge \frac{1}{2}I(A; B)[qq] + \langle\phi'_{B_1 E}\rangle,
$$ {#eq-10.327}
where the resources on the left-hand side can be used to achieve the result on the right-hand side, in an asymptotic i.i.d. setting, and the entropic quantities are evaluated in the state $\phi_{ABE}$. That is, if $A_1^{(n)}$ denotes the state Alice sends and $A_2^{(n)}$ denotes the state she keeps, then for any positive $\varepsilon$, the state of $A_2^{(n)} E^n$ is $\varepsilon$-close in the $L^1$ norm to a product state, where $\log |A_1^{(n)}| = \frac{n}{2} I(A; E) + o(n)$, while $A_2^{(n)} B_2^{(n)}$ contains $\frac{n}{2} I(A; B) - o(n)$ shared ebits of entanglement. Eq.(10.327) means that for any input pure state $\phi_{ABE}$ there is a way to choose the subsystem $A_2^{(n)}$ of the specified dimension such that $A_2^{(n)}$ and $E^n$ are nearly uncorrelated and the specified amount of entanglement is harvested in $A_2^{(n)} B_2^{(n)}$.

The mother protocol is in a sense *dual* to the father protocol. While the father protocol consumes entanglement to achieve quantum communication, the mother protocol consumes quantum communication and harvests entanglement. For the mother, $I(A; B)$ quantifies the correlation between Alice and Bob at the beginning of the protocol (something *good*), and $I(A; E)$ quantifies the noise in the initial shared entanglement (something *bad*). The mother protocol can also be viewed as a quantum generalization of the Slepian-Wolf distributed compression protocol discussed in §10.1.3. The mother protocol merges Alice's and Bob's shares of the purification of $E$ by sending Alice's share to Bob, much as distributed source coding merges the classical correlations shared by Alice and Bob by sending Alice's classical information to Bob. For this reason the mother protocol has been called the *fully quantum Slepian-Wolf protocol*; the modifier "fully" will be clarified below, when we discuss *state merging*, a variant on quantum state transfer in which classical communication is assumed to be freely available. For the mother (or father) protocol, $\frac{1}{2}I(A; E)$ (or $\frac{1}{2}I(R; E)$) quantifies the price we pay to execute the protocol, while $\frac{1}{2}I(A; B)$ (or $\frac{1}{2}I(R; B)$) quantifies the reward we receive.

We may also view the mother protocol as a generalization of the entanglement concentration protocol discussed in §10.4, extending that discussion in three ways:
1. The initial entangled state shared by Alice and Bob may be mixed rather than pure.
2. The communication from Alice to Bob is quantum rather than classical.
3. The amount of communication that suffices to execute the protocol is quantified by the resource inequality.

Also note that if the state of $AE$ is pure (uncorrelated with $B$), then the mother protocol reduces to Schumacher compression. In that case $\frac{1}{2}I(A; E) = H(A)$, and the mother

<!-- Page 70 -->
resource inequality states that the purification of $E^n$ can be transferred to Bob with high fidelity using $n H(A) + o(n)$ qubits of quantum communication.

Before proving the mother resource inequality, we will first discuss a few of its interesting consequences.

*Hashing inequality.*
Suppose Alice and Bob wish to distill entanglement from many copies of the state $\phi_{ABE}$, using only local operations and classical communication (LOCC). In the catalytic setting, they can borrow some quantum communication, use the mother protocol to distill some shared entanglement, and then use classical communication and their harvested entanglement to repay their debt via quantum teleportation. Using the teleportation resource inequality
$$
\mathrm{TP} : [qq] + 2[c \to c] \ge [q \to q]
$$ {#eq-10.328}
$\frac{n}{2} I(A; E)$ times, and combining with the mother resource inequality, we obtain
$$
\langle\phi_{ABE}\rangle + I(A; E)[c \to c] \ge I_c(A \rangle B)[qq] + \langle\phi'_{B_1 E}\rangle,
$$ {#eq-10.329}
since the net amount of distilled entanglement is $\frac{1}{2}I(A; B)$ per copy of $\phi$ achieved by the mother minus the $\frac{1}{2}I(A; E)$ per copy consumed by teleportation, and
$$
\frac{1}{2}I(A; B) - \frac{1}{2}I(A; E) = H(B) - H(E) = I_c(A \rangle B).
$$ {#eq-10.330}
Eq.(10.329) is the *hashing inequality*, which quantifies an achievable rate for distilling ebits of entanglement shared by Alice and Bob from many copies of a mixed state $\boldsymbol{\rho}_{AB}$, using one-way classical communication, assuming that $I_c(A \rangle B) = -H(A|B)$ is positive. Furthermore, the hashing inequality tells us how much classical communication suffices for this purpose.

In the case where the state $\boldsymbol{\rho}_{AB}$ is pure, $I_c(A \rangle B) = H(A) - H(AB) = H(A)$ and there is no environment $E$; thus we recover our earlier conclusion about concentration of pure-state bipartite entanglement — that $H(A)$ Bell pairs can be extracted per copy, with a negligible classical communication cost.

As another example, suppose that Alice prepares $n$ copies of the two-qubit Bell pair $|\phi^+\rangle$, and then sends half of each pair to Bob via the depolarizing channel with error probability $p$, so that after transmission each noisy Bell pair shared by Alice and Bob has fidelity $1 - p$ with $|\phi^+\rangle$ as in eq.(10.311). Then the same computation as in §10.7.4 yields
$$
\begin{aligned}
I_c(A \rangle B) &= H(B) - H(AB) = 1 - H_2(p) - p \log_2 3, \\
I(A; E) &= H(A) - I_c(A \rangle B) = H_2(p) + p \log_2 3.
\end{aligned}
$$ {#eq-10.331}
The interpretation is similar to our explanation of how to achieve the one-shot capacity of this channel: Alice and Bob can use a random stabilizer code to achieve this distillation rate. Alice measures the code's $n - k$ stabilizer generators on her $n$ qubits, and sends the measurement outcomes to Bob. Bob measures the same stabilizer generators on his $n$ qubits, and notes where his syndrome bits differ from Alice's. Using this information, Bob infers what Pauli operators to apply to his qubits so that the two syndromes now agree; ensuring that Alice and Bob now hold $k$ encoded Bell pairs. If the rate $\bar{R} = k/n$ is less than $I_c(A \rangle B)$, then for large $n$ Alice and Bob recover $k$ encoded copies of $|\phi^+\rangle$ with high probability.

<!-- Page 71 -->
*State merging.*
Suppose Alice and Bob share the purification of Eve's state, and Alice wants to transfer her share of the purification to Bob, where now unlimited classical communication from Alice to Bob is available at no cost. In contrast to the mother protocol, Alice wants to achieve the transfer with as little one-way quantum communication as possible, even if she needs to send more bits in order to send fewer qubits.

In the catalytic setting, Alice and Bob can borrow some quantum communication, perform the mother protocol, then use teleportation and the entanglement extracted by the mother protocol to repay some of the borrowed quantum communication. Combining teleportation of $\frac{n}{2} I(A; B)$ qubits with the mother resource inequality, we obtain
$$
\langle\phi_{ABE}\rangle + H(A|B)[q \to q] + I(A; B)[c \to c] \ge \langle\phi'_{B_1 E}\rangle,
$$ {#eq-10.332}
using
$$
\frac{1}{2}I(A; E) - \frac{1}{2}I(A; B) = H(E) - H(B) = H(AB) - H(B) = H(A|B).
$$ {#eq-10.333}
Eq.(10.332) is the *state-merging inequality*, expressing how much quantum and classical communication suffices to achieve the state transfer in an i.i.d. setting, assuming that $H(A|B)$ is nonnegative.

Like the mother protocol, this state merging protocol can be viewed as a (partially) quantum version of the Slepian-Wolf protocol for merging classical correlations. In the classical setting, $H(X|Y)$ quantifies Bob's remaining ignorance about Alice's information $X$ when Bob knows only $Y$; correspondingly, Alice can reveal $X$ to Bob by sending $H(X|Y)$ bits per letter of $X$. Similarly, state merging provides an operational meaning to the quantum conditional information $H(A|B)$, as the number of qubits per copy of $\phi$ that Alice sends to Bob to convey her share of the purification of $E$, assuming classical communication is free. In this sense we may regard $H(A|B)$ as a measure of Bob's remaining "ignorance" about the shared purification of $E$ when he holds only $B$.

Classically, $H(X|Y)$ is nonnegative, and zero if and only if Bob is already certain about $XY$, but quantumly $H(A|B)$ can be negative. How can Bob have "negative uncertainty" about the quantum state of $AB$? If $H(A|B) < 0$, or equivalently if $I(A; E) < I(A; B)$, then the mother protocol yields more quantum entanglement than the amount of quantum communication it consumes. Therefore, when $H(A|B)$ is negative (i.e. $I_c(A \rangle B)$ is positive), the mother resource inequality implies the Hashing inequality, asserting that classical communication from Alice to Bob not only achieves state transfer, but also distills $-H(A|B)$ ebits of entanglement per copy of $\phi$. These distilled ebits can be deposited in the entanglement bank, to be withdrawn as needed in future rounds of state merging, thus reducing the quantum communication cost of those future rounds. Bob's "negative uncertainty" today reduces the quantum communication cost of tasks to be performed tomorrow.

### 10.8.3 Operational meaning of strong subadditivity

The observation that $H(A|B)$ is the quantum communication cost of state merging allows us to formulate a simple operational proof of the strong subadditivity of von Neumann entropy, expressed in the form
$$
H(A|BC) \le H(A|B), \quad \text{or} \quad -H(A|B) \le -H(A|BC).
$$ {#eq-10.334}

<!-- Page 72 -->
When $H(A|B)$ is positive, eq.(10.334) is the obvious statement that it is no harder to merge Alice's system with Bob's if Bob holds $C$ as well as $B$. When $H(A|B)$ is negative, eq.(10.334) is the obvious statement that Alice and Bob can distill no less entanglement using one-way classical communication if Bob holds $C$ as well as $B$.

To complete this argument, we need to know that $H(A|B)$ is not only achievable but also that it is the optimal quantum communication cost of state merging, and that $-H(A|B)$ ebits is the optimal yield of hashing. The optimality follows from the principle that, for a bipartite pure state, $k$ qubits of quantum communication cannot increase the shared entanglement of $AB$ by more than $k$ ebits.

If $H(A|B)$ is negative, consider cutting the system $ABE$ into the two parts $AE$ and $B$, as in the following figure:

```
  +---+   \       +---+              +----+   \       +----+ +----+
  | A |    \      | B |              | A2 |    \      | B2 | | B1 |
  +---+     \     +---+              +----+     \     +----+ +----+
    \        \     /                   \         \     /      /
     \   ===  \   /                     \   ===   \   /      /
      \        \ /                       \         \ /      /
       \        \                         \         \      /
      +---+      \                       +---+       \    /
      | E |       \                      | E |        \  /
      +---+        \                     +---+         \/
```

In the hashing protocol, applied to $n$ copies of $\phi_{ABE}$, the entanglement across this cut at the beginning of the protocol is $n H(B)$. By the end of the protocol $E^n$ has decoupled from $A_2^{(n)}$ and has entanglement $n H(E)$ with $B_1^{(n)}$, ignoring $o(n)$ corrections. If $k$ ebits shared by Alice and Bob are distilled, the final entanglement across the $AE\text{-}B$ cut is
$$
n H(E) + k \le n H(B) \implies \frac{k}{n} \le H(B) - H(E) = -H(A|B).
$$ {#eq-10.335}
This inequality holds because LOCC cannot increase the entanglement across the cut, and implies that no more than $-H(A|B)$ ebits of entanglement per copy of $\phi_{ABE}$ can be distilled in the hashing protocol, asymptotically. (To be clear, this argument does not exclude entanglement distillation via LOCC at a rate higher than $-H(A|B)$; rather it shows that a protocol achieving distillation at a higher rate could not succeed at transferring the purification of $E$ to $B_1$.)

On the other hand, if $H(A|B)$ is positive, at the conclusion of state merging $B_1^{(n)}$ is entangled with $E^n$, and the entanglement across the $AE\text{-}B$ cut is at least $n H(E)$. To achieve this increase in entanglement, the number of qubits sent from Alice to Bob must be at least
$$
k \ge n H(E) - n H(B) \implies \frac{k}{n} \ge H(E) - H(B) = H(A|B).
$$ {#eq-10.336}
This inequality holds because the entanglement across the cut cannot increase by more than the quantum communication across the cut, and implies that at least $H(A|B)$ qubits must be sent per copy of $\phi_{ABE}$ to achieve state merging.

To summarize, we have proven strong subadditivity, not by the traditional route of sophisticated matrix analysis, but via a less direct method. This proof is built on two cornerstones of quantum information theory — the decoupling principle and the theory of typical subspaces — which are essential ingredients in the proof of the mother resource inequality.

<!-- Page 73 -->
### 10.8.4 Negative conditional entropy in thermodynamics

As a further application of the decoupling mother resource inequality, we now revisit Landauer's Principle, developing another perspective on the implications of negative quantum conditional entropy. Recall that erasure of a bit is a process which maps the bit to 0 irrespective of its initial value. This process is irreversible — knowing only the final state 0 after erasure, we cannot determine whether the initial state before erasure was 0 or 1. Irreversibility implies that erasure incurs an unavoidable thermodynamic cost. According to Landauer's Principle, erasing a bit at temperature $T$ requires work no less than $W = kT \ln 2$.

A specific erasure procedure is analyzed in Exercise 10.21. Suppose a two-level quantum system has energy eigenstates $|0\rangle$, $|1\rangle$ with corresponding eigenvalues $E_0 = 0$ and $E_1 = E \ge 0$. Initially the qubit is in an unknown mixture of these two states, and the energy splitting is $E = 0$. We erase the bit in three steps. In the first step, we bring the bit into contact with a heat bath at temperature $T > 0$, and wait for the bit to come to thermal equilibrium with the bath. In this step the bit "forgets" its initial value, but the bit is not yet erased because it has not been reset. In the second step, with the bit still in contact with the bath, we turn on a control field which slowly increases $E$ to a value much larger than $kT$ while maintaining thermal equilibrium all the while, thus resetting the bit to $|0\rangle$. In the third step, we isolate the bit from the bath and turn off the control field, so the two states of the bit become degenerate again. As shown in Exercise 10.21, work $W = kT \ln 2$ is required to execute step 2, with the energy dissipated as heat flowing from bit to bath.

We can also run the last two steps backward, increasing $E$ while the bit is isolated from the bath, then decreasing $E$ with the bit in contact with the bath. This procedure maps the state $|0\rangle$ to the maximally mixed state of the bit, extracting work $W = kT \ln 2$ from the bath in the process.

Erasure is irreversible because the agent performing the erasure does not know the information being erased. (If a copy of the information were stored in her memory, survival of that copy would mean that the erasure had not succeeded). From an information-theoretic perspective, the reduction in the thermodynamic entropy of the erased bit, and hence the work required to perform the erasure, arises because erasure reduces the agent's ignorance about the state of the bit, ignorance which is quantified by the Shannon entropy. But to be more precise, it is the conditional entropy of the system, given the state of the agent's memory, which captures the agent's ignorance before erasure and therefore also the thermodynamic cost of erasing. Thus the minimal work needed to erase system $A$ should be expressed as
$$
W(A|O) = H(A|O) kT \ln 2,
$$ {#eq-10.337}
where $O$ is the memory of the observer who performs the erasure, and $H(A|O)$ quantifies that observer's ignorance about the state of $A$.

But what if $A$ and $O$ are quantum systems? We know that if $A$ and $O$ are entangled, then the conditional entropy $H(A|O)$ can be negative. Does that mean we can erase $A$ while extracting work rather than doing work?

Yes, we can! Suppose for example that $A$ and $O$ are qubits and their initial state is maximally entangled. By controlling the contact between $AO$ and the heat bath, the observer can extract work $W = 2 kT \ln 2$ while transforming $AO$ to a maximally mixed state, using the same work extraction protocol as described above. Then she can do work

<!-- Page 74 -->
$W = kT \ln 2$ to return $A$ to the state $|0\rangle$. The net effect is to erase $A$ while extracting work $W = kT \ln 2$, satisfying the equality eq.(10.337).

To appreciate why this trick works, we should consider the joint state of $AO$ rather than the state of $A$ alone. Although the marginal state of $A$ is mixed at the beginning of the protocol and pure at the end, the state of $AO$ is pure at the beginning and mixed at the end. Positive work is extracted by sacrificing the purity of $AO$.

To generalize this idea, let's consider $n \gg 1$ copies of the state $\boldsymbol{\rho}_{AO}$ of system $A$ and memory $O$. Our goal is to map the $n$ copies of $A$ to the erased state $|000\dots 0\rangle$ while using or extracting the optimal amount of work. In fact, the optimal work per copy is given by eq.(10.337) in the $n \to \infty$ limit.

To achieve this asymptotic work per copy, the observer first projects $A^n$ onto its typical subspace, succeeding with probability $1 - o(1)$. A unitary transformation then rotates the typical subspace to a subsystem $\bar{A}$ containing $n(H(A) + o(1))$ qubits, while "erasing" the complementary qubits as in eq.(10.149). Now it only remains to erase $\bar{A}$.

The mother resource inequality ensures that we may decompose $\bar{A}$ into subsystems $A_1 A_2$ such that $A_2$ contains $\frac{n}{2}(I(A; O) - o(1))$ qubits and is nearly maximally entangled with a subsystem of $O^n$. What is important for the erasure protocol is that we may identify a subsystem of $\bar{A}O^n$ containing $n(I(A; O) - o(1))$ qubits which is only distance $o(1)$ away from a pure state. By controlling the contact between this subsystem and the heat bath, we may extract work $W = n(I(A; O) - o(1)) kT \ln 2$ while transforming the subsystem to a maximally mixed state. We then proceed to erase $\bar{A}$, expending work $kT \ln |\bar{A}| = n(H(A) + o(1)) kT \ln 2$. The net work cost of the erasure, per copy of $\boldsymbol{\rho}_{AO}$, is therefore
$$
W = (H(A) - I(A; O) + o(1)) kT \ln 2 = (H(A|O) + o(1)) kT \ln 2,
$$ {#eq-10.338}
and the erasure succeeds with probability $1 - o(1)$. A notable feature of the protocol is that only the subsystem of $O^n$ which is entangled with $A_2$ is affected. Any correlation of the memory $O$ with other systems remains intact, and can be exploited in the future to reduce the cost of erasure of those other systems.

As does the state merging protocol, this erasure protocol provides an operational interpretation of strong subadditivity. For positive $H(A|O)$, $H(A|O) \ge H(A|OO')$ means that it is no harder to erase $A$ if the observer has access to both $O$ and $O'$ than if she has access to $O$ alone. For negative $H(A|O)$, $-H(A|OO') \ge -H(A|O)$ means that we can extract at least as much work from $AOO'$ as from its subsystem $AO$.

To carry out this protocol and extract the optimal amount of work while erasing $A$, we need to know which subsystem of $O^n$ provides the purification of $A_2$. The decoupling argument ensures that this subsystem exists, but does not provide a constructive method for finding it, and therefore no concrete protocol for erasing at optimal cost. This quandary is characteristic of Shannon theory; for example, Shannon's noisy channel coding theorem ensures the existence of a code that achieves the channel capacity, but does not provide any explicit code construction.

# Section 10.7: Quantum Channel Capacities and Decoupling [PDF Pages 57-66]

<!-- ============================================================ -->
<!-- Source: chap10.pdf, Physical Pages: 57-66                     -->
<!-- Transcribed: 2026-10-12                                       -->
<!-- ============================================================ -->

<!-- Page 57 -->
## 10.7 Quantum Channel Capacities and Decoupling

### 10.7.1 Coherent information and the quantum channel capacity

As we have already emphasized, it's marvelous that the capacity for a classical channel can be expressed in terms of the optimal correlation between input and output for a single use of the channel,
$$
C := \max_X I(X; Y).
$$ {#eq-10.270}
Another pleasing feature of this formula is its *robustness*. For example, the capacity does not increase if we allow the sender and receiver to share randomness, or if we allow feedback from receiver to sender. But for quantum channels the story is more complicated. We've seen already that no simple single-letter formula is known for the classical capacity of a quantum channel, if we allow entanglement among the channel inputs, and we'll soon see that the same is true for the quantum capacity. In addition, it turns out that entanglement shared between sender and receiver can boost the classical and quantum capacities of some channels, and so can "backward" communication from receiver to sender. There are a variety of different notions of capacity for quantum channels, all reasonably natural, and all with different achievable rates.

While Shannon's theory of classical communication over noisy classical channels is

<!-- Page 58 -->
pristine and elegant, the same cannot be said for the theory of communication over noisy quantum channels, at least not in its current state. It's still a work in progress. Perhaps some day another genius like Shannon will construct a beautiful theory of quantum capacities. For now, at least there are a lot of interesting things we can say about achievable rates. Furthermore, the tools that have been developed to address questions about quantum capacities have other applications beyond communication theory.

The most direct analog of the classical capacity of a classical channel is the quantum capacity of a quantum channel, unassisted by shared entanglement or feedback. The quantum channel $\mathcal{N}^{A \to B}$ is a TPCP map from $\mathcal{H}_A$ to $\mathcal{H}_B$, and Alice is to use the channel $n$ times to convey a quantum state to Bob with high fidelity. She prepares her state $|\psi\rangle$ in a code subspace
$$
\mathcal{H}^{(n)} \subseteq \mathcal{H}_A^{\otimes n}
$$ {#eq-10.271}
and sends it to Bob, who applies a decoding map, attempting to recover $|\psi\rangle$. The rate $\bar{R}$ of the code is the number of encoded qubits sent per channel use,
$$
\bar{R} = \frac{1}{n} \log_2 \dim\left(\mathcal{H}^{(n)}\right).
$$ {#eq-10.272}
(Here, deviating from our earlier practice, we have used $\bar{R}$ rather than $R$ to denote the communication rate; from now on we will use $R$ to denote the reference system, which is introduced in the next paragraph.) We say that the rate $\bar{R}$ is *achievable* if there is a sequence of codes with increasing $n$ such that for any $\varepsilon, \delta > 0$ and for sufficiently large $n$ the rate is at least $\bar{R} - \delta$ and Bob's recovered state $\boldsymbol{\rho}$ has fidelity $F = \langle\psi|\boldsymbol{\rho}|\psi\rangle \ge 1 - \varepsilon$. The *quantum channel capacity* $Q(\mathcal{N})$ is the supremum of all achievable rates.

There is a regularized formula for $Q(\mathcal{N})$. To understand the formula we first need to recall that any channel $\mathcal{N}^{A \to B}$ has an isometric Stinespring dilation $\boldsymbol{U}^{A \to BE}$ where $E$ is the channel's "environment." Furthermore, any input density operator $\boldsymbol{\rho}_A$ has a purification; if we introduce a *reference system* $R$, for any $\boldsymbol{\rho}_A$ there is a pure state $\psi_{RA}$ such that $\boldsymbol{\rho}_A = \mathrm{tr}_R(|\psi\rangle\langle\psi|)$. (I will sometimes use $\psi$ rather than the Dirac ket $|\psi\rangle$ to denote a pure state vector, when the context makes the meaning clear and the ket notation seems unnecessarily cumbersome.) Applying the channel's dilation to $\psi_{RA}$, we obtain an output pure state $\phi_{RBE}$, which we represent graphically as:

```
  +---+
  | R |
  +---+
    :
  +---+       +---+       +---+
  | A | ----> | U | ----> | B |
  +---+       +---+       +---+
                |
                v
              +---+
              | E |
              +---+
```

We then define the *one-shot quantum capacity* of the channel $\mathcal{N}$ by
$$
Q_1(\mathcal{N}) := \max_A (-H(R|B)_{\phi_{RBE}}).
$$ {#eq-10.273}
Here the maximum is taken over all possible input density operators $\{\boldsymbol{\rho}_A\}$, and $H(R|B)$ is the quantum conditional entropy
$$
H(R|B) = H(RB) - H(B) = H(E) - H(B),
$$ {#eq-10.274}
where in the last equality we used $H(RB) = H(E)$ in a pure state of $RBE$. The quantity

<!-- Page 59 -->
$-H(R|B)$ has such a pivotal role in quantum communication theory that it deserves to have its own special name. We call it the *coherent information* from $R$ to $B$ and denote it
$$
I_c(R \rangle B)_\phi = -H(R|B)_\phi = H(B)_\phi - H(E)_\phi.
$$ {#eq-10.275}
This quantity does not depend on how the purification $\phi$ of the density operator $\boldsymbol{\rho}_A$ is chosen; any one purification can be obtained from any other by a unitary transformation acting on $R$ alone, which does not alter $H(B)$ or $H(E)$. Indeed, since the expression $H(B) - H(E)$ only depends on the marginal state of $BE$, for the purpose of computing this quantity we could just as well consider the input to the channel to be the mixed state $\boldsymbol{\rho}_A$ obtained from $\psi_{RA}$ by tracing out the reference system $R$. Furthermore, the coherent information does not depend on how we choose the dilation of the quantum channel; given a purification of the input density operator $\boldsymbol{\rho}_A$, $I_c(R \rangle B)_\phi = H(B) - H(RB)$ is determined by the output density operator of $RB$.

For a classical channel, $H(R|B)$ is always nonnegative and the coherent information is never positive. In the quantum setting, $I_c(R \rangle B)$ is positive if the reference system $R$ is more strongly correlated with the channel output $B$ than with the environment $E$. Indeed, an alternative way to express the coherent information is
$$
I_c(R \rangle B) = \frac{1}{2}(I(R; B) - I(R; E)) = H(B) - H(E),
$$ {#eq-10.276}
where we note that (because $\phi_{RBE}$ is pure)
$$
\begin{aligned}
I(R; B) &= H(R) + H(B) - H(RB) = H(R) + H(B) - H(E), \\
I(R; E) &= H(R) + H(E) - H(RE) = H(R) + H(E) - H(B).
\end{aligned}
$$ {#eq-10.277}

Now we can state the regularized formula for the quantum channel capacity --- it is the optimal asymptotic coherent information per letter
$$
Q(\mathcal{N}^{A \to B}) = \lim_{n \to \infty} \max_{A^n} \frac{1}{n} I_c(R^n \rangle B^n)_{\phi_{R^n B^n E^n}},
$$ {#eq-10.278}
where the input density operator $\boldsymbol{\rho}_{A^n}$ is allowed to be entangled across the $n$ channel uses. If coherent information were subadditive, we could reduce this expression to a single-letter quantity, the one-shot capacity $Q_1(\mathcal{N})$. But, unfortunately, for some channels the coherent information can be superadditive, in which case the regularized formula is not very informative. At least we can say that $Q_1(\mathcal{N})$ is an achievable rate, and therefore a lower bound on the capacity.

### 10.7.2 The decoupling principle

Before we address achievability, let's understand why eq.(10.278) is an upper bound on the capacity. First we note that the monotonicity of mutual information implies a corresponding monotonicity property for the coherent information. Suppose that the channel $\mathcal{N}_1^{A \to B}$ is followed by a channel $\mathcal{N}_2^{B \to C}$. Because mutual information is monotonic we have
$$
I(R; A) \ge I(R; B) \ge I(R; C),
$$ {#eq-10.279}
which can also be expressed as
$$
H(R) - H(R|A) \ge H(R) - H(R|B) \ge H(R) - H(R|C),
$$ {#eq-10.280}

<!-- Page 60 -->
and hence
$$
I_c(R \rangle A) \ge I_c(R \rangle B) \ge I_c(R \rangle C).
$$ {#eq-10.281}
A quantum channel cannot increase the coherent information, which has been called the *quantum data-processing inequality*.

Suppose now that $\boldsymbol{\rho}_A$ is a quantum code state, and that the two channels acting in succession are a noisy channel $\mathcal{N}^{A \to B}$ and the decoding map $\mathcal{D}^{B \to \hat{B}}$ applied by Bob to the channel output in order to recover the channel input. Consider the action of the dilation $\boldsymbol{U}^{A \to BE}$ of $\mathcal{N}$ followed by the dilation $\boldsymbol{V}^{B \to \hat{B}B'}$ of $\mathcal{D}$ on the input purification $\psi_{RA}$, under the assumption that Bob is able to recover *perfectly*:
$$
\psi_{RA} \xrightarrow{\boldsymbol{U}} \phi_{RBE} \xrightarrow{\boldsymbol{V}} \tilde{\psi}_{R\hat{B}B'E} = \psi_{R\hat{B}} \otimes \chi_{B'E}.
$$ {#eq-10.282}
If the decoding is perfect, then after decoding Bob holds in system $\hat{B}$ the purification of the state of $R$, so that
$$
H(R) = I_c(R \rangle A)_\psi = I_c(R \rangle \hat{B})_{\tilde{\psi}}.
$$ {#eq-10.283}
Since the initial and final states have the same coherent information, the quantum data processing inequality implies that the same must be true for the intermediate state $\phi_{RBE}$:
$$
\begin{aligned}
H(R) &= I_c(R \rangle B) = H(B) - H(E) \\
&\implies H(B) = H(RE) = H(R) + H(E).
\end{aligned}
$$ {#eq-10.284}
Thus the state of $RE$ is a product state. We have found that if Bob is able to recover perfectly from the action of the channel dilation $\boldsymbol{U}^{A \to BE}$ on the pure state $\psi_{RA}$, then, in the resulting channel output pure state $\phi_{RBE}$, the marginal state $\boldsymbol{\rho}_{RE}$ must be the product $\boldsymbol{\rho}_R \otimes \boldsymbol{\rho}_E$. Recall that we encountered this criterion for recoverability earlier, when discussing quantum error-correcting codes in Chapter 7.

Conversely, suppose that $\psi_{RA}$ is an entangled pure state, and Alice wishes to transfer the purification of $R$ to Bob by sending it through the noisy channel $\boldsymbol{U}^{A \to BE}$. And suppose that in the resulting tripartite pure state $\phi_{RBE}$, the marginal state of $RE$ factorizes as $\boldsymbol{\rho}_{RE} = \boldsymbol{\rho}_R \otimes \boldsymbol{\rho}_E$. Then $B$ decomposes into subsystems $B = B_1 B_2$ such that
$$
\phi_{RBE} = \boldsymbol{W}_B \left(\tilde{\psi}_{RB_1} \otimes \chi_{B_2 E}\right).
$$ {#eq-10.285}
where $\boldsymbol{W}_B$ is some unitary change of basis in $B$; this holds because the most general purification of $\boldsymbol{\rho}_{RE}$ can be obtained from a particular purification by applying a unitary transformation to $B$ alone. Now Bob can construct an isometric decoder $\boldsymbol{V}^{B_1 \to \hat{B}}\boldsymbol{W}_B^\dagger$, which extracts the purification of $R$ into Bob's preferred subsystem $\hat{B}$. Since all purifications of $R$ differ by an isometry on Bob's side, Bob can choose his decoding map to output the state $\psi_{R\hat{B}}$; then the input state of $RA$ is successfully transmitted to $R\hat{B}$ as desired. Furthermore, we may choose the initial state to be a maximally entangled state $\Phi_{RA}$ of the reference system with the code space of a quantum code; if the marginal state of $RE$ factorizes in the resulting output pure state $\phi_{RBE}$, then by the relative state method of Chapter 3 we conclude that *any* state in the code space can be sent through the channel and decoded with perfect fidelity by Bob.

We have found that purified quantum information transmitted through the noisy channel is exactly correctable if and only if the reference system is completely uncorrelated with the channel's environment, or as we sometimes say, *decoupled* from the

<!-- Page 61 -->
environment. This is the *decoupling principle*, a powerful notion underlying many of the key results in the theory of quantum channels.

So far we have shown that exact correctability corresponds to exact decoupling. But we can likewise see that approximate correctability corresponds to approximate decoupling. Suppose for example that the state of $RE$ is close to a product state in the $L^1$ norm:
$$
\|\boldsymbol{\rho}_{RE} - \boldsymbol{\rho}_R \otimes \boldsymbol{\rho}_E\|_1 \le \varepsilon.
$$ {#eq-10.286}
As we learned in Chapter 2, if two density operators are close together in this norm, that means they also have fidelity close to one and hence purifications with a large overlap. Any purification of the product state $\boldsymbol{\rho}_R \otimes \boldsymbol{\rho}_E$ has the form
$$
\tilde{\phi}_{RBE} = \boldsymbol{W}_B\left(\tilde{\psi}_{RB_1} \otimes \chi_{B_2 E}\right),
$$ {#eq-10.287}
and since all purifications of $\boldsymbol{\rho}_{RE}$ can be transformed to one another by an isometry acting on the purifying system $B$, there is a way to choose $\boldsymbol{W}_B$ such that
$$
F(\boldsymbol{\rho}_{RE}, \boldsymbol{\rho}_R \otimes \boldsymbol{\rho}_E) = \left|\langle\phi_{RBE}|\tilde{\phi}_{RBE}\rangle\right|^2 \ge 1 - \|\boldsymbol{\rho}_{RE} - \boldsymbol{\rho}_R \otimes \boldsymbol{\rho}_E\|_1 \ge 1 - \varepsilon.
$$ {#eq-10.288}
Here we have used Uhlmann's theorem, which asserts that the fidelity of two density operators is equal to the maximum overlap of the purifications of the density operators. Furthermore, because fidelity is monotonic, both under tracing out $E$ and under the action of Bob's decoding map, and because Bob can decode $\tilde{\phi}_{RBE}$ perfectly, we conclude that
$$
F\left(\mathcal{D}^{B \to \hat{B}}(\boldsymbol{\rho}_{RB}), \psi_{R\hat{B}}\right) \ge 1 - \varepsilon
$$ {#eq-10.289}
if Bob chooses the proper decoding map $\mathcal{D}$. Thus approximate decoupling in the $L^1$ norm implies high-fidelity correctability. It is convenient to note that a similar argument still works if $\boldsymbol{\rho}_{RE}$ is close in the $L^1$ norm to $\tilde{\boldsymbol{\rho}}_R \otimes \tilde{\boldsymbol{\rho}}_E$, where $\tilde{\boldsymbol{\rho}}_R$ is not necessarily $\mathrm{tr}_E(\boldsymbol{\rho}_{RE})$ and $\tilde{\boldsymbol{\rho}}_E$ is not necessarily $\mathrm{tr}_R(\boldsymbol{\rho}_{RE})$.

On the other hand, if (approximate) decoupling fails, the fidelity of Bob's decoded state will be seriously compromised. Suppose that in the state $\phi_{RBE}$ we have
$$
I(R; E) = H(R) + H(E) - H(RE) \ge \varepsilon > 0.
$$ {#eq-10.290}
Then the coherent information of $\phi$ is
$$
I_c(R \rangle B)_\phi = H(B)_\phi - H(E)_\phi = H(RE)_\phi - H(E)_\phi \le H(R)_\phi - \varepsilon.
$$ {#eq-10.291}
By the quantum data processing inequality, we know that the coherent information of Bob's decoded state $\tilde{\psi}_{R\hat{B}}$ is no larger; hence
$$
I_c(R \rangle \hat{B})_{\tilde{\psi}} = H(R)_{\tilde{\psi}} - H(R\hat{B})_{\tilde{\psi}} \le H(R)_\phi - \varepsilon,
$$ {#eq-10.292}
and therefore
$$
H(R\hat{B})_{\tilde{\psi}} \ge \varepsilon.
$$ {#eq-10.293}
The deviation from perfect decoupling means that the decoded state of $R\hat{B}$ has some residual entanglement with the environment $E$, and is therefore impure.

Now we have the tools to derive an upper bound on the quantum channel capacity

<!-- Page 62 -->
$Q(\mathcal{N})$. For $n$ channel uses, let $\psi^{(n)}$ be a maximally entangled state of a reference system $\mathcal{H}_R^{(n)} \subseteq \mathcal{H}_R^{\otimes n}$ with a code space $\mathcal{H}_A^{(n)} \subseteq \mathcal{H}_A^{\otimes n}$, where $\dim \mathcal{H}_A^{(n)} = 2^{n\bar{R}}$, so that
$$
I_c(R^n \rangle A^n)_{\psi^{(n)}} = H(R^n)_{\psi^{(n)}} = n\bar{R}.
$$ {#eq-10.294}
(Here $\bar{R}$ denotes the communication rate; we are now using $R$ to denote the reference system.) Now $A^n$ is transmitted to $B^n$ through $\left(\boldsymbol{U}^{A \to BE}\right)^{\otimes n}$, yielding the pure state $\phi^{(n)}$ of $R^n B^n E^n$. If Bob can decode with high fidelity, then his decoded state must have coherent information $H(R^n)_{\psi^{(n)}} - o(n)$, and the quantum data processing inequality then implies that
$$
I_c(R^n \rangle B^n)_{\phi^{(n)}} = H(R^n)_{\psi^{(n)}} - o(n) = n\bar{R} - o(n)
$$ {#eq-10.295}
and hence
$$
\bar{R} = \frac{1}{n} I_c(R^n \rangle B^n)_{\phi^{(n)}} + o(1).
$$ {#eq-10.296}
Taking the limit $n \to \infty$ we see that the expression for $Q(\mathcal{N})$ in eq.(10.278) is an upper bound on the quantum channel capacity. In Exercise 10.16, you will sharpen the statement eq.(10.295), showing that
$$
H(R^n) - I_c(R^n \rangle B^n) \le 2H_2(\varepsilon) + 4\varepsilon n\bar{R}
$$ {#eq-10.297}
if there is a decoding map that achieves fidelity $F \ge 1 - \varepsilon$.

To show that $Q(\mathcal{N})$ is an achievable rate, rather than just an upper bound, we will need to formulate a quantum version of Shannon's random coding argument. Our strategy (see §10.9.3) will be to demonstrate the existence of codes that achieve approximate decoupling of $E^n$ from $R^n$.

### 10.7.3 Degradable channels

Though coherent information can be superadditive in some cases, there are classes of channels for which the coherent information is additive, and therefore the quantum channel capacity matches the one-shot capacity, for which there is a single-letter formula. One such class is the class of *degradable channels*.

To understand what a degradable channel is, we first need the concept of a *complementary channel*. Any channel $\mathcal{N}^{A \to B}$ has a Stinespring dilation $\boldsymbol{U}^{A \to BE}$, from which we obtain $\mathcal{N}^{A \to B}$ by tracing out the environment $E$. Alternatively we obtain the channel $\mathcal{N}_c^{A \to E}$ complementary to $\mathcal{N}^{A \to B}$ by tracing out $B$ instead. Since we have the freedom to compose $\boldsymbol{U}^{A \to BE}$ with an isometry $\boldsymbol{V}^{E \to E}$ without changing $\mathcal{N}^{A \to B}$, the complementary channel is defined only up to an isometry acting on $E$. This lack of uniqueness need not trouble us, because the properties of interest for the complementary channel are invariant under such isometries.

We say that the channel $\mathcal{N}^{A \to B}$ is degradable if we can obtain its complementary channel by composing $\mathcal{N}^{A \to B}$ with a channel mapping $B$ to $E$:
$$
\mathcal{N}_c^{A \to E} = \mathcal{T}^{B \to E} \circ \mathcal{N}^{A \to B}.
$$ {#eq-10.298}
In this sense, when Alice sends a state through the channel, Bob, who holds system $B$, receives a less noisy copy than Eve, who holds system $E$.

Now suppose that $\boldsymbol{U}_1^{A_1 \to B_1 E_1}$ and $\boldsymbol{U}_2^{A_2 \to B_2 E_2}$ are dilations of the degradable channels $\mathcal{N}_1$ and $\mathcal{N}_2$. Alice introduces a reference system $R$ and prepares an input pure state

<!-- Page 63 -->
$\psi_{R A_1 A_2}$, then sends the state to Bob via $\mathcal{N}_1 \otimes \mathcal{N}_2$, preparing the output pure state $\phi_{R B_1 B_2 E_1 E_2}$. We would like to evaluate the coherent information $I_c(R \rangle B_1 B_2)_\phi$ in this state.

The key point is that because both channels are degradable, there is a product channel $\mathcal{T}_1 \otimes \mathcal{T}_2$ mapping $B_1 B_2$ to $E_1 E_2$, and the monotonicity of mutual information therefore implies
$$
I(B_1; B_2) \ge I(E_1; E_2).
$$ {#eq-10.299}
Therefore, the coherent information satisfies
$$
\begin{aligned}
I_c(R \rangle B_1 B_2) &= H(B_1 B_2) - H(E_1 E_2) \\
&= H(B_1) + H(B_2) - I(B_1; B_2) - H(E_1) - H(E_2) + I(E_1; E_2) \\
&\le H(B_1) - H(E_1) + H(B_2) - H(E_2).
\end{aligned}
$$ {#eq-10.300}
These quantities are all evaluated in the state $\phi_{R B_1 B_2 E_1 E_2}$. But notice that for the evaluation of $H(B_1) - H(E_1)$, the isometry $\boldsymbol{U}_2^{A_2 \to B_2 E_2}$ is irrelevant. This quantity is really the same as the coherent information $I_c(RA_2 \rangle B_1)$, where now we regard $A_2$ as part of the reference system for the input to channel $\mathcal{N}_1$. Similarly $H(B_2) - H(E_2) = I_c(RA_1 \rangle B_2)$, and therefore,
$$
I_c(R \rangle B_1 B_2) \le I_c(RA_2 \rangle B_1) + I_c(RA_1 \rangle B_2) \le Q_1(\mathcal{N}_1) + Q_1(\mathcal{N}_2),
$$ {#eq-10.301}
where in the last inequality we use the definition of the one-shot capacity as coherent information maximized over all inputs. Since $Q_1(\mathcal{N}_1 \otimes \mathcal{N}_2)$ is likewise defined by maximizing the coherent information $I_c(R \rangle B_1 B_2)$, we find that
$$
Q_1(\mathcal{N}_1 \otimes \mathcal{N}_2) \le Q_1(\mathcal{N}_1) + Q_1(\mathcal{N}_2)
$$ {#eq-10.302}
if $\mathcal{N}_1$ and $\mathcal{N}_2$ are degradable.

The regularized formula for the capacity of $\mathcal{N}$ is
$$
Q(\mathcal{N}) = \lim_{n \to \infty} \frac{1}{n} Q_1(\mathcal{N}^{\otimes n}) \le Q_1(\mathcal{N}),
$$ {#eq-10.303}
where the last inequality follows from eq.(10.302) assuming that $\mathcal{N}$ is degradable. We'll see that $Q_1(\mathcal{N})$ is actually an achievable rate, and therefore a single-letter formula for the quantum capacity of a degradable channel.

As a concrete example of a degradable channel, consider the *generalized dephasing channel* with dilation
$$
U^{A \to BE} : |x\rangle_A \mapsto |x\rangle_B \otimes |\alpha_x\rangle_E,
$$ {#eq-10.304}
where $\{|x\rangle_A\}$, $\{|x\rangle_B\}$ are orthonormal bases for $\mathcal{H}_A$, $\mathcal{H}_B$ respectively, and the states $\{|\alpha_x\rangle_E\}$ of the environment are normalized but not necessarily orthogonal. (We discussed the special case where $A$ and $B$ are qubits in §3.4.2.) The corresponding channel is
$$
\mathcal{N}^{A \to B} : \boldsymbol{\rho} \mapsto \sum_{x,x'} |x\rangle\langle x|\boldsymbol{\rho}|x'\rangle\langle x'| \langle \alpha_{x'}|\alpha_x\rangle,
$$ {#eq-10.305}
which has the complementary channel
$$
\mathcal{N}_c^{A \to E} : \boldsymbol{\rho} \mapsto \sum_x |\alpha_x\rangle\langle x|\boldsymbol{\rho}|x\rangle\langle \alpha_x|.
$$ {#eq-10.306}

<!-- Page 64 -->
In the special case where the states $\{|\alpha_x\rangle_E = |x\rangle_E\}$ are orthonormal, we obtain the *completely dephasing channel*
$$
\Delta^{A \to B} : \boldsymbol{\rho} \mapsto \sum_x |x\rangle\langle x|\boldsymbol{\rho}|x\rangle\langle x|,
$$ {#eq-10.307}
whose complement $\Delta^{A \to E}$ has the same form as $\Delta^{A \to B}$. (Here subscripts have been suppressed to avoid cluttering the notation, but it should be clear from the context whether $|x\rangle$ denotes $|x\rangle_A$, $|x\rangle_B$, or $|x\rangle_E$ in the expressions for $\mathcal{N}^{A \to B}$, $\mathcal{N}_c^{A \to E}$, $\Delta^{A \to B}$, and $\Delta^{A \to E}$.) We can easily check that
$$
\mathcal{N}_c^{A \to E} = \mathcal{N}_c^{C \to E} \circ \Delta^{B \to C} \circ \mathcal{N}^{A \to B};
$$ {#eq-10.308}
therefore $\mathcal{N}_c \circ \Delta$ degrades $\mathcal{N}$ to $\mathcal{N}_c$. Thus $\mathcal{N}$ is degradable and $Q(\mathcal{N}) = Q_1(\mathcal{N})$.

Further examples of degradable channels are discussed in Exercise 10.18.

We may also say that a channel $\mathcal{N}^{A \to B}$ is *antidegradable* if we can obtain that channel from its complementary channel by composing $\mathcal{N}_c^{A \to E}$ with a channel mapping $E$ to $B$:
$$
\mathcal{N}^{A \to B} = \mathcal{T}^{E \to B} \circ \mathcal{N}_c^{A \to E}.
$$ {#eq-10.309}
In this sense, Bob receives a noisier output than Eve. It is easy to see that the quantum capacity of an antidegradable channel must vanish. Eve can simulate Bob's output by applying $\mathcal{T}^{E \to B}$ to her output. Therefore, if a quantum state is transmitted through many uses of the channel $\mathcal{N}^{A \to B}$ from Alice to Bob, and Bob can decode the state with high fidelity, then Eve can decode it as well. Hence a nonzero capacity for an antidegradable channel is disallowed by the no-cloning theorem.

### 10.7.4 Capacity of the depolarizing channel

As we discussed in Chapter 3, the depolarizing channel with error probability $p$ acts on the input density operator $\boldsymbol{\rho}$ of a single qubit according to
$$
\mathcal{N}_p^{A \to B}(\boldsymbol{\rho}) = (1-p)\boldsymbol{\rho} + \frac{p}{3}\left(\boldsymbol{X}\boldsymbol{\rho}\boldsymbol{X} + \boldsymbol{Y}\boldsymbol{\rho}\boldsymbol{Y} + \boldsymbol{Z}\boldsymbol{\rho}\boldsymbol{Z}\right),
$$ {#eq-10.310}
where $\{\boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z}\}$ denote the Pauli matrices. Let's compute the one-shot capacity of this channel.

Because of the channel's symmetry, we can easily guess that the coherent information will be optimized by an input density operator that is maximally mixed. Therefore we consider the action of the channel on the maximally entangled state $|\phi^+\rangle_{RA} = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$, where $A$ is the channel input and $R$ is the reference system, obtaining the output
$$
\boldsymbol{\rho}_{RB} = (1-p)|\phi^+\rangle\langle\phi^+| + \frac{p}{3}\left(|\psi^+\rangle\langle\psi^+| + |\psi^-\rangle\langle\psi^-| + |\phi^-\rangle\langle\phi^-|\right).
$$ {#eq-10.311}
The one-shot capacity is the coherent information
$$
Q_1(\mathcal{N}_p) = I_c(R \rangle B) = H(B) - H(RB)
$$ {#eq-10.312}
if this quantity is nonnegative, and zero otherwise.

Because $\boldsymbol{\rho}_{RB}$ is a mixture of Bell states, the marginal density operator $\boldsymbol{\rho}_B$ is maximally mixed and hence $H(B) = 1$. Since the eigenvalues of $\boldsymbol{\rho}_{RB}$ are $\left(1-p, \frac{p}{3}, \frac{p}{3}, \frac{p}{3}\right)$, we have
$$
\begin{aligned}
H(RB) &= -(1-p)\log_2(1-p) - p\log_2\left(\frac{p}{3}\right) = H_2(p) + p\log_2 3 \\
&\implies I_c(R \rangle B) = 1 - H_2(p) - p\log_2 3,
\end{aligned}
$$ {#eq-10.313}

<!-- Page 65 -->
which is positive for $p < p_1 \approx .18929$. Thus the one-shot capacity $Q_1(\mathcal{N}_p)$ is nonzero for error probability $p < p_1$.

This expression for $Q_1(\mathcal{N}_p)$ has a simple interpretation --- it is the communication rate achieved by random stabilizer codes such that the probability of a decoding error vanishes asymptotically. To see why, suppose that the number $n$ of channel uses is very large, so that the number of transmitted qubits with errors is close to $pn$ with high probability. Approximating the number of ways to choose which qubits have errors by $\binom{n}{np}$, and noticing that for each damaged qubit there are three possible uniformly distributed Pauli errors, we conclude that the number of typical errors is
$$
\approx \binom{n}{np} 3^{pn} \approx 2^{n(H_2(p) + p\log_2 3)}.
$$ {#eq-10.314}
Now consider $n$-qubit stabilizer codes with $k$ logical qubits, and imagine averaging uniformly over such codes. These codes have $n - k$ independent commuting stabilizer generators, and measuring all these generators yields an error syndrome with $n - k$ bits. If the number of possible syndromes $2^{n-k}$ is much larger than the number of typical errors, then the observed syndrome is very unlikely to point to any particular typical error merely by accident; instead with high probability the syndrome will point to a unique typical error, the one that actually occurred, which can therefore be decoded correctly.

Concretely, the probability of a decoding error due to a syndrome decoding ambiguity can be estimated as
$$
\mathrm{error\ prob} \approx \frac{\#\ \mathrm{typical\ errors}}{\#\ \mathrm{syndromes}} \approx \frac{2^{n(H_2(p) + p\log_2 3)}}{2^{n-k}} = 2^{-n(Q_1(\mathcal{N}_p) - \bar{R})},
$$ {#eq-10.315}
where $\bar{R} = k/n$ is the encoding rate. We conclude that the error probability approaches zero as $n \to \infty$ for any rate $\bar{R}$ less than $Q_1(\mathcal{N}_p)$.

We used a similar counting argument to obtain a lower bound on the classical capacity $C(p) = 1 - H_2(p)$ of the binary symmetric channel in §10.1.5. In that case we could find a matching upper bound by noting that if the communication rate were larger than $C(p)$ then there would not enough distinct syndromes to distinguish among all the typical errors. Curiously, this argument fails to provide a upper bound on the quantum communication rate achieved by stabilizer codes for a very noisy depolarizing channel $\mathcal{N}_p$ where $p$ is close to $p_1$.

Counting syndromes does not yield an upper bound on the quantum capacity because quantum codes can be highly *degenerate*; that is, there may be many nontrivial errors that act trivially on the code space. We encountered an instructive example of a degenerate stabilizer code in Chapter 7: the toric code, in which $Z$ errors forming closed loops on the two-dimensional qubit lattice (or $X$ errors forming closed loops on the dual lattice) are contained in the code stabilizer. A more mundane example is the quantum repetition code spaced by codewords $|0\rangle^{\otimes n}$ and $|1\rangle^{\otimes n}$. In this case $Z_i Z_j$ is in the code stabilizer, where $i$ and $j$ label any pair among the $n$ qubits.

It turns out that a positive capacity can be attained for $p$ slightly above $p_1$ by concatenating the length-$m$ quantum repetition code with a random stabilizer code for some values of $m > 1$. Correspondingly, one finds that, for some values of the number $m$ of channels uses and of the error probability $p$, the coherent information per channel use is higher than $Q_1(\mathcal{N}_p)$.

<!-- Page 66 -->
Consider the input to $m$ channels uses
$$
|\Phi\rangle_{R A_1 A_2 \cdots A_m} = \frac{1}{\sqrt{2}}\left(|0\rangle^{\otimes(m+1)} + |1\rangle^{\otimes(m+1)}\right)_{R A_1 A_2 \cdots A_m},
$$ {#eq-10.316}
where $R$ is the reference system. After $I \otimes \left(\mathcal{N}_p^{A \to B}\right)^{\otimes m}$ acts on this state, we may compute explicitly $\frac{1}{m}I_c(R \rangle B_1 B_2 \cdots B_m)$. One finds that for $m = 5$ (which turns out to be the optimal case) this quantity, and therefore also $Q(\mathcal{N}_p)$, is positive up to $p < p_5$, where $p_5 \approx .19036$ is strictly larger than $p_1$.

For small $p$, $\frac{1}{m}I_c(R \rangle B_1 B_2 \cdots B_m)$ is close to $\frac{1}{m}$, hence much smaller for $m > 1$ than for $m = 1$. But if the channel is sufficiently noisy, the coherent information is superadditive, and one finds a higher value for $m > 1$, indicating that the quantum capacity exceeds $Q_1(\mathcal{N}_p)$.

The value of $p_*$, the largest value of $p$ for which the capacity is nonzero, is of considerable interest, but it is still unknown. Exercise 10.13 shows that the depolarizing channel is antidegradable (and therefore has vanishing capacity) for $p \ge .25$; hence $p_* \le .25$. On the other hand, the best currently known lower bound is $p_* \ge .19088$. Perhaps someday a single-letter formula will be found for the quantum capacity of the depolarizing channel, but for now the superadditivity of coherent information has hindered efforts to obtain a precise estimate of the capacity in the extremely noisy regime. It's humbling.

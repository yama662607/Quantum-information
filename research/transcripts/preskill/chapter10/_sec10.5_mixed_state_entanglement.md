# Section 10.5 Quantifying Mixed-State Entanglement

## 10.5 Quantifying Mixed-State Entanglement

### 10.5.1 Asymptotic irreversibility under LOCC

The entanglement cost $E_C$ and the distillable entanglement $E_D$ are natural and operationally meaningful ways to quantify entanglement. It's quite satisfying to find that, because entanglement dilution and concentration are asymptotically reversible for pure states, these two measures of pure-state bipartite entanglement agree, and provide another operational role for the von Neumann entropy of a marginal quantum state.

We can define $E_C$ and $E_D$ for bipartite mixed states just as we did for pure states, but the story is more complicated -- when we prepare many copies of a mixed state shared by Alice and Bob, the dilution of Bell pairs is not in general reversible, even asymptotically, and the distillable entanglement can be strictly less than the entanglement cost, though it can never be larger. There are even bipartite mixed states with nonzero entanglement cost and zero distillable entanglement, a phenomenon called *bound entanglement*. This irreversibility is not shocking; any bipartite operation which maps many copies of the pure state $|\phi^+\rangle_{AB}$ to many copies of the mixed state $\bm{\rho}_{AB}$ necessarily discards some information to the environment, and we don't normally expect a process that forgets information to be reversible.

This separation between $E_C$ and $E_D$ raises the question, what is the preferred way to quantify the amount of entanglement when two parties share a mixed quantum state? The answer is: it depends. Many different measures of bipartite mixed-state entanglement have been proposed, each with its own distinctive advantages and disadvantages. Even though they do not always agree, both $E_C$ and $E_D$ are certainly valid measures. A further distinction can be made between the rate $E_{D1}$ at which entanglement can be distilled with one-way communication between the parties, and the rate $E_D$ with two-way communication. There are bipartite mixed states for which $E_D > E_{D1}$, and even states for which $E_D$ is nonzero while $E_{D1}$ is zero. In contrast to the pure-state case, we don't have nice formulas for the values of the various entanglement measures, though there are useful upper and lower bounds. We will derive a lower bound on $E_{D1}$ in §10.8.2 (the hashing inequality).

There are certain properties that any reasonable measure of bipartite quantum entanglement should have. The most important is that it must not increase under local operations and classical communication, because quantum entanglement cannot be created by LOCC alone. A function on bipartite states that is nonincreasing under LOCC is called an *entanglement monotone*. Note that an entanglement monotone will also be invariant under local unitary operations $U_{AB} = U_A \otimes U_B$, for if $U_{AB}$ can reduce the entanglement for any state, its inverse can increase entanglement.

A second important property is that a bipartite entanglement measure must vanish for separable states. Recall from Chapter 4 that a bipartite mixed state is separable if it can be expressed as a convex combination of product states,
$$
\bm{\rho}_{AB} = \sum_x p(x) |\alpha(x)\rangle\langle\alpha(x)|_A \otimes |\beta(x)\rangle\langle\beta(x)|_B. \tag{10.192}
$$
A separable state is not entangled, as it can be created using LOCC. Via classical communication, Alice and Bob can establish a shared source of randomness, the distribution $X = \{x, p(x)\}$. Then they may jointly sample from $X$; if the outcome is $x$, Alice prepares $|\alpha(x)\rangle$ while Bob prepares $|\beta(x)\rangle$.

A third desirable property for a bipartite entanglement measure is that it should agree with $E = E_C = E_D$ for bipartite pure states. Both the entanglement cost and the distillable entanglement respect all three of these properties.

We remark in passing that, despite the irreversibility of entanglement dilution under LOCC, there is a mathematically viable way to formulate a reversible theory of bipartite entanglement which applies even to mixed states. In this formulation, we allow Alice and Bob to perform arbitrary bipartite operations that are incapable of creating entanglement; these include LOCC as well as additional operations which cannot be realized using LOCC. In this framework, dilution and concentration of entanglement become asymptotically reversible even for mixed states, and a unique measure of entanglement can be formulated characterizing the optimal rate of conversion between copies of $\bm{\rho}_{AB}$ and Bell pairs using these non-entangling operations.

Irreversible bipartite entanglement theory under LOCC, and also the reversible theory under non-entangling bipartite operations, are both examples of *resource theories*. In the resource theory framework, one or more parties are able to perform some restricted class of operations, and they are capable of preparing a certain restricted class of states using these operations. In addition, the parties may also have access to *resource states*, which are outside the class they can prepare on their own. Using their restricted operations, they can transform resource states from one form to another, or consume resource states to perform operations beyond what they could achieve with their restricted operations alone. The name "resource state" conveys that such states are valuable because they may be consumed to do useful things.

In a two-party setting, where LOCC is allowed or more general non-entangling operations are allowed, bipartite entangled states may be regarded as a valuable resource. Resource theory also applies if the allowed operations are required to obey certain symmetries; then states breaking this symmetry become a resource. In thermodynamics, states deviating from thermal equilibrium are a resource. Entanglement theory, as a particularly well developed resource theory, provides guidance and tools which are broadly applicable to many different interesting situations.

### 10.5.2 Squashed entanglement

As an example of an alternative bipartite entanglement measure, consider the *squashed entanglement* $E_{\mathrm{sq}}$, defined by
$$
E_{\mathrm{sq}}(\bm{\rho}_{AB}) = \inf \left\{ \frac{1}{2} I(A; B|C) : \bm{\rho}_{AB} = \mathrm{tr}_C(\bm{\rho}_{ABC}) \right\}. \tag{10.193}
$$
The squashed entanglement of $\bm{\rho}_{AB}$ is the greatest lower bound on the quantum conditional mutual information of all possible extensions of $\bm{\rho}_{AB}$ to a tripartite state $\bm{\rho}_{ABC}$; it can be shown to be an entanglement monotone. The locution "squashed" conveys that choosing an optimal conditioning system $C$ squashes out the non-quantum correlations between $A$ and $B$.

For pure states the extension is superfluous, so that
$$
E_{\mathrm{sq}}(|\psi\rangle_{AB}) = \frac{1}{2}I(A; B) = H(A) = H(B) = E(|\psi\rangle_{AB}). \tag{10.194}
$$
For a separable state, we may choose the extension
$$
\bm{\rho}_{ABC} = \sum_x p(x) |\alpha(x)\rangle\langle\alpha(x)|_A \otimes |\beta(x)\rangle\langle\beta(x)|_B \otimes |x\rangle\langle x|_C, \tag{10.195}
$$
where $\{|x\rangle_C\}$ is an orthonormal set; the state $\bm{\rho}_{ABC}$ has the block-diagonal form eq.(10.87) and hence $I(A; B|C) = 0$. Conversely, if $\bm{\rho}_{AB}$ has any extension $\bm{\rho}_{ABC}$ with $I(A; B|C) = 0$, then $\bm{\rho}_{ABC}$ has the form eq.(10.87) and therefore $\bm{\rho}_{AB}$ is separable.

$E_{\mathrm{sq}}$ is difficult to compute, because the infimum is to be evaluated over all possible extensions, where the system $C$ may have arbitrarily high dimension. This property also raises the logical possibility that there are nonseparable states for which the infimum vanishes; conceivably, though a nonseparable $\bm{\rho}_{AB}$ can have no finite-dimensional extension for which $I(A; B|C) = 0$, perhaps $I(A; B|C)$ can approach zero as the dimension of $C$ increases. Fortunately, though this is not easy to show, it turns out that $E_{\mathrm{sq}}$ is strictly positive for any nonseparable state. In this sense, then, it is a faithful entanglement measure, strictly positive if and only if the state is nonseparable.

One desirable property of $E_{\mathrm{sq}}$, not shared by $E_C$ and $E_D$, is its additivity on tensor products (Exercise 10.6),
$$
E_{\mathrm{sq}}(\bm{\rho}_{AB} \otimes \bm{\rho}_{A'B'}) = E_{\mathrm{sq}}(\bm{\rho}_{AB}) + E_{\mathrm{sq}}(\bm{\rho}_{A'B'}). \tag{10.196}
$$
Though, unlike $E_C$ and $E_D$, squashed entanglement does not have an obvious operational meaning, any additive entanglement monotone which matches $E$ for bipartite pure states is bounded above and below by $E_C$ and $E_D$ respectively,
$$
E_C \ge E_{\mathrm{sq}} \ge E_D. \tag{10.197}
$$

### 10.5.3 Entanglement monogamy

Classical correlations are *polyamorous*; they can be shared among many parties. If Alice and Bob read the same newspaper, then they have information in common and become correlated. Nothing prevents Claire from reading the same newspaper; then Claire is just as strongly correlated with Alice and with Bob as Alice and Bob are with one another. Furthermore, David, Edith, and all their friends can read the newspaper and join the party as well.

Quantum correlations are not like that; they are harder to share. If Bob's state is pure, then the tripartite quantum state is a product $\bm{\rho}_B \otimes \bm{\rho}_{AC}$, and Bob is completely uncorrelated with Alice and Claire. If Bob's state is mixed, then he can be entangled with other parties. But if Bob is fully entangled with Alice (shares a pure state with Alice), then the state is a product $\bm{\rho}_{AB} \otimes \bm{\rho}_C$; Bob has used up all his ability to entangle by sharing with Alice, and Bob cannot be correlated with Claire at all. Conversely, if Bob shares a pure state with Claire, the state is $\bm{\rho}_A \otimes \bm{\rho}_{BC}$, and Bob is uncorrelated with Alice. Thus we say that quantum entanglement is *monogamous*.

Entanglement measures obey *monogamy inequalities* which reflect this tradeoff between Bob's entanglement with Alice and with Claire in a three-party state. Squashed entanglement, in particular, obeys a monogamy relation following easily from its definition, which was our primary motivation for introducing this quantity; we have
$$
E_{\mathrm{sq}}(A; B) + E_{\mathrm{sq}}(A; C) \le E_{\mathrm{sq}}(A; BC). \tag{10.198}
$$
In particular, in the case of a pure tripartite state, $E_{\mathrm{sq}} = H(A)$ is the (pure-state) entanglement shared between $A$ and $BC$. The inequality is saturated if Alice's system is divided into subsystems $A_1$ and $A_2$ such that the tripartite pure state is
$$
|\psi\rangle_{ABC} = |\psi_1\rangle_{A_1 B} \otimes |\psi_2\rangle_{A_2 C}. \tag{10.199}
$$
In general, combining eq.(10.197) with eq.(10.198) yields
$$
E_D(A; B) + E_D(A; C) \le E_C(A; BC); \tag{10.200}
$$
loosely speaking, the entanglement cost $E_C(A; BC)$ imposes a ceiling on Alice's ability to entangle with Bob and Claire individually, requiring her to trade in some distillable entanglement with Bob to increase her distillable entanglement with Claire.

To prove the monogamy relation eq.(10.198), we note that mutual information obeys a *chain rule* which is really just a restatement of the definition of conditional mutual information:
$$
I(A; BC) = I(A; C) + I(A; B|C). \tag{10.201}
$$
A similar equation follows directly from the definition if we condition on a fourth system $D$,
$$
I(A; BC|D) = I(A; C|D) + I(A; B|CD). \tag{10.202}
$$
Now, $E_{\mathrm{sq}}(A; BC)$ is the infimum of $I(A; BC|D)$ over all possible extensions of $\bm{\rho}_{ABC}$ to $\bm{\rho}_{ABCD}$. But since $\bm{\rho}_{ABCD}$ is also an extension of $\bm{\rho}_{AB}$ and $\bm{\rho}_{AC}$, we have
$$
I(A; BC|D) \ge E_{\mathrm{sq}}(A; C) + E_{\mathrm{sq}}(A; B) \tag{10.203}
$$
for any such extension. Taking the infimum over all $\bm{\rho}_{ABCD}$ yields eq.(10.198).

A further aspect of monogamy arises when we consider extending a quantum state to more parties. We say that the bipartite state $\bm{\rho}_{AB}$ of systems $A$ and $B$ is *$k$-extendable* if there is a $(k+1)$-part state $\bm{\rho}_{AB_1\dots B_k}$ whose marginal state on $AB_j$ matches $\bm{\rho}_{AB}$ for each $j = 1, 2, \dots k$, and such that $\bm{\rho}_{AB_1\dots B_k}$ is invariant under permutations of the $k$ systems $B_1, B_2 \dots B_k$. Separable states are $k$-extendable for every $k$, and entangled pure states are not even 2-extendable. Every entangled mixed state fails to be $k$-extendable for some finite $k$, and we may regard the maximal value $k_{\max}$ for which such a symmetric extension exists as a rough measure of how entangled the state is -- bipartite entangled states with larger and larger $k_{\max}$ are closer and closer to being separable.

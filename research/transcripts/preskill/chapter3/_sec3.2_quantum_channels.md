# Section 3.2: Quantum channels [PDF Pages 11-19]

<!-- ============================================================ -->
<!-- Source: chap3.pdf, Physical Pages: 11-19                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 11 -->
## 3.2 Quantum channels

### 3.2.1 The operator-sum representation

We now proceed to the next step in our program of understanding the behavior of one part of a bipartite quantum system. We have seen that a pure state of the bipartite system $AB$ may behave like a mixed state when we observe subsystem $A$ alone, and that an orthogonal measurement of the bipartite system can realize a (nonorthogonal) POVM on $A$ alone. Next we ask, if a state of the bipartite system undergoes unitary evolution, how do we describe the evolution of $A$ alone?

In effect, we have already answered this question in our discussion of generalized measurements. If system $A$ starts out in a pure state $|\psi\rangle$ (unentangled with $B$), and then interacts with $B$, the joint state of $AB$ has the form eq.(3.23); the resulting density operator for $A$ is found by tracing out $B$. Equivalently, we may imagine measuring system $B$ in the basis $\{|a\rangle\}$, but failing to record the measurement outcome, so we are forced to average over all the possible post-measurement states, weighted by their probabilities. The result is that the initial density operator $\boldsymbol{\rho} = |\psi\rangle\langle\psi|$ is subjected to a linear map $\mathcal{E}$, which acts as

$$
\mathcal{E}(\boldsymbol{\rho}) = \sum_a \boldsymbol{M}_a \boldsymbol{\rho} \boldsymbol{M}_a^\dagger,
$$ {#eq-3.32}

<!-- Page 12 -->
where the operators $\{\boldsymbol{M}_a\}$ obey the completeness relation eq.(3.25). Being linear, $\mathcal{E}$ acts as in eq.(3.32) not just on pure states, but on any density operator.

A linear map of the form eq.(3.32), where the $\{\boldsymbol{M}_a\}$ obey eq.(3.25), is called a *quantum channel*. The word "channel" is drawn from communication theory --- we are to imagine a sender who transmits the state $\boldsymbol{\rho}$ though a communication link to another party who receives the modified state $\mathcal{E}(\boldsymbol{\rho})$. Sometimes the word *superoperator* is used as a synonym for quantum channel, where "super" conveys that the map takes operators to operators rather than vectors to vectors. Yet another name for the same object is *trace-preserving completely positive map*, or *TPCP map* for short. The justification for this name will emerge shortly. Eq.(3.32) is said to be an *operator-sum representation* of the quantum channel, and the operators $\{\boldsymbol{M}_a\}$ are called the *Kraus operators* or *operation elements* of the channel.

A quantum channel maps density operators to density operators; that is, has the following easily verified properties:

1. *Linearity.* $\mathcal{E}(\alpha\boldsymbol{\rho}_1 + \beta\boldsymbol{\rho}_2) = \alpha\mathcal{E}(\boldsymbol{\rho}_1) + \beta\mathcal{E}(\boldsymbol{\rho}_2)$.
2. *Preserves Hermiticity.* $\boldsymbol{\rho} = \boldsymbol{\rho}^\dagger$ implies $\mathcal{E}(\boldsymbol{\rho}) = \mathcal{E}(\boldsymbol{\rho})^\dagger$.
3. *Preserves positivity.* $\boldsymbol{\rho} \ge 0$ implies $\mathcal{E}(\boldsymbol{\rho}) \ge 0$.
4. *Preserves trace.* $\text{tr}(\mathcal{E}(\boldsymbol{\rho})) = \text{tr}(\boldsymbol{\rho})$.

These properties partially explain the locution "trace-preserving completely positive map," except that we are still missing the reason for the modifier "completely." That's coming soon.

We've seen how a quantum channel acting on system $A$ arises from a unitary transformation acting on $A$ and $B$ followed by a partial trace on $B$. As in our discussion of generalized measurements, we can also run this argument backwards to see that any quantum channel may be realized this way. Given a quantum channel $\mathcal{E}$ acting on $A$ with Kraus operators $\{\boldsymbol{M}_a\}$, we may introduce the auxiliary system $B$ with Hilbert space dimension matching the number of Kraus operators. A unitary transformation may then be constructed whose action on $|\psi\rangle_A \otimes |0\rangle_B$ is as in eq.(3.23), from which the quantum channel $\mathcal{E}$ is obtained by tracing out $B$.

The operator-sum representation of a given quantum channel $\mathcal{E}$ is not unique, because we can perform the partial trace on $B$ in any basis we please. When expressed in terms of rotated basis states $\{|\mu\rangle\}$ such that

$$
|a\rangle = \sum_\mu |\mu\rangle V_{\mu a}
$$ {#eq-3.33}

<!-- Page 13 -->
for unitary $V$, the joint state of $AB$ becomes

$$
\sum_{a,\mu} \boldsymbol{M}_a|\psi\rangle_A \otimes |\mu\rangle_B V_{\mu a} = \sum_\mu \boldsymbol{N}_\mu |\psi\rangle_A \otimes |\mu\rangle_B
$$ {#eq-3.34}

where the new Kraus operators are

$$
\boldsymbol{N}_\mu = \sum_a V_{\mu a}\boldsymbol{M}_a.
$$ {#eq-3.35}

We will see soon that any two operator-sum representations of the same quantum channel are always related by such a unitary change of basis for the Kraus operators.

Quantum channels are important because they provide us with a formalism for discussing *decoherence*, the evolution of pure states into mixed states. *Unitary* evolution of $\boldsymbol{\rho}_A$ is the special case in which there is only one term in the operator sum. If there are two or more terms, then there are pure initial states of $A$ which become entangled with $B$ under evolution governed by the joint unitary transformation $U_{AB}$, and therefore the state of $A$ becomes mixed when we trace out $B$.

Two channels $\mathcal{E}_1$ and $\mathcal{E}_2$ can be composed to obtain another channel $\mathcal{E}_2 \circ \mathcal{E}_1$; if $\mathcal{E}_1$ describes evolution from yesterday to today, and $\mathcal{E}_2$ describes evolution from today to tomorrow, then $\mathcal{E}_2 \circ \mathcal{E}_1$ describes the evolution from yesterday to tomorrow. Specifically, if $\mathcal{E}_1$ has an operator-sum representation with $N$ Kraus operators $\{\boldsymbol{M}_a\}$, and $\mathcal{E}_2$ has an operator-sum representation with $M$ Kraus operators $\{\boldsymbol{N}_\mu\}$, then $\mathcal{E}_2 \circ \mathcal{E}_1$ has an operator-sum representation with $NM$ Kraus operators $\{\boldsymbol{N}_\mu \boldsymbol{M}_a\}$. Because we can compose them in this way, we say that quantum channels form a dynamical *semigroup*.

### 3.2.2 Reversibility

A unitary transformation $\boldsymbol{U}$ has a unitary inverse $\boldsymbol{U}^\dagger$. Thus if today's quantum state was obtained by applying $\boldsymbol{U}$ to yesterday's state, we can in principle recover yesterday's state by applying $\boldsymbol{U}^\dagger$ to today's state. Unitary time evolution is reversible.

Is the same true for general quantum channels? If channel $\mathcal{E}_1$ with Kraus operators $\{\boldsymbol{M}_a\}$ is inverted by channel $\mathcal{E}_2$ with Kraus operators $\{\boldsymbol{N}_\mu\}$, then for any pure state $|\psi\rangle$ we have

$$
\mathcal{E}_2 \circ \mathcal{E}_1(|\psi\rangle\langle\psi|) = \sum_{\mu,a} \boldsymbol{N}_\mu \boldsymbol{M}_a|\psi\rangle\langle\psi|\boldsymbol{M}_a^\dagger \boldsymbol{N}_\mu^\dagger = |\psi\rangle\langle\psi|.
$$ {#eq-3.36}

Since the left-hand side is a sum of positive terms, eq.(3.36) can hold only if each of these terms is proportional to $|\psi\rangle\langle\psi|$, hence

$$
\boldsymbol{N}_\mu \boldsymbol{M}_a = \lambda_{\mu a}\boldsymbol{I}
$$ {#eq-3.37}

<!-- Page 14 -->
for each $\mu$ and $a$. Using the completeness relation, we find

$$
\boldsymbol{M}_b^\dagger \boldsymbol{M}_a = \boldsymbol{M}_b^\dagger \left(\sum_\mu \boldsymbol{N}_\mu^\dagger \boldsymbol{N}_\mu\right) \boldsymbol{M}_a = \sum_\mu \lambda_{\mu b}^* \lambda_{\mu a}\boldsymbol{I} \equiv \beta_{ba}\boldsymbol{I}.
$$ {#eq-3.38}

where each $\beta_{aa}$ is real and positive unless $\boldsymbol{M}_a = 0$.

Since the channel $\mathcal{E}_1$ maps system $A$ to itself, each Kraus operator $\boldsymbol{M}_a$ is a square $d \times d$ matrix, where $d$ is the dimension of $A$. Therefore $\boldsymbol{M}_a$ has a polar decomposition, which yields

$$
\boldsymbol{M}_a = \boldsymbol{U}_a \sqrt{\boldsymbol{M}_a^\dagger \boldsymbol{M}_a} = \sqrt{\beta_{aa}}\boldsymbol{U}_a
$$ {#eq-3.39}

for some unitary $\boldsymbol{U}_a$, and it then follows that

$$
\boldsymbol{M}_b^\dagger \boldsymbol{M}_a = \sqrt{\beta_{aa}\beta_{bb}}\boldsymbol{U}_b^\dagger \boldsymbol{U}_a = \beta_{ba}\boldsymbol{I},
$$ {#eq-3.40}

and hence

$$
\boldsymbol{U}_a = \frac{\beta_{ba}}{\sqrt{\beta_{aa}\beta_{bb}}}\boldsymbol{U}_b
$$ {#eq-3.41}

for each $a$ and $b$. We conclude that each Kraus operator $\boldsymbol{M}_a$ is proportional to a single unitary matrix, and hence that $\mathcal{E}_1$ is a unitary map. A quantum channel can be inverted by another quantum channel only if it is unitary.

We have found that decoherence is irreversible. Once system $A$ becomes entangled with system $B$, we can't undo the damage to $A$ if we don't have access to $B$. Decoherence causes quantum information to leak to a system's environment, and because we cannot control the environment this information cannot be recovered.

This argument applies to a channel which maps $A$ to $A'$ as long as $A$ and $A'$ have the same dimension. But the conclusion can be evaded if $A'$ has a larger dimension than $A$, since in that case the Kraus operators are rectangular, and the polar decomposition does not apply. We will take advantage of this exception when developing the theory of quantum error correction in Chapter 7.

### 3.2.3 Quantum channels in the Heisenberg picture

We have described quantum channels using the *Schrödinger picture* in which the quantum state evolves with time. Sometimes it is convenient to use the *Heisenberg picture*, in which the state is stationary and the operators evolve instead.

When time evolution is unitary, in the Schrödinger picture the state vector at time $t$ is obtained from the state vector at time 0 by

$$
|\psi(t)\rangle = \boldsymbol{U}(t)|\psi(0)\rangle
$$ {#eq-3.42}

<!-- Page 15 -->
where $\boldsymbol{U}(t)$ is unitary, and correspondingly a density operator evolves according to

$$
\boldsymbol{\rho}(t) = \boldsymbol{U}(t)\boldsymbol{\rho}(0)\boldsymbol{U}(t)^\dagger.
$$ {#eq-3.43}

In the Heisenberg picture the density operator $\boldsymbol{\rho}$ is fixed, and an operator $\boldsymbol{A}$ evolves according to

$$
\boldsymbol{A}(t) = \boldsymbol{U}(t)^\dagger \boldsymbol{A}(0)\boldsymbol{U}(t).
$$ {#eq-3.44}

This evolution law is chosen so that the two pictures agree on the expectation values of observables at any time:

$$
\langle\boldsymbol{A}\rangle_{t,\text{Schr}} = \text{tr}(\boldsymbol{A}(0)\boldsymbol{\rho}(t)) = \text{tr}(\boldsymbol{A}(t)\boldsymbol{\rho}(0)) = \langle\boldsymbol{A}\rangle_{t,\text{Heis}},
$$ {#eq-3.45}

where we have used the cyclic property of the trace.

Likewise, if the $\mathcal{E}$ is a quantum channel which acts on density operators according to

$$
\boldsymbol{\rho}' = \mathcal{E}(\boldsymbol{\rho}) = \sum_a \boldsymbol{M}_a \boldsymbol{\rho} \boldsymbol{M}_a^\dagger,
$$ {#eq-3.46}

we may use an alternative description in which the state is fixed, but operators evolve as

$$
\boldsymbol{A}' = \mathcal{E}^*(\boldsymbol{A}) = \sum_a \boldsymbol{M}_a^\dagger \boldsymbol{A} \boldsymbol{M}_a,
$$ {#eq-3.47}

so that

$$
\text{tr}(\boldsymbol{A}\mathcal{E}(\boldsymbol{\rho})) = \text{tr}(\mathcal{E}^*(\boldsymbol{A})\boldsymbol{\rho}).
$$ {#eq-3.48}

We say that $\mathcal{E}^*$ is the *dual* or *adjoint* of $\mathcal{E}$.

Note that the dual of a channel need not be a channel, that is, might not be trace preserving. Instead, the completeness property of the Kraus operators $\{\boldsymbol{M}_a\}$ implies that

$$
\mathcal{E}^*(\boldsymbol{I}) = \boldsymbol{I}
$$ {#eq-3.49}

if $\mathcal{E}$ is a channel. We say that a map is *unital* if it preserves the identity operator, and conclude that the dual of a channel is a unital map.

Not all quantum channels are unital, but some are. If the Kraus operators of $\mathcal{E}$ satisfy

$$
\sum_a \boldsymbol{M}_a^\dagger \boldsymbol{M}_a = \boldsymbol{I} = \sum_a \boldsymbol{M}_a \boldsymbol{M}_a^\dagger,
$$ {#eq-3.50}

then $\mathcal{E}$ is unital and its dual $\mathcal{E}^*$ is also a unital channel. A unital quantum channel maps a maximally mixed density operator to itself; it is the quantum version of a doubly stochastic classical map, which maps probability distributions to probability distributions and preserves the uniform distribution.

<!-- Page 16 -->
### 3.2.4 Quantum operations

Generalized measurements and quantum channels are actually special cases of a more general notion called a *quantum operation*. As already noted, a generalized measurement can be realized by entangling a system with a meter and performing an orthogonal measurement on the meter, while a quantum channel arises if we measure the meter but completely forget the measurement outcome. In a quantum operation, we imagine measuring the meter, then retaining some of the information about the outcome while discarding the rest.

We may consider a generalized measurement described by Kraus operators $\{\boldsymbol{M}_{a\mu}\}$ which carry two labels, $a$ and $\mu$. These obey the usual completeness relation

$$
\sum_{a,\mu} \boldsymbol{M}_{a\mu}^\dagger \boldsymbol{M}_{a\mu} = \boldsymbol{I}.
$$ {#eq-3.51}

Suppose that, after a measurement that projects onto a definite value for both $a$ and $\mu$, we remember $a$ but forget $\mu$. Then, if the quantum state is $\boldsymbol{\rho}$ before the measurement, the post-measurement state (up to a normalization factor) is

$$
\mathcal{E}_a(\boldsymbol{\rho}) \equiv \sum_\mu \boldsymbol{M}_{a\mu}\boldsymbol{\rho}\boldsymbol{M}_{a\mu}^\dagger,
$$ {#eq-3.52}

where the outcome $a$ occurs with probability

$$
\text{Prob}(a) = \text{tr}\,\mathcal{E}_a(\boldsymbol{\rho}).
$$ {#eq-3.53}

Eq.(3.52) looks like the operator-sum representation for a quantum channel, except that now instead of the completeness relation the Kraus operators obey an inequality constraint

$$
\sum_\mu \boldsymbol{M}_{a\mu}^\dagger \boldsymbol{M}_{a\mu} \le \boldsymbol{I}.
$$ {#eq-3.54}

(We write $\boldsymbol{A} \le \boldsymbol{I}$ as a shorthand for the statement that $\boldsymbol{I} - \boldsymbol{A}$ is a nonnegative operator; that is, the eigenvalues of the Hermitian operator $\boldsymbol{A}$ are no larger than 1.) Our earlier notion of a generalized measurement is recovered when $\mu$ takes just one value (all information about the outcome is retained), and the operation becomes a channel when $a$ takes just one value (all information about the outcome is discarded).

The state needs to be renormalized to restore the unit trace condition; therefore under an operation the state really evolves nonlinearly according to

$$
\boldsymbol{\rho} \mapsto \frac{\mathcal{E}_a(\boldsymbol{\rho})}{\text{tr}\,\mathcal{E}_a(\boldsymbol{\rho})}.
$$ {#eq-3.55}

<!-- Page 17 -->
It is often convenient, though, to regard the operation as a linear map that takes $\boldsymbol{\rho}$ to a subnormalized state. For example, we may want to consider a sequence of $n$ consecutive measurements with outcomes $\{a_1, a_2, \dots, a_{n-1}, a_n\}$, where the $i$th measurement transforms the state according to the operation $\mathcal{E}_{a_i}$. Rather than renormalizing the state after each measurement, we can wait until after the final measurement in the sequence before renormalizing. The final state can then be written

$$
\boldsymbol{\rho} \mapsto \frac{\mathcal{E}_{a_n} \circ \mathcal{E}_{a_{n-1}} \circ \dots \circ \mathcal{E}_{a_2} \circ \mathcal{E}_{a_1}(\boldsymbol{\rho})}{\text{tr}\,\mathcal{E}_{a_n} \circ \mathcal{E}_{a_{n-1}} \circ \dots \circ \mathcal{E}_{a_2} \circ \mathcal{E}_{a_1}(\boldsymbol{\rho})}
$$ {#eq-3.56}

where the normalizing factor in the denominator is just the probability of the observed sequence of measurement outcomes.

### 3.2.5 Linearity

A quantum channel specifies how an initial density operator evolves to a final density operator. Why on general grounds should we expect evolution of a quantum state to be described by a linear map? One possible answer is that nonlinear evolution would be incompatible with interpreting the density operator as an ensemble of possible states.

Suppose that $\mathcal{E}$ maps an initial state at time $t=0$ to a final state at time $t=T$, and suppose that at time $t=0$ the initial state $\boldsymbol{\rho}_i$ is prepared with probability $p_i$. Then the time-evolved state at $t=T$ will be $\mathcal{E}(\boldsymbol{\rho}_i)$ with probability $p_i$.

On the other hand we argued in Chapter 2 that an ensemble in which $\boldsymbol{\sigma}_i$ is prepared with probability $q_i$ can be described by the convex combination of density operators

$$
\boldsymbol{\sigma} = \sum_i q_i \boldsymbol{\sigma}_i.
$$ {#eq-3.57}

Therefore the initial state is described by $\sum_i p_i \boldsymbol{\rho}_i$, which evolves to

$$
\boldsymbol{\rho}' = \mathcal{E}\left(\sum_i p_i \boldsymbol{\rho}_i\right).
$$ {#eq-3.58}

But we can also apply eq.(3.57) to the ensemble of final states, concluding that the final state may alternatively be described by

$$
\boldsymbol{\rho}' = \sum_i p_i \mathcal{E}(\boldsymbol{\rho}_i).
$$ {#eq-3.59}

Equating the two expressions for $\boldsymbol{\rho}'$ we find that $\mathcal{E}$ must act linearly, at least on convex combinations of states.

<!-- Page 18 -->
Similar reasoning applies to quantum operations, if we regard the normalization of an operation $\mathcal{E}_a$ as indicating the probability of the corresponding measurement outcome. Suppose again that the initial state $\boldsymbol{\rho}_i$ is prepared with *a priori* probability $p_i$ and subsequently measured. If the state is $\boldsymbol{\rho}_i$ then measurement outcome $a$ occurs with conditional probability $p(a|i)$, and the post-measurement state is $\mathcal{E}_a(\boldsymbol{\rho}_i)/p(a|i)$; hence the state ensemble after the measurement is described by the density operator

$$
\boldsymbol{\rho}' = \sum_i p(i|a)\frac{\mathcal{E}_a(\boldsymbol{\rho}_i)}{p(a|i)},
$$ {#eq-3.60}

where $p(i|a)$ is the *a posteriori* probability that state $\boldsymbol{\rho}_i$ was prepared, taking into account the information gained by doing the measurement. On the other hand, applying the operation $\mathcal{E}_a$ to the convex combination of the initial states $\{\boldsymbol{\rho}_i\}$ yields

$$
\boldsymbol{\rho}' = \frac{\mathcal{E}_a\left(\sum_i p_i \boldsymbol{\rho}_i\right)}{p_a}.
$$ {#eq-3.61}

Invoking Bayes' rule

$$
p_i p(a|i) = p_a p(i|a)
$$ {#eq-3.62}

we see that the operation $\mathcal{E}_a$ is required to be a linear map:

$$
\mathcal{E}_a\left(\sum_i p_i \boldsymbol{\rho}_i\right) = \sum_i p_i \mathcal{E}_a(\boldsymbol{\rho}_i).
$$ {#eq-3.63}

### 3.2.6 Complete positivity

A quantum channel is a linear map taking density operators to density operators. In particular, if its input is a nonnegative operator than so is its output. We therefore say that a channel is a *positive map*.

But a channel has a stronger property than mere positivity; it is *completely positive*. This means that the channel remains positive even when we consider it to be acting on just part of a larger system.

If a channel $\mathcal{E}$ maps linear operators on Hilbert space $\mathcal{H}_A$ to linear operators on Hilbert space $\mathcal{H}_{A'}$, we will usually express this more economically by saying $\mathcal{E}$ maps $A$ to $A'$. We may extend the input Hilbert space to $\mathcal{H}_A \otimes \mathcal{H}_B$, and consider the extended channel $\mathcal{E} \otimes I$ mapping $AB$ to $A'B$. We say that $\mathcal{E}$ is *completely positive* if any such extension of $\mathcal{E}$ is positive.

Clearly, quantum channels are completely positive, because if $\mathcal{E}$ has an operator-sum representation with Kraus operators $\{\boldsymbol{M}_a\}$, then $\mathcal{E} \otimes I$ has an operator-sum representation with Kraus operators $\{\boldsymbol{M}_a \otimes \boldsymbol{I}\}$.

<!-- Page 19 -->
Likewise, quantum operations, though not necessarily trace preserving, are also completely positive.

It is perfectly reasonable to demand that a channel be completely positive if it is to describe the time evolution of a quantum system --- even though the channel acts on just part of the world, it should map an initial state of the whole world to a final state of the whole world. It is therefore important to note that not all positive maps are completely positive; complete positivity is a stronger condition.

A simple example is the transpose map $T$, mapping the $d$-dimensional system $A$ to itself. In a particular basis $\{|i\rangle\}$, $T$ acts as

$$
T : |i\rangle\langle j| \mapsto |j\rangle\langle i|
$$ {#eq-3.64}

and hence

$$
T : \boldsymbol{\rho} \mapsto \boldsymbol{\rho}^T.
$$ {#eq-3.65}

The map $T$ is evidently positive because

$$
\langle\psi|\boldsymbol{\rho}^T|\psi\rangle = \sum_{i,j}\psi_j^* (\boldsymbol{\rho}^T)_{ji}\psi_i = \sum_{i,j}\psi_i (\boldsymbol{\rho})_{ij}\psi_j^* = \langle\psi^*|\boldsymbol{\rho}|\psi^*\rangle
$$ {#eq-3.66}

for any vector $|\psi\rangle$; therefore $\boldsymbol{\rho}^T$ is nonnegative if $\boldsymbol{\rho}$ is.

But $T$ is not completely positive. Consider the (unconventionally normalized) maximally entangled state on $AB$, where $B$ is also $d$-dimensional:

$$
|\tilde{\Phi}\rangle_{AB} = \sum_{i=0}^{d-1} |i\rangle_A \otimes |i\rangle_B \equiv \sum_i |i,i\rangle.
$$ {#eq-3.67}

The extension of $T$ acts on this state as

$$
T \otimes I : |\tilde{\Phi}\rangle\langle\tilde{\Phi}| = \sum_{i,j} |i\rangle\langle j| \otimes |i\rangle\langle j| \mapsto \sum_{i,j} |j\rangle\langle i| \otimes |i\rangle\langle j| \equiv \sum_{i,j} |j,i\rangle\langle i,j|;
$$ {#eq-3.68}

that is, it maps $|\tilde{\Phi}\rangle\langle\tilde{\Phi}|$ to the SWAP operator which interchanges the systems $A$ and $B$:

$$
\text{SWAP} : |\psi\rangle_A \otimes |\phi\rangle_B = \sum_{i,j}\psi_i \phi_j |i,j\rangle \mapsto \sum_{i,j}\phi_j \psi_i |j,i\rangle = |\phi\rangle_A \otimes |\psi\rangle_B.
$$ {#eq-3.69}

Since the square of SWAP is the identity, its eigenvalues are $\pm 1$. States which are symmetric under interchange of $A$ and $B$ have eigenvalue 1, while antisymmetric states have eigenvalue -1. Thus SWAP has negative eigenvalues, which means that $T \otimes I$ is not positive and therefore $T$ is not completely positive.

# Section 8.3: Quantum Computing with Nonabelian Fluxons and Generalized Anyon Models [PDF Pages 32-42]

<!-- ============================================================ -->
<!-- Source: chap8.pdf, Physical Pages: 32-42                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 32 -->
## 9.11 Quantum computing with nonabelian fluxons

A model of anyons is characterized by the answers to two basic questions: (1) What happens when two anyons are combined together (what are the *fusion rules*)? (2) What happens when two anyons are exchanged (what are the *braiding rules*)? We have discussed how these questions

<!-- Page 33 -->
are answered in the special case of a nonabelian superconductor model associated with a nonabelian finite group $G$, and now we wish to see how these fusion and braiding rules can be invoked in a simulation of a quantum circuit.

In formulating the simulation, we will assume these physical capabilities:

*Pair creation and identification.* We can create pairs of particles, and for each pair we can identify the particle type (the conjugacy class $\alpha$ of the flux of each particle in the pair, and the particles's charge --- an irreducible representation $R^{(\alpha)}$ of the flux's normalizer group $N(\alpha)$). This assumption is reasonable because there is no symmetry relating particles of different types; they have distinguishable physical properties --- for example, different energy gaps and effective masses. In practice, the only particle types that will be needed are fluxons that carry no charge and chargeons that carry no flux.

*Pair annihilation.* We can bring two particles together, and observe whether the pair annihilates completely. Thus we obtain the answer to the question: Does this pair of particles have trivial flux and charge, or not? This assumption is reasonable, because if the pair carries a nontrivial value of some conserved quantity, a localized excitation must be left behind when the pair fuses, and this leftover particle is detectable in principle.

*Braiding.* We can guide the particles along specified trajectories, and so perform exchanges of the particles. Quantum gates will be simulated by choosing particles world lines that realize particular braids.

These primitive capabilities allow us to realize some further derived capabilities that will be used repeatedly. First, we can use the chargeons to calibrate the fluxons and assemble a flux bureau of standards. Suppose that we are presented with two pairs of fluxons in the states $|a, a^{-1}\rangle$ and $|b, b^{-1}\rangle$, and we wish to determine whether the fluxes $a$ and $b$ match or not. We create a chargeon-antichargeon pair, where the charge of the chargeon is the irreducible representation $R$ of $G$. Then we carry the chargeon around a closed path that encloses the first member of the first fluxon pair and the second member of the second fluxon pair, we reunite the chargeon and antichargeon, and observed whether the chargeon pair annihilates or not. Since the total flux enclosed by the chargeon's path is $ab^{-1}$, the chargeon pair annihilates with probability

$$
\text{Prob}(0) = \left|\frac{\chi^R(ab^{-1})}{|R|}\right|^2,
$$ {#eq-8.49}

<!-- Page 34 -->
which is less than one if the flux $ab^{-1}$ is not the identity (assuming that the representation $R$ is not one-dimensional and represents $ab^{-1}$ nontrivially). Thus, if annihilation of the chargeon pair does not occur, we know for sure that $a$ and $b$ are distinct fluxes, and each time annihilation does occur, it becomes increasingly likely that $a$ and $b$ are equal. By repeating this procedure a modest number of times, we can draw a conclusion about whether $a$ and $b$ are the same, with high statistical confidence.

This procedure allows us to sort the fluxon pairs into bins, where each pair in a bin has the same flux. If a bin contains $n$ pairs, its state is, in general, a mixture of states of the form

$$
\sum_{a \in G} \psi_a |a, a^{-1}\rangle^{\otimes n}.
$$ {#eq-8.50}

By discarding just one pair in the bin, each such state becomes a mixture

$$
\sum_{a \in G} \rho_a \left(|a, a^{-1}\rangle \langle a, a^{-1}|\right)^{\otimes(n-1)};
$$ {#eq-8.51}

we may regard each bin as containing $(n - 1)$ pairs, all with the same definite flux, but where that flux is as yet unknown.

Which bin is which? We want to label the bins with elements of $G$. To arrive at a consistent labeling, we withdraw fluxon pairs from three different bins. Suppose the three pairs are $|a, a^{-1}\rangle$, $|b, b^{-1}\rangle$, and $|c, c^{-1}\rangle$, and that we want to check whether $c = ab$. We create a chargeon-antichargeon pair, carry the chargeon around a closed path that encloses the first member of the first fluxon pair, the first member of the second fluxon pair, and second member of the third fluxon pair, and observe whether the reunited chargeon pair annihilates or not. Since the total flux enclosed by the chargeon's path is $abc^{-1}$, by repeating this procedure we can determine with high statistical confidence whether $ab$ and $c$ are the same. Such observations allow us to label the bins in some manner that is consistent with the group composition rule. This labeling is unique apart from group automorphisms (and ambiguities arising from any automorphisms may be resolved arbitrarily).

Once the flux bureau of standards is established, we can use it to measure the unknown flux of an unlabeled pair. If the state of the pair to be measured is $|d, d^{-1}\rangle$, we can withdraw the labeled pair $|a, a^{-1}\rangle$ from a bin, and use chargeon pairs to measure the flux $ad^{-1}$. By repeating this procedure with other labeled fluxes, we can eventually determine the value of the flux $d$, realizing a projective measurement of the flux.

For a simulation of a quantum circuit using fluxons, we will need to perform logic gates that act upon the value of the flux. The basic gate we will use is realized by winding counterclockwise a fluxon pair with state

<!-- Page 35 -->
$|a, a^{-1}\rangle$ around the first member of another fluxon pair with state $|b, b^{-1}\rangle$. Since the $|a, a^{-1}\rangle$ pair has trivial total flux, the $|b, b^{-1}\rangle$ pair is unaffected by this procedure. But since in effect the flux $b$ travels counterclockwise about both members of the pair whose initial state was $|a, a^{-1}\rangle$, this pair is transformed as

$$
|a, a^{-1}\rangle \mapsto |bab^{-1}, ba^{-1}b^{-1}\rangle.
$$ {#eq-8.52}

We will refer to this operation as the *conjugation gate* acting on the fluxon pair.

To summarize what has been said so far, our primitive and derived capabilities allow us to: (1) Perform a projective flux measurement, (2) perform a destructive measurement that determines whether or not the flux and charge of a pair is trivial, and (3) execute a conjugation gate. Now we must discuss how to simulate a quantum circuit using these capabilities.

The next step is to decide how to encode qubits using fluxons. Appropriate encodings can be chosen in many ways; we will stick to one particular choice that illustrates the key ideas --- namely we will encode a qubit by using a pair of fluxons, where the total flux of the pair is trivial. We select two noncommuting elements $a, b \in G$, where $b^2 = e$, and choose a computational basis for the qubit

$$
|\bar{0}\rangle = |a, a^{-1}\rangle, \quad |\bar{1}\rangle = |bab^{-1}, ba^{-1}b^{-1}\rangle.
$$ {#eq-8.53}

The crucial point is that a single isolated fluxon with flux $a$ looks identical to a fluxon with the conjugate flux $bab^{-1}$. Therefore, if the two fluxons in a pair are kept far apart from one another, local interactions with the environment will not cause a superposition of the states $|\bar{0}\rangle$ and $|\bar{1}\rangle$ to decohere. The quantum information is protected from damage because it is stored nonlocally, by exploiting a topological degeneracy of the states where the fluxon and antifluxon are pinned to fixed and distantly separated positions.

However, in contrast with the topological degeneracy that arises in systems with abelian anyons, this protected qubit can be measured relatively easily, without resorting to delicate interferometric procedures that extract Aharonov-Bohm phases. We have already described how to measure flux using previously calibrated fluxons; therefore we can perform a projective measurement of the encoded Pauli operator $\bar{Z}$ (a projection onto the basis $\{|\bar{0}\rangle, |\bar{1}\rangle\}$). We can also measure the complementary Pauli operator $\bar{X}$, albeit destructively and imperfectly. The $\bar{X}$ eigenstates are

$$
|\pm\rangle = \frac{1}{\sqrt{2}}(|\bar{0}\rangle \pm |\bar{1}\rangle) \equiv \frac{1}{\sqrt{2}}\left(|a, a^{-1}\rangle \pm |bab^{-1}, ba^{-1}b^{-1}\rangle\right);
$$ {#eq-8.54}

<!-- Page 36 -->
therefore the state $|-\rangle$ is *orthogonal* to the zero-charge state

$$
|0; \alpha\rangle = \frac{1}{\sqrt{|\alpha|}} \left(\sum_{c \in \alpha} |c, c^{-1}\rangle\right),
$$ {#eq-8.55}

where $\alpha$ is the conjugacy class that contains $a$. On the other hand, the state $|+\rangle$ has a nonzero overlap with $|0; \alpha\rangle$

$$
\langle + | 0; \alpha\rangle = \sqrt{2/|\alpha|};
$$ {#eq-8.56}

Therefore, if the two members of the fluxon pair are brought together, complete annihilation is impossible if the state of the pair is $|-\rangle$, and occurs with probability $\text{Prob}(0) = 2/|\alpha|$ if the state is $|+\rangle$.

Note that it is also possible to prepare a fluxon pair in the state $|+\rangle$. One way to do that is to create a pair in the state $|0; \alpha\rangle$. If $\alpha$ contains only the two elements $a$ and $bab^{-1}$ we are done. Otherwise, we compare the newly created pair with calibrated pairs in each of the states $|c, c^{-1}\rangle$, where $c \in \alpha$ and $c$ is distinct from both $a$ and $bab^{-1}$. If the pair fails to match any of these $|c, c^{-1}\rangle$ pairs, its state must be $|+\rangle$.

To go further, we need to characterize the computational power of the conjugation gate. Let us use a more compact notation, in which the state $|x, x^{-1}\rangle$ of a fluxon pair is simply denoted $|x\rangle$, and consider the transformations of the state $|x, y, z\rangle$ that can be built from conjugation gates. By winding the third pair through the first, either counterclockwise or clockwise, we can execute the gates

$$
|x, y, z\rangle \mapsto |x, y, xzx^{-1}\rangle, \quad |x, y, z\rangle \mapsto |x, y, x^{-1}zx\rangle,
$$ {#eq-8.57}

and by winding the third pair through the second, either counterclockwise or clockwise, we can execute

$$
|x, y, z\rangle \mapsto |x, y, yzy^{-1}\rangle, \quad |x, y, z\rangle \mapsto |x, y, y^{-1}zy\rangle;
$$ {#eq-8.58}

furthermore, by borrowing a pair with flux $|c\rangle$ from the bureau of standards, we can execute

$$
|x, y, z\rangle \mapsto |x, y, czc^{-1}\rangle
$$ {#eq-8.59}

for any constant $c \in G$. Composing these elementary operations, we can execute any gate of the form

$$
|x, y, z\rangle \mapsto |x, y, fzf^{-1}\rangle,
$$ {#eq-8.60}

where the function $f(x, y)$ can be expressed in *product form* --- that is, as a finite product of group elements, where the elements appearing in

<!-- Page 37 -->
the product may be the inputs $x$ and $y$, their inverses $x^{-1}$ and $y^{-1}$, or constant elements of $G$, each of which may appear in the product any number of times.

What are the functions $f(x, y)$ that can be expressed in this form? The answer depends on the structure of the group $G$, but the following characterization will suffice for our purposes. Recall that a subgroup $H$ of a finite group $G$ is *normal* if for any $h \in H$ and any $g \in G$, $ghg^{-1} \in H$, and recall that a finite group $G$ is said to be *simple* if $G$ has no normal subgroups other than $G$ itself and the trivial group $\{e\}$. It turns out that if $G$ is a simple nonabelian finite group, then any function $f(x, y)$ can be expressed in product form. In the computer science literature, a closely related result is often called *Barrington's theorem*.

In particular, then, if the group $G$ is a nonabelian simple group, there is a function $f$ realizable in product form such that

$$
f(a, a) = f(a, bab^{-1}) = f(bab^{-1}, a) = e, \quad f(bab^{-1}, bab^{-1}) = b.
$$ {#eq-8.61}

Thus for $x, y, z \in \{a, bab^{-1}\}$, the action eq. (9.60) causes the flux of the third pair to "flip" if and only if $x = y = bab^{-1}$; we have constructed from our elementary operations a Toffoli gate in the computational basis. Therefore, conjugation gates suffice for universal reversible *classical* computation acting on the standard basis states.

The nonabelian simple group of minimal order is $A_5$, the group of even permutations of five objects, with $|A_5| = 60$. Therefore, one concrete realization of universal classical computation using conjugation gates is obtained by choosing $a$ to be the three-cycle element $a = (345) \in A_5$, and $b$ to be the product of two-cycles $b = (12)(34) \in A_5$, so that $bab^{-1} = (435)$.

With this judicious choice of the group $G$, we achieve a topological realization of universal classical computation, but how can be go still further, to realize universal quantum computation? We have the ability to prepare computational basis states, to measure in the computational basis, and to execute Toffoli gates, but these tools are entirely classical. The only nonclassical tricks at our disposal are the ability to prepare $\bar{X} = 1$ eigenstates, and the ability to perform an imperfect destructive measurement of $\bar{X}$. Fortunately, these additional capabilities are sufficient.

In our previous discussions of quantum fault tolerance, we have noted that if we can do the classical gates Toffoli and CNOT, it suffices for universal quantum computation to be able to apply each of the Pauli operators $X, Y$, and $Z$, and to be able to perform projective measurements of each of $X, Y$, and $Z$. We already know how to apply the classical gate $X$ and to measure $Z$ (that is, project onto the computational basis). Projective measurement of $X$ and $Y$, and execution of $Z$, are still missing from our repertoire. (Of course, if we can apply $X$ and $Z$, we can also apply their product $ZX = iY$.)

<!-- Page 38 -->
Next, let's see how to elevate our imperfect destructive measurement of $X$ to a reliable projective measurement of $X$. Recall the action by conjugation of a CNOT on Pauli operators:

$$
\text{CNOT} : XI \mapsto XX,
$$ {#eq-8.62}

where the first qubit is the control and the second qubit is the target of the CNOT. Therefore, CNOT gates, together with the ability to prepare $X = 1$ eigenstates and to perform destructive measurements of $X$, suffice to realize projective measurements of $X$. We can prepare an ancilla qubit in the $X = 1$ eigenstate, perform a CNOT with the ancilla as control and the data to be measured as target, and then measure the ancilla destructively. The measurement prepares the data in an eigenstate of $X$, whose eigenvalue matches the outcome of the measurement of the ancilla. In our case, the destructive measurement is not fully reliable, but we can repeat the measurement multiple times. Each time we prepare and measure a fresh ancilla, and after a few repetitions, we have acceptable statistical confidence in the inferred outcome of the measurement.

Now that we can measure $X$ projectively, we can prepare $X = -1$ eigenstates as well as $X = 1$ eigenstates (for example, we follow a $Z$ measurement with an $X$ measurement until we eventually obtain the outcome $X = -1$). Then, by performing a CNOT gate whose target is an $X = -1$ eigenstate, we can realize the Pauli operator $Z$ acting on the control qubit.

It only remains to show that a measurement of $Y$ can be realized.

Measurement of $Y$ seems problematic at first, since our physical capabilities have not provided any means to distinguish between $Y = 1$ and $Y = -1$ eigenstates (that is, between a state $\psi$ and its complex conjugate $\psi^*$). However, this ambiguity actually poses no serious difficulty, because it makes no difference how the ambiguity is resolved. Were we to replace measurement of $Y$ by measurement of $-Y$ in our simulation of a unitary transformation $U$, the effect would be that $U^*$ is simulated instead; this replacement would not alter the probability distributions of outcomes for measurements in the standard computational basis.

To be explicit, we can formulate a protocol for measuring $Y$ by noting first that applying a Toffoli gate whose target qubit is an $X = -1$ eigenstate realizes the controlled-phase gate $\Lambda(Z)$ acting on the two control qubits. By composing this gate with the CNOT gate $\Lambda(X)$, we obtain the gate $\Lambda(iY)$ acting as

$$
\begin{aligned}
\Lambda(iY) : \quad & |X = +1\rangle \otimes |Y = +1\rangle \mapsto |Y = +1\rangle \otimes |Y = +1\rangle, \\
& |X = +1\rangle \otimes |Y = -1\rangle \mapsto |Y = -1\rangle \otimes |Y = -1\rangle, \\
& |X = -1\rangle \otimes |Y = +1\rangle \mapsto |Y = -1\rangle \otimes |Y = +1\rangle, \\
& |X = -1\rangle \otimes |Y = -1\rangle \mapsto |Y = +1\rangle \otimes |Y = -1\rangle,
\end{aligned}
$$ {#eq-8.63}

<!-- Page 39 -->
where the first qubit is the control and the second is the target. Now suppose that my trusted friend gives me just one qubit that he assures me has been prepared in the state $|Y = 1\rangle$. I know how to prepare $|X = 1\rangle$ states myself and I can execute $\Lambda(iY)$ gates; therefore since a $\Lambda(iY)$ gate with $|Y = 1\rangle$ as its target transforms $|X = 1\rangle$ to $|Y = 1\rangle$, I can make many copies of the $|Y = 1\rangle$ state I obtained from my friend. When I wish to measure $Y$, I apply the inverse of $\Lambda(iY)$, whose target is the qubit to be measured, and whose control is one of my $Y = 1$ states; then I perform an $X$ measurement of the ancilla to read out the result of the $Y$ measurement of the other qubit.

What if my friend lies to me, and gives me a copy of the state $|Y = -1\rangle$ instead? Then I'll make many copies of the $|Y = -1\rangle$ state, and I will be measuring $-Y$ when I think I am measuring $Y$. My simulation will work just the same as before; I'll actually be simulating the complex conjugate of the ideal circuit, but that won't change the final outcome of the quantum computation. If my friend flipped a coin to decide whether to give me the $|Y = 1\rangle$ state or the $|Y = -1\rangle$, this too would have no effect on the fidelity of my simulation. Therefore, it turns out I don't need by friend's help at all --- instead of using the $|Y = 1\rangle$ state I would have received from him, I may use the random state $\rho = I/2$ (an equally weighted mixture of $|Y = 1\rangle$ and $|Y = -1\rangle$, which I know how to prepare myself).

This completes the demonstration that we can simulate a quantum circuit efficiently and fault tolerantly using the fluxons and chargeons of a nonabelian superconductor, at least in the case where $G$ is a simple nonabelian finite group.[^sec8_3_footnote1] Viewed as a whole, including all state preparation and calibration of fluxes, the simulation can be described this way: Many pairs of anyons (fluxons and chargeons) are prepared, the anyon world lines follow a particular braid, and pairs of anyons are fused to see whether they will annihilate. The simulation is nondeterministic in the sense that the actual braid executed by the anyons depends on the outcomes of measurements performed (via fusion) during the course of the simulation. It is robust if the temperature is low compared to the energy gap, and if particles are kept sufficiently far apart from one another (except when pairs are being created and fused), to suppress the exchange of virtual anyons. Small deformations in the world lines of the particles have no effect on the outcome of the computation, as long as the braiding of the particles is in the correct topological class.

[^sec8_3_footnote1]: Mochon has shown that universal quantum computation is possible for a larger class of groups.

<!-- Page 40 -->
## 9.12 Anyon models generalized

Our discussion of the nonabelian superconductor model provides an existence proof for fault-tolerant quantum computation using anyons. But the model certainly has drawbacks. The scheme we described lacks beauty, elegance, or simplicity.

I have discussed this model in such detail because it is rather concrete and so helps us to build intuition about the properties of nonabelian anyons. But now that we understand better the key concepts of braiding and fusing in anyon models, we are ready to start thinking about anyons in a more general and abstract way. Our new perspective will lead us to new models, including some that are far simpler than those we have considered so far. We will be able to jettison much of the excess baggage that burdened the nonabelian superconductor model, such as the distinction between fluxons and chargeons, the calibration of fluxes, and the measurements required to simulate nonclassical gates. The simpler models we will now encounter are more naturally conducive to fault-tolerant computing, and more plausibly realizable in reasonable physical systems.

A model of anyons is a theory of particles on a two-dimensional surface (which we will assume to be the plane), where the particles carry locally conserved charges. We also assume that the theory has a mass gap, so that there are no long-range interactions between particles mediated by massless particles. The model has three defining properties:

1. A list of particle types. The types are labels that specify the possible values of the conserved charge that a particle can carry.
2. Rules for fusing and splitting, which specify the possible values of the charge that can be obtained when two particles of known charge are combined together, and the possible ways in which the charge carried by a single particle can be split into two parts.
3. Rules for braiding, which specify what happens when two particles are exchanged (or when one particle is rotated by $2\pi$).

Let's now discuss each of these properties in more detail.

### 9.12.1 Labels

I will use Latin letters $\{a, b, c, \dots\}$ for the labels that distinguish different types of particles. (For the case of the nonabelian superconductor, the label was $(\alpha, R^{(\alpha)})$, specifying a conjugacy class and an irreducible representation of the normalizer of the class, but now our notation will be more compact). We will assume that the set of possible labels is finite. The symbol $a$ represents the value of the conserved charge carried by the

<!-- Page 41 -->
particle. Sometimes we say that this label specifies a *superselection sector* of the theory. This term just means that the label $a$ is a property of a localized object that cannot be changed by any local physical process. That is, if one particle is at all times well isolated from other particles, its label will never change. In particular, local interactions between the particle and its environment may jostle the particle, but will not alter the label. This local conservation of charge is the essential reason that anyons are amenable to fault-tolerant quantum information processing.

There is one special label --- the identity label 1. A particle with the label 1 is really the same thing as no particle at all. Furthermore, for each particle label $a$ there is a conjugate label $\bar{a}$, and there is a charge conjugation operation $C$ (where $C^2 = I$) acting on the labels that maps a label to its conjugate:

$$
C : a \mapsto \bar{a} \mapsto a.
$$ {#eq-8.64}

It is possible for a label to be self-conjugate, so that $\bar{a} = a$. For example, $\bar{1} = 1$.

We will want to consider states of $n$ particles, where the particles have a specified order. Therefore, it is convenient to imagine that the particles are arranged on a particular line (such as the real axis) from left to right in consecutive order. The $n$ particles are labeled $(a_1, a_2, a_3, \dots, a_n)$, where $a_1$ is attached to the particle furthest to the left, $a_n$ to the particle furthest to the right.

### 9.12.2 Fusion spaces

When two particles are combined together, the composite object also has a charge. The *fusion rules* of the model specify the possible values of the total charge $c$ when the constituents have charges $a$ and $b$. These can be written

$$
a \times b = \sum_c N_{ab}^c c,
$$ {#eq-8.65}

where each $N_{ab}^c$ is a nonnegative integer and the sum is over the complete set of labels. Note that $a, b$ and $c$ are labels, not vector spaces; the product on the left-hand side is not a tensor product and the sum on the right-hand side is not a direct sum. Rather, the fusion rules can be regarded as an abstract relation on the label set that maps the ordered triple $(a, b; c)$ to $N_{ab}^c$. This relation is symmetric in $a$ and $b$ ($a \times b = b \times a$) --- the possible charges of the composite do not depend on whether $a$ is on the left or the right. Read backwards, the fusion rules specify the possible ways for the charge $c$ to split into two parts with charges $a$ and $b$.

If $N_{ab}^c = 0$, then charge $c$ cannot be obtained when we combine $a$ and $b$. If $N_{ab}^c = 1$, then $c$ can be obtained --- in a unique way. If $N_{ab}^c > 1$,

<!-- Page 42 -->
then $c$ can be obtained in $N_{ab}^c$ *distinguishable ways*. The notion that fusing two charges can yield a third charge in more than one possible way should be familiar from group representation theory. For example, the rule governing the fusion of two octet representations of $\text{SU}(3)$ is

$$
8 \times 8 = 1 + 8 + 8 + 10 + \overline{10} + 27,
$$ {#eq-8.66}

so that $N_{88}^8 = 2$. We emphasize again, however, that while the fusion rules for group representations can be interpreted as a decomposition of a tensor product of vector spaces as a direct sum of vector spaces, in general the fusion rules in an anyon model have no such interpretation.

The $N_{ab}^c$ distinguishable ways that $c$ can arise by fusing $a$ and $b$ can be regarded as the orthonormal basis states of a Hilbert space $V_{ab}^c$. We call $V_{ab}^c$ a *fusion space* and the states it contains *fusion states*. The basis elements for $V_{ab}^c$ may be denoted

$$
\{|ab; c, \mu\rangle, \quad \mu = 1, 2, \dots, N_{ab}^c\}.
$$ {#eq-8.67}

It is quite convenient to introduce a graphical notation for the fusion basis states:

– Figure: Fusion basis state $|ab; c, \mu\rangle$ (incoming lines $a, b$, fusion vertex $\mu$, outgoing line $c$) and dual basis state $\langle ab; c, \mu|$ (incoming line $c$, splitting vertex $\mu$, outgoing lines $a, b$) –

The state $|ab; c, \mu\rangle$ is represented as a circle containing the symbol $\mu$; connected to the circle are lines labeled $a$ and $b$ with incoming arrows, representing the charges being fused, and a line labeled $c$ with an outgoing arrow, representing the result of the fusion. There is a dual vector space $V_c^{ab}$ describing the states that arise when charge $c$ splits into charges $a$ and $b$, and a dual basis with the sense of the arrow reversed ($c$ coming in, $a$ and $b$ going out). The spaces $V_{ab}^c$ with different values of $c$ are mutually orthogonal, so that the fusion basis elements satisfy

$$
\langle ab; c' \mu' | ab; c, \mu\rangle = \delta_c^{c'} \delta_\mu^{\mu'},
$$ {#eq-8.68}

and the completeness of the fusion basis can be expressed as

$$
\sum_{c, \mu} |ab; c, \mu\rangle \langle ab; c, \mu| = I_{ab},
$$ {#eq-8.69}

where $I_{ab}$ denotes the projector onto the space $\bigoplus_c V_{ab}^c$, the full Hilbert space for the anyon pair $ab$.

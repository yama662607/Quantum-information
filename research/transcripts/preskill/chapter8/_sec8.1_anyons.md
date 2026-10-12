# Section 8.1: Anyons, anyone? [PDF Pages 4-13]

<!-- ============================================================ -->
<!-- Source: chap8.pdf, Physical Pages: 4-13                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 4 -->
# 9 Topological quantum computation

## 9.1 Anyons, anyone?

A central theme of quantum theory is the concept of *indistinguishable particles* (also called *identical particles*). For example, all electrons in the world are exactly alike. Therefore, for a system with many electrons, an operation that *exchanges* two of the electrons (swaps their positions) is a symmetry --- it leaves the physics unchanged. This symmetry is represented by a unitary transformation acting on the many-electron wave function.

For the indistinguishable particles in three-dimensional space that we normally talk about in physics, particle exchanges are represented in one of two distinct ways. If the particles are bosons (like, for example, $^4\text{He}$ atoms in a superfluid), then an exchange of two particles is represented by the identity operator: the wave function is invariant, and we say the particles obey Bose statistics. If the particles are fermions (like, for example, electrons in a metal), then an exchange is represented by multiplication by $(-1)$: the wave function changes sign, and we say that the particles obey Fermi statistics.

The concept of identical-particle statistics becomes ambiguous in one spatial dimension. The reason is that for two particles to swap positions in one dimension, the particles need to pass through one another. If the wave function changes sign when two identical particles are exchanged, we could say that the particles are noninteracting fermions, but we could just as well say that the particles are interacting bosons, such that the sign change is induced by the interaction as the particles pass one another. More generally, the exchange could modify the wavefunction by a multiplicative phase $e^{i\theta}$ that could take values other than $+1$ or $-1$, but we could account for this phase change by describing the particles as either bosons or fermions.

<!-- Page 5 -->
Thus, identical-particle statistics is a rather tame concept in three (or more) spatial dimensions and also in one dimension. But in between these two dull cases, in two dimensions, a remarkably rich variety of types of particle statistics are possible, so rich that we have far to go before we can give a useful classification of all of the possibilities.

Indistinguishable particles in two dimensions that are neither bosons nor fermions are called *anyons*. Anyons are a fascinating theoretical construct, but do they have anything to do with the physics of real systems that can be studied in the laboratory? The remarkable answer is: "Yes!" Even in our three-dimensional world, a two-dimensional gas of electrons can be realized by trapping the electrons in a thin layer between two slabs of semiconductor, so that at low energies, electron motion in the direction orthogonal to the layer is frozen out. In a sufficiently strong magnetic field and at sufficiently low temperature, and if the electrons in the material are sufficiently mobile, the two-dimensional electron gas attains a profoundly entangled ground state that is separated from all excited states by a nonzero energy gap. Furthermore, the low-energy particle excitations in the systems do not have the quantum numbers of electrons; rather they are anyons, and carry electric charges that are fractions of the electron charge. The anyons have spectacular effects on the transport properties of the sample, manifested as the fractional quantum Hall effect.

Anyons will be our next topic. But why? True, I have already said enough to justify that anyons are a deep and fascinating subject. But this is not a course about the unusual behavior of exotic phases attainable in condensed matter systems. It is a course about quantum computation.

In fact, there is a connection, first appreciated by Alexei Kitaev in 1997: anyons provide an unusual, exciting, and perhaps promising means of realizing fault-tolerant quantum computation.

So that sounds like something we should be interested in. After all, I have already given 12 lectures on the theory of quantum error correction and fault-tolerant quantum computing. It is a beautiful theory; I have enjoyed telling you about it and I hope you enjoyed hearing about it. But it is also daunting. We've seen that an ideal quantum circuit can be simulated faithfully by a circuit with noisy gates, provided the noisy gates are not *too* noisy, and we've seen that the overhead in circuit size and depth required for the simulation to succeed is reasonable. These observations greatly boost our confidence that large scale quantum computers will really be built and operated someday. Still, for fault tolerance to be effective, quantum gates need to have quite high fidelity (by the current standards of experimental physics), and the overhead cost of achieving fault tolerance is substantial. Even though reliable quantum computation with noisy gates is possible in principle, there always will

<!-- Page 6 -->
be a strong incentive to improve the fidelity of our computation by improving the hardware rather than by compensating for the deficiencies of the hardware through clever circuit design. By using anyons, we might achieve fault tolerance by designing hardware with an intrinsic resistance to decoherence and other errors, significantly reducing the size and depth blowups of our circuit simulations. Clearly, then, we have ample motivation for learning about anyons. Besides, it will be fun!

In some circles, this subject has a reputation (not fully deserved in my view) for being abstruse and inaccessible. I intend to start with the basics, and not to clutter the discussion with details that are mainly irrelevant to our central goals. That way, I hope to keep the presentation clear without really dumbing it down.

What are these goals? I will *not* be explaining how the theory of anyons connects with observed phenomena in fractional quantum Hall systems. In particular, *abelian* anyons arise in most of these applications. From a quantum information viewpoint, abelian anyons are relevant to robust *storage* of quantum information (and we have already gotten a whiff of that connection in our study of toric quantum codes). We will discuss abelian anyons here, but our main interest will be in *nonabelian* anyons, which as we will see can be endowed with surprising computational power.

Kitaev (quant-ph/9707021) pointed out that a system of nonabelian anyons with suitable properties can efficiently simulate a quantum circuit; this idea was elaborated by Ogburn and me (quant-ph/9712048), and generalized by Mochon (quant-ph/0206128, quant-ph/0306063). In Kitaev's original scheme, measurements were required to simulate some quantum gates. Freedman, Larsen and Wang (quant-ph/000110) observed that if we use the right kind of anyons, all measurements can be postponed until the readout of the final result of the computation. Freedman, Kitaev, and Wang (quant-ph/0001071) also showed that a system of anyons can be simulated efficiently by a quantum circuit; thus the anyon quantum computer and the quantum circuit model have equivalent computational power. The aim of these lectures is to explain these important results.

We will focus on the applications of anyons to quantum computing, not on the equally important issue of how systems of anyons with desirable properties can be realized in practice.[^fn-8.1] It will be left to you to figure that out!

[^fn-8.1]: Two interesting approaches to realizing nonabelian anyons --- using superconducting junction arrays and using cold atoms trapped in optical lattices --- have been discussed in the recent literature.

<!-- Page 7 -->
## 9.2 Flux-charge composites

For those of us who are put off by abstract mathematical constructions, it will be helpful to begin our exploration of the theory of anyons by thinking about a concrete model. So let's start by recalling a more familiar concept, the *Aharonov-Bohm effect*.

Imagine electromagnetism in a two-dimensional world, where a "flux tube" is a localized "pointlike" object (in three dimensions, you may envision a plane intersecting a magnetic solenoid directed perpendicular to the plane). The flux might be enclosed behind an impenetrable wall, so that an object outside can never visit the region where the magnetic field is nonzero. But even so, the magnetic field has a measurable influence on charged particles outside the flux tube. If an electric charge $q$ is adiabatically transported (counterclockwise) around a flux $\Phi$, the wave function of the charge acquires a *topological phase* $e^{iq\Phi}$ (where we use units with $\hbar = c = 1$). Here the word "topological" means that the Aharonov-Bohm phase is robust when we deform the trajectory of the charged particle --- all that matters is the "winding number" of the charge about the flux.

The concept of topological invariance arises naturally in the study of fault tolerance. Topological properties are those that remain invariant when we smoothly deform a system, and a fault-tolerant quantum gate is one whose action on protected information remains invariant (or nearly so) when we deform the implementation of the gate by adding noise. The topological invariance of the Aharonov-Bohm phenomenon is the essential property that we hope to exploit in the design of quantum gates that are intrinsically robust.

We usually regard the Aharonov-Bohm effect as a phenomenon that occurs in quantum electrodynamics, where the photon is exactly massless. But it is useful to recognize that Aharonov-Bohm phenomena can also occur in massive theories. For example, we might consider a "superconducting" system composed of charge $e$ particles, such that composite objects with charge $ne$ form a condensate (where $n$ is an integer). In this superconductor, there is a quantum of flux $\Phi_0 = 2\pi/ne$, the minimal nonzero flux such that a charge-$(ne)$ particle in the condensate, when transported around the flux, acquires a *trivial* Aharonov-Bohm phase. An isolated region that contains a flux quantum is an island of normal material surrounded by the superconducting condensate, prevented from spreading because the magnetic flux cannot penetrate into the superconductor. That is, it is a stable particle, what we could call a "fluxon." When one of the charge-$e$ particles is transported around a fluxon, its wave function acquires the nontrivial topological phase $e^{ie\Phi_0} = e^{2\pi i/n}$. But in the superconductor, the photon acquires a mass via the Higgs mechanism, and there are no massless particles. That topological phases

<!-- Page 8 -->
are compatible with massive theories is important, because massless particles are easily excited, a potentially copious source of decoherence.

Now, let's imagine that, in our two-dimensional world, flux and electric charge are permanently bound together (for some reason). A fluxon can be envisioned as flux $\Phi$ confined inside an impenetrable circular wall, and an electric charge $q$ is stuck to the *outside* of the wall. What is the angular momentum of this flux-charge composite? Suppose that we carefully rotate the object counterclockwise by angle $2\pi$, returning it to its original orientation. In doing so, we have transported the charge $q$ about the flux $\Phi$, generating a topological phase $e^{iq\Phi}$. This rotation by $2\pi$ is represented in Hilbert space by the unitary transformation

$$
\boldsymbol{U}(2\pi) = e^{-i 2\pi\boldsymbol{J}} = e^{iq\Phi},
$$ {#eq-8.1}

where $\boldsymbol{J}$ is the angular momentum. We conclude, then, that the possible eigenvalues of angular momentum are

$$
J = m - \frac{q\Phi}{2\pi} \quad (m = \text{integer}).
$$ {#eq-8.2}

We can characterize this spectrum by an angular variable $\theta \in [0, 2\pi)$, defined by $\theta = q\Phi \pmod{2\pi}$, and say that the eigenvalues are shifted away from integer values by $-\theta/2\pi$. We will refer to the phase $e^{i\theta}$ that represents a counterclockwise rotation by $2\pi$ as the *topological spin* of the composite object.

But shouldn't a rotation by $2\pi$ act trivially on a physical system (isn't it the same as doing nothing)? No, we know better than that, from our experience with *spinors* in three dimensions. For a system with fermion number $F$, we have

$$
e^{-2\pi i \boldsymbol{J}} = (-1)^F;
$$ {#eq-8.3}

if the fermion number is odd, the eigenvalues of $\boldsymbol{J}$ are shifted by $1/2$ from the integers. This shift is physically acceptable because there is a $(-1)^F$ *superselection rule*: no observable local operator can change the value of $(-1)^F$ (there is no physical process that can create or destroy an isolated fermion). Acting on a coherent superposition of states with different values of $(-1)^F$, the effect of $e^{-2\pi i\boldsymbol{J}}$ is

$$
e^{-i 2\pi \boldsymbol{J}} (a|\text{even } F\rangle + b|\text{odd } F\rangle) = a|\text{even } F\rangle - b|\text{odd } F\rangle.
$$ {#eq-8.4}

The relative sign in the superposition flips, but this has no detectable physical effects, since all observables are block diagonal in the $(-1)^F$ basis.

Similarly, in two dimensions, the shift in the angular momentum spectrum $e^{-2\pi i\boldsymbol{J}} = e^{i\theta}$ has no unacceptable physical consequences if there is

<!-- Page 9 -->
a $\theta$ superselection rule, ensuring that the relative phase in a superposition of states with different values of $\theta$ is physically inaccessible (not just in practice but even in principle). As for fermions, there is no allowed physical process that can create or destroy an isolated anyon.

In three dimensions, only $\theta = 0, \pi$ are allowed, because (as you probably know) of a topological property of the three-dimensional rotation group $\text{SO}(3)$: a closed path in $\text{SO}(3)$ beginning at the identity and ending at a rotation by $4\pi$ can be smoothly contracted to a trivial path. It follows that a rotation by $4\pi$ really is represented by the identity, and therefore that the eigenvalues of a rotation by $2\pi$ are $+1$ and $-1$. But the two-dimensional rotation group $\text{SO}(2)$ does not have this topological property, so that any value of $\theta$ is possible in principle.

Note that the angular momentum $\boldsymbol{J}$ changes sign under time reversal ($\boldsymbol{T}$) and also under parity ($\boldsymbol{P}$). Unless $\theta = 0$ or $\pi$, the spectrum of $\boldsymbol{J}$ is asymmetric about zero, and therefore a theory of anyons typically will not be $\boldsymbol{T}$ or $\boldsymbol{P}$ invariant. In our flux-charge composite model the origin of this symmetry breaking is not mysterious --- it arises from the nonzero magnetic field. But in a system with no intrinsic breaking of $\boldsymbol{T}$ and $\boldsymbol{P}$, if anyons occur then either these symmetries must be broken spontaneously, or else the particle spectrum must be "doubled" so that for each anyon with exchange phase $e^{i\theta}$ there also exists an otherwise identical particle with exchange phase $e^{-i\theta}$.

## 9.3 Spin and statistics

For identical particles in three dimensions, there is a well known connection between spin and statistics: indistinguishable particles with integer spin are bosons, and those with half-odd-integer spin are fermions. In two dimensions, the spin can be any real number. What does this new possibility of "fractional spin" imply about statistics? The answer is that statistics, too, can be "fractionalized"!

What happens if we perform an exchange of two of our flux-charge composite objects, in a counterclockwise sense? Each charge $q$ is adiabatically transported *half way* around the flux $\Phi$ of the other object. We can anticipate, then, that each charge will acquire an Aharonov-Bohm phase that is half of the phase generated by a complete revolution of the charge about the flux. Adding together the phases arising from the transport of both charges, we find that the exchange of the two flux-charge composites changes their wave function by the phase

$$
\exp\left[i\left(\frac{1}{2}q\Phi + \frac{1}{2}q\Phi\right)\right] = e^{iq\Phi} = e^{i\theta} = e^{-2\pi i\boldsymbol{J}}.
$$ {#eq-8.5}

The phase generated when the two objects are exchanged matches the

<!-- Page 10 -->
phase generated when one of the two objects is rotated by $2\pi$. Thus the connection between spin and statistics continues to hold, in a form that is a natural generalization of the connection that applies to bosons and fermions.

The origin of this connection is fairly clear in our flux-charge composite model, but in fact it holds much more generally. Why? Reading textbooks on relativistic quantum field theory, one can easily get the impression that the spin-statistics connection is founded on Lorentz invariance, and has something to do with the properties of the complexified Lorentz group. Actually, this impression is quite misleading. All that is essential for a spin-statistics connection to hold is *the existence of antiparticles*. Special relativity is not an essential ingredient.

Consider an anyon, characterized by the phase $\theta$, and suppose that this particle has a corresponding antiparticle. This means that the particle and its antiparticle, when combined, have trivial quantum numbers (in particular, zero angular momentum) and therefore that there are physical processes in which particle-antiparticle pairs can be created and annihilated. Draw a world line in spacetime that represents a process in which two particle-antiparticle pairs are created (one pair on the left and the other pair on the right), the particle from the pair on the right is exchanged *in a counterclockwise sense* with the particle from the pair on the left, and then both pairs reannihilate. (The world line has an orientation; if directed forward in time it represents a particle, and if directed backward in time it represents an antiparticle.) Turning our diagram $90^\circ$, we obtain a depiction of a process in which a single particle-antiparticle pair is created, the particle and antiparticle are exchanged in a *clockwise* sense, and then the pair reannihilates. Turning it $90^\circ$ yet again, we have a process in which two pairs are created and the *antiparticle* from the pair on the right is exchanged, in a counterclockwise sense, with the antiparticle from the pair on the left, before reannihilation.

$$
R_{aa} = R_{a\bar{a}}^{-1} = R_{\bar{a}\bar{a}}
$$

What do we conclude from these manipulations? Denote by $R_{ab}$ the unitary operator that represents a counterclockwise exchange of particles of types $a$ and b (so that the inverse operator $R_{ab}^{-1}$ represents a clockwise exchange), and denote by $\bar{a}$ the antiparticle of $a$. We have found that

$$
R_{aa} = R_{a\bar{a}}^{-1} = R_{\bar{a}\bar{a}}.
$$ {#eq-8.6}

<!-- Page 11 -->
If $a$ is an anyon with exchange phase $e^{i\theta}$, then its antiparticle $\bar{a}$ also has the *same* exchange phase. Furthermore, when $a$ and $\bar{a}$ are exchanged counterclockwise, the phase acquired is $e^{-i\theta}$.

These conclusions are unsurprising when we interpret them from the perspective of our flux-charge composite model of anyons. The antiparticle of the object with flux $\Phi$ and charge $q$ has flux $-\Phi$ and charge $-q$. Hence, when we exchange two antiparticles, the minus signs cancel and the effect is the same as though the particles were exchanged. But if we exchange a particle and an antiparticle, then the relative sign of charge and flux results in the exchange phase $e^{-iq\Phi} = e^{-i\theta}$.

But what is the connection between these observations about statistics and the spin? Continuing to contemplate the same spacetime diagram, let us consider its implications regarding the *orientation* of the particles. For keeping track of the orientation, it is convenient to envision the particle world line not as a thread but as a *ribbon* in spacetime. I claim that our process can be smoothly deformed to one in which a particle-antiparticle pair is created, the particle is rotated counterclockwise by $2\pi$, and then the pair reannihilates. A convenient way to verify this assertion is to take off your belt (or borrow a friend's). The buckle at one end specifies an orientation; point your thumb toward the buckle, and following the right-hand rule, twist the belt by $2\pi$ before rebuckling it. You should be able to check that you can lay out the belt to match the spacetime diagram for any of the exchange processes described earlier, and also for the process in which the particle rotates by $2\pi$.

Thus, in a topological sense, rotating a particle counterclockwise by $2\pi$ is really the same thing as exchanging two particles in a counterclockwise sense (or exchanging particle and antiparticle in a clockwise sense), which provides a satisfying explanation for a general spin-statistics connection.[^fn-8.2] I emphasize again that this argument invokes processes in which particle-antiparticle pairs are created and annihilated, and therefore the existence of antiparticles is an essential prerequisite for it to apply.

## 9.4 Combining anyons

We know that a composite object composed of two fermions is a boson. What happens when we build a composite object by combining two anyons?

[^fn-8.2]: Actually, this discussion has been oversimplified. Though it is adequate for abelian anyons, we will see that it must be amended for nonabelian anyons, because $R_{ab}$ has more than one eigenvalue in the nonabelian case. Similarly, the discussion in the next section of "combining anyons" will need to be elaborated because, in the nonabelian case, more than one kind of composite anyon can be obtained when two anyons are fused together.

<!-- Page 12 -->
Suppose that $a$ is an anyon with exchange phase $e^{i\theta}$, and that we build a "molecule" from $n$ of these $a$ anyons. What phase is acquired under a counterclockwise exchange of the two molecules?

The answer is clear in our flux-charge composite model. Each of the $n$ charges in one molecule acquires a phase $e^{i\theta/2}$ when transported half way around each of the $n$ fluxes in the other molecule. Altogether then, $2n^2$ factors of the phase $e^{i\theta/2}$ are generated, resulting in the total phase

$$
e^{i\theta_n} = e^{i n^2 \theta}.
$$ {#eq-8.7}

Said another way, the phase $e^{i\theta}$ occurs altogether $n^2$ times because in effect $n$ anyons in one molecule are being exchanged with $n$ anyons in the other molecule. Contrary to what we might have naively expected, if we split a fermion (say) into two identical constituents, the constituents have, not an exchange phase of $\sqrt{-1} = i$, but rather $(e^{i\pi})^{1/4} = e^{i\pi/4}$.

This behavior is compatible with the spin-statistics connection: the angular momentum $\boldsymbol{J}$ of the $n$-anyon molecule satisfies

$$
e^{-2\pi i\boldsymbol{J}_n} = e^{-2\pi i n^2 \boldsymbol{J}} = e^{i n^2 \theta}.
$$ {#eq-8.8}

For example, consider a molecule of two anyons, and imagine rotating the molecule counterclockwise by $2\pi$. Not only does each anyon in the molecule rotate by $2\pi$; in addition one of the anyons revolves around the other. One revolution is equivalent to two successive exchanges, so that the phase generated by the revolution is $e^{i 2\theta}$. The total effect of the two rotations and the revolution is the phase

$$
\exp [i (\theta + \theta + 2\theta)] = e^{i 4\theta}.
$$ {#eq-8.9}

Another way to understand why the angular momenta of the anyons in the molecule do not combine additively is to note that the total angular momentum of the molecule consists of two parts --- the spin angular momentum $\boldsymbol{S}$ of each of the two anyons (which is additive) and the orbital angular momentum $\boldsymbol{L}$ of the anyon pair. Because the counterclockwise transport of one anyon around the other generates the nontrivial phase $e^{i 2\theta}$, the dependence of the two-anyon wavefunction $\psi$ on the relative azimuthal angle $\phi$ is not single-valued; instead,

$$
\psi(\phi + 2\pi) = e^{-i 2\theta}\psi(\phi).
$$ {#eq-8.10}

This means that the spectrum of the orbital angular momentum $\boldsymbol{L}$ is shifted away from integer values:

$$
e^{-i 2\pi\boldsymbol{L}} = e^{2i\theta},
$$ {#eq-8.11}

<!-- Page 13 -->
and this orbital angular momentum combines additively with the spin $\boldsymbol{S}$ to produce the total angular momentum

$$
-2\pi \boldsymbol{J} = -2\pi \boldsymbol{L} - 2\pi \boldsymbol{S} = 2\theta + 2\theta + 2\pi(\text{integer}) = 4\theta + 2\pi(\text{integer}).
$$ {#eq-8.12}

What if, on the other hand, we build a molecule $\bar{a}a$ from an anyon $a$ and its antiparticle $\bar{a}$? Then, as we've seen, the spin $\boldsymbol{S}$ has the same value as for the $aa$ molecule. But the exchange phase has the opposite value, so that the noninteger part of the orbital angular momentum is $-2\pi \boldsymbol{L} = -2\theta$ instead of $-2\pi \boldsymbol{L} = 2\theta$, and the total angular momentum $\boldsymbol{J} = \boldsymbol{L} + \boldsymbol{S}$ is an integer. This property is necessary, of course, if the $\bar{a}a$ pair is to be able to annihilate without leaving behind an object that carries nontrivial angular momentum.

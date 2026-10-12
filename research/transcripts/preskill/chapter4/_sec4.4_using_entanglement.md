# Section 4.4: Using entanglement [PDF Pages 27-36]

<!-- ============================================================ -->
<!-- Source: chap4.pdf, Physical Pages: 27-36                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 27 -->
## 4.4 Using entanglement

After Bell's work, quantum entanglement became a subject of intensive study, among those interested in the foundations of quantum theory.

<!-- Page 28 -->
Gradually, a new viewpoint evolved: entanglement is not just a unique tool for exposing the weirdness of quantum mechanics, but also a potentially valuable *resource*. By exploiting entangled quantum states, we can perform tasks that are otherwise difficult or impossible.

### 4.4.1 Dense coding

Our first example is an application of entanglement to communication. Alice wants to send messages to Bob. She might send classical bits (like dots and dashes in Morse code), but let's suppose that Alice and Bob are linked by a *quantum* channel. For example, Alice can prepare qubits (like photons) in any polarization state she pleases, and send them to Bob, who measures the polarization along the axis of his choice. Is there any advantage to sending qubits instead of classical bits?

In principle, if their quantum channel has perfect fidelity, and Alice and Bob perform the preparation and measurement with perfect efficiency, then they are no *worse* off using qubits instead of classical bits. Alice can prepare, say, either $|\uparrow_z\rangle$ or $|\downarrow_z\rangle$, and Bob can measure along $\hat{z}$ to infer the choice she made. This way, Alice can send one classical bit with each qubit. But in fact, that is the best she can do. Sending one qubit at a time, no matter how she prepares it and no matter how Bob measures it, no more than one classical bit can be carried by each qubit (even if the qubits are entangled with one another). This statement, a special case of the Holevo bound on the classical information capacity of a quantum channel, will be derived in Chapter 5.

But now, let's change the rules a bit --- let's suppose that Alice and Bob share an entangled pair of qubits in the state $|\phi^+\rangle_{AB}$. The pair was prepared last year; one qubit was shipped to Alice and the other to Bob, in the hope that the shared entanglement would come in handy someday. Now, use of the quantum channel is very expensive, so Alice can afford to send only one qubit to Bob. Yet it is of the utmost importance for Alice to send Bob *two* classical bits of information.

Fortunately, Alice remembers about the entangled state $|\phi^+\rangle_{AB}$ that she shares with Bob, and she carries out a protocol that she and Bob had arranged for just such an emergency. On her member of the entangled pair, she can perform one of four possible unitary transformations:

1) $\bm{I}$ (she does nothing) ,
2) $\bm{\sigma}_1$ ($180^\circ$ rotation about $\hat{x}$-axis) ,
3) $\bm{\sigma}_2$ ($180^\circ$ rotation about $\hat{y}$-axis) ,
4) $\bm{\sigma}_3$ ($180^\circ$ rotation about $\hat{z}$-axis) .

<!-- Page 29 -->
As we have seen, by doing so, she transforms $|\phi^+\rangle_{AB}$ to one of 4 mutually orthogonal states:

1) $|\phi^+\rangle_{AB}$ ,
2) $|\psi^+\rangle_{AB}$ ,
3) $|\psi^-\rangle_{AB}$ (up to a phase) ,
4) $|\phi^-\rangle_{AB}$ .

Now, she sends her qubit to Bob, who receives it and then performs an orthogonal collective measurement on the pair that projects onto the maximally entangled basis. The measurement outcome unambiguously distinguishes the four possible actions that Alice could have performed. Therefore the single qubit sent from Alice to Bob has successfully carried 2 bits of classical information! Hence this procedure is called "dense coding."

A nice feature of this protocol is that, if the message is highly confidential, Alice need not worry that an eavesdropper will intercept the transmitted qubit and decipher her message. The transmitted qubit has density matrix $\bm{\rho}_A = \frac{1}{2}\bm{I}_A$, and so carries no information at all. All the information is in the correlations between qubits $A$ and $B$, and this information is inaccessible unless the adversary is able to obtain both members of the entangled pair. (Of course, the adversary can "jam" the channel, preventing the information from reaching Bob.)

From one point of view, Alice and Bob really *did* need to use the channel twice to exchange two bits of information. For example, we can imagine that Alice prepared the state $|\phi^+\rangle$ herself. Last year, she sent half of the state to Bob, and now she sends him the other half. So in effect, Alice has sent two qubits to Bob in one of four mutually orthogonal states, to convey two classical bits of information as the Holevo bound allows.

Still, dense coding is rather weird, for several reasons. First, Alice sent the first qubit to Bob long before she knew what her message was going to be. Second, each qubit by itself carries no information at all; all the information is encoded in the correlations between the qubits. Third, it would work just as well for Bob to prepare the entangled pair and send half to Alice; then two classical bits are transmitted from Alice to Bob by sending a single qubit from Bob to Alice and back again.

Anyway, when an emergency arose and two bits had to be sent immediately while only one use of the channel was possible, Alice and Bob could exploit the pre-existing entanglement to communicate more efficiently. They used entanglement as a resource.

<!-- Page 30 -->
### 4.4.2 Quantum teleportation

In dense coding, quantum information could be exploited to enhance the transmission of classical information. Specifically, if Alice and Bob share entanglement, then sending one qubit is sufficient to convey two classical bits. Now one wonders about the converse. If Alice and Bob share entanglement, can sending two classical bits suffice to convey a qubit?

Imagine that Charlie has prepared for Alice a qubit in the state $|\psi\rangle$, but Alice doesn't know anything about what state Charlie prepared. Bob needs this qubit desperately, and Alice wants to help him. But that darn quantum channel is down again! Alice can send only *classical* information to Bob.

She could try measuring $\vec{\bm{\sigma}} \cdot \hat{n}$, projecting her qubit to either $|\uparrow_{\hat{n}}\rangle$ or $|\downarrow_{\hat{n}}\rangle$. She could send the one-bit measurement outcome to Bob who could then proceed to prepare the state that Alice found. But you showed in Exercise ?? that Bob's state $|\varphi\rangle$ will not be a perfect copy of Alice's; on the average it will match Alice's qubit with fidelity
$$
F = |\langle\varphi|\psi\rangle|^2 = \frac{2}{3},
\tag{4.81}
$$
This fidelity is better than could have been achieved if Bob had merely chosen a state at random ($F = \frac{1}{2}$), but it is not nearly as good as the fidelity that Bob requires. Furthermore, as we will see in Chapter 5, there is no protocol in which Alice measures the qubit and sends classical information to Bob that achieves a fidelity better than 2/3.

Fortunately, Alice and Bob recall that they share the maximally entangled state $|\phi^+\rangle_{AB}$, which they prepared last year. Why not use the entanglement as a *resource*? If they are willing to consume the shared entanglement and communicate classically, can Alice send her qubit to Bob with fidelity better than 2/3?

In fact they can achieve fidelity $F = 1$, by carrying out the following protocol: Alice unites the unknown qubit $|\psi\rangle_C$ she wants to send to Bob with her half of the $|\phi^+\rangle_{AB}$ pair that she shares with Bob. She measures the two commuting observables
$$
\bm{\sigma}_1^{(C)} \otimes \bm{\sigma}_1^{(A)}, \quad \bm{\sigma}_3^{(C)} \otimes \bm{\sigma}_3^{(A)},
\tag{4.82}
$$
thus performing *Bell measurement* --- a projection of the two qubits onto one of the four maximally entangled states $|\phi^\pm\rangle_{CA}, |\psi^\pm\rangle_{CA}$. She sends her measurement outcome (two bits of classical information) to Bob over the classical channel. Upon receiving this information, Bob performs one

<!-- Page 31 -->
of four operations on his qubit
$$
\begin{array}{lcccc}
\text{Alice measures} & |\phi^+\rangle_{CA} & \to & \text{Bob applies} & \bm{I}^{(B)}, \\
\text{Alice measures} & |\psi^+\rangle_{CA} & \to & \text{Bob applies} & \bm{\sigma}_1^{(B)}, \\
\text{Alice measures} & |\psi^-\rangle_{CA} & \to & \text{Bob applies} & \bm{\sigma}_2^{(B)}, \\
\text{Alice measures} & |\phi^-\rangle_{CA} & \to & \text{Bob applies} & \bm{\sigma}_3^{(B)}.
\end{array}
\tag{4.83}
$$
This action transforms Bob's qubit (his member of the entangled pair that he initially shared with Alice) into a perfect copy of $|\psi\rangle_C$. This magic trick is called *quantum teleportation*.

How does it work? We merely note that for $|\psi\rangle = a|0\rangle + b|1\rangle$, we may write
$$
\begin{aligned}
|\psi\rangle_C |\phi^+\rangle_{AB} &= (a|0\rangle_C + b|1\rangle_C)\frac{1}{\sqrt{2}}(|00\rangle_{AB} + |11\rangle_{AB}) \\
&= \frac{1}{\sqrt{2}}(a|000\rangle_{CAB} + a|011\rangle_{CAB} + b|100\rangle_{CAB} + b|111\rangle_{CAB}) \\
&= \frac{1}{2}a(|\phi^+\rangle_{CA} + |\phi^-\rangle_{CA})|0\rangle_B + \frac{1}{2}a(|\psi^+\rangle_{CA} + |\psi^-\rangle_{CA})|1\rangle_B \\
&\quad + \frac{1}{2}b(|\psi^+\rangle_{CA} - |\psi^-\rangle_{CA})|0\rangle_B + \frac{1}{2}b(|\phi^+\rangle_{CA} - |\phi^-\rangle_{CA})|1\rangle_B \\
&= \frac{1}{2}|\phi^+\rangle_{CA}(a|0\rangle_B + b|1\rangle_B) \\
&\quad + \frac{1}{2}|\psi^+\rangle_{CA}(a|1\rangle_B + b|0\rangle_B) \\
&\quad + \frac{1}{2}|\psi^-\rangle_{CA}(a|1\rangle_B - b|0\rangle_B) \\
&\quad + \frac{1}{2}|\phi^-\rangle_{CA}(a|0\rangle_B - b|1\rangle_B) \\
&= \frac{1}{2}|\phi^+\rangle_{CA}|\psi\rangle_B + \frac{1}{2}|\psi^+\rangle_{CA}\bm{\sigma}_1|\psi\rangle_B \\
&\quad + \frac{1}{2}|\psi^-\rangle_{CA}(-i\bm{\sigma}_2)|\psi\rangle_B + \frac{1}{2}|\phi^-\rangle_{CA}\bm{\sigma}_3|\psi\rangle_B.
\end{aligned}
\tag{4.84}
$$
Thus we see that when Alice performs the Bell measurement on qubits $C$ and $A$, all four outcomes are equally likely. Once Bob learns Alice's measurement outcome, he possesses the pure state $\bm{\sigma}|\psi\rangle$, where $\bm{\sigma}$ is a known Pauli operator, one of $\{\bm{I}, \bm{\sigma}_1, \bm{\sigma}_2, \bm{\sigma}_3\}$. The action prescribed in eq. (4.83) restores Bob's qubit to the initial state $|\psi\rangle$.

Quantum teleportation is a curious procedure. Initially, Bob's qubit is completely uncorrelated with the unknown qubit $|\psi\rangle_C$, but Alice's Bell

<!-- Page 32 -->
measurement establishes a correlation between $A$ and $C$. The measurement outcome is in fact completely random, so Alice (and Bob) actually acquire no information at all about $|\psi\rangle$ by making this measurement. And that is a good thing, as we know that if they were to collect any information about the state they would unavoidably disturb the state.

How then does the quantum state manage to travel from Alice to Bob? It is a bit puzzling. On the one hand, we can hardly say that the two classical bits that were transmitted carried this information --- the bits were random. So we are tempted to say that the shared entangled pair made the teleportation possible. But remember that the entangled pair was actually prepared last year, long before Alice ever dreamed that she would be sending the qubit to Bob . . .

We should also note that the teleportation procedure is fully consistent with the no-cloning principle. True, a copy of the state $|\psi\rangle_B$ appeared in Bob's hands. But the original $|\psi\rangle_C$ had to be destroyed by Alice's measurement before the copy could be created.

Our findings about dense coding and quantum teleportation can be summarized as statements about how one type of resource can simulate another. Let us introduce the terminology *ebit* for an entangled pair of qubits shared by two parties ($e$ for entangled), and *cbit* for a classical bit ($c$ for classical). We teleport one qubit from Alice to Bob by consuming one ebit and sending two cbits, and we send two cbits from Alice and Bob via dense coding by consuming one ebit and transporting one qubit. Thus we may say
$$
\begin{aligned}
1\text{ ebit} + 2\text{ cbits} &\to 1\text{ qubit}, \\
1\text{ ebit} + 1\text{ qubit} &\to 2\text{ cbits},
\end{aligned}
\tag{4.85}
$$
meaning that the resources on the left suffice to simulate the resources on the right. Entanglement is essential in these protocols. Without ebits, a qubit is worth only one cbit, and without ebits, a "teleported" qubit has fidelity $F \le 2/3$.

### 4.4.3 Quantum teleportation and maximal entanglement

The teleportation concept has an air of mystery. One would like to understand more deeply why it works. A helpful clue is that to teleport with fidelity $F = 1$ the entangled state consumed in the protocol must be *maximally* entangled. And the crucial feature of bipartite maximally entangled states is that *either Alice or Bob* can transform one maximally entangled state to another by applying a local unitary transformation.

To see more clearly how quantum teleportation works, consider teleporting an $N$-dimensional system using an $N \times N$ maximally entangled

<!-- Page 33 -->
state of the form
$$
|\Phi\rangle = \frac{1}{\sqrt{N}}\sum_{i=0}^{N-1} |i\rangle\otimes|i\rangle.
\tag{4.86}
$$
A useful property of this state is
$$
\begin{aligned}
{}_{CA}\langle\Phi|\Phi\rangle_{AB} &= \frac{1}{N}\sum_{i,j}({}_C\langle i|\otimes{}_A\langle i|)(|j\rangle_A\otimes|j\rangle_B) \\
&= \frac{1}{N}\sum_i |i\rangle_B\,{}_C\langle i| \equiv \frac{1}{N}(\bm{T})_{BC}
\end{aligned}
\tag{4.87}
$$
Here we have defined the *transfer operator* $(\bm{T})_{BC}$ which has the property
$$
\bm{T}_{BC}|\varphi\rangle_C = \bm{T}_{BC}\left(\sum_i a_i|i\rangle_C\right) = \sum_i a_i|i\rangle_B = |\varphi\rangle_B;
\tag{4.88}
$$
it maps a state in $C$ to the identical state in $B$. This property has no invariant meaning independent of the choice of basis in $B$ and $C$; rather $\bm{T}_{BC}$ just describes an arbitrary way to relate the orthonormal bases of the two systems. Of course, Alice and Bob would need to align their bases in some way to verify that teleportation has really succeeded.

Now recall that any other $N \times N$ maximally entangled state has a Schmidt decomposition of the form
$$
\frac{1}{\sqrt{N}}\sum_{i=0}^{N-1} |i'\rangle\otimes|i\rangle,
\tag{4.89}
$$
and so can be expressed as
$$
|\Phi(\bm{U})\rangle \equiv \bm{U}\otimes\bm{I}|\Phi\rangle,
\tag{4.90}
$$
where
$$
\bm{U}|i\rangle = |i'\rangle = \sum_j |j\rangle U_{ji}.
\tag{4.91}
$$
Writing
$$
|\Phi(\bm{U})\rangle_{AB} = \frac{1}{\sqrt{N}}\sum_{i,j}|j\rangle_A\otimes|i\rangle_B\,U_{ji},
\tag{4.92}
$$
we can easily verify that
$$
{}_{CA}\langle\Phi(\bm{U})|\Phi(\bm{V}^T)\rangle_{AB} = \frac{1}{N}\left(\bm{V}\bm{U}^{-1}\right)_B\bm{T}_{BC},
\tag{4.93}
$$

<!-- Page 34 -->
where $\bm{V}^T$ denotes the transpose of $\bm{V}$ in the standard basis ($V_{ij}^T = V_{ji}$); in particular, then, the transfer operator can be expressed as
$$
\frac{1}{N}\bm{T}_{BC} = {}_{CA}\langle\Phi(\bm{U})|\Phi(\bm{U}^T)\rangle_{AB},
\tag{4.94}
$$
for any unitary $\bm{U}$.

Now suppose that Alice and Bob share $|\Phi\rangle_{AB}$, and that Charlie has prepared the state $|\psi\rangle_C$ and has deposited it in Alice's laboratory. Alice performs a measurement that projects $CA$ onto a maximally entangled basis, obtaining the outcome $|\Phi(\bm{U}_a)\rangle_{CA}$ for some unitary $\bm{U}_a$. Then we know from eq. (4.94) that *if* Alice and Bob had shared the state $|\Phi(\bm{U}_a^T)\rangle_{AB}$ instead of $|\Phi\rangle_{AB}$, then Alice's measurement would have prepared in Bob's lab a perfect replica of the state $|\psi\rangle$. Unfortunately, they did not have the foresight to share the right state to begin with. But it's not too late! Bob realizes that
$$
|\Phi(\bm{U}_a^T)\rangle = \bm{I}_A \otimes (\bm{U}_a)_B |\Phi\rangle_{AB},
\tag{4.95}
$$
and of course $(\bm{U}_a)_B$ commutes with Alice's measurement. Hence, when Bob hears from Alice that her measurement outcome was $|\Phi(\bm{U}_a)\rangle_{CA}$, he applies $(\bm{U}_a)_B$ to his half of the state he had shared with Alice. Then the protocol is equivalent to one in which they had shared the right maximally entangled state to begin with, and Bob's state has been transformed into $|\psi\rangle_B$!

This approach to teleportation has some conceptual advantages. For one, we can easily see that Alice is not required to perform an orthogonal measurement. To achieve teleportation with fidelity $F = 1$ it suffices that she perform a POVM with operation elements $\bm{M}_a$, where each $\bm{M}_a$ has the property
$$
\bm{M}_a^\dagger\bm{M}_a \propto |\Phi(\bm{U}_a)\rangle\langle\Phi(\bm{U}_a)|
\tag{4.96}
$$
for some unitary $\bm{U}_a$. Also, we can easily see how the teleportation protocol should be modified if the initial maximally entangled state that Alice and Bob share is not $|\Phi\rangle_{AB}$ but rather
$$
|\Phi(\bm{V}^T)\rangle_{AB} = \bm{I}_A \otimes \bm{V}_B |\Phi\rangle_{AB}.
\tag{4.97}
$$
If Alice's measurement outcome is $|\Phi(\bm{U}_a)\rangle_{CA}$, then eq. (4.93) tells us that the state Bob receives is
$$
\bm{V}\bm{U}_a^{-1}|\psi\rangle_B.
\tag{4.98}
$$
To recover $|\psi\rangle_B$, Bob must apply $\bm{U}_a\bm{V}^{-1}$.

<!-- Page 35 -->
The operator ordering in eq. (4.98) may seem counterintuitive at first --- it seems as though Alice's measurement ($\bm{U}_a$) precedes the preparation of the shared entangled state ($\bm{V}$). But this "time reversal" has a straightforward interpretation. If Alice's measurement outcome is $|\Phi(\bm{U}_a)\rangle_{CA}$, then Bob would have received a perfect copy of $|\psi\rangle$ if the initial entangled state had been $\bm{I}_A \otimes (\bm{U}_a)_B |\Phi\rangle_{AB}$. To simulate the situation in which the entangled state had been chosen properly from the start, Bob first applies $\bm{V}^{-1}$ to undo the "twist" in $|\Phi(\bm{V}^T)\rangle_{AB}$, recovering $|\Phi\rangle_{AB}$, and then applies $\bm{U}_a$ to transform the entangled state to the desired one.

There is a more fanciful interpretation of eq. (4.98) which, while not necessary, is nonetheless irresistable. We might "explain" how quantum information is transferred from Alice and Bob by following the world line of a qubit traveling in spacetime. The qubit moves forward in time from Charlie's preparation to Alice's measurement, then backward in time from the measurement to the initial preparation of the entangled pair, and finally forward in time again from the preparation of the pair to Bob's laboratory. Since this world line visits Alice's measurement before arriving at the preparation of the entanglement, $\bm{U}_a^{-1}$ acts "first" and $\bm{V}$ acts "later on."

### 4.4.4 Quantum software

Teleportation has some interesting applications. For example, imagine that Alice and Bob wish to apply the "quantum gate" $\bm{V}$ to the unknown state $|\psi\rangle_C$. But applying $\bm{V}$ requires sophisticated hardware that they can't afford.

A more economical alternative is to purchase *quantum software* from a vendor. The software is a bipartite state that the vendor certifies to be
$$
|\Phi(\bm{V}^T)\rangle_{AB} = \bm{I}_A \otimes \bm{V}_B |\phi\rangle_{AB}.
\tag{4.99}
$$
Alice's hardware is powerful enough for her to perform a measurement that projects onto the basis $\{|\Phi(\bm{U}_a)\rangle_{CA}\}$; once the outcome $a$ is known, the state $\bm{V}\bm{U}_a^{-1}|\psi\rangle_B$ has been prepared. Bob can then complete the execution of $\bm{V}$ to $|\psi\rangle$ by applying $\bm{V}\bm{U}_a\bm{V}^{-1}$.

This procedure may seem silly --- why assume that Bob is able to apply $\bm{V}\bm{U}_a\bm{V}^{-1}$ but unable to apply $\bm{V}$? In fact it is not so silly, and has important applications to fault-tolerant quantum computation that we will explore further in Chapter 8. In some cases, executing $\bm{V}\bm{U}_a\bm{V}^{-1}$ really is a lot easier than applying $\bm{V}$. Furthermore, Alice and Bob might be able to prepare the quantum software themselves, instead of buying it, even though they can't apply $\bm{V}$ reliably. This is possible because it is easier to verify that a *known* quantum state has been properly prepared than to

<!-- Page 36 -->
verify that a known unitary transformation has been successfully applied to an unknown state. If the hardware that applies $\bm{V}$ cannot be trusted, then we prefer to use it to prepare software offline, and then subject the software to quality assurance, rather than risk causing irrevocable damage to our unknown state through a faulty execution of $\bm{V}$.

Each application of $\bm{V}$ consumes one copy of the quantum software. Thus, this protocol for executing $\bm{V}$ with the help of quantum software uses entanglement as a resource.

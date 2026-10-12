# Section 4.5: Quantum cryptography [PDF Pages 36-41]

<!-- ============================================================ -->
<!-- Source: chap4.pdf, Physical Pages: 36-41                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 36 -->
## 4.5 Quantum cryptography

### 4.5.1 EPR quantum key distribution

Everyone has secrets, including Alice and Bob. Alice needs to send a highly private message to Bob, but Alice and Bob have a very nosy friend, Eve, who they know will try to listen in. Can they communicate with assurance that Eve is unable to eavesdrop?

Obviously, they should use some kind of code. Trouble is, aside from being very nosy, Eve is also very smart. Alice and Bob are not confident that they are clever enough to devise a code that Eve cannot break.

Except there is one coding scheme that is surely unbreakable. If Alice and Bob share a *private key*, a string of random bits known only to them, then Alice can convert her message to ASCII (a string of bits no longer than the key) add each bit of her message (modulo 2) to the corresponding bit of the key, and send the result to Bob. Receiving this string, Bob can add the key to it to extract Alice's message.

This scheme is secure because even if Eve should intercept the transmission, she will not learn anything because the transmitted string itself carries no information --- the message is encoded in a correlation between the transmitted string and the key (which Eve doesn't know).

There is still a problem, though, because Alice and Bob need to establish a shared random key, and they must ensure that Eve can't know the key. They could meet to exchange the key, but that might be impractical. They could entrust a third party to transport the key, but what if the intermediary is secretly in cahoots with Eve? They could use "public key" distribution protocols, but the security of such protocols is founded on assumptions about the computational resources available to a potential adversary. Indeed, we will see in Chapter 6 that public key protocols are vulnerable to attack by an eavesdropper who is equipped with a quantum computer.

Can Alice and Bob exploit quantum information (and specifically entanglement) to solve the key exchange problem? They can! Quantum key distribution protocols can be devised that are invulnerable to any attack

<!-- Page 37 -->
allowed by the laws of physics.

Let's suppose that Alice and Bob share a supply of entangled pairs, each prepared in the state $|\phi^+\rangle$. To establish a shared private key, they may carry out this protocol:

For each qubit in her/his possession, Alice and Bob decide to measure either $\bm{\sigma}_1$ or $\bm{\sigma}_3$. The decision is pseudo-random, each choice occuring with probability 1/2. Then, after the measurements are performed, both Alice and Bob publicly announce what observables they measured, but do not reveal the outcomes they obtained. For those cases (about half) in which they measured their qubits along different axes, their results are discarded (as Alice and Bob obtained uncorrelated outcomes). For those cases in which they measured along the same axis, their results, though random, are *perfectly correlated*. Hence, they have established a shared random key.

But, is this protocol really invulnerable to a sneaky attack by Eve? In particular, Eve might have clandestinely tampered with the pairs at some time in the past. Then the pairs that Alice and Bob possess might be (unbeknownst to Alice and Bob) not perfect $|\phi^+\rangle$'s, but rather pairs that are entangled with qubits in Eve's possession. Eve can then wait until Alice and Bob make their public announcements, and proceed to measure her qubits in a manner designed to acquire maximal information about the results that Alice and Bob obtained. Alice and Bob must protect themselves against this type of attack.

If Eve has indeed tampered with Alice's and Bob's pairs, then the most general possible state for an $AB$ pair and a set of $E$ qubits has the form
$$
\begin{aligned}
|\Upsilon\rangle_{ABE} &= |00\rangle_{AB}|e_{00}\rangle_E + |01\rangle_{AB}|e_{01}\rangle_E \\
&\quad + |10\rangle_{AB}|e_{10}\rangle_E + |11\rangle_{AB}|e_{11}\rangle_E,
\end{aligned}
\tag{4.100}
$$
where Eve's states $|e_{ij}\rangle_E$ are neither normalized nor mutually orthogonal. Now recall that the defining property or $|\phi^+\rangle$ is that it is an eigenstate with eigenvalue $+1$ of both $\bm{\sigma}_1^{(A)}\bm{\sigma}_1^{(B)}$ and $\bm{\sigma}_3^{(A)}\bm{\sigma}_3^{(B)}$. Suppose that $A$ and $B$ are able to verify that the pairs in their possession have this property. To satisfy $\bm{\sigma}_3^{(A)}\bm{\sigma}_3^{(B)} = 1$, we must have
$$
|\Upsilon\rangle_{AB} = |00\rangle_{AB}|e_{00}\rangle_E + |11\rangle_{AB}|e_{11}\rangle_E,
\tag{4.101}
$$
and to also satisfy $\bm{\sigma}_1^{(A)}\bm{\sigma}_1^{(B)} = 1$, we must have
$$
|\Upsilon\rangle_{ABE} = \frac{1}{\sqrt{2}}(|00\rangle_{AB} + |11\rangle_{AB})|e\rangle_E = |\phi^+\rangle_{AB}|e\rangle_E.
\tag{4.102}
$$
We see that it is possible for the $AB$ pairs to be eigenstates of $\bm{\sigma}_1^{(A)}\bm{\sigma}_1^{(B)}$ and $\bm{\sigma}_3^{(A)}\bm{\sigma}_3^{(B)}$ only if they are completely unentangled with Eve's qubits.

<!-- Page 38 -->
Therefore, Eve will not be able to learn anything about Alice's and Bob's measurement results by measuring her qubits. The random key is secure.

To verify the properties $\bm{\sigma}_1^{(A)}\bm{\sigma}_1^{(B)} = 1 = \bm{\sigma}_3^{(A)}\bm{\sigma}_3^{(B)}$, Alice and Bob can sacrifice a portion of their shared key, and publicly compare their measurement outcomes. They should find that their results are indeed perfectly correlated. If so they will have high statistical confidence that Eve is unable to intercept the key. If not, they have detected Eve's nefarious activity. They may then discard the key, and make a fresh attempt to establish a secure key.

As I have just presented it, the quantum key distribution protocol seems to require entangled pairs shared by Alice and Bob, but this is not really so. We might imagine that Alice prepares the $|\phi^+\rangle$ pairs herself, and then measures one qubit in each pair before sending the other to Bob. This is completely equivalent to a scheme in which Alice prepares one of the four states
$$
|\uparrow_z\rangle, |\downarrow_z\rangle, |\uparrow_x\rangle, |\downarrow_x\rangle,
\tag{4.103}
$$
(chosen at random, each occuring with probability 1/4) and sends the qubit to Bob. Bob's measurement and the verification are then carried out as before. This scheme (known as the BB84 quantum key distribution protocol) is just as secure as the entanglement-based scheme.$^\dagger$

Another intriguing variation is called the "time-reversed EPR" scheme. Here both Alice and Bob prepare one of the four states in eq. (4.103), and they both send their qubits to Charlie. Then Charlie performs a Bell measurement on the pair --- that is, he measures $\bm{\sigma}_1^{(A)}\bm{\sigma}_1^{(B)}$ and $\bm{\sigma}_3^{(A)}\bm{\sigma}_3^{(B)}$, orthogonally projecting out one of $|\phi^\pm\rangle |\psi^\pm\rangle$, and he publicly announces the result. Since all four of these states are simultaneous eigenstates of $\bm{\sigma}_1^{(A)}\bm{\sigma}_1^{(B)}$ and $\bm{\sigma}_3^{(A)}\bm{\sigma}_3^{(B)}$, when Alice and Bob both prepared their spins along the same axis (as they do about half the time) they share a single bit.$^\ddagger$ Of course, Charlie could be allied with Eve, but Alice and Bob can verify that Charlie and Eve have acquired no information as before, by comparing a portion of their key. This scheme has the advantage that Charlie could operate a central switching station by storing qubits received from many parties, and then perform his Bell measurement when two of the parties request a secure communication link. (Here we assume that Charlie has a stable quantum memory in which qubits can be stored

---
$^\dagger$ Except that in the EPR scheme, Alice and Bob can wait until just before they need to talk to generate the key, thus reducing the risk that Eve might at some point burglarize Alice's safe to learn what states Alice prepared (and so infer the key).

$^\ddagger$ Until Charlie makes his measurement, the states prepared by Bob and Alice are totally uncorrelated. A definite correlation (or anti-correlation) is established after Charlie performs his measurement.

<!-- Page 39 -->
accurately for as long as necessary.) A secure key can be established even if the quantum communication line is down temporarily, as long as both parties had the foresight to send their qubits to Charlie on an earlier occasion (when the quantum channel was open).

So far, we have made the unrealistic assumption that the quantum communication channel is perfect, but of course in the real world errors will occur. Therefore even if Eve has been up to no mischief, Alice and Bob will sometimes find that their verification test will fail. But how are they to distinguish errors due to imperfections of the channel from errors that occur because Eve has been eavesdropping?

To address this problem, Alice and Bob can enhance their protocol in two ways. First they implement (classical) error correction to reduce the effective error rate. For example, to establish each bit of their shared key they could actually exchange a block of three random bits. If the three bits are not all the same, Alice can inform Bob which of the three is different than the other two; Bob can flip that bit in his block, and *then* use majority voting to determine a bit value for the block. This way, Alice and Bob share the same key bit even if an error occured for one bit in the block of three.

However, error correction alone does not suffice to ensure that Eve has acquired negligible information about the key --- error correction must be supplemented by (classical) privacy amplification. For example, after performing error correction so that they are confident that they share the same key, Alice and Bob might extract a bit of "superkey" as the *parity* of $n$ key bits. To know *anything* about the parity of $n$ bits, Eve would need to know *something* about each of the bits. Therefore, the parity bit is considerably more secure, on the average, than each of the individual key bits.

If the error rate of the channel is low enough, one can show that quantum key distribution, supplemented by error correction and privacy amplification, is invulnerable to any attack that Eve might muster (in the sense that the information acquired by Eve can be guaranteed to be arbitrarily small). We will return to the problem of proving the security of quantum key distribution in Chapter 7.

### 4.5.2 No cloning

The security of quantum key distribution is based on an essential difference between quantum information and classical information. It is not possible to acquire information that *distinguishes* between nonorthogonal quantum states without *disturbing* the states.

For example, in the BB84 protocol, Alice sends to Bob any one of the four states $|\uparrow_z\rangle, |\downarrow_z\rangle, |\uparrow_x\rangle, |\downarrow_x\rangle$, and Alice and Bob are able to verify that

<!-- Page 40 -->
none of their states are perturbed by Eve's attempt at eavesdropping. Suppose, more generally, that $|\varphi\rangle$ and $|\psi\rangle$ are two nonorthogonal states in $\mathcal{H}$ ($\langle\psi|\varphi\rangle \ne 0$) and that a unitary transformation $U$ is applied to $\mathcal{H} \otimes \mathcal{H}_E$ (where $\mathcal{H}_E$ is a Hilbert space accessible to Eve) that leaves both $|\psi\rangle$ and $|\varphi\rangle$ undisturbed. Then
$$
\begin{aligned}
U : \quad & |\psi\rangle \otimes |0\rangle_E \to |\psi\rangle \otimes |e\rangle_E, \\
& |\varphi\rangle \otimes |0\rangle_E \to |\varphi\rangle \otimes |f\rangle_E,
\end{aligned}
\tag{4.104}
$$
and unitarity implies that
$$
\begin{aligned}
\langle\psi|\varphi\rangle &= ({}_E\langle 0| \otimes \langle\psi|)(|\varphi\rangle \otimes |0\rangle_E) \\
&= ({}_E\langle e| \otimes \langle\psi|)(|\varphi\rangle \otimes |f\rangle_E) \\
&= \langle\psi|\varphi\rangle\langle e|f\rangle.
\end{aligned}
\tag{4.105}
$$
Hence, for $\langle\psi|\varphi\rangle \ne 0$, we have $\langle e|f\rangle = 1$, and therefore since the states are normalized, $|e\rangle = |f\rangle$. This means that no measurement in $\mathcal{H}_E$ can reveal any information that distinguishes $|\psi\rangle$ from $|\varphi\rangle$. In the BB84 case this argument shows that, if Eve does not disturb the states sent by Alice, then the state in $\mathcal{H}_E$ is the same irrespective of which of the four states $|\uparrow_z\rangle, |\downarrow_z\rangle, |\uparrow_x\rangle, |\downarrow_x\rangle$ is sent by Alice, and therefore Eve learns nothing about the key shared by Alice and Bob. On the other hand, if Alice is sending to Bob one of the two orthogonal states $|\uparrow_z\rangle$ or $|\downarrow_z\rangle$, there is nothing to prevent Eve from acquiring a copy of the information (as with classical bits).

We have noted earlier that if we have many identical copies of a qubit, then it is possible to measure the mean value of noncommuting observables like $\bm{\sigma}_1, \bm{\sigma}_2$, and $\bm{\sigma}_3$ to completely determine the density matrix of the qubit. Inherent in the conclusion that nonorthogonal state cannot be distinguished without disturbing them, then, is the implicit provision that it is not possible to make a perfect copy of a qubit. (If we could, we would make as many copies as we need to find $\langle\bm{\sigma}_1\rangle, \langle\bm{\sigma}_2\rangle$, and $\langle\bm{\sigma}_3\rangle$ to any specified accuracy.) Let's now make this point explicit: there is no such thing as a perfect quantum Xerox machine.

Orthogonal quantum states (like classical information) *can* be reliably copied. For example, the unitary transformation that acts as
$$
\begin{aligned}
U : \quad & |0\rangle_A|0\rangle_E \to |0\rangle_A|0\rangle_E, \\
& |1\rangle_A|0\rangle_E \to |1\rangle_A|1\rangle_E,
\end{aligned}
\tag{4.106}
$$
copies the first qubit onto the second if the first qubit is in one of the states $|0\rangle_A$ or $|1\rangle_A$. But if instead the first qubit is in the state $|\psi\rangle = a|0\rangle_A + b|1\rangle_A$, then
$$
\begin{aligned}
U : \quad & (a|0\rangle_A + b|1\rangle_A)|0\rangle_E \\
& \to a|0\rangle_A|0\rangle_E + b|1\rangle_A|1\rangle_E.
\end{aligned}
\tag{4.107}
$$

<!-- Page 41 -->
This is *not* the state $|\psi\rangle \otimes |\psi\rangle$ (a tensor product of the original and the copy); rather it is something very different -- an entangled state of the two qubits.

To consider the most general possible quantum Xerox machine, we allow the full Hilbert space to be larger than the tensor product of the space of the original and the space of the copy. Then the most general "copying" unitary transformation acts as
$$
\begin{aligned}
U : \quad & |\psi\rangle_A |0\rangle_E |0\rangle_F \to |\psi\rangle_A |\psi\rangle_E |e\rangle_F, \\
& |\varphi\rangle_A |0\rangle_E |0\rangle_F \to |\varphi\rangle_A |\varphi\rangle_E |f\rangle_F.
\end{aligned}
\tag{4.108}
$$
Unitarity then implies that
$$
\langle\psi|\varphi\rangle = \langle\psi|\varphi\rangle\langle\psi|\varphi\rangle\langle e|f\rangle;
\tag{4.109}
$$
therefore, if $\langle\psi|\varphi\rangle \ne 0$, then
$$
1 = \langle\psi|\varphi\rangle\langle e|f\rangle.
\tag{4.110}
$$
Since the states are normalized, we conclude that
$$
|\langle\psi|\varphi\rangle| = 1,
\tag{4.111}
$$
so that $|\psi\rangle$ and $|\varphi\rangle$ actually represent the same ray. No unitary machine can make a copy of both $|\varphi\rangle$ and $|\psi\rangle$ if $|\varphi\rangle$ and $|\psi\rangle$ are *distinct, nonorthogonal* states. This result is called the no-cloning theorem.

# Section 10.3 Quantum Source Coding

## 10.3 Quantum Source Coding

What is the quantum analog of Shannon's source coding theorem?

Let's consider a long message consisting of $n$ letters, where each letter is a pure quantum state chosen by sampling from the ensemble
$$
\{|\varphi(x)\rangle, p(x)\}. \tag{10.122}
$$
If the states of this ensemble are mutually orthogonal, then the message might as well be classical; the interesting quantum case is where the states are not orthogonal and therefore not perfectly distinguishable. The density operator realized by this ensemble is
$$
\bm{\rho} = \sum_x p(x) |\varphi(x)\rangle \langle\varphi(x)|, \tag{10.123}
$$
and the entire $n$-letter message has the density operator
$$
\bm{\rho}^{\otimes n} = \bm{\rho} \otimes \cdots \otimes \bm{\rho}. \tag{10.124}
$$
How redundant is the quantum information in this message? We would like to devise a quantum code allowing us to compress the message to a smaller Hilbert space, but without much compromising the fidelity of the message. Perhaps we have a quantum memory device, and we know the statistical properties of the recorded data; specifically, we know $\bm{\rho}$. We want to conserve space on our (very expensive) quantum hard drive by compressing the data.

The optimal compression that can be achieved was found by Schumacher. As you might guess, the message can be compressed to a Hilbert space $\mathcal{H}$ with
$$
\dim \mathcal{H} = 2^{n(H(\bm{\rho}) + o(1))} \tag{10.125}
$$
with negligible loss of fidelity as $n \to \infty$, while errorless compression to dimension $2^{n(H(\bm{\rho}) - \Omega(1))}$ is not possible. In this sense, the von Neumann entropy is the number of qubits of quantum information carried per letter of the message. Compression is always possible unless $\bm{\rho}$ is maximally mixed, just as we can always compress a classical message unless the information source is uniformly random. This result provides a precise operational interpretation for von Neumann entropy.

Once Shannon's results are known and understood, the proof of Schumacher's compression theorem is not difficult, as the mathematical ideas needed are very similar to those used by Shannon. But conceptually quantum compression is very different from its classical counterpart, as the imperfect distinguishability of nonorthogonal quantum states is the central idea.

### 10.3.1 Quantum compression: an example

Before discussing Schumacher's quantum compression protocol in full generality, it is helpful to consider a simple example. Suppose that each letter is a single qubit drawn from the ensemble
$$
|\uparrow_z\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad p = \frac{1}{2}, \tag{10.126}
$$
$$
|\uparrow_x\rangle = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}, \quad p = \frac{1}{2}, \tag{10.127}
$$
so that the density operator of each letter is
$$
\begin{aligned}
\bm{\rho} &= \frac{1}{2} |\uparrow_z\rangle\langle\uparrow_z| + \frac{1}{2} |\uparrow_x\rangle\langle\uparrow_x| \\
&= \frac{1}{2} \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + \frac{1}{2} \begin{pmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} \end{pmatrix} = \begin{pmatrix} \frac{3}{4} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{4} \end{pmatrix}.
\end{aligned} \tag{10.128}
$$
As is obvious from symmetry, the eigenstates of $\bm{\rho}$ are qubits oriented up and down along the axis $\hat{n} = \frac{1}{\sqrt{2}}(\hat{x} + \hat{z})$,
$$
|0'\rangle \equiv |\uparrow_{\hat{n}}\rangle = \begin{pmatrix} \cos\frac{\pi}{8} \\ \sin\frac{\pi}{8} \end{pmatrix}, \quad |1'\rangle \equiv |\downarrow_{\hat{n}}\rangle = \begin{pmatrix} \sin\frac{\pi}{8} \\ -\cos\frac{\pi}{8} \end{pmatrix}; \tag{10.129}
$$
the eigenvalues are
$$
\lambda(0') = \frac{1}{2} + \frac{1}{2\sqrt{2}} = \cos^2\frac{\pi}{8}, \quad \lambda(1') = \frac{1}{2} - \frac{1}{2\sqrt{2}} = \sin^2\frac{\pi}{8}; \tag{10.130}
$$
evidently $\lambda(0') + \lambda(1') = 1$ and $\lambda(0')\lambda(1') = \frac{1}{8} = \det\bm{\rho}$. The eigenstate $|0'\rangle$ has equal (and relatively large) overlap with both signal states
$$
|\langle 0'|\uparrow_z\rangle|^2 = |\langle 0'|\uparrow_x\rangle|^2 = \cos^2\frac{\pi}{8} = .8535, \tag{10.131}
$$
while $|1'\rangle$ has equal (and relatively small) overlap with both,
$$
|\langle 1'|\uparrow_z\rangle|^2 = |\langle 1'|\uparrow_x\rangle|^2 = \sin^2\frac{\pi}{8} = .1465. \tag{10.132}
$$
Thus if we don't know whether $|\uparrow_z\rangle$ or $|\uparrow_x\rangle$ was sent, the best guess we can make is $|\psi\rangle = |0'\rangle$. This guess has the maximal fidelity with $\bm{\rho}$
$$
F = \frac{1}{2}|\langle\uparrow_z|\psi\rangle|^2 + \frac{1}{2}|\langle\uparrow_x|\psi\rangle|^2, \tag{10.133}
$$
among all possible single-qubit states $|\psi\rangle$ ($F = .8535$).

Now imagine that Alice needs to send three letters to Bob, but she can afford to send only two qubits. Still, she wants Bob to reconstruct her state with the highest possible fidelity. She could send Bob two of her three letters, and ask Bob to guess $|0'\rangle$ for the third. Then Bob receives two letters with perfect fidelity, and his guess has $F = .8535$ for the third; hence $F = .8535$ overall. But is there a more clever procedure that achieves higher fidelity?

Yes, there is. By diagonalizing $\bm{\rho}$, we decomposed the Hilbert space of a single qubit into a "likely" one-dimensional subspace (spanned by $|0'\rangle$) and an "unlikely" one-dimensional subspace (spanned by $|1'\rangle$). In a similar way we can decompose the Hilbert space of three qubits into likely and unlikely subspaces. If $|\psi\rangle = |\psi_1\rangle \otimes |\psi_2\rangle \otimes |\psi_3\rangle$ is any signal state, where the state of each qubit is either $|\uparrow_z\rangle$ or $|\uparrow_x\rangle$, we have
$$
\begin{aligned}
|\langle 0'0'0'|\psi\rangle|^2 &= \cos^6 \frac{\pi}{8} = .6219, \\
|\langle 0'0'1'|\psi\rangle|^2 &= |\langle 0'1'0'|\psi\rangle|^2 = |\langle 1'0'0'|\psi\rangle|^2 = \cos^4 \frac{\pi}{8} \sin^2 \frac{\pi}{8} = .1067, \\
|\langle 0'1'1'|\psi\rangle|^2 &= |\langle 1'0'1'|\psi\rangle|^2 = |\langle 1'1'0'|\psi\rangle|^2 = \cos^2 \frac{\pi}{8} \sin^4 \frac{\pi}{8} = .0183, \\
|\langle 1'1'1'|\psi\rangle|^2 &= \sin^6 \frac{\pi}{8} = .0031.
\end{aligned} \tag{10.134}
$$
Thus, we may decompose the space into the likely subspace $\Lambda$ spanned by $\{|0'0'0'\rangle, |0'0'1'\rangle, |0'1'0'\rangle, |1'0'0'\rangle\}$, and its orthogonal complement $\Lambda^\perp$. If we make an incomplete orthogonal measurement that projects a signal state onto $\Lambda$ or $\Lambda^\perp$, the probability of projecting onto the likely subspace $\Lambda$ is
$$
p_{\mathrm{likely}} = .6219 + 3(.1067) = .9419, \tag{10.135}
$$
while the probability of projecting onto the unlikely subspace is
$$
p_{\mathrm{unlikely}} = 3(.0183) + .0031 = .0581. \tag{10.136}
$$
To perform this measurement, Alice could, for example, first apply a unitary transformation $\bm{U}$ that rotates the four high-probability basis states to
$$
|\cdot\rangle \otimes |\cdot\rangle \otimes |0\rangle, \tag{10.137}
$$
and the four low-probability basis states to
$$
|\cdot\rangle \otimes |\cdot\rangle \otimes |1\rangle; \tag{10.138}
$$
then Alice measures the third qubit to perform the projection. If the outcome is $|0\rangle$, then Alice's input state has in effect been projected onto $\Lambda$. She sends the remaining two unmeasured qubits to Bob. When Bob receives this compressed two-qubit state $|\psi_{\mathrm{comp}}\rangle$, he decompresses it by appending $|0\rangle$ and applying $\bm{U}^{-1}$, obtaining
$$
|\psi'\rangle = \bm{U}^{-1}(|\psi_{\mathrm{comp}}\rangle \otimes |0\rangle). \tag{10.139}
$$
If Alice's measurement of the third qubit yields $|1\rangle$, she has projected her input state onto the low-probability subspace $\Lambda^\perp$. In this event, the best thing she can do is send the state that Bob will decompress to the most likely state $|0'0'0'\rangle$ -- that is, she sends the state $|\psi_{\mathrm{comp}}\rangle$ such that
$$
|\psi'\rangle = \bm{U}^{-1}(|\psi_{\mathrm{comp}}\rangle \otimes |0\rangle) = |0'0'0'\rangle. \tag{10.140}
$$
Thus, if Alice encodes the three-qubit signal state $|\psi\rangle$, sends two qubits to Bob, and Bob decodes as just described, then Bob obtains the state $\bm{\rho}'$
$$
|\psi\rangle\langle\psi| \to \bm{\rho}' = \bm{E}|\psi\rangle\langle\psi|\bm{E} + |0'0'0'\rangle\langle\psi|(\bm{I} - \bm{E})|\psi\rangle\langle 0'0'0'|, \tag{10.141}
$$
where $\bm{E}$ is the projection onto $\Lambda$. The fidelity achieved by this procedure is
$$
\begin{aligned}
F &= \langle\psi|\bm{\rho}'|\psi\rangle = (\langle\psi|\bm{E}|\psi\rangle)^2 + (\langle\psi|(\bm{I} - \bm{E})|\psi\rangle)(\langle\psi|0'0'0'\rangle)^2 \\
&= (.9419)^2 + (.0581)(.6219) = .9234.
\end{aligned} \tag{10.142}
$$
This is indeed better than the naive procedure of sending two of the three qubits each with perfect fidelity.

As we consider longer messages with more letters, the fidelity of the compression improves, as long as we don't try to compress too much. The von Neumann entropy of the one-qubit ensemble is
$$
H(\bm{\rho}) = H\left(\cos^2\frac{\pi}{8}\right) = .60088\dots \tag{10.143}
$$
Therefore, according to Schumacher's theorem, we can shorten a long message by the factor, say, .6009, and still achieve very good fidelity.

### 10.3.2 Schumacher compression in general

The key to Shannon's noiseless coding theorem is that we can code the typical sequences and ignore the rest, without much loss of fidelity. To quantify the compressibility of quantum information, we promote the notion of a typical sequence to that of a typical subspace. The key to Schumacher's noiseless quantum coding theorem is that we can code the typical subspace and ignore its orthogonal complement, without much loss of fidelity.

We consider a message of $n$ letters where each letter is a pure quantum state drawn from the ensemble $\{|\varphi(x)\rangle, p(x)\}$, so that the density operator of a single letter is
$$
\bm{\rho} = \sum_x p(x) |\varphi(x)\rangle\langle\varphi(x)|. \tag{10.144}
$$
Since the letters are drawn independently, the density operator of the entire message is
$$
\bm{\rho}^{\otimes n} \equiv \bm{\rho} \otimes \cdots \otimes \bm{\rho}. \tag{10.145}
$$
We claim that, for $n$ large, this density matrix has nearly all of its support on a subspace of the full Hilbert space of the messages, where the dimension of this subspace asymptotically approaches $2^{nH(\bm{\rho})}$.

This claim follows directly from the corresponding classical statement, for we may consider $\bm{\rho}$ to be realized by an ensemble of orthonormal pure states, its eigenstates, where the probability assigned to each eigenstate is the corresponding eigenvalue. In this basis our source of quantum information is effectively classical, producing messages which are tensor products of $\bm{\rho}$ eigenstates, each with a probability given by the product of the corresponding eigenvalues. For a specified $n$ and $\delta$, define the $\delta$-typical subspace $\Lambda$ as the space spanned by the eigenvectors of $\bm{\rho}^{\otimes n}$ with eigenvalues $\lambda$ satisfying
$$
2^{-n(H-\delta)} \ge \lambda \ge 2^{-n(H+\delta)}. \tag{10.146}
$$
Borrowing directly from Shannon's argument, we infer that for any $\delta, \varepsilon > 0$ and $n$ sufficiently large, the sum of the eigenvalues of $\bm{\rho}^{\otimes n}$ that obey this condition satisfies
$$
\mathrm{tr}(\bm{\rho}^{\otimes n}\bm{E}) \ge 1 - \varepsilon, \tag{10.147}
$$
where $\bm{E}$ denotes the projection onto the typical subspace $\Lambda$, and the number $\dim(\Lambda)$ of such eigenvalues satisfies
$$
2^{n(H+\delta)} \ge \dim(\Lambda) \ge (1-\varepsilon)2^{n(H-\delta)}. \tag{10.148}
$$
Our coding strategy is to send states in the typical subspace faithfully. We can make a measurement that projects the input message onto either $\Lambda$ or $\Lambda^\perp$; the outcome will be $\Lambda$ with probability $p_\Lambda = \mathrm{tr}(\bm{\rho}^{\otimes n}\bm{E}) \ge 1 - \varepsilon$. In that event, the projected state is coded and sent. Asymptotically, the probability of the other outcome becomes negligible, so it matters little what we do in that case.

The coding of the projected state merely packages it so it can be carried by a minimal number of qubits. For example, we apply a unitary change of basis $\bm{U}$ that takes each state $|\psi_{\mathrm{typ}}\rangle$ in $\Lambda$ to a state of the form
$$
\bm{U}|\psi_{\mathrm{typ}}\rangle = |\psi_{\mathrm{comp}}\rangle \otimes |0_{\mathrm{rest}}\rangle, \tag{10.149}
$$
where $|\psi_{\mathrm{comp}}\rangle$ is a state of $n(H + \delta)$ qubits, and $|0_{\mathrm{rest}}\rangle$ denotes the state $|0\rangle \otimes \cdots \otimes |0\rangle$ of the remaining qubits. Alice sends $|\psi_{\mathrm{comp}}\rangle$ to Bob, who decodes by appending $|0_{\mathrm{rest}}\rangle$ and applying $\bm{U}^{-1}$.

Suppose that
$$
|\varphi(\vec{x})\rangle = |\varphi(x_1)\rangle \otimes \cdots \otimes |\varphi(x_n)\rangle, \tag{10.150}
$$
denotes any one of the $n$-letter pure state messages that might be sent. After coding, transmission, and decoding are carried out as just described, Bob has reconstructed a state
$$
|\varphi(\vec{x})\rangle\langle\varphi(\vec{x})| \mapsto \bm{\rho}'(\vec{x}) = \bm{E}|\varphi(\vec{x})\rangle\langle\varphi(\vec{x})|\bm{E} + \bm{\rho}_{\mathrm{Junk}}(\vec{x})\langle\varphi(\vec{x})|(\bm{I}-\bm{E})|\varphi(\vec{x})\rangle, \tag{10.151}
$$
where $\bm{\rho}_{\mathrm{Junk}}(\vec{x})$ is the state we choose to send if the measurement yields the outcome $\Lambda^\perp$. What can we say about the fidelity of this procedure?

The fidelity varies from message to message, so we consider the fidelity averaged over the ensemble of possible messages:
$$
\begin{aligned}
\bar{F} &= \sum_{\vec{x}} p(\vec{x}) \langle\varphi(\vec{x})|\bm{\rho}'(\vec{x})|\varphi(\vec{x})\rangle \\
&= \sum_{\vec{x}} p(\vec{x}) \langle\varphi(\vec{x})|\bm{E}|\varphi(\vec{x})\rangle \langle\varphi(\vec{x})|\bm{E}|\varphi(\vec{x})\rangle + \sum_{\vec{x}} p(\vec{x}) \langle\varphi(\vec{x})|\bm{\rho}_{\mathrm{Junk}}(\vec{x})|\varphi(\vec{x})\rangle \langle\varphi(\vec{x})|(\bm{I}-\bm{E})|\varphi(\vec{x})\rangle \\
&\ge \sum_{\vec{x}} p(\vec{x}) \langle\varphi(\vec{x})|\bm{E}|\varphi(\vec{x})\rangle^2,
\end{aligned} \tag{10.152}
$$
where the last inequality holds because the "Junk" term is nonnegative. Since any real number $z$ satisfies
$$
(z-1)^2 \ge 0, \quad \text{or} \quad z^2 \ge 2z - 1, \tag{10.153}
$$
we have (setting $z = \langle\varphi(\vec{x})|\bm{E}|\varphi(\vec{x})\rangle$)
$$
\langle\varphi(\vec{x})|\bm{E}|\varphi(\vec{x})\rangle^2 \ge 2\langle\varphi(\vec{x})|\bm{E}|\varphi(\vec{x})\rangle - 1, \tag{10.154}
$$
and hence
$$
\begin{aligned}
\bar{F} &\ge \sum_{\vec{x}} p(\vec{x})(2\langle\varphi(\vec{x})|\bm{E}|\varphi(\vec{x})\rangle - 1) \\
&= 2\,\mathrm{tr}(\bm{\rho}^{\otimes n}\bm{E}) - 1 \ge 2(1-\varepsilon) - 1 = 1 - 2\varepsilon.
\end{aligned} \tag{10.155}
$$
Since $\varepsilon$ and $\delta$ can be as small as we please, we have shown that it is possible to compress the message to $n(H + o(1))$ qubits, while achieving an average fidelity that becomes arbitrarily good as $n$ gets large.

Is further compression possible? Let us suppose that Bob will decode the message $\bm{\rho}_{\mathrm{comp}}(\vec{x})$ that he receives by appending qubits and applying a unitary transformation $\bm{U}^{-1}$, obtaining
$$
\bm{\rho}'(\vec{x}) = \bm{U}^{-1}(\bm{\rho}_{\mathrm{comp}}(\vec{x}) \otimes |0\rangle\langle 0|)\bm{U} \tag{10.156}
$$
("unitary decoding"), and suppose that $\bm{\rho}_{\mathrm{comp}}(\vec{x})$ has been compressed to $n(H - \delta')$ qubits. Then, no matter how the input messages have been encoded, the decoded messages are all contained in a subspace $\Lambda'$ of Bob's Hilbert space with $\dim(\Lambda') = 2^{n(H-\delta')}$.

If the input message is $|\varphi(\vec{x})\rangle$, then the density operator reconstructed by Bob can be diagonalized as
$$
\bm{\rho}'(\vec{x}) = \sum_{a_{\vec{x}}} |a_{\vec{x}}\rangle \lambda_{a_{\vec{x}}} \langle a_{\vec{x}}|, \tag{10.157}
$$
where the $|a_{\vec{x}}\rangle$'s are mutually orthogonal states in $\Lambda'$. The fidelity of the reconstructed message is
$$
\begin{aligned}
F(\vec{x}) &= \langle\varphi(\vec{x})|\bm{\rho}'(\vec{x})|\varphi(\vec{x})\rangle \\
&= \sum_{a_{\vec{x}}} \lambda_{a_{\vec{x}}} \langle\varphi(\vec{x})|a_{\vec{x}}\rangle \langle a_{\vec{x}}|\varphi(\vec{x})\rangle \\
&\le \sum_{a_{\vec{x}}} \langle\varphi(\vec{x})|a_{\vec{x}}\rangle \langle a_{\vec{x}}|\varphi(\vec{x})\rangle \le \langle\varphi(\vec{x})|\bm{E}'|\varphi(\vec{x})\rangle,
\end{aligned} \tag{10.158}
$$
where $\bm{E}'$ denotes the orthogonal projection onto the subspace $\Lambda'$. The average fidelity therefore obeys
$$
\bar{F} = \sum_{\vec{x}} p(\vec{x}) F(\vec{x}) \le \sum_{\vec{x}} p(\vec{x}) \langle\varphi(\vec{x})|\bm{E}'|\varphi(\vec{x})\rangle = \mathrm{tr}(\bm{\rho}^{\otimes n}\bm{E}'). \tag{10.159}
$$
But, according to the Ky Fan dominance principle discussed in §10.2.2, since $\bm{E}'$ projects onto a space of dimension $2^{n(H-\delta')}$, $\mathrm{tr}(\bm{\rho}^{\otimes n}\bm{E}')$ can be no larger than the sum of the $2^{n(H-\delta')}$ largest eigenvalues of $\bm{\rho}^{\otimes n}$. The $\delta$-typical eigenvalues of $\bm{\rho}^{\otimes n}$ are no smaller than $2^{-n(H-\delta)}$, so the sum of the $2^{n(H-\delta')}$ largest eigenvalues can be bounded above:
$$
\mathrm{tr}(\bm{\rho}^{\otimes n}\bm{E}') \le 2^{n(H-\delta')} 2^{-n(H-\delta)} + \varepsilon = 2^{-n(\delta'-\delta)} + \varepsilon, \tag{10.160}
$$
where the $+ \varepsilon$ accounts for the contribution from the atypical eigenvalues. Since we may choose $\varepsilon$ and $\delta$ as small as we please for sufficiently large $n$, we conclude that the average fidelity $\bar{F}$ gets small as $n \to \infty$ if we compress to $H(\bm{\rho}) - \Omega(1)$ qubits per letter.

We find, then, that $H(\bm{\rho})$ qubits per letter is the optimal compression of the quantum information that can be achieved if we are to obtain good fidelity as $n$ goes to infinity. This is Schumacher's quantum source coding theorem.

The above argument applies to any conceivable encoding scheme, but only to a restricted class of decoding schemes, unitary decodings. The extension of the argument to general decoding schemes is sketched in §10.6.3. The conclusion is the same. The point is that $n(H-\delta)$ qubits are too few to faithfully encode the typical subspace.

There is another useful way to think about Schumacher's quantum compression protocol. Suppose that Alice's density operator $\bm{\rho}_A^{\otimes n}$ has a purification $|\psi\rangle_{RA}$ which Alice shares with Robert. Alice wants to convey her share of $|\psi\rangle_{RA}$ to Bob with high fidelity, sending as few qubits to Bob as possible. To accomplish this task, Alice can use the same procedure as described above, attempting to compress the state of $A$ by projecting onto its typical subspace $\Lambda$. Alice's projection succeeds with probability
$$
P(\bm{E}) = \langle\psi|\bm{I} \otimes \bm{E}|\psi\rangle = \mathrm{tr}(\bm{\rho}^{\otimes n}\bm{E}) \ge 1 - \varepsilon, \tag{10.161}
$$
where $\bm{E}$ projects onto $\Lambda$, and when successful prepares the state
$$
\frac{(\bm{I}\otimes\bm{E})|\psi\rangle}{\sqrt{P(\bm{E})}}. \tag{10.162}
$$
Therefore, after Bob decompresses, the state he shares with Robert has fidelity $F_e$ with $|\psi\rangle$ satisfying
$$
F_e \ge \langle\psi|\bm{I} \otimes \bm{E}|\psi\rangle \langle\psi|\bm{I} \otimes \bm{E}|\psi\rangle = \left(\mathrm{tr}(\bm{\rho}^{\otimes n}\bm{E})\right)^2 = P(\bm{E})^2 \ge (1-\varepsilon)^2 \ge 1-2\varepsilon. \tag{10.163}
$$
We conclude that Alice can transfer her share of the pure state $|\psi\rangle_{RA}$ to Bob by sending $nH(\bm{\rho}) + o(n)$ qubits, achieving arbitrarily good *entanglement fidelity* $F_e$ as $n \to \infty$. In §10.8.2 we'll derive a more general version of this result.

To summarize, there is a close analogy between Shannon's classical source coding theorem and Schumacher's quantum source coding theorem. In the classical case, nearly all long messages are typical sequences, so we can code only these and still have a small probability of error. In the quantum case, nearly all long messages have nearly perfect overlap with the typical subspace, so we can code only the typical subspace and still achieve good fidelity.

Alternatively, Alice could send classical information to Bob, the string $x_1 x_2 \cdots x_n$, and Bob could follow these classical instructions to reconstruct Alice's state $|\varphi(x_1)\rangle \otimes \cdots \otimes |\varphi(x_n)\rangle$. By this means, they could achieve high-fidelity compression to $H(X) + o(1)$ bits -- or qubits -- per letter, where $X$ is the classical ensemble $\{x, p(x)\}$. But if $\{|\varphi(x)\rangle, p(x)\}$ is an ensemble of *nonorthogonal* pure states, this classically achievable amount of compression is not optimal; some of the classical information about the preparation of the state is redundant, because the nonorthogonal states cannot be perfectly distinguished. Schumacher coding goes further, achieving optimal compression to $H(\bm{\rho}) + o(1)$ qubits per letter. Quantum compression packages the message more efficiently than classical compression, but at a price -- Bob receives the quantum state Alice intended to send, but Bob doesn't know what he has. In contrast to the classical case, Bob can't fully decipher Alice's quantum message accurately. An attempt to read the message will unavoidably disturb it.

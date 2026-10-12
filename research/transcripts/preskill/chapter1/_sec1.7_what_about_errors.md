# Section 1.7: What about errors? [PDF Pages 15-19]

<!-- ============================================================ -->
<!-- Source: chap1.pdf, Physical Pages: 15-19                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 15 -->
## 1.7 What about errors?

As significant as Shor’s factoring algorithm may prove to be, there is another recently discovered feature of quantum information that may be just as important: the discovery of quantum error correction. Indeed, were it not for this development, the prospects for quantum computing technology would not seem bright.

As we have noted, the essential property of quantum information that a quantum computer exploits is the existence of nonlocal correlations among the different parts of a physical system. If I look at only part of the system at a time, I can decipher only very little of the information encoded in the system.

<!-- Page 16 -->
Unfortunately, these nonlocal correlations are extremely fragile and tend to decay very rapidly in practice. The problem is that our quantum system is inevitably in contact with a much larger system, its environment. It is virtually impossible to perfectly isolate a big quantum system from its environment, even if we make a heroic effort to do so. Interactions between a quantum device and its environment establish nonlocal correlations between the two. Eventually the quantum information that we initially encoded in the device becomes encoded, instead, in correlations between the device and the environment. At that stage, we can no longer access the information by observing only the device. In practice, the information is irrevocably lost. Even if the coupling between device and environment is quite weak, this happens to a macroscopic device remarkably quickly.

Erwin Schrödinger chided the proponents of the mainstream interpretation of quantum mechanics by observing that the theory will allow a quantum state of a cat of the form
$$
|\text{cat}\rangle = \frac{1}{\sqrt{2}}\left(|\text{dead}\rangle + |\text{alive}\rangle\right).
$$ {#eq-1.17}
To Schrödinger, the possibility of such states was a blemish on the theory, because every cat he had seen was either dead or alive, not half dead and half alive.

One of the most important advances in quantum theory over the past 15 years is that we have learned how to answer Schrödinger with growing confidence. The state $|\text{cat}\rangle$ is possible in principle, but is rarely seen because it is *extremely* unstable. The cats Schrödinger observed were never well isolated from the environment. If someone were to prepare the state $|\text{cat}\rangle$, the quantum information encoded in the superposition of $|\text{dead}\rangle$ and $|\text{alive}\rangle$ would *immediately* be transferred to correlations between the cat and the environment, and become completely inaccessible. In effect, the environment continually measures the cat, projecting it onto either the state $|\text{alive}\rangle$ or $|\text{dead}\rangle$. This process is called *decoherence*. We will return to the study of decoherence later in the course.

Now, to perform a complex quantum computation, we need to prepare a delicate superposition of states of a relatively large quantum system (though perhaps not as large as a cat). Unfortunately, this system cannot be perfectly isolated from the environment, so this superposition, like the state $|\text{cat}\rangle$, decays very rapidly. The encoded quantum information is quickly lost, and our quantum computer crashes.

<!-- Page 17 -->
To put it another way, contact between the computer and the environment (decoherence) causes *errors* that degrade the quantum information. To operate a quantum computer reliably, we must find some way to prevent or correct these errors.

Actually, decoherence is not our only problem. Even if we could achieve perfect isolation from the environment, we could not expect to operate a quantum computer with perfect accuracy. The quantum gates that the machine executes are unitary transformations that operate on a few qubits at a time, let’s say $4 \times 4$ unitary matrices acting on two qubits. Of course, these unitary matrices form a continuum. We may have a protocol for applying $U_0$ to 2 qubits, but our execution of the protocol will not be flawless, so the actual transformation
$$
U = U_0\left(1 + O(\varepsilon)\right)
$$ {#eq-1.18}
will differ from the intended $U_0$ by some amount of order $\varepsilon$. After about $1/\varepsilon$ gates are applied, these errors will accumulate and induce a serious failure. Classical analog devices suffer from a similar problem, but small errors are much less of a problem for devices that perform discrete logic.

In fact, modern digital circuits are remarkably reliable. They achieve such high accuracy with help from *dissipation*. We can envision a classical gate that acts on a bit, encoded as a ball residing at one of the two minima of a double-lobed potential. The gate may push the ball over the intervening barrier to the other side of the potential. Of course, the gate won’t be implemented perfectly; it may push the ball a little too hard. Over time, these imperfections might accumulate, causing an error.

To improve the performance, we *cool* the bit (in effect) after each gate. This is a dissipative process that releases heat to the environment and compresses the phase space of the ball, bringing it close to the local minimum of the potential. So the small errors that we may make wind up heating the environment rather than compromising the performance of the device.

But we can’t cool a quantum computer this way. Contact with the environment may enhance the reliability of classical information, but it would destroy encoded quantum information. More generally, accumulation of error will be a problem for classical reversible computation as well. To prevent errors from building up we need to discard the information about the errors, and throwing away information is always a dissipative process.

Still, let’s not give up too easily. A sophisticated machinery has been developed to contend with errors in classical information, the theory of er-

<!-- Page 18 -->
ror correcting codes. To what extent can we coopt this wisdom to protect quantum information as well?

How does classical error correction work? The simplest example of a classical error-correcting code is a repetition code: we replace the bit we wish to protect by 3 copies of the bit,
$$
\begin{aligned}
0 &\to (000), \\
1 &\to (111).
\end{aligned}
$$ {#eq-1.19}
Now an error may occur that causes one of the three bits to flip; if it’s the first bit, say,
$$
\begin{aligned}
(000) &\to (100), \\
(111) &\to (011).
\end{aligned}
$$ {#eq-1.20}
Now in spite of the error, we can still decode the bit correctly, by majority voting.

Of course, if the probability of error in each bit were $p$, it would be possible for two of the three bits to flip, or even for all three to flip. A double flip can happen in three different ways, so the probability of a double flip is $3p^2(1 - p)$, while the probability of a triple flip is $p^3$. Altogether, then, the probability that majority voting fails is $3p^2(1 - p) + p^3 = 3p^2 - 2p^3$. But for
$$
3p^2 - 2p^3 < p \quad \text{or} \quad p < \frac{1}{2},
$$ {#eq-1.21}
the code improves the reliability of the information.

We can improve the reliability further by using a longer code. One such code (though far from the most efficient) is an $N$-bit repetition code. The probability distribution for the average value of the bit, by the central limit theorem, approaches a Gaussian with width $1/\sqrt{N}$ as $N \to \infty$. If $P = \frac{1}{2} + \varepsilon$ is the probability that each bit has the correct value, then the probability that the majority vote fails (for large $N$) is
$$
P_{\text{error}} \sim e^{-N\varepsilon^2},
$$ {#eq-1.22}
arising from the tail of the Gaussian. Thus, for any $\varepsilon > 0$, by introducing enough redundancy we can achieve arbitrarily good reliability. Even for $\varepsilon < 0$, we’ll be okay if we always assume that majority voting gives the

<!-- Page 19 -->
*wrong* result. Only for $P = \frac{1}{2}$ is the cause lost, for then our block of $N$ bits will be *random*, and encode no information.

In the 50’s, John Von Neumann showed that a classical computer with noisy components can work reliably, by employing sufficient redundancy. He pointed out that, if necessary, we can compute each logic gate many times, and accept the majority result. (Von Neumann was especially interested in how his brain was able to function so well, in spite of the unreliability of neurons. He was pleased to explain why he was so smart.)

But now we want to use error correction to keep a *quantum computer* on track, and we can immediately see that there are difficulties:

1. **Phase errors.** With quantum information, more things can go wrong. In addition to bit-flip errors
$$
\begin{aligned}
|0\rangle &\to |1\rangle, \\
|1\rangle &\to |0\rangle.
\end{aligned}
$$ {#eq-1.23}
there can also be *phase errors*
$$
\begin{aligned}
|0\rangle &\to |0\rangle, \\
|1\rangle &\to -|1\rangle.
\end{aligned}
$$ {#eq-1.24}
A phase error is serious, because it makes the state $\frac{1}{\sqrt{2}}[|0\rangle + |1\rangle]$ flip to the orthogonal state $\frac{1}{\sqrt{2}}[|0\rangle - |1\rangle]$. But the classical coding provided no protection against phase errors.

2. **Small errors.** As already noted, quantum information is continuous. If a qubit is intended to be in the state
$$
a|0\rangle + b|1\rangle,
$$ {#eq-1.25}
an error might change $a$ and $b$ by an amount of order $\varepsilon$, and these small errors can accumulate over time. The classical method is designed to correct large (bit flip) errors.

3. **Measurement causes disturbance.** In the majority voting scheme, it seemed that we needed to *measure* the bits in the code to detect and correct the errors. But we can’t measure qubits without *disturbing* the quantum information that they encode.

4. **No cloning.** With classical coding, we protected information by making extra copies of it. But we know that quantum information *cannot* be copied with perfect fidelity.

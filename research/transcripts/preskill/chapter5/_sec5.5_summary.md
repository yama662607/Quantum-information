# Section 5.5: Summary [PDF Pages 45-46]

<!-- ============================================================ -->
<!-- Source: chap5.pdf, Physical Pages: 45-46                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 45 -->
## 5.5 Summary

*Classical circuits.* The complexity of a problem can be characterized by the size of a uniform family of logic circuits that solve the problem: The problem is hard if the size of the circuit is a superpolynomial function of the size of the input, and easy otherwise. One classical universal computer can simulate another efficiently, so the classification of complexity is machine independent. The 3-bit Toffoli gate is universal for classical reversible computation. A reversible computer can simulate an irreversible computer without a significant slowdown and without unreasonable memory resources.

*Quantum Circuits.* Although there is no proof, it seems likely that polynomial-size quantum circuits cannot be simulated in general by polynomial-size randomized classical circuits ($\mathrm{BQP} \neq \mathrm{BPP}$); however, polynomial space is sufficient ($\mathrm{BQP} \subseteq \mathrm{PSPACE}$). A noisy quantum circuit can simulate an ideal quantum circuit of size $T$ to acceptable accuracy

<!-- Page 46 -->
if each quantum gate has an accuracy of order $1/T$. Any $n$-qubit unitary transformation can be constructed from two-qubit gates. A generic two-qubit quantum gate, if it can act on any two qubits in a device, is sufficient for universal quantum computation. One universal quantum computer can simulate another to accuracy $\varepsilon$ with a $\operatorname{polylog}(1/\varepsilon)$ overheard cost; therefore the complexity class BQP is machine independent. Do the Exercises to learn more about universal sets of quantum gates.

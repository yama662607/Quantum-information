# Section 10.10: Summary & Section 10.11: Bibliographical Notes [PDF Pages 84-87]

<!-- ============================================================ -->
<!-- Source: chap10.pdf, Physical Pages: 84-87                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 84 -->
## 10.10 Summary

**Shannon entropy and classical data compression.** The *Shannon entropy* of an ensemble $X = \{x, p(x)\}$ is $H(X) := \mathbb{E}_X[-\log p(x)]$; it quantifies the compressibility of classical information. A message $n$ letters long, where each letter is drawn independently from $X$, can be compressed to $H(X)$ bits per letter (and no further), yet can still be decoded with arbitrarily good accuracy as $n \to \infty$.

**Conditional entropy and information merging.** The *conditional entropy* $H(X|Y) = H(XY) - H(Y)$ quantifies how much the information source $X$ can be compressed when $Y$ is known. If $n$ letters are drawn from $XY$, where Alice holds $X$ and Bob holds $Y$, Alice can convey $X$ to Bob by sending $H(X|Y)$ bits per letter, asymptotically as $n \to \infty$.

**Mutual information and classical channel capacity.** The *mutual information* $I(X;Y) = H(X) + H(Y) - H(XY)$ quantifies how information sources $X$ and Y are correlated; when we learn the value of $y$ we acquire (on the average) $I(X;Y)$ bits of information about $x$, and vice versa. The capacity of a memoryless noisy classical communication channel is $C = \max_X I(X;Y)$. This is the highest number of bits per letter that can be transmitted through $n$ uses of the channel, using the best possible code, with negligible error probability as $n \to \infty$.

**Von Neumann entropy and quantum data compression.** The *von Neumann entropy* of a density operator $\rho$ is

<!-- Page 85 -->
$$
H(\rho) = -\mathrm{tr}\,\rho \log \rho;
$$ {#eq-10.374}

it quantifies the compressibility of an ensemble of pure quantum states. A message $n$ letters long, where each letter is drawn independently from the ensemble $\{|\varphi(x)\rangle, p(x)\}$, can be compressed to $H(\rho)$ qubits per letter (and no further) where $\rho = \sum_x p(x) |\varphi(x)\rangle\langle\varphi(x)|$, yet can still be decoded with arbitrarily good fidelity as $n \to \infty$.

**Entanglement concentration and dilution.** The *entanglement* $E$ of a bipartite pure state $|\psi\rangle_{AB}$ is $E = H(\rho_A)$ where $\rho_A = \mathrm{tr}_B(|\psi\rangle\langle\psi|)$. With local operations and classical communication, we can prepare $n$ copies of $|\psi\rangle_{AB}$ from $nE$ Bell pairs (but not from fewer), and we can distill $nE$ Bell pairs (but not more) from $n$ copies of $|\psi\rangle_{AB}$, asymptotically as $n \to \infty$.

**Accessible information.** The *Holevo chi* of an ensemble $\mathcal{E} = \{\rho(x), p(x)\}$ of quantum states is

$$
\chi(\mathcal{E}) = H\left(\sum_x p(x)\rho(x)\right) - \sum_x p(x) H(\rho(x)).
$$ {#eq-10.375}

The *accessible information* of an ensemble $\mathcal{E}$ of quantum states is the maximal number of bits of information that can be acquired about the preparation of the state (on the average) with the best possible measurement. The accessible information cannot exceed the Holevo chi of the ensemble. The product-state capacity of a quantum channel $\mathcal{N}$ is

$$
C_1(\mathcal{N}) = \max_{\mathcal{E}} \chi(\mathcal{N}(\mathcal{E})).
$$ {#eq-10.376}

This is the highest number of classical bits per letter that can be transmitted through $n$ uses of the quantum channel, with negligible error probability as $n \to \infty$, assuming that each codeword is a product state.

**Decoupling and quantum communication.** In a tripartite pure state $\phi_{RBE}$, we say that systems $R$ and $E$ *decouple* if the marginal density operator of $RE$ is a product state, in which case $R$ is purified by a subsystem of $B$. A quantum state transmitted through a noisy quantum channel $\mathcal{N}^{A \to B}$ (with isometric dilation $U^{A \to BE}$) can be accurately decoded if a reference system $R$ which purifies channel's input $A$ nearly *decouples* from the channel's environment $E$.

**Father and mother protocols.** The *father and mother resource inequalities* specify achievable rates for entanglement-assisted quantum communication and quantum state transfer, respectively. Both follow from the *decoupling inequality*, which establishes a sufficient condition for approximate decoupling in a tripartite mixed state. By combining the father and mother protocols with superdense coding and teleportation, we can derive achievable rates for other protocols, including entanglement-assisted classical communication, quantum communication, entanglement distillation, and quantum state merging.

### Homage to Ben Schumacher:

Ben.  
He rocks.  
I remember  
When  
He showed me how to fit  

<!-- Page 86 -->
A qubit  
In a small box.  

I wonder how it feels  
To be compressed.  
And then to pass  
A fidelity test.  

Or does it feel  
At all, and if it does  
Would I squeal  
Or be just as I was?  

If not undone  
I'd become as I'd begun  
And write a memorandum  
On being random.  
Had it felt like a belt  
Of rum?  

And might it be predicted  
That I'd become addicted,  
Longing for my session  
Of compression?  

I'd crawl  
To Ben again.  
And call,  
Put down your pen!  
Don't stall!  
Make me small!  

## 10.11 Bibliographical Notes

Cover and Thomas [2] is an excellent textbook on classical information theory. Shannon's original paper [3] is still very much worth reading.

Nielsen and Chuang [4] provide a clear introduction to some aspects of quantum Shannon theory. Wilde [1] is a more up-to-date and very thorough account.

Properties of entropy are reviewed in [5]. Strong subadditivity of von Neumann entropy was proven by Lieb and Ruskai [6], and the condition for equality was derived by Hayden et al. [7]. The connection between separability and majorization was pointed out by Nielsen and Kempe [8].

Bekenstein's entropy bound was formulated in [9] and derived by Casini [10]. Entropic uncertainty relations are reviewed in [11], and I follow their derivation. The original derivation, by Maassen and Uffink [12] uses different methods.

Schumacher compression was first discussed in [13, 14], and Bennett et al. [15] devised protocols for entanglement concentration and dilution. Measures of mixed-state entanglement are reviewed in [16]. The reversible theory of mixed-state entanglement was formulated by Brandão and Plenio [17] (a flaw in their analysis was addressed in [18, 19]). Squashed entanglement was introduced by Christandl and Winter [20], and its monogamy discussed by Koashi and Winter [21]. Brandão, Christandl, and Yard [22] showed that squashed entanglement is positive for any nonseparable bipartite state. Do-

<!-- Page 87 -->
herty, Parrilo, and Spedalieri [23] showed that every nonseparable bipartite state fails to be $k$-extendable for some finite $k$.

The Holevo bound was derived in [24]. Peres–Wootters coding was discussed in [25]. The product-state capacity formula was derived by Holevo [26] and by Schumacher and Westmoreland [27]. Hastings [28] showed that Holevo chi can be superadditive. Horodecki, Shor, and Ruskai [29] introduced entanglement-breaking channels, and additivity of Holevo chi for these channels was shown by Shor [30].

Necessary and sufficient conditions for quantum error correction were formulated in terms of the decoupling principle by Schumacher and Nielsen [31]; that (regularized) coherent information is an upper bound on quantum capacity was shown by Schumacher [32], Schumacher and Nielsen [31], and Barnum et al. [33]. That coherent information is an achievable rate for quantum communication was conjectured by Lloyd [34] and by Schumacher [32], then proven by Shor [35] and by Devetak [36]. Devetak and Winter [37] showed it is also an achievable rate for entanglement distillation. The quantum Fano inequality was derived by Schumacher [32].

Approximate decoupling was analyzed by Schumacher and Westmoreland [38], and used to prove capacity theorems by Devetak [36], by Horodecki et al. [39], by Hayden et al. [40], and by Abeyesinghe et al. [41]. The entropy of Haar-random subsystems had been discussed earlier, by Lubkin [42], Lloyd and Pagels [43], and Page [44]. Devetak, Harrow, and Winter [45, 46] introduced the mother and father protocols and their descendants. Devatak and Shor [47] introduced degradable quantum channels and proved that coherent information is additive for these channels. Bennett et al. [48, 49] found the single-letter formula for entanglement-assisted classical capacity. Superadditivity of coherent information was discovered by Shor and Smolin [50] and by DiVincenzo et al. [51]. Smith and Yard [52] found extreme examples of superadditivity, in which two zero-capacity channels have nonzero capacity when used jointly. The achievable rate for state merging was derived by Horodecki et al. [39], and used by them to prove strong subadditivity of von Neumann entropy.

Decoupling was applied to Landuaer's principle by Renner et al. [53], and to black holes by Hayden and Preskill [54]. The fast scrambling conjecture was proposed by Sekino and Susskind [55].

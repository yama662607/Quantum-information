# Section 7.16: Good Quantum Codes

**Source:** Preskill Lecture Notes, Chapter 7, pp. 47–48 (Physical pages 53–54).

---

A family of $[[n, k, d]]$ codes is *good* if it contains codes whose "rate" $R = k/n$ and "error probability" $p = t/n$ (where $t = (d - 1)/2$) both approach a nonzero limit as $n \to \infty$. We can use the stabilizer formalism to prove a "quantum Gilbert-Varshamov" bound that demonstrates the existence of good quantum codes. In fact, good codes can be chosen to be nondegenerate.

The *quantum Gilbert-Varshamov bound* says that
$$
|\mathcal{E}^{(2)}| - 1 < 2^{n-k} \left(\frac{1 - 2^{-2n}}{1 - 2^{-2k}}\right).
$$ {#eq-7.207}
is a sufficient condition for the existence of a (possibly degenerate) binary stabilizer code that can correct all Pauli operators in a set $\mathcal{E}$; here $|\mathcal{E}^{(2)}|$ denotes the number of distinct Pauli operators of the form $E_a^\dagger E_b$, where $E_a, E_b \in \mathcal{E}$. One consequence of this bound is that there exist "good" $[[n, k, d = 2t + 1]]$ stabilizer codes that achieve an asymptotic rate $R = k/n = 1 - H_2(2t/n) - (2t/n)\log_2 3$.

Let $\mathcal{S}$ denote the set of all $[[n, k]]$ quantum stabilizer codes. We want to show that this set contains a code that corrects all errors in $\mathcal{E}$. That is, we are seeking a code in $\mathcal{S}$ with stabilizer $S$ such that $S^\perp \setminus S$ contains no element of $\mathcal{E}^{(2)} \setminus \boldsymbol{I}$.

Consider this bipartite graph: Vertices on the left are labeled by codes in $\mathcal{S}$ and vertices on the right are labeled by $n$-qubit Pauli operators, excluding the identity. For each code (with stabilizer $S$), we draw edges connecting that code's vertex to each of its nontrivial logical operators — that is, to each Pauli operator in $S^\perp \setminus S$. Our goal, then, is to show that there is some code which is not connected by an edge to any element of $\mathcal{E}^{(2)} \setminus \boldsymbol{I}$. We'll do that by showing that the total number of edges which connect with elements of $\mathcal{E}^{(2)} \setminus \boldsymbol{I}$ is smaller than the number of elements of $\mathcal{S}$. Thus, once we eliminate from $\mathcal{S}$ all the codes that fail to correct $\mathcal{E}$, there must be at least one code left over, which does correct $\mathcal{E}$.

Now, each stabilizer code with $n - k$ generators has $|S^\perp \setminus S| = 2^{n+k} - 2^{n-k}$ nontrivial logical operators; thus there are $2^{n+k} - 2^{n-k}$ edges connecting to each vertex on the left. For each nonzero Pauli operator $x$ on the right, there is an edge connecting it to the code with stabilizer $S$ if and only if $x$ is contained in $S^\perp \setminus S$. Note that the number $N_e$ of such edges does not depend on $x$.

There are two ways to count the total number of edges, which must agree: the number of codes $|\mathcal{S}|$ times the number of edges connecting to each code equals the number of nontrivial Pauli operators times the number of edges connecting to each nontrivial Pauli operator, or
$$
|\mathcal{S}| \cdot (2^{n+k} - 2^{n-k}) = (2^{2n} - 1) \cdot N_e \Rightarrow |\mathcal{S}|/N_e = 2^{n-k}\left(\frac{1 - 2^{-2n}}{1 - 2^{-2k}}\right).
$$ {#eq-7.208}
Finally, note that the total number of codes connecting to at least one element of $\mathcal{E}^{(2)} \setminus \boldsymbol{I}$ is no larger than $(|\mathcal{E}^{(2)}| - 1) \cdot N_e$; therefore, a code which corrects $\mathcal{E}$ (one connecting to no elements of $\mathcal{E}^{(2)} \setminus \boldsymbol{I}$) surely exists provided that
$$
|\mathcal{S}| > (|\mathcal{E}^{(2)}| - 1) \cdot N_e,
$$ {#eq-7.209}
from which eq.(7.207) follows.

### The old argument

We will only sketch the argument, without carrying out the requisite counting precisely. Let $\mathcal{E} = \{\boldsymbol{E}_a\}$ be a set of errors to be corrected, and denote by $\mathcal{E}^{(2)} = \{\boldsymbol{E}_a^\dagger \boldsymbol{E}_b\}$, the products of pairs of elements of $\mathcal{E}$. Then to construct a nondegenerate code that can correct the errors in $\mathcal{E}$, we must find a set of stabilizer generators such that some generator anti-commutes with each element of $\mathcal{E}^{(2)}$.

To see if a code with length $n$ and $k$ qubits can do the job, begin with the set $\mathcal{S}^{(n-k)}$ of all abelian subgroups of the Pauli group with $n - k$ generators. We will gradually pare away the subgroups that are unsuitable stabilizers for correcting the errors in $\mathcal{E}$, and then see if any are left.

Each nontrivial error $\boldsymbol{E}_a$ commutes with a fraction $\sim 1/2^{n-k}$ of all groups contained in $\mathcal{S}^{(n-k)}$, since it is required to commute with each of the $n - k$ generators of the group. (There is a small correction to this fraction that we may ignore for large $n$.) Each time we add another element to $\mathcal{E}^{(2)}$, a fraction $2^{k-n}$ of all stabilizer candidates must be rejected. When $\mathcal{E}^{(2)}$ has been fully assembled, we have rejected at worst a fraction
$$
|\mathcal{E}^{(2)}| \cdot 2^{k-n},
$$ {#eq-7.210}
of all the subgroups contained in $\mathcal{S}^{(n-k)}$ (where $|\mathcal{E}^{(2)}|$ is the number of elements of $\mathcal{E}^{(2)}$). As long as this fraction is less than one, a stabilizer that does the job will exist for large $n$.

If we want to correct $t = pn$ errors, then $\mathcal{E}^{(2)}$ contains operators of weight at most $2t$ and we may estimate
$$
\log_2 |\mathcal{E}^{(2)}| \lesssim \log_2 \left[\binom{n}{2pn} 3^{2pn}\right] \sim n\left[H_2(2p) + 2p\log_2 3\right].
$$ {#eq-7.211}
Therefore, nondegenerate quantum stabilizer codes that correct $pn$ errors exist, with asymptotic rate $R = k/n$ given by
$$
\log_2 |\mathcal{E}^{(2)}| + k - n < 0, \quad \text{or} \quad R < 1 - H_2(2p) - 2p\log_2 3.
$$ {#eq-7.212}
Thus is the (asymptotic form of the) quantum Gilbert-Varshamov bound.

We conclude that codes with a nonzero rate must exist that protect against errors that occur with any error probability $p < p_{\mathrm{GV}} \simeq .0946$. The maximum error probability allowed by the Rains bound is $p = 1/6$, for a code that can protect against every error operator of weight $\le pn$.

Though good quantum codes exist, the explicit construction of families of good codes is quite another matter. Indeed, no such constructions are known.

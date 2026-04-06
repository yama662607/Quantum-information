# 書籍 115ページ 解説 (Extremal measurements and ensembles - Proof Continued)

## 1. 全文の日本語訳

各 $a \in \Sigma$ に対して、$\theta : \Sigma \to \mathrm{Herm}(\mathcal{X})$ を $\theta(a) = \nu_0(a) - \nu_1(a)$ として定義します。次が成り立ちます：
$$ \sum_{a \in \Sigma} \theta(a) = \sum_{a \in \Sigma} \nu_0(a) - \sum_{a \in \Sigma} \nu_1(a) = \mathbb{1}_{\mathcal{X}} - \mathbb{1}_{\mathcal{X}} = 0. \quad (2.270) $$

さらに、各 $a \in \Sigma$ に対して、
$$ \mathrm{im}(\theta(a)) \subseteq \mathrm{im}(\nu_0(a)) + \mathrm{im}(\nu_1(a)) = \mathrm{im}(\mu(a)) \quad (2.271) $$
が成り立ちます。ここでの等号は、$\nu_0(a)$ と $\nu_1(a)$ が正定値であり、$\mu(a) = (\nu_0(a) + \nu_1(a))/2$ であるという事実の結果です。最後に、$\nu_0$ と $\nu_1$ が異なるという仮定から、$\theta$ が恒等的にゼロではないことが導かれます。

今度は、$\theta : \Sigma \to \mathrm{Herm}(\mathcal{X})$ を恒等的にゼロではなく、かつ
$$ \sum_{a \in \Sigma} \theta(a) = 0 \quad (2.272) $$
および、すべての $a \in \Sigma$ に対して $\mathrm{im}(\theta(a)) \subseteq \mathrm{im}(\mu(a))$ を満たす関数であると仮定します。各 $a \in \Sigma$ に対して、
$$ \mu(a) + \varepsilon_a \theta(a) \ge 0 \quad \text{および} \quad \mu(a) - \varepsilon_a \theta(a) \ge 0 \quad (2.273) $$
を満たす正の実数 $\varepsilon_a > 0$ が存在しなければなりません。これは、$\mu(a)$ が正定値であり、$\theta(a)$ が $\mathrm{im}(\theta(a)) \subseteq \mathrm{im}(\mu(a))$ を満たすエルミート演算子であるという事実に基づいています。ここで、
$$ \varepsilon = \min \{ \varepsilon_a : a \in \Sigma \} \quad (2.274) $$
と置き、次を定義します：
$$ \mu_0 = \mu - \varepsilon\theta \quad \text{および} \quad \mu_1 = \mu + \varepsilon\theta. \quad (2.275) $$

$\mu = (\mu_0 + \mu_1)/2$ であることは明らかです。$\theta$ が恒等的にゼロではなく $\varepsilon$ が正であるため、$\mu_0$ と $\mu_1$ は異なります。最後に、$\mu_0$ と $\mu_1$ が測定（POVM）であることが成り立ちます。仮定 (2.272) は、
$$ \sum_{a \in \Sigma} \mu_0(a) = \sum_{a \in \Sigma} \mu_1(a) = \sum_{a \in \Sigma} \mu(a) = \mathbb{1}_{\mathcal{X}} \quad (2.276) $$
を意味し、一方で不等式 (2.273) は、各 $a \in \Sigma$ に対して測定演算子 $\mu_0(a)$ と $\mu_1(a)$ が正定値であることを意味します。したがって、$\mu$ が端点測定ではないことが確立され、証明が完了します。 $\square$

定理 2.47 は、以下の系（colloraries）を含む様々な示唆を伴います。最初の系は、端点測定が最大でも $\dim(\mathcal{X})^2$ 個の非ゼロの測定演算子しか持つことができないという見解を示しています。

---

## 2. 詳細な解説

115ページでは、定理 2.47 の証明の核心部分が展開されています。

### ① 証明の後半：$\theta$ の構成（前半）
異なる 2 つの測定 $\nu_0, \nu_1$ から差 $\theta$ を作る際、単に引き算をするだけでなく、その演算子の「像（image）」がどうなっているかを議論しています。
*   **重要な恒等式 (2.271)**: $\nu_0, \nu_1$ が正定値であるとき、その和 $\mu$ の像はそれぞれの像を合わせた空間と一致します。この性質により、差である $\theta$ の像も $\mu$ の像の中にすっぽりと収まります。これが「ズレの自由度」を定義する重要な鍵です。

### ② 証明の後半：摂動の構成（後半）
ここがこの証明の最も巧妙な部分です。
*   **微小な正の数 $\varepsilon$ (2.274)**: 
    「$\mu(a)$ の像の中に $\theta(a)$ が収まっている」という条件があれば、どんなに $\theta$ が激しく動いても、非常に小さく（$\varepsilon$ 倍）して足したり引いたりすれば、$\mu(a)$ の正定値性を壊すことはありません。
*   **物理的帰結**: 
    もしこのような「壊さないズレ $\theta$」が一つでも存在するなら、測定 $\mu$ は「左にずらしたもの ($\mu_0$)」と「右にずらしたもの ($\mu_1$)」のちょうど真ん中に位置していることになります。
*   **結論**: 
    真ん中にある、ということはその点は「端（境界）」ではない、つまり端点（極値的）ではない、という理屈です。

### ③ 次のステップへの繋がり
ページ最後の一文で、非常に強力な制約が登場しています。
*   **非ゼロのアウトカム数の上限**: 定理 2.47 から数学的に導かれる結果として、端点測定（＝究極に鋭い測定）であっても、アウトカムの種類数は空間の次元 $d$ に対して $d^2$ 個が限界である、という事実が示唆されています。これは状態トモグラフィーなどで必要な数と一致しており、量子情報の基本的な幾何学的構造を浮き彫りにしています。

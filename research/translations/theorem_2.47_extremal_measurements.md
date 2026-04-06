# 定理 2.47：端点測定の判定条件 (Theorem 2.47)

このドキュメントでは、測定 $\mu$ が「端点（extremal）」であるための必要十分条件を与える **定理 2.47** について、教科書（114–115ページ）のすべての記述と数式を網羅し、論理の飛躍を補いながら詳細に解説します。

---

## 1. 定理のステートメント

$\mathcal{X}$ を複素ユークリッド空間、$\Sigma$ をアルファベットとし、$\mu : \Sigma \to \text{Pos}(\mathcal{X})$ を測定とする。
$\mu$ が端点測定であるための必要十分条件は、以下の 2 条件を満たす任意の関数 $\theta : \Sigma \to \text{Herm}(\mathcal{X})$ に対して、 $\theta$ が恒等的に零 ($\theta = 0$) となることである：

1.  **総和ゼロ条件**: $\displaystyle \sum_{a \in \Sigma} \theta(a) = 0 \quad \dots (2.266)$
2.  **像の包含条件**: すべての $a \in \Sigma$ に対して、$\text{im}(\theta(a)) \subseteq \text{im}(\mu(a))$

**[厳密な定式化：量化子による記述]**
$$ \mu \in \text{Ext}(\text{Meas}(\Sigma, \mathcal{X})) \iff \forall \theta \in \text{Herm}(\mathcal{X})^{\Sigma} : \left[ \left( \sum_{a \in \Sigma} \theta(a) = 0 \land \forall a \in \Sigma, \text{im}(\theta(a)) \subseteq \text{im}(\mu(a)) \right) \implies \theta = 0 \right] $$

---

## 2. 証明の構成

定理の主張を $P \iff Q$ と置くと、証明は以下の 2 ステップで行われます：

1.  **逆方向 ($\impliedby$) の証明 [十分条件]**: 
    対偶 **「$\mu$ が端点でなければ、$\theta \neq 0$ が存在する」** を証明します。（教科書前半：114頁〜115頁冒表）
2.  **順方向 ($\implies$) の証明 [必要条件]**: 
    対偶 **「$\theta \neq 0$ が存在すれば、$\mu$ は端点ではない」** を証明します。（教科書後半：115頁「Conversely...」以降）

---

## 3. 証明：逆方向 ($\impliedby$) [十分条件]
**主張：$\mu$ が端点でない $\implies$ 条件を満たす $\theta \neq 0$ が存在する**

### Step 1: 端点でない場合の仮定
$\mu$ が端点でないなら、ある異なる測定 $\mu_0, \mu_1$ と $\lambda \in (0, 1)$ により $\mu = \lambda \mu_0 + (1 - \lambda) \mu_1 \dots (2.267)$ と書けます。

### Step 2: 等重みの混合への整理 (2.268, 2.269)
比率を $1/2$ ずつにするため、$\nu_0, \nu_1$ を次のように構成します $\dots (2.269)$：
*   **$\lambda \le 1/2$ のとき**: $\nu_0 = 2\lambda \mu_0 + (1-2\lambda)\mu_1, \quad \nu_1 = \mu_1$
*   **$\lambda > 1/2$ のとき**: $\nu_0 = \mu_0, \quad \nu_1 = (2\lambda - 1)\mu_0 + (2 - 2\lambda)\mu_1$

これにより、$\mu = \frac{\nu_0 + \nu_1}{2} \dots (2.268)$ となります。

### Step 3: $\theta$ の定義と検証 (2.270, 2.271)
$\theta = \nu_0 - \nu_1$ と定義すると、$\nu_0 \neq \nu_1$ なので **$\theta \neq 0$** です。
*   **条件1**: $\sum \theta(a) = \sum \nu_0(a) - \sum \nu_1(a) = \mathbb{1} - \mathbb{1} = 0 \dots (2.270)$
*   **条件2**: $\mu = \frac{\nu_0 + \nu_1}{2}$ より各 $\nu_i(a)$ の像は $\mu(a)$ の像に含まれるため、$\text{im}(\theta(a)) \subseteq \text{im}(\mu(a)) \dots (2.271)$

これで、十分条件の対偶が示されました。

---

## 4. 証明：順方向 ($\implies$) [必要条件]
**主張：条件を満たす $\theta \neq 0$ が存在する $\implies \mu$ は端点ではない**

### Step 1: ゼロでない $\theta$ の存在を仮定 (2.272)
条件を満たし、かつ恒等的にゼロではない $\theta$ が存在すると仮定します。
$$ \sum_{a \in \Sigma} \theta(a) = 0 \quad \dots (2.272) $$

### Step 2: 摂動 $\epsilon$ による構成 (2.273, 2.274)
$\text{im}(\theta) \subseteq \text{im}(\mu)$ より、十分に小さな $\epsilon > 0$ に対して以下が成り立ちます：
$$ \mu(a) \pm \epsilon \theta(a) \ge 0 \quad \dots (2.273) $$
ここで $\epsilon = \min \{ \epsilon_a : a \in \Sigma \} \dots (2.274)$ とします。

### Step 3: 新しい測定の定義 (2.275, 2.276)
$$ \mu_0 = \mu - \epsilon \theta, \quad \mu_1 = \mu + \epsilon \theta \quad \dots (2.275) $$
これらは $\sum \theta = 0$ により規格化条件も満たすため、有効な測定です $\dots (2.276)$。

### Step 4: 結論
$\mu = \frac{\mu_0 + \mu_1}{2}$ かつ $\mu_0 \neq \mu_1$ なので、$\mu$ は端点ではありません。
これで必要条件の対偶が示されました。 $\square$

---

## 5. 数学的補足：式 (2.273) の厳密な証明

**命題**: $A \in \text{Pos}(\mathcal{X})$、 $B \in \text{Herm}(\mathcal{X})$ とし、$\text{im}(B) \subseteq \text{im}(A)$ であるとする。このとき、ある $\epsilon > 0$ が存在して $A \pm \epsilon B \ge 0$ が成り立つ。

**証明**:
1.  **サポート空間への制限**:
    $V = \text{im}(A)$ と置く。$A$ はエルミートなので、$\mathcal{X} = V \oplus \text{ker}(A)$ と直交分解できる。
    仮定 $\text{im}(B) \subseteq V$ より、任意の $\phi \in \text{ker}(A)$ に対して $B\phi = 0$ であることがわかる。したがって、全空間 $\mathcal{X}$ において $A \pm \epsilon B \ge 0$ を示すには、部分空間 $V$ 上で制限された演算子が正定値であることを示せば十分である。

2.  **$A$ の最小固有値**:
    $A$ を $V$ 上に制限した演算子 $A|_V$ は、定義よりすべての固有値が正である。
    その最小固有値を $\lambda_{\min}(A) > 0$ とすると、任意の単位ベクトル $u \in V$ に対して次が成り立つ：
    $$ \langle u, Au \rangle \ge \lambda_{\min}(A) $$

3.  **$B$ の有界性**:
    同様に、エルミート演算子 $B$ の $V$ 上での最大固有値（または演算子ノルム）を $\|B\|_V$ とすると、任意の単位ベクトル $u \in V$ に対して次が成り立つ：
    $$ |\langle u, Bu \rangle| \le \|B\|_V $$

4.  **$\epsilon$ の構成**:
    ここで、$\epsilon > 0$ を $\epsilon < \frac{\lambda_{\min}(A)}{\|B\|_V}$ となるように選ぶ（もし $\|B\|_V = 0$ なら任意の $\epsilon$ でよい）。
    このとき、任意の単位ベクトル $u \in V$ に対する期待値は：
    $$ \langle u, (A \pm \epsilon B)u \rangle = \langle u, Au \rangle \pm \epsilon \langle u, Bu \rangle \ge \lambda_{\min}(A) - \epsilon \|B\|_V > 0 $$

5.  **結論**:
    期待値が常に正（厳密には $V$ 上で正、$\text{ker}(A)$ 上で $0$）であるため、演算子として $A \pm \epsilon B \ge 0$ が示された。

---

## 6. 別解：平方根による因数分解を用いたエレガントな証明

行列解析や量子情報理論では、前述の固有値に注目する手法のほかに、**半正定値行列の平方根（$\mu^{1/2}$）**を使って「くくり出す」という、より代数的な証明手法がよく使われます。

### 証明のステップ
1.  **$\theta$ の書き換え**:
    あるエルミート行列 $X$ を用いて、$\theta(a)$ を次のように表現します。
    $$ \theta(a) = \mu(a)^{1/2} X \mu(a)^{1/2} $$
2.  **因数分解**:
    $$ \mu(a) \pm \epsilon \theta(a) = \mu(a)^{1/2} ( \mathbb{1}_{\text{im}} \pm \epsilon X ) \mu(a)^{1/2} $$
    ここで $\mathbb{1}_{\text{im}}$ は $\mu(a)$ の像空間 $\text{im}(\mu(a))$ への射影演算子です。
3.  **正定値性の保証**:
    中身の $(\mathbb{1}_{\text{im}} \pm \epsilon X)$ において、$X$ の（実数である）固有値の絶対値の最大値を $\|X\|$ とすると、$\epsilon \le 1/\|X\|$ と選べばこの項は $0$ 以上になります。
4.  **結論**:
    両側から $\mu(a)^{1/2}$ という「同じ形の演算子」で挟んでいるため、全体として正定値性が保たれます。

### 【重要】なぜ「像の包含関係」がこの表現を可能にするのか？

ご質問のあった「なぜ $\text{im}(\theta) \subseteq \text{im}(\mu)$ が Step 1 の書き換えを保証するのか」という点について補足します。

> [!NOTE]
> **数学的背景：擬逆行列と像の制約**
> 1. **「届かない場所」を排除する**: $\mu(a)^{1/2}$ で両側から挟んで何かを作ろうとする際、$\mu(a)$ が $0$ になっているベクトル（核 $\text{ker}(\mu)$ の成分）に対しては、何を掛けても $0$ にしかなりません。もし $\theta$ が $\text{im}(\mu)$ の外側（核の方向）に少しでも成分を持っていたら、$\mu^{1/2} X \mu^{1/2}$ という形では絶対に表現できません。
> 2. **擬逆行列による $X$ の構成**: 条件 $\text{im}(\theta) \subseteq \text{im}(\mu)$ があれば、$\mu(a)$ の像空間内だけで機能する「逆行列」である **擬逆行列（ムーア・ペンローズ逆行列）$\mu(a)^+$** を使って、$X$ を次のように明示的に定義できます：
>    $$ X = (\mu(a)^{1/2})^+ \theta(a) (\mu(a)^{1/2})^+ $$
>    これに両側から $\mu^{1/2}$ を掛けると、$\text{im}(\theta) \subseteq \text{im}(\mu)$ という条件のおかげで、周辺の射影演算子が消えて $\mu^{1/2} X \mu^{1/2} = \theta$ が厳密に成り立ちます。

この手法の最大のメリットは、**「実数の不等式 $y \pm \epsilon x = y(1 \pm \epsilon \frac{x}{y}) \ge 0$」を考えるのと全く同じ感覚**を行列（演算子）でも適用できる点にあります。

# 量子情報を理解するためのライブラリ・教材ツール調査

調査日：2026-10-16。Luna の3担当が、状態・チャネルと数理最適化、回路SDK、テンソル・可視化の観点から一次資料を調査した。以下はその結果を、この授業の目的に合わせて整理したもの。対象は **外部候補33件と既存環境の道具6件**。ブラウザツールや Julia/MATLAB 製品も含めて数えている。

## この授業での選び方

当面は **Qiskit + NumPy + SymPy + Plotly** で、回路・行列・厳密な途中式・操作できる図を対応させる。この組合せは既存環境にあり、今回の位相・混合状態の教材で実行できた。SDKを増やすより、同じ計算を異なる表現で確認することを優先する。

追加するなら、密度演算子・開放系を深掘りする **QuTiP**、Kraus/Choi表現や情報理論の行列計算には **toqito** が有力。**QuAIRKit** も状態・測定・チャネルのチュートリアルがまとまっている。回路操作をすぐ試す補助教材には **Quirk** が使える。ここでの推奨は教育上の判断で、これらの追加導入・動作検証はまだ行っていない。

「Pythonのバージョン条件を満たす」「macOSを対象としている」「このMacのApple Siliconで実行確認済み」は区別する。下表の対応条件は主に公式ドキュメント・パッケージ設定に基づく。GPU・クラウドは、明示した用途以外では必須としない。リリース番号は変わるため、リンク先で導入時に再確認する。

## 既存環境で使える道具：6件

| 道具 | 理論を取り返す実験 | 公開教材での扱い・一次資料 |
|---|---|---|
| NumPy | 2×2行列の積・トレース、固有値、SVDによるSchmidt係数 | 行列を隠さず計算できる。[SVD](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html) |
| SciPy | ハミルトニアンから行列指数を作り、ゲートと時間発展をつなぐ | レンダリング時の計算に使う。[expm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.expm.html) |
| SymPy | 位相干渉や密度行列を分数・記号のまま導出する | 今回はQiskitの数値結果と厳密式を照合。[行列](https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html) |
| Matplotlib | 回路図、密度行列、誤差や確率の静的な図 | 発表用に保存しやすい。[公式教材](https://matplotlib.org/stable/tutorials/index.html) |
| Plotly | 位相・混合度のスライダー、Bloch図、確率曲線 | 事前計算したフレームなら、公開HTMLだけで操作可能。今回採用。[sliders](https://plotly.com/python/sliders/) |
| ipywidgets | Notebook内でゲートやノイズの値を変えて再計算 | Pythonコールバックにはカーネルが必要。静的HTMLへの埋込みだけで任意のPython処理が動くわけではない。[埋込み](https://ipywidgets.readthedocs.io/en/stable/embedding.html)、[Quarto](https://quarto.org/docs/interactive/widgets/jupyter.html) |

確認時の環境：NumPy 2.3.5、SciPy 1.16.3、SymPy 1.14.0、Matplotlib 3.10.8、Plotly 6.5.0、ipywidgets 8.1.8。回路の基準は Qiskit 2.2.3 / Aer 0.17.2。今回の追加パッケージはない。

## 状態・測定・チャネルを深掘りする：11件

| 候補 | 何が理解しやすくなるか | 導入・保守上の判断と一次資料 |
|---|---|---|
| **QuTiP** | ket / density operator、部分トレース、POVM、Lindblad方程式を共通のオブジェクトで扱う | Python ≥3.11、macOS/CPU対応。BSD-3-Clause。2026年も更新を確認。回路SDKより状態・開放系の理論に向く。[測定](https://qutip.readthedocs.io/en/stable/guide/guide-measurement.html)、[導入](https://qutip.org/download.html)、[設定](https://github.com/qutip/qutip/blob/master/pyproject.toml) |
| **qutip-qip** | QuTiPでゲート列からパルス・ノイズ付きの時間発展へ進む | QuTiP ≥5、Python ≥3.11。BSD-3-Clause。2026年のリリースあり。回路から実装の物理へ進むときに有用。[公式リポジトリ](https://github.com/qutip/qutip-qip)、[教材](https://qutip-qip.readthedocs.io/en/latest/tutorials_v5.html) |
| **toqito** | Kraus/Choi、チャネルの性質、エンタングルメント、状態識別を行列計算で照合 | Python 3.12–3.14の案内、MIT。2026年のリリースあり。CVXPY等のソルバー依存は別途確認。[公式文書](https://toqito.readthedocs.io/en/latest/)、[導入](https://toqito.readthedocs.io/en/latest/getting_started.html) |
| **QuAIRKit** | 純粋・混合状態、PVM/POVM、Kraus/Choi/Stinespring表現からQPEまで | Python 3.10–3.12、PyTorch依存。公式READMEにApple Silicon向け案内。Apache-2.0、2026年のリリースあり。追加依存は比較的大きい。[公式](https://github.com/QuAIR/QuAIRKit)、[状態](https://quairkit.com/QuAIRKit/latest/tutorials/introduction/state.html)、[測定](https://quairkit.com/QuAIRKit/latest/tutorials/introduction/measure.html) |
| CVXPY | POVM最適化・Helstrom識別を半正定値計画として表す | 量子専用ではない。Python ≥3.11、Apache-2.0。ソルバー・複素変数の条件を確認。[導入](https://www.cvxpy.org/install/)、[設定](https://github.com/cvxpy/cvxpy/blob/master/pyproject.toml) |
| PICOS | 複素行列、部分トレース、量子情報の凸最適化を記号的に書く | GPLv3。ソルバー選択が必要。Python 3.12/ARMの実動作は未確認。[量子情報機能](https://picos-api.gitlab.io/picos/qis.html)、[導入](https://picos-api.gitlab.io/picos/introduction.html) |
| QICS | 量子相対エントロピー等の錐を含む最適化 | MIT、CPU向け。Python ≥3.8の案内。今回のアルゴリズム入門より、情報理論を最適化として扱う段階向け。[公式](https://github.com/kerry-he/qics)、[論文](https://arxiv.org/abs/2410.17803) |
| Dynamiqs | JAXで微分可能なSchrödinger/Lindblad時間発展、ノイズのパラメータ走査 | Python ≥3.11、CPUが基本、GPU任意。Apache-2.0。2026年も更新あり。API変化に注意。[導入](https://www.dynamiqs.org/stable/documentation/getting_started/installation.html)、[公式](https://github.com/dynamiqs/dynamiqs) |
| numqi | PPT、エンタングルメント、トモグラフィー等の数値実験 | インストール文書にARM関連の依存案内あり。Python 3.12での実動作・ライセンス・直近の保守状況は今回未確定。採用前に確認。[導入](https://numqi.github.io/numqi/installation/)、[公式](https://github.com/numqi/numqi) |
| QuantumOptics.jl | 密度行列・マスター方程式をJuliaで扱う | Pythonとは別環境。CPU計算候補。ARMでの実動作・ライセンス詳細は未確認。[導入](https://docs.qojulia.org/installation/)、[公式](https://github.com/qojulia/QuantumOptics.jl) |
| QETLAB | Choi行列、PPT、状態・チャネル識別のMATLAB教材 | BSD-2-Clause。MATLABと、最適化ではCVX等が必要。Python環境へそのまま追加する選択肢ではない。[公式サイト](https://qetlab.com/)、[公式コード](https://github.com/nathanieljohnston/QETLAB) |

## 回路とアルゴリズムを別の視点から見る：11件

| 候補 | 教材での持ち味 | 導入・保守上の判断と一次資料 |
|---|---|---|
| **Cirq** | state vector / density matrix、途中段階の状態を追う | Python ≥3.11、macOS/CPU、Apache-2.0。2026年も更新あり。今のQiskit教材と役割が重なる。[シミュレーション](https://quantumai.google/cirq/simulate/simulation)、[導入](https://quantumai.google/cirq/start/install) |
| **PennyLane** | `default.qubit` / `default.mixed`、状態の検査、後には変分回路の微分 | Python ≥3.11、CPU、Apache-2.0。2026年も更新あり。最適化を学ぶ段階で優先度が上がる。[回路検査](https://docs.pennylane.ai/en/stable/introduction/inspecting_circuits.html)、[導入](https://docs.pennylane.ai/en/stable/development/guide/installation.html) |
| Qibo | NumPyバックエンドで回路と密度行列を扱う | Python ≥3.11、CPU使用可、Apache-2.0。2026年10月の更新を確認。GPUは任意。[API](https://qibo.science/qibo/stable/api-reference/qibo.html)、[導入](https://qibo.science/qibo/stable/getting-started/installation.html) |
| Qrisp | 高水準の量子変数、算術、アルゴリズムの組立て | Python ≥3.11,<3.14の設定。EPL-2.0等の選択ライセンスは公式で確認。行列を理解する最初の教材より、その後の抽象化に向く。[状態ベクトル](https://qrisp.eu/reference/Core/generated/qrisp.QuantumSession.statevector.html)、[公式](https://github.com/eclipse-qrisp/Qrisp) |
| pytket | 回路の変形・最適化と等価性を比較 | Python ≥3.10、Apache-2.0。密度行列などの実行機能はバックエンド拡張依存。拡張ごとの対応・保守を確認。[回路](https://docs.quantinuum.com/tket/user-guide/manual/manual_circuit.html)、[拡張](https://docs.quantinuum.com/tket/api-docs/extensions.html) |
| Amazon Braket SDK | ローカルの状態ベクトル・密度行列とクラウド実行を共通形式で扱う | Python ≥3.11、Apache-2.0。ローカル用途にAWS実機は不要。クラウド利用は別途アカウント・費用が関係する。[シミュレータ](https://docs.aws.amazon.com/braket/latest/developerguide/braket-submit-tasks-simulators.html)、[公式](https://github.com/amazon-braket/amazon-braket-sdk-python) |
| CUDA-Q | ハイブリッドプログラムと複数実行基盤 | 現行Quick StartにはApple SiliconのCPU実行を案内。NVIDIA GPUの利用条件とは区別する。Python ≥3.11、Apache-2.0。[導入](https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html)、[リリース](https://github.com/NVIDIA/cuda-quantum/releases) |
| Tequila | 変分アルゴリズムの目的関数・期待値を抽象化 | MIT。実行基盤の依存があり、Macでのネイティブ拡張に注意。Python 3.12/ARMの実動作は未確認。[公式](https://github.com/tequilahub/tequila) |
| Perceval | 離散的な光量子回路・光源・損失を学ぶ | CPU、Python 3.10–3.14の案内、2026年のリリースあり。量子ビットの符号化と異なるため、今回の導入には追加説明が必要。ライセンス詳細は採用時確認。[公式](https://github.com/Quandela/Perceval) |
| Strawberry Fields | 連続変数量子系、Gaussian/Fock表現、ホモダイン測定 | **調査時点でアーカイブ済み**。Apache-2.0。Python 3.8–3.10向け案内で、現環境3.12への新規採用は優先しない。[公式](https://github.com/XanaduAI/strawberryfields) |
| MrMustard | 光量子状態・チャネルの位相空間/Fock表現 | **調査時点でアーカイブ済み**。Apache-2.0。Python 3.12対応の設定があっても保守継続を意味しない。[公式](https://github.com/XanaduAI/MrMustard)、[設定](https://github.com/XanaduAI/MrMustard/blob/develop/pyproject.toml) |

## エンタングルメント・特殊回路・図解：11件

| 候補 | 教材での持ち味 | 導入・保守上の判断と一次資料 |
|---|---|---|
| **Quimb** | 部分トレース、エントロピー、テンソルネットワーク・MPS | Python ≥3.11、CPU。2026年の更新あり。ライセンス検出APIの結果だけでは確定せず、採用時にLICENSEを確認。[導入](https://quimb.readthedocs.io/en/latest/installation.html)、[公式](https://github.com/jcmgray/quimb) |
| TeNPy | Schmidt係数・MPS/MPO、DMRG・時間発展 | Apache-2.0、Python 3.12対応の履歴あり。ネイティブ拡張とMacの実動作は別途確認。多体系の理解向け。[公式](https://github.com/tenpy/tenpy) |
| TensorNetwork | ノード・辺・縮約でテンソル積を図式化 | **調査時点でアーカイブ済み**。Apache-2.0。新規教材の基盤より既存資料を読む参考候補。[公式](https://github.com/google/TensorNetwork) |
| ITensors.jl | 添字付きテンソルとMPS/MPOをJuliaで記述 | Apache-2.0。別途Julia環境が必要。現在の依存・関連パッケージ分割は採用時に確認。[公式](https://github.com/ITensor/ITensors.jl)、[開発FAQ](https://docs.itensor.org/ITensors/v0.9/faq/Development.html) |
| NetKet | JAXによる多体系の変分状態・ニューラル量子状態 | Python ≥3.11、CPU使用可、Apache-2.0。2026年の更新あり。今回の基本回路からは距離がある。[導入](https://netket.readthedocs.io/en/stable/install.html) |
| Stim | stabilizer・Clifford・Pauliノイズの高速計算 | Apache-2.0、Apple ARM向け配布あり。ただし任意の非Clifford回路を一般に扱う道具ではない。誤り訂正向け。[公式](https://github.com/quantumlib/Stim) |
| PyZX | ZX図式による回路変形と等価性 | Apache-2.0、CPU、2026年も更新あり。干渉を学んだ後、回路を変形して同じ答えになる理由を調べる教材に向く。[公式](https://github.com/zxcalc/pyzx) |
| QuantumClifford.jl | stabilizerの純粋・混合状態、Pauli測定 | MIT、Julia/CPU。2026年のリリースあり。誤り訂正や特殊な状態表現の比較に向く。[公式](https://github.com/QuantumSavory/QuantumClifford.jl) |
| **Quirk** | ブラウザで回路を組み、途中の振幅・確率をすぐ観察 | Apache系ライセンスのブラウザ教材。インストール不要。測定の簡略化があり、一般の測定後状態・CPTP写像の説明を全面的に委ねない。古いリリースとWiki更新は区別する。[実演](https://algassert.com/quirk)、[使い方](https://github.com/Strilanc/Quirk/wiki/How-to-use-Quirk) |
| Q.js | JavaScript/ブラウザの簡単な回路・Bell状態実験 | ブラウザ教材候補。直近の保守・ライセンス・密度行列機能は今回未確定。新規基盤としての採用判断は保留。[公式](https://github.com/stewdio/q.js)、[デモ](https://quantumjavascript.app/) |
| Manim Community | ブラケットの変形、Bloch球、振幅増幅の説明動画 | MIT、CPU中心、動画生成用の外部依存あり。**量子シミュレータではない**。発表用アニメーションの制作段階で検討。[公式](https://github.com/ManimCommunity/manim)、[導入](https://docs.manim.community/en/stable/installation.html) |

## 教材へ取り込む順序と検証

1. **今回**：既存のSymPyで厳密な式、Qiskitで回路と密度行列、Plotlyで位相・混合度の操作を用意する。連続位相 → 純粋/混合 → 制御演算 → Deutsch の順にする。
2. **チャネルの表現を学び直す回**：QuTiP / toqito / QuAIRKitから一つを試し、同じチャネルのKraus・Choi・環境系を用いた表現を、小さな行列で照合する。
3. **その後**：状態識別ならCVXPY、エンタングルメントならQuimb、誤り訂正ならStim、変分回路ならPennyLaneというように、学ぶ問題が必要とする道具を追加する。

追加候補の評価では、まず単一量子ビットの行列計算・部分トレース・既知の測定確率を照合する。同じ記号でも基底順序、テンソル積順序、Choi正規化等が異なるので、数値の見かけだけを比較しない。

公開HTMLでは、事前計算したPlotly図と、Pythonを再実行する対話を区別する。本プロジェクトのQuarto Live/Pyodideの制約は [docs/quarto-live.md](../../docs/quarto-live.md) を参照。標準のPyodideでQiskitが動くことを前提にしない。

## 調査の限界

外部33候補は導入していない。ライセンスやPython条件が未確定の項目は未確定と記載した。公開リポジトリの更新・アーカイブ状態は保守の参考情報であり、品質や将来の保守を保証しない。主要候補のGitHubメタデータは親担当でも照合した。各公式URLは導入時に再確認する。

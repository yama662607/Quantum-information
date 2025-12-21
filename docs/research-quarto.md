# Quartoによる高機能ドキュメント作成サンプル

## 基本構造（YAMLフロントマターとセクション構造）

Quartoドキュメントは、ファイル先頭にYAML形式のメタデータブロック（フロントマター）を配置し、その後にMarkdown本文を書いていきます。YAMLフロントマターではタイトルや著者、日付のほか、出力フォーマットや全体設定を指定できます([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=,format%3A%20pdf))。例えば以下のように記述します（`---`で開始・終了）:

```
yamlCopy code`---
title: "Quarto機能デモ"
author: ["山田 太郎"]
date: "2025-12-21"
format: 
  html: default
  pdf: default
toc: true              # 目次を自動生成
number-sections: true  # セクション番号を付与
jupyter: python3       # Pythonカーネルを使用
---
`
```

上記では、HTMLとPDFの両方の出力を指定し、全フォーマット共通オプションとして目次（`toc: true`）とセクション番号（`number-sections: true`）を有効化しています([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=The%20next%20three%20lines%20are,specified%20at%20the%20root%20level))([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Next%2C%20we%20have%20the%20,specific%20options))。QuartoはMarkdownを拡張した記法を採用しており、見出しは`#`記号で指定します。例えば章や節の構成には以下のようにMarkdown記法で見出しレベルを使います。

```
markdownCopy code`# 第一章 タイトル

本文...

## セクション 1

内容...

### 小セクション

内容...

## セクション 2

...
`
```

`number-sections: true`の場合、これらの見出しに自動で番号付けされます([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=Section%20Numbering))。目次（Table of Contents）も`toc: true`により生成され、既定では見出しレベル3までを含みます（`toc-depth`オプションで深さ調整可能([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=Table%20of%20Contents))）。特定の見出しを目次や番号付けから除外したい場合、見出し行の末尾にクラス属性として`.unlisted`（目次除外）や`.unnumbered`（番号除外）を付与できます([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=If%20you%20want%20to%20exclude,classes%20to%20it))。

YAMLフロントマターでは、このほか文書全体の設定としてキーワードや要旨、ライセンス情報なども指定可能です([3](https://quarto.org/docs/authoring/front-matter.html#:~:text=Scholarly%20articles%20require%20much%20more,on%20copyright%2C%20licensing%20and%20funding))([3](https://quarto.org/docs/authoring/front-matter.html#:~:text=license%3A%20,specific%20funding%20for%20this%20work))。特に学術論文向けには`abstract`（要約）や`keywords`、`bibliography`（参考文献ファイル）等のフィールドを利用できます。

## 複数出力フォーマット（HTMLとPDFなど）

Quartoでは単一のソースファイルから複数の形式に同時に出力できます。フロントマターの`format`キーに複数フォーマットを列挙することで、例えばHTMLとPDF、さらにWord（docx）など複数の出力を指定可能です([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=,top%3D30mm))。上記例では`format:`以下に`html: default`および`pdf: default`を記述しましたが、各フォーマットごとにオプションを細かく指定することもできます。例えば:

```
yamlCopy code`format:
  html:
    code-fold: true       # HTMLではコードブロックの折りたたみを許可
    html-math-method: katex  # 数式をKaTeXで表示
  pdf:
    toc: true             # PDFでも目次を付与
    number-sections: true # PDFでも番号付け
    geometry: 
      - top=30mm
      - left=20mm        # PDFの余白設定
  docx: default           # Word出力もデフォルト設定で有効
`
```

このように記述すると、Quarto実行時に単一の`.qmd`ファイルから複数の出力ファイルが生成されます([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Rendering))([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Then%20the%20following%20files%20would,be%20created))。例えば上記設定で`document.qmd`をレンダリングすると、`document.html`, `document.pdf`, `document.docx`が一度に作成されます([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Then%20the%20following%20files%20would,be%20created))。コマンドラインでは`quarto render document.qmd`で全出力、`quarto render document.qmd --to pdf`のように`--to`オプションで特定フォーマットだけを出力することも可能です([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=We%20can%20select%20one%20or,to%60%20option))。

**PDF出力の注意:** QuartoでPDFを生成する場合、内部でPandoc+LaTeXによるコンパイルを行います。そのため事前にTeX環境（TeX Liveなど）のインストールが必要です([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Caution%20LaTeX%20Required%20for%20,pdf))。Quarto公式ではTexLiveを簡易に導入できるTinyTeXの利用を推奨しています([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=Prerequisites))。LaTeXが利用可能であれば、YAMLでPDF固有のオプション（例えば`mainfont`や用紙サイズ、documentclass等）も指定できます([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=Quarto%20uses%20KOMA%20Script%20document,emphasis%20on%20typography%20and%20versatility))。QuartoのPDF出力は既定でKOMA-Scriptの`scrartcl`（article相当）クラスを使用し、美しい組版になるようデフォルト設定が工夫されています([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=Document%20Class))([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=You%20can%20set%20,LaTeX%20packages%20you%20have%20installed))。`documentclass`を`book`等に変えれば両面印刷や章ごとの改ページなど本用の設定も自動適用されます([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=Note))。

## コードチャンクと出力制御（eval, echo, output他）

QuartoではMarkdown文中にプログラミング言語のコードブロック（コードチャンク）を含めて、計算やプロットを自動実行しその結果を埋め込むことができます。コードチャンクは一般的なフェンス区切り（` ```{言語名}`）で記述し、実行時には指定した言語のカーネル（上の例ではPython）でコードが評価されます。**コードセルオプション**として、チャンクの先頭に特殊コメント`#|`で始まる行で様々な出力制御を指定できます([4](https://quarto.org/docs/computations/execution-options.html#:~:text=Code%20block%20options%20are%20included,are%20considered%20options))。主なオプションには以下のようなものがあります([4](https://quarto.org/docs/computations/execution-options.html#:~:text=Option%20Description%20,halt%20processing%20of%20the%20document)):

- `eval`: コードを実行するか否か。`false`の場合、そのチャンクは**実行されず**コードそのものが表示されます([4](https://quarto.org/docs/computations/execution-options.html#:~:text=Option%20Description%20,Include%20warnings%20in%20the%20output))。

- `echo`: ソースコードを出力に表示するか。`false`にするとコードは非表示になり、結果（アウトプット）のみが表示されます([4](https://quarto.org/docs/computations/execution-options.html#:~:text=Option%20Description%20,Include%20warnings%20in%20the%20output))。

- `output`（または類似の`results`オプションに相当）: コード実行結果を表示するか。`true`/`false`のほか、`asis`を指定すると出力を生のMarkdown/HTMLとして扱います([4](https://quarto.org/docs/computations/execution-options.html#:~:text=output%29.%20,halt%20processing%20of%20the%20document))。例えばコード内でMarkdown形式の表を生成してprintした場合に、そのMarkdownをそのまま解析させたい場合などに`output: asis`を使います。

- `warning`: 実行時の警告メッセージを出力に含めるか（`false`で抑制）([4](https://quarto.org/docs/computations/execution-options.html#:~:text=have%20any%20of%20Quarto%E2%80%99s%20standard,halt%20processing%20of%20the%20document))。

- `error`: エラー発生時にメッセージを出力に含めるか（`false`にするとエラーも無視して処理続行。ただしデフォルトではエラーで処理停止）([4](https://quarto.org/docs/computations/execution-options.html#:~:text=have%20any%20of%20Quarto%E2%80%99s%20standard,halt%20processing%20of%20the%20document))。

- `include`: 出力にコードも結果も一切含めない場合に`false`を指定します([4](https://quarto.org/docs/computations/execution-options.html#:~:text=,output%20from%20the%20code%20block))（この設定はそのチャンクの**すべて**の出力を抑制し、計算だけ行う隠れた処理に使えます）。

- `fig-cap`, `tbl-cap`: コードが生成する図表にキャプションを与える場合の指定（次節参照）。

- `label`: このチャンクからの図表やリストをクロスリファレンス可能にするための識別子（`fig-`や`tbl-`などで始める。詳細は後述）。

**グローバル設定:** これらのコード実行オプションはフロントマターの`execute`キー下で全チャンクに対するデフォルトを設定できます([4](https://quarto.org/docs/computations/execution-options.html#:~:text=Output%20Options))([4](https://quarto.org/docs/computations/execution-options.html#:~:text=,echo%3A%20false%20jupyter%3A%20python3))。例えば全体で`echo: false`を指定しつつ特定チャンクだけ`#| echo: true`で例外的にコードを見せる、といった制御が可能です([4](https://quarto.org/docs/computations/execution-options.html#:~:text=the%20Python%20example%20to%20specify,code%20into%20the%20output%20document))([4](https://quarto.org/docs/computations/execution-options.html#:~:text=Note%20that%20we%20can%20override,block%20basis.%20For%20example))。

**コードチャンクの記述例:**

```
markdownCopy code````{python}
#| echo: false
#| warning: false
data = [1, 2, 3, 4]
print("データの長さ:", len(data))
`
```

```
powershellCopy code`上記の場合、このPythonコードは実行され、その結果（`データの長さ: 4`）だけがドキュメント中に表示されます（コード自体は`echo: false`により非表示）。また実行中の警告も`warning: false`で抑制しています。

QuartoはR、Python、Juliaなど複数の言語に対応しています。Rの場合はR Markdownに近いknitrオプション形式も使用できますが、QuartoではYAMLスタイルのオプション記述（上記の`#|`形式）に統一することが推奨されています:contentReference[oaicite:31]{index=31}。PythonやJuliaでも同様に`#|`コメントでオプションを指定します。

## 数式の表示（LaTeX記法）
QuartoではLaTeX形式の数式記法をサポートしており、文章中に数式をそのまま埋め込むことができます。インライン数式はドル記号`$ ... $`で囲み、別行立ての表示数式は`$$ ... $$`で囲んで記述します。例えば、アインシュタインの質量エネルギー等価の式をインラインで表記するには`$E = mc^2$`のように書きます。ブロック表示なら:

```markdown
Einsteinの特殊相対性理論によれば、質量とエネルギーの等価性は次式で表されます:

$$
E = mc^{2}
$$
`
```

と記述します。Quartoでレンダリングすると、インライン数式`$E=mc^2$`は本文中でE=mc2E = mc^{2}E=mc2のように表示され、ブロック数式は中央に独立した式としてレンダリングされます([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Einstein%27s%20theory%20of%20special%20relatively,equivalence%20of%20mass%20and%20energy))([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=%5C%28E%20%3D%20mc))。

デフォルトではHTML出力時にMathJax（もしくはPandoc内蔵のmathml）により数式が描画されますが、オプションでKaTeXを使うことも可能です([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=html%3A%20code,docx%3A%20default))。例えばフロントマターで`html-math-method: katex`と指定すると、高速なKaTeXでHTML中の数式が描画されます([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=html%3A%20code,docx%3A%20default))。

**数式番号と参照:** Quartoでは数式を含むあらゆる要素にラベルを付けて相互参照する機能があります（詳細は後述の「クロスリファレンス」参照）。数式の場合、表示形式の式(`$$ $$`で囲んだもの)の直後に`{#eq-ラベル名}`と記述してラベル付けできます([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=%23%23%20Equation%20%7B%23sec))。例えば上記の式にラベル`eq-energia`を付けるには:

```
markdownCopy code`$$
E = mc^2
$$ {#eq-energia}
`
```

とします。こうしておくと、文中で「@eq-energia」という形で参照を挿入でき、出力時に自動で式番号付きで参照されます（例：「式(1)」のように）([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=See%20%40fig,demonstration%20of%20a%20simple%20plot))([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Equation%20%60%40eq))。

## 図の挿入とキャプション、クロスリファレンス

文章中に画像やプロットを挿入する方法はいくつかあります。**静的画像**の場合、Markdownの標準記法である `![キャプション](パス){オプション}` を用いればOKです。例えば`![クマの写真](bear.png){#fig-bear width=50%}`のように記述すると、`bear.png`という画像ファイルが幅50%で挿入され、「クマの写真」というキャプションが付与されます。また `{#fig-bear}` によりこの図にID「fig-bear」が付き、後で参照可能になります([5](https://quarto.org/docs/authoring/figures.html#:~:text=and%20then%20referencing%20the%20figure,prefix.%20For%20example))。Quartoでは図表ラベルは**プレフィックスで種類を判断**します。`fig-`で始まるIDは図、`tbl-`で始まるIDは表というように扱われ([5](https://quarto.org/docs/authoring/figures.html#:~:text=Important%20Label%20Prefix))、自動番号や参照時の表記（Figure/Table）が適切に行われます。

**コードから生成した図:** PythonやRコードの出力としてプロットを作成する場合、チャンクオプションで図のキャプションやラベルを指定できます。先ほどのコードチャンク例に、例えばMatplotlibでプロットを描くコードを組み込むとします:

```
markdownCopy code````{python}
#| label: fig-sin
#| fig-cap: "正弦波のグラフ"
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
`
```

```
perlCopy code`
このチャンクでは`label: fig-sin`により図に「fig-sin」というIDが割り当てられ、`fig-cap:`でキャプション「正弦波のグラフ」を指定しています:contentReference[oaicite:41]{index=41}。Quartoはこのコードを実行し、生成されたプロット画像を自動で本文に埋め込み、指定のキャプション付き図として配置します。ラベルが付いているため、この図は「図1: 正弦波のグラフ」のように番号付きで表示され、文中で`@fig-sin`と書けば「図1」への参照ハイパーリンクに自動変換されます:contentReference[oaicite:42]{index=42}。

**図の配置とレイアウト:** Quartoでは複数の図を並べて配置することも容易です。PandocのDivブロック機能を利用し、複数の画像を以下のように囲めば、並列配置と一括キャプションが可能です:contentReference[oaicite:43]{index=43}:contentReference[oaicite:44]{index=44}。

```markdown
::: {#fig-elephants layout-ncol=2}
![ゾウA](elephant1.png){#fig-elephant1}

![ゾウB](elephant2.png){#fig-elephant2}

有名な象たち
:::
`
```

上記では2つの画像を`layout-ncol=2`属性付きのdivブロックで囲みました。こうすると2カラムで画像が並び、最後の段落「有名な象たち」が全体のメインキャプション「Figure 1: 有名な象たち」として表示されます([5](https://quarto.org/docs/authoring/figures.html#:~:text=Image%3A%20An%20artistic%20rendition%20of,are%20centered%20beneath%20both%20pictures))([5](https://quarto.org/docs/authoring/figures.html#:~:text=the%20left,are%20centered%20beneath%20both%20pictures))。各画像には個別に`![タイトル](画像){#fig-id}`とキャプションを付けているので、出力ではそれぞれ「(a) ゾウA」「(b) ゾウB」のようなサブキャプション付きで並びます([5](https://quarto.org/docs/authoring/figures.html#:~:text=Image%3A%20An%20artistic%20rendition%20of,are%20centered%20beneath%20both%20pictures))。なお、このような**サブ図（subfigure）**には自動で(a), (b)といった識別子が付きます。Quartoでは空行で段落を区切ることで、それぞれの画像が別個の図として認識される点に注意が必要です([5](https://quarto.org/docs/authoring/figures.html#:~:text=Note%20that%20the%20empty%20lines,images%20within%20the%20same%20paragraph))。

図のレイアウト制御として、`layout-ncol`のほかに`layout-nrow`を指定してグリッド状（複数行×列）に配置することもできます([5](https://quarto.org/docs/authoring/figures.html#:~:text=Multiple%20Rows))。さらに詳細なレイアウト（例えば各行で列数が異なるケース）もカスタムCSSやラップ用Divを駆使すれば実現可能です([5](https://quarto.org/docs/authoring/figures.html#:~:text=Image%3A%20A%202x2%20grid%20of,Lin%20Wang%2C%20and%20Abdul%20Abbas))。

**図の位置とLaTeX設定:** PDF出力時には図の位置指定や浮動配置がLaTeXに委ねられるため、Quartoでは`fig-pos`オプションでLaTeXの図環境オプション（[h], [t]など）を指定できます([5](https://quarto.org/docs/authoring/figures.html#:~:text=Figure%20Position))([5](https://quarto.org/docs/authoring/figures.html#:~:text=The%20default%20LaTeX%20,pos))。また`fig-env`で用いる環境名（figure*, subfigureなど）を直接指定することも可能です([5](https://quarto.org/docs/authoring/figures.html#:~:text=There%20are%20a%20number%20of,image%20or%20the%20fenced%20div))([5](https://quarto.org/docs/authoring/figures.html#:~:text=%21%5BElephant%5D%28surus.jpg%29%7B%23fig))。例えば`fig-env="figure*"`とすれば二段組の場合に両カラムにまたがる図を作ることができます([5](https://quarto.org/docs/authoring/figures.html#:~:text=There%20are%20a%20number%20of,image%20or%20the%20fenced%20div))。これらはPDF特有の高度な調整ですが、必要に応じてYAMLの`format: pdf`以下や個々のチャンクオプションで設定できます。

## テーブルの作成と整形

表（テーブル）はMarkdownの表記法を基本的に利用できます。シンプルなパイプ区切り表は次のように記述します:

```
markdownCopy code`| 商品   | 価格  | 備考            |
|--------|------:|-----------------|
| りんご |  200 | 甘い           |
| みかん |  150 |                 |
| バナナ |  100 | 安い・おいしい |
`
```

上記は左寄せ・右寄せ・中央揃えの指定をヘッダ下のコロンで行っています（価格欄は`------:`と末尾コロンで右寄せ）([6](https://quarto.org/docs/authoring/tables.html#:~:text=,123))。Quartoではこの表をそのままHTMLやPDFにレンダリングできます。

**キャプションとラベル:** 図同様、表にもキャプションとIDを付けられます。Markdown表の直後に説明文を`:`で始める行として書き、その末尾に `{#tbl-...}` とIDを指定します([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=For%20markdown%20tables%2C%20add%20a,For%20example))([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=%3A%20My%20Caption%20%7B%23tbl))。例えば:

```
markdownCopy code`| Col1 | Col2 | Col3 |
|------|------|------|
| A    | B    | C    |
| D    | E    | F    |

: これはサンプル表です {#tbl-sample}
`
```

このようにすると「Table: これはサンプル表です」というキャプション付きの表となり、ID `tbl-sample`が割り当てられます([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=For%20markdown%20tables%2C%20add%20a,For%20example))([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=See%20%40tbl))。参照時は文章中に`@tbl-sample`と記述すれば、表番号とキャプション（例：「表1」）が自動挿入されます([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=%3A%20My%20Caption%20%7B%23tbl))。表の場合もIDは`tbl-`で始める必要があります([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=Important%20Label%20Prefix))。

QuartoはPandoc拡張により**Grid表**（罫線表）にも対応しています。複数行のセルや改行を含む内容を表にしたい場合、`+`と`|`を組み合わせたGrid表記法が利用できます([6](https://quarto.org/docs/authoring/tables.html#:~:text=match%20at%20L812%20,))([6](https://quarto.org/docs/authoring/tables.html#:~:text=match%20at%20L844%20,in%20wrapper%20%7C))。ただし一般的な用途ではパイプ表で十分なことが多いでしょう。

**表の書式設定:** HTML出力では、表に対してCSSクラスを指定してデザインを調整できます。Quarto標準で用意されているクラスには、ストライプ（縞模様行）を付ける`.striped`や行にマウスオーバー時のハイライトを付ける`.hover`などがあります([6](https://quarto.org/docs/authoring/tables.html#:~:text=,))。例えばキャプション行を`: キャプションテキスト {.striped .hover}`とすれば、その表は縞模様＋行ハイライト付きで描画されます([6](https://quarto.org/docs/authoring/tables.html#:~:text=,))。列幅の調整も可能で、表ヘッダ区切り線中のダッシュ数で相対的な幅を指定できます([6](https://quarto.org/docs/authoring/tables.html#:~:text=match%20at%20L498%20For%20example,be%20sized%20to%20their%20contents))([6](https://quarto.org/docs/authoring/tables.html#:~:text=of%20dashes%20in%20each%20column,column%20table))。より明示的には、キャプション行に`{tbl-colwidths="[40,60]"}`のようにスタイル属性を書いて各列幅（%指定）を決めることもできます([6](https://quarto.org/docs/authoring/tables.html#:~:text=You%20can%20also%20explicitly%20specify,colwidths))([6](https://quarto.org/docs/authoring/tables.html#:~:text=,))。

なお、QuartoではRの**gt**パッケージや**knitr::kable**、Pythonの**pandas.DataFrame**など様々な方法で生成した表を埋め込めます。Rで`knitr::kable`を使う場合、チャンクオプションで`tbl-cap`や`label`を指定するとキャプション付き表を出力できます([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=You%20can%20also%20cross,cap%60%20cell%20options.%20For%20example))。Pythonの場合、pandasのDataFrameを単純にprintすればMarkdown表として出力されるほか、`display(Markdown(...))`で明示的にMarkdown形式テーブルを渡すこともできます([6](https://quarto.org/docs/authoring/tables.html#:~:text=%23%7C%20label%3A%20tbl,Astronomical%20object))。これらも`#| tbl-cap:`や`#| label: tbl-...`をチャンクに書けばクロスリファレンス対応の表となります([6](https://quarto.org/docs/authoring/tables.html#:~:text=%23%7C%20label%3A%20tbl,Astronomical%20object))([6](https://quarto.org/docs/authoring/tables.html#:~:text=%23%7C%20label%3A%20tbl,colwidths%3A%20%5B60%2C40))。

**複合表とサブテーブル:** Quartoは複数の表を並べて一つの図表として扱うことも可能です。図の場合と同様にDivブロックで囲み`layout-ncol`属性を使えばサブテーブルを横並びできます([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=))([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=%3A%3A%3A%20%7B%23tbl,G))。各表に個別キャプションとIDを付け、ブロックの最後に全体キャプションを付けることで、「表1: ○○ (a)… (b)…」といった複合表を実現できます([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=))([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=,G))。サブキャプションを(a),(b)など記号のみにしたい場合はチャンクオプションで`tbl-subcap: true`を指定する方法もあります([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=If%20you%E2%80%99d%20like%20subfigure%20captions,than%20providing%20explicit%20subcaption%20text))（テキストなしで識別子のみのサブキャプション）。

## 図表番号とクロスリファレンス

上記までに触れたように、Quartoは図・表・数式・コードブロック・セクション見出しなどに**ラベルを付けて相互参照（クロスリファレンス）**する機能を備えています。参照付き要素には一律に「番号」が付き、本文中から`@ラベル`で参照すると「図1」「表2」「式(3)」のように種類に応じた番号付きで表示され、クリックするとその要素箇所へハイパーリンクします([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=See%20%40fig,demonstration%20of%20a%20simple%20plot))([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Image%3A%20Rendered%20page%20with%20linked,references%20to%20figures%20and%20equations))。これにより「上記の図1に示すように…」「表2より…」といった記述が動的に管理でき、文書構成が変わって図表番号が変わっても参照が自動更新されます。

ラベルはYAMLフロントマター内で利用するクロスレファレンス拡張機能により、**接頭辞でタイプを区別**します([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Cross,and%20a%20caption))([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Entity%20Reference%20Label%20%2F%20Caption,plot))。代表的な接頭辞と参照対象:

- `fig-` : 図（Figure）([5](https://quarto.org/docs/authoring/figures.html#:~:text=Important%20Label%20Prefix))

- `tbl-` : 表（Table）([6](https://quarto.org/docs/authoring/tables.html#:~:text=%23%7C%20label%3A%20tbl,Astronomical%20object))

- `eq-` : 数式（Equation）([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Equation%20%60%40eq))

- `sec-` : セクション（Section見出し）([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=See%20%40fig,demonstration%20of%20a%20simple%20plot))

- `lst-` : コードリスト（Listing）([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=Code%20Listings))

例えばセクション見出しに`# データ分析 {#sec-analysis}`のようにIDを付け、他の箇所で`@sec-analysis`と参照すれば「第1章」など節番号つきで参照できます([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=See%20%40fig,demonstration%20of%20a%20simple%20plot))。コードリスト（ソースコードの断片）も、チャンクに直接IDを付与するかDivで囲んで`#lst-` IDとキャプションを与えることで参照可能な「リスティング」として扱えます([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=To%20create%20a%20reference,cap%60%20attribute.%20For%20example))([7](https://quarto.org/docs/authoring/cross-references.html#:~:text=To%20create%20a%20cross,the%20caption%20inside%20the%20div))。例えば:

```
markdownCopy code````{#lst-algo .python}
# ソートアルゴリズムの例
def quicksort(arr): ...
`
```

上記をリスト@lst-algoで示した。

```
rubyCopy code`
とすると、コードブロックに「Listing 1: ソートアルゴリズムの例」というキャプションが付き、参照`@lst-algo`が「Listing 1」にリンクされます:contentReference[oaicite:92]{index=92}。

Quartoはデフォルトでキャプション中に「Figure」「Table」「Equation」などの語を付与しますが、この接頭辞（ラベル表記）は変更可能です:contentReference[oaicite:93]{index=93}。例えば「Fig.」や「図」などにカスタマイズしたい場合、YAMLで`locale`設定やLuaフィルタを用いて変更することもできます（詳細は公式ドキュメントのCross-Reference Options参照）。

## 脚注、参考文献と引用
**脚注:** Markdown標準の脚注記法(`[^1]`や`^[...]`)が利用できます。本文中で例えば`脚注の例^[ここに脚注内容]`と書くと、その箇所に上付き番号が付き、ページ末または文末に脚注内容が小さく表示されます。Quartoでは脚注の既定位置を変更するオプションもあります。フロントマターで`reference-location`を設定すると、脚注（および引用文献リスト）の配置を制御できます:contentReference[oaicite:94]{index=94}。`reference-location: margin`とすれば脚注がページ下ではなく余白（マージン）に表示され、いわゆるサイドノートになります:contentReference[oaicite:95]{index=95}。デフォルト値`block`ではページ下部に脚注が並びます。また、脚注ではない**余談注（asides）**として、本文中の一部テキストを余白に出すこともできます。例えば`[この部分が余白に表示]{.aside}`のように書けば、そのテキストが脚注番号なしで余白に表示されます:contentReference[oaicite:96]{index=96}。

**文献リストと引用（References & Citations）:** QuartoはPandocのciteproc機能を利用しており、文献管理はBibTeXやCSL(JSON)ファイルで行えます。フロントマターに`bibliography: refs.bib`のように文献データベースファイルを指定し:contentReference[oaicite:97]{index=97}、本文中で`[@文献キー]`と書くと引用挿入されます:contentReference[oaicite:98]{index=98}。たとえばBibTeXファイル`references.bib`に以下のエントリがあるとします:

```bibtex
@article{knuth1984,
  title={Literate programming},
  author={Knuth, Donald E.},
  journal={The Computer Journal},
  year={1984},
  ...}
`
```

これをフロントマターで指定し、本文中で`Knuth曰く常にリテラルに書くべき[@knuth1984]`と記述すると、出力時に「Knuth (1984)曰く常にリテラルに書くべき」もしくは引用スタイルに応じ「(Knuth 1984)」のような形式で組み込まれます([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Knuth%20says%20always%20be%20literate,knuth1984))([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Note%20that%20items%20within%20the,syntax))。文末には自動的に参考文献セクションが生成され、該当文献の書誌情報が整形されて表示されます([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Image%3A%20Rendered%20document%20with%20references,111))。文献リストの見出しは自分で「## 参考文献」等と付けておく必要があります([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Knuth%20says%20always%20be%20literate,knuth1984))([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=References%20will%20be%20included%20at,bottom%20of%20the%20source%20file))（付け忘れても文献は最後に追加されますが、見出しが無いと一覧だけが唐突に出現します）。

引用表記は柔軟で、[@key pp.123]のようにページ指定したり、文中で埋め込む場合[@key]、カッコ外で著者名だけ出す@keyなどPandocの仕様に準じます([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Note%20that%20items%20within%20the,syntax))。引用スタイルはデフォルトではChicago風ですが、`csl`オプションに対応するCSLファイル（例えばAPAスタイルのCSL）を指定すれば書式を変更できます。例えば`csl: apa.csl`をYAMLに加えればAPAフォーマットで文献一覧と引用が整形されます。

## カスタムCSSやテーマの適用

見た目の調整について、Quartoは**テーマ**と**カスタムCSS**による柔軟なカスタマイズが可能です。HTML出力ではBootstrapを基盤とした複数のテーマが用意されており、フロントマターの`theme:`で指定できます([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=Use%20of%20any%20of%20these,option.%20For%20example))。利用可能なテーマには、Bootstrap標準の"flatly"や"yeti"、またBootswatchの"cosmo"や"darkly"など多数があります([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=,zephyr))。例えば:

```
yamlCopy code`format:
  html:
    theme: united
`
```

とすれば明るめのUnitedテーマが適用されます([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=Use%20of%20any%20of%20these,option.%20For%20example))。テーマを適用するとフォントや色、余白などが一括設定されます。ただし細部の調整が必要な場合、**テーマ変数**や**Sass (SCSS)**を用いたカスタムテーマを導入できます([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=You%20can%20do%20extensive%20customization,all%20of%20the%20variables%20here))。Quartoでは1つのテーマとして複数ファイルを指定でき、例えば:

```
yamlCopy code`format:
  html:
    theme:
      - cosmo    # 既存テーマ
      - custom.scss  # 上書き用自作SCSS
`
```

と書けばCosmoテーマをベースに`custom.scss`で定義したスタイルを上書きできます([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=theme%3A%20))。SCSSファイルでは変数セクション（`/*-- scss:defaults --*/`コメント以降）にBootstrapのSass変数を書き換え、ルールセクション（`/*-- scss:rules --*/`以降）に任意のCSSを記述します([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=%2F%2A,weight%3A%20%20500%20%21default))([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=h1%2C%20h2%2C%20h3%2C%20h4%2C%20h5%2C,3%29%3B))。例えば`$font-size-base`を変更したり、見出しにシャドウ効果を加えるCSSを書くなど自在です。

単にいくつかのスタイルを微調整したい場合は、通常のCSSファイルを読み込むこともできます。QuartoドキュメントYAMLでは`format: html: css: custom.css`のようにCSSファイルパスを指定するか、プロジェクト全体の設定ファイル`_quarto.yml`で`css: [`複数のCSSリスト`]`を指定できます([9](https://stackoverflow.com/questions/74026514/how-to-apply-css-style-to-quarto-output#:~:text=Write%20the%20CSS%20properties%20for,from%20a%20quarto%20document%20file))（Stack Overflow回答の指摘による）。このCSSは最終HTMLに埋め込まれ、任意のセレクタでスタイルを上書きできます。**注意:** QuartoのHTML出力はデフォルトでBootstrapを用いているため、既存クラス名と競合しないようにするか、!important指定やセレクタの優先度を考慮する必要があります。場合によってはQuartoのテーマ機能でSCSSとして書くほうが簡潔です。

PDF出力に関しては、LaTeXテンプレートのカスタマイズになります。QuartoはPandocデフォルトのLaTeXテンプレートを使用しますが、`includes:`オプションで独自のTeXを挿入できます（例えば`includes: in-header: mypreamble.tex`でプリアンブル挿入）。またフォントや余白はYAMLの`mainfont`, `fontsize`, `geometry`などで指定可能です([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=,sections%3A%20true%20colorlinks%3A%20true))([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=format%3A%20pdf%3A%20documentclass%3A%20scrartcl%20papersize%3A,letter))。デフォルトテーマではKOMA-Scriptを使用しているため、美しい余白や本文フォントが設定されていますが、`documentclass`を変えて標準の`article`にすれば従来の見た目にもできます([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=You%20can%20set%20,LaTeX%20packages%20you%20have%20installed))。

最後に、Quartoには**ライトモード/ダークモード**の切り替え機能もあります。`theme:`に`light`と`dark`を指定すると、読者がトグルで切り替え可能な2種類のテーマを提供できます([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=Dark%20Mode))([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=))。例えば:

```
yamlCopy code`format:
  html:
    theme:
      light: flatly
      dark: darkly
    respect-user-color-scheme: true
`
```

とすると、初期表示はユーザのOS設定（ライト/ダーク）に合わせ、自動トグルボタンもHTMLに追加されます([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=When%20providing%20both%20a%20dark,the%20user%E2%80%99s%20preference%20across%20sessions))([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=html%3A%20respect))。コードハイライトも自動で明暗に応じた配色が選択されます([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=Quarto%20will%20automatically%20select%20the,more%20information%2C%20see%20Code%20Highlighting))。

## レイアウト制御（カラムレイアウト、Div構造など）

Quartoで凝ったレイアウトを実現するには、いくつかの手法があります。基本的に本文の幅は約700pxに最適化されていますが([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Article%20Layout))、余白部分（マージン）や全幅の利用、複数カラム表示が可能です。

**マージンへの要素配置:** 先述した脚注をマージンに出す方法のほか、図や表、テキストを意図的に余白に置くこともできます。チャンクオプションで`column: margin`を指定すると、そのコードが生成した図や表は余白部分に小さく配置されます([10](https://quarto.org/docs/blog/posts/2022-02-17-advanced-layout/#:~:text=Margin%20Figures))([10](https://quarto.org/docs/blog/posts/2022-02-17-advanced-layout/#:~:text=Figures%20that%20you%20create%20using,be%20placed%20in%20the%20margin))。例えばRのプロットチャンクに`#| column: margin`と付ければ、そのグラフは紙面の余白側に表示され、本文の流れを邪魔しません([10](https://quarto.org/docs/blog/posts/2022-02-17-advanced-layout/#:~:text=Figures%20that%20you%20create%20using,be%20placed%20in%20the%20margin))([10](https://quarto.org/docs/blog/posts/2022-02-17-advanced-layout/#:~:text=Figure%C2%A01%3A%20MPG%20vs%20horsepower%2C%20colored,by%20transmission))。同様にテーブルにも使えます([10](https://quarto.org/docs/blog/posts/2022-02-17-advanced-layout/#:~:text=Margin%20Tables))([10](https://quarto.org/docs/blog/posts/2022-02-17-advanced-layout/#:~:text=You%20an%20also%20place%20tables,column%3A%20margin))。また任意のMarkdownコンテンツをマージンに置きたい場合、`::: {.column-margin}`で囲んだブロックを使います([10](https://quarto.org/docs/blog/posts/2022-02-17-advanced-layout/#:~:text=You%20can%20also%20place%20content,margin%60%20class.%20For%20example))([10](https://quarto.org/docs/blog/posts/2022-02-17-advanced-layout/#:~:text=We%20know%20from%20the%20first,a%2C%20b))。これを使うと数式や文章の一部を余白に出すことができ、紙面を有効活用できます。

**カラムレイアウト:** Quarto自体には複雑なグリッドレイアウトを宣言的に記述する簡単な構文はありませんが、PandocのDivやBootstrapの行列システムを活用できます。Pandocのfenced Divを`.columns`や`.column`クラス付きで用いれば、複数段組の文章を作ることも可能です（例えば2カラム文章にするなど）。例えば:

```
markdownCopy code`:::::{.columns}
::: {.column width="50%"}
左カラムのテキスト。
:::
::: {.column width="50%"}
右カラムのテキスト。
:::
:::::
`
```

のようにすれば2カラムのレイアウトになります（ただしBootstrapのグリッドを使うために自前CSSが必要な場合があります）。一方、Quartoが提供する簡便な方法として**パネルレイアウト**があります。インタラクティブドキュメント（ShinyやDashboard）向けですが、`layout-ncol`や`layout-nrow`で出力要素（図表やコントロール）を矩形グリッドに配置できます([5](https://quarto.org/docs/authoring/figures.html#:~:text=Multiple%20Rows))。これは前述の図や表のサブレイアウトで活用しました。

**コールアウトと非表示要素:** レイアウト制御としては、情報を枠で強調表示する*コールアウト*も有用です。`::: {.callout-note}`のようにDivにクラスを付けると、Note/Tip/Warningなど5種類のスタイルで内容を囲んで表示できます([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Callouts))([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Note))。コールアウトはサイドバー的な視覚効果がありますが、本文幅内に配置されます。またHTMLでは詳細ブロック(`<details>`タグ)を直接書くことで折りたたみ可能なセクションを作れますが、Quartoではそれに相当するMarkdown拡張は提供していません（コードブロックの折りたたみは後述する`code-fold`で可能）。

なお、Quartoは高機能なレイアウトが必要な場合に**カスタムレイアウトテンプレート**を作成する仕組みもあります。例えば複数の図表やテキストを組み合わせた独自レイアウトを頻繁に使うなら、Luaフィルタやカスタムショートコード（後述）で再利用可能な構造を定義することも可能です。

## 目次（TOC）やナビゲーション構造

**単一ドキュメントの目次:** 先に説明した通り、フロントマターで`toc: true`とすればHTML/PDFいずれの出力でも自動目次が生成されます([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=Table%20of%20Contents))。HTMLではサイドバーやページ上部に目次パネルが配置され、PDFでは通常「Contents」として本文の前に目次ページが挿入されます。`toc-depth`で目次に含める見出しレベルを指定でき、例えば`toc-depth: 2`ならH3（###）以下の見出しは目次に載りません([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=Table%20of%20Contents))。目次のタイトルは`toc-title`オプションで変更可能です([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=toc))。特定の見出しを目次から除外したい場合は、前述のように見出しに`.unlisted`クラスを付与します([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=If%20you%20want%20to%20exclude,classes%20to%20it))。

**複数ドキュメントのナビゲーション:** Quartoでは複数のページからなるWebサイトやブック形式のプロジェクトを作成できます（次項で詳述）。その場合、各ページをリンクするナビゲーションが自動生成されます。特に**Quarto Book**プロジェクトでは、サイドバーに章立てが表示され、前後の章への移動リンク、トップページへのリンクなどが付きます([11](https://quarto.org/docs/books/#:~:text=HTML%20books%20are%20actually%20just,29%20between%20different%20chapters))。サイトナビゲーションはプロジェクト設定ファイル`_quarto.yml`で定義し、ページ（または章）リストを並べるか、あるいはカスタムのナビバー構造をYAMLで記述します([12](https://quarto.org/docs/books/book-structure.html#:~:text=The%20structure%20of%20a%20Quarto,incorporate%20multiple%20parts%20and%2For%20appendices))。例えばブックでは:

```
yamlCopy code`project:
  type: book
book:
  title: "サンプルブック"
  chapters:
    - index.qmd
    - chapter1.qmd
    - chapter2.qmd
    - references.qmd
`
```

のように順序を定義します([11](https://quarto.org/docs/books/#:~:text=project%3A%20type%3A%20book))([11](https://quarto.org/docs/books/#:~:text=date%3A%20%228%2F18%2F2021%22%20chapters%3A%20,references.qmd))。HTMLブックではこれに基づいて左側に目次パネル（サイドバー）が生成され、各章の見出しも含めた展開型のナビゲーションが表示されます。また全ページ横断の検索ボックスも付与されます([11](https://quarto.org/docs/books/#:~:text=HTML%20books%20are%20actually%20just,29%20between%20different%20chapters))。サイト（bookでないwebサイト）では`website:`セクションでnavbarメニューを定義できます([13](https://quarto.org/docs/websites/website-navigation.html#:~:text=Website%20Navigation%20,menus))。

PDFブックの場合、全章が結合され1つのPDFになり、目次は自動的に章・節を含む詳細なものが入ります（LaTeXのbookクラス機能を利用）([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=Note))。この場合ナビゲーションはPDF内のしおり（ブックマーク）として機能します。

## インタラクティブ要素（コード折りたたみ、対話型チャートなど）

**コード折りたたみ:** HTML出力では、コードセルを折りたたんで表示できる機能があります。フロントマターまたはチャンク単位で`code-fold: true`を指定すると、そのコードブロックは初期状態で非表示（結果のみ表示）になり、ユーザが「Show/Hide Code」をクリックすると展開されるようになります([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=html))。これは読者に必要以上のコードを見せずに済むため、教材などで有用です。たとえば全体オプションとして`code-fold: true`を設定すれば、全コードブロックが折りたたみ可能になります([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=html))。特定のチャンクだけ常に表示したい場合は、そのチャンクで`code-fold: false`や`echo: true`を指定してオーバーライドします。

**対話型プロットやウィジェット:** Quartoはノートブックドキュメントとして、JavaScriptベースの対話機能を持つオブジェクトを埋め込むことが可能です。例えばPythonのPlotlyやBokehによるインタラクティブグラフ、またはipywidgetsによるインタラクティブUIを出力として含めると、HTML上で対話可能になります([14](https://quarto.org/docs/interactive/widgets/jupyter.html#:~:text=Jupyter%20Widgets%20enable%20you%20to,and%20threejs%20directly%20from%20Python))([15](https://quarto.org/docs/interactive/#:~:text=Widgets))。Quartoはそれらを**クライアントサイドで完結する形**で埋め込むため、完成したHTMLはスタンドアロンで対話機能を有します([15](https://quarto.org/docs/interactive/#:~:text=Widgets))([15](https://quarto.org/docs/interactive/#:~:text=Jupyter%20Widgets%20and%20htmlwidgets%20are,within%20normal%20static%20HTML%20documents))。たとえばPlotlyで生成したグラフオブジェクト`fig`をJupyterカーネルで表示するコードを書けば、そのままHTMLではPlotlyのJSライブラリと図が埋め込まれ、ユーザはマウスオーバーやズームなどの操作ができます。Rでも同様にhtmlwidgets（例えばleaflet, plotly, DTなど）を用いれば対話要素を埋め込めます([16](https://quarto.org/docs/interactive/widgets/htmlwidgets.html#:~:text=htmlwidgets%20for%20R%20,and%20threejs%20directly%20from%20R))([15](https://quarto.org/docs/interactive/#:~:text=Widgets))。

**注意点:** これら対話要素はHTMLでのみ有効で、PDFやWordには静的な画像または表としてエクスポートされます。QuartoはPandocの機能で、対話チャートをPNG画像にフォールバックさせる処理も持っています（例えばPlotly図は静止画に変換）。そのため、HTML閲覧時には動的、PDFでは静的画像として、という形で同一ソースから両対応コンテンツを提供可能です。

**その他のインタラクティブ拡張:** Quartoは高度な例として、Observable JavaScriptやShinyとの連携も可能です。Observable JSセルをQuarto文書に埋め込むことで、相互に値を反映しあうダイナミックなノートブックを実現できます([15](https://quarto.org/docs/interactive/#:~:text=Observable%20JS%20uses%20some%20special,created%20with%20the%20following%20code))([15](https://quarto.org/docs/interactive/#:~:text=sel.filter%28d%20%3D%3E%20d.fame%20))。またRのShinyを組み込めば、Quartoドキュメント内でリアクティブなUI部品とプロットを動作させることもできます([15](https://quarto.org/docs/interactive/#:~:text=Shiny))([15](https://quarto.org/docs/interactive/#:~:text=To%20learn%20more%20see%20the,on%20Using%20Shiny%20with%20Quarto))（ただしShinyの場合はサーバが必要になる点がJSウィジェットと異なります([15](https://quarto.org/docs/interactive/#:~:text=Shiny%20makes%20it%20very%20straightforward,use%20Shiny%20to%20a%20server))）。これらはやや高度な利用法ですが、Quartoドキュメントは単なる静的レポートに留まらずリッチなインタラクティブ教材・ダッシュボードにもなり得ます。

## マルチページ構成やブック構成（Quarto Book）

Quartoを使うと、複数の章立てドキュメントを束ねて**本（Book）形式**の出力を作成できます([11](https://quarto.org/docs/books/#:~:text=Quarto%20Books%20are%20combinations%20of,in%20a%20variety%20of%20formats))。Bookプロジェクトでは各章を個別の`.qmd`ファイルとして用意し、プロジェクトの`_quarto.yml`で順序やブックタイトル等を指定します([11](https://quarto.org/docs/books/#:~:text=project%3A%20type%3A%20book))。例えば前述の`_quarto.yml`例では4つの章（index, intro, summary, references）が定義されていました([11](https://quarto.org/docs/books/#:~:text=date%3A%20%228%2F18%2F2021%22%20chapters%3A%20,references.qmd))。`index.qmd`はブック全体のイントロや前書きに相当し、HTML出力では自動的にブック全体のトップページになります。

**ブックの出力:** Quartoはブックを複数フォーマットで出力可能です([11](https://quarto.org/docs/books/#:~:text=Quarto%20Books%20are%20combinations%20of,in%20a%20variety%20of%20formats))。HTMLブックの場合、各章が独立したHTMLページとなり、サイトとして相互にリンクされます([11](https://quarto.org/docs/books/#:~:text=HTML%20books%20are%20actually%20just,29%20between%20different%20chapters))。検索機能やサイドバー目次も標準で付きます([11](https://quarto.org/docs/books/#:~:text=HTML%20books%20are%20actually%20just,29%20between%20different%20chapters))。一方、PDFブックでは全章が連結された一冊のPDF（もしくはLaTeX文書）になります([11](https://quarto.org/docs/books/#:~:text=Terminal))。`quarto render`コマンドをプロジェクトルートで実行すると、`_book/`ディレクトリにHTMLページ群および`mybook.pdf`（ファイル名はbook設定のタイトルから）等が出力されます([11](https://quarto.org/docs/books/#:~:text=quarto%20render))([11](https://quarto.org/docs/books/#:~:text=Terminal))。複数フォーマット指定していれば、同時にEPUBやWordを生成することもできます([11](https://quarto.org/docs/books/#:~:text=Quarto%20Books%20are%20combinations%20of,in%20a%20variety%20of%20formats))。

**章番号と参照:** Bookプロジェクトでは章ごとに番号が付き、クロスリファレンスも章を跨いで機能します([11](https://quarto.org/docs/books/#:~:text=consequently%20support%20all%20of%20the,Cross%20References%20between%20different%20chapters))。Quartoは自動的に章番号を各ファイルのH1見出しに割り振ります。例えばChapter 2の中の図表は「Figure 2.1」「Figure 2.2」のように章番号込みで番号付けされ、参照もその形式になります。別の章から参照する場合も`@fig-label`でOKで、適切に章番号付きの参照テキストが入ります（Quarto BookではCross-References機能が拡張され、異なるファイル間でも整合性が保たれます([11](https://quarto.org/docs/books/#:~:text=HTML%20books%20are%20actually%20just,29%20between%20different%20chapters))([11](https://quarto.org/docs/books/#:~:text=consequently%20support%20all%20of%20the,Cross%20References%20between%20different%20chapters))）。

**ブックの拡張機能:** Quarto Bookでは、複数章をパートごとにグループ化したり、付録(appendix)を付けたりといった高度な構成も可能です([11](https://quarto.org/docs/books/#:~:text=Once%20you%E2%80%99ve%20got%20the%20basic,ways%20to%20enhance%20your%20book))。付録にした章ファイルには自動でアルファベット番号(A, B, C…)が付与されるなどの仕組みがあります。さらに索引や用語集を作る機能はQuarto自体にはありませんが、Luaフィルタを使って索引を生成することも実践されています。

ブックやサイトを公開（デプロイ）する際は、GitHub PagesやNetlify、あるいは社内サーバーなど静的ホスティングにアップロードすることで利用者に提供できます([11](https://quarto.org/docs/books/#:~:text=Quarto%20books%20can%20be%20published,Publishing%20Websites%20for%20additional%20details))([11](https://quarto.org/docs/books/#:~:text=See%20the%20documentation%20on%20Publishing,site))。Quartoは`quarto publish`コマンドも用意しており、GitHub連携などもサポートしています。

## プレゼンテーション（Reveal.jsスライド等）

Quartoは文書だけでなく**プレゼンテーションスライド**もMarkdownで作成できます。特にReveal.jsを用いたHTMLスライド、PowerPoint（pptx）、Beamer（LaTeXスライド）に対応しています([17](https://quarto.org/docs/presentations/revealjs/index.html#:~:text=))。スライドを作るには、フロントマターで`format: revealjs`等と指定します。例えば:

```
yamlCopy code`format: revealjs
`
```

とした`.qmd`ファイルをレンダリングすると、HTMLのスライドショーが生成されます([17](https://quarto.org/docs/presentations/revealjs/index.html#:~:text=format%3A%20revealjs%20))。Markdownの見出し(`#`など)がスライドの区切り（水平スライド）になり、`---`（水平線）を書くと手動のスライド区切りとしても機能します。スライド内で縦方向のサブスライドを作りたい場合、`##`見出しを用いるか、`:::`区切りを使うことで可能です（QuartoはPandocのスライド機能を継承しています）。

スライドでは、ノート機能（`???`で区切って下に書いた部分は講演者ノートになる）、箇条書きの段階的表示（リストに`>`を付けるとインクリメンタル表示）などReveal.js固有の機能も利用できます([17](https://quarto.org/docs/presentations/revealjs/index.html#:~:text=))。テーマも数種類（Reveal用のテーマや自作CSS）選択可能で、フロントマターの`revealjs:`セクションで設定します。例えば背景や遷移効果、スライド比率なども細かく指定できます。

Quartoの強みは、同じ内容から記事とスライドを両方生成することも容易な点です。たとえば`format: [html, revealjs]`と2つ書けば、1つの.qmdから通常のHTML文書とスライドHTMLを同時に出力できます（もちろんレイアウトに適した記述に工夫は必要ですが）。また、条件付きコンテンツ機能を使えば「スライド用には含めるが記事用には省く内容」などを記述できます([11](https://quarto.org/docs/books/#:~:text=))。これはYAMLで`filters:`や特殊マークアップを用いて実現しますが、詳細はQuarto公式の「Conditional Content」を参照してください。

## コードセルのシンタックスハイライトとコードフォーマット整形

**シンタックスハイライト:** QuartoはPandocを通じて多言語の構文ハイライトに対応しています。デフォルトでは落ち着いた配色のテーマが適用されていますが、YAMLの`highlight-style`オプションでテーマを変更できます([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=PDF%20Basics%20,themes%20include%3A%20arrow%2C%20pygments))。利用可能なハイライトテーマには*pygments*, *tango*, *kate*, *monochrome*, *espresso*, *zenburn*, *haddock*, *breezedark*などがあります([2](https://quarto.org/docs/output-formats/pdf-basics.html#:~:text=PDF%20Basics%20,themes%20include%3A%20arrow%2C%20pygments))。例えば:

```
yamlCopy code`highlight-style: pygments
`
```

とすればPygmentsの色付けが使われます([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=toc%3A%20true%20number,left%3D20mm%20html))。ダークテーマ用には`breezedark`などを指定できます。Quartoはライト/ダーク両モードを提供している場合、自動的に適切なハイライトテーマのバリエーションを切り替えます([8](https://quarto.org/docs/output-formats/html-themes.html#:~:text=HTML%20Theming%20,you%20have%20specified%20when%20possible))。例えば`highlight-style: atom-one`はライトとダーク両方の配色を持つテーマで、ダークモード時には自動で暗色用スタイルが適用されます([18](https://stackoverflow.com/questions/77937498/custom-syntax-highlighting-for-light-and-dark-mode-quarto#:~:text=Custom%20syntax%20highlighting%20for%20light,one%20will%20automatically))。カスタムのシンタックスハイライト配色を使いたい場合は、自分でJSONまたは.themeファイルをPandoc用に用意しQuartoに読み込ませることも可能ですが、多くの場合既存テーマで事足りるでしょう。

**コードフォーマッタの適用（Blackなど）:** コードの整形（フォーマット）は、Quarto本体には自動適用機能がありませんが、**フィルタ（拡張機能）**を使って実現できます。例えばPythonコードに対して自動でBlackフォーマッタをかけたい場合、コミュニティ提供のQuartoフィルタ「black-formatter」を利用できます([19](https://github.com/shafayetShafee/black-formatter#:~:text=Black))。これはLuaで書かれたPandocフィルタで、内部でBlackを呼び出してコードセルの内容を整形してくれます([19](https://github.com/shafayetShafee/black-formatter#:~:text=Before%20using%20this%20filter%2C%20make,See%20here%20for%20installation%20command))。使用手順としては、プロジェクトディレクトリでコマンド`quarto add shafayetShafee/black-formatter`を実行しフィルタをインストールした後、ドキュメントのYAMLに:

```
yamlCopy code`filters:
  - black-formatter
`
```

と記述します([19](https://github.com/shafayetShafee/black-formatter#:~:text=))。またBlack自体もシステムにインストールしておく必要があります([19](https://github.com/shafayetShafee/black-formatter#:~:text=Using))。Blackのオプション（行長など）はプロジェクトルートの`pyproject.toml`で指定可能で、例えば行長80桁にしたければ`[tool.black] line-length = 80`と書きます([19](https://github.com/shafayetShafee/black-formatter#:~:text=And%20it%20is%20possible%20to,toml%20file))。Blackフィルタを適用すると、レンダリング時に各Pythonチャンクのコードが自動でフォーマットされ、出力ドキュメントには整形済みのコードが表示されます([19](https://github.com/shafayetShafee/black-formatter#:~:text=Then%20add%20the%20filter%20in,your%20quarto%20document))。

エディタレベルでも、VS CodeやRStudioでBlackを導入しておけばソースを書く段階で整形できますが([20](https://forum.posit.co/t/format-python-code-in-quarto-r-markdown-files/159452#:~:text=Community%20forum,support%20for%20it%20I%20believe))、Quartoフィルタを使うことで再現性を保ちながらビルド時にコード整形できる点は便利です。Black以外にも、例えばRのstylerによるフォーマットや特定のLint処理をフィルタで組み込むことも考えられます。Quarto自体は「任意言語+任意フォーマッタの組み合わせ全て」に対応することは困難なので、フィルタ機構でそれらを補えるようになっています([21](https://github.com/orgs/quarto-dev/discussions/11063#:~:text=Code%20Block%20Formatting%2FFixers%3F%20%2311063%20,))。

## カスタムマクロやフィルタの活用

QuartoはPandocベースであるため、Pandocの**Luaフィルタ**や**JSONフィルタ**、さらにはQuarto独自の**ショートコード**機能を用いてカスタマイズを拡張できます。

**ショートコード（Shortcodes）:** これはMarkdown中に簡易なマクロのような記法で動的コンテンツを挿入する仕組みです。Hugo等の静的サイトジェネレータに似た発想で、`{{< 名前 パラメータ >}}`という書式で書きます。Quartoにはいくつか標準ショートコードが用意されており、例えばプレースホルダー画像を差し込みたい場合は`{{< placeholder 300 200 >}}`と書けば300x200pxのダミー画像が生成されます([22](https://quarto.org/docs/authoring/placeholder.html#:~:text=match%20at%20L464%20,pixel%20PNG))。形式はPNGまたはSVGを選べ、`format="svg"`を付ければSVG形式のベクター画像になります([22](https://quarto.org/docs/authoring/placeholder.html#:~:text=%7B%7B,))([22](https://quarto.org/docs/authoring/placeholder.html#:~:text=match%20at%20L469%20,height))。他にも`{{< lorem >}}`でダミーテキスト（羅列）を生成したり([22](https://quarto.org/docs/authoring/placeholder.html#:~:text=,pixel%20PNG))、`{{< quarto-version >}}`で現在使用しているQuartoのバージョン番号を表示するなどのショートコードがあります。ショートコードは自作することも可能で、その場合はextensionとしてLuaフィルタを登録する形になります。

**フィルタ（Filters）:** 既にBlackフォーマッタの例で触れましたが、QuartoはPandocフィルタを通じて入出力のMarkdown AST（抽象構文木）を加工できます([19](https://github.com/shafayetShafee/black-formatter#:~:text=Black))。LuaでPandocフィルタを記述するか、Python/Rのパッケージを使ってJSONフィルタを実装することもできます。フィルタはYAMLの`filters:`に列挙して指定し、複数適用もできます。例えば数式を自動番号しつつWordに出力する際に書式調整するフィルタや、特定のマークアップを置換するフィルタなど、ニーズに応じて自作・導入が可能です。Quarto公式サイトやGitHubには有志によるフィルタ（例: 図表キャプションのカスタム、特定語のインデックス自動生成など）が公開されています。

**拡張機能（Extension）:** Quartoではフィルタやレイアウト、テーマなどをパッケージ化した**Extension**を導入できます([19](https://github.com/shafayetShafee/black-formatter#:~:text=Installing))。`quarto add <GitHubリポジトリ>`でプロジェクトに追加し、必要に応じてYAMLに設定を追記するだけで利用可能です。例えば前述のBlackフォーマッタや、日本語文書向けの組版調整（禁則処理など）フィルタ、あるいは学会用テンプレート（フォーマット）などもExtensionとして提供されています([23](https://github.com/arcruz0/quarto-compact#:~:text=GitHub%20github,right%3D.8in))。Extensionは自作して配布することも可能で、Quarto公式のガイドも用意されています([24](https://quarto.org/docs/extensions/formats.html#:~:text=Custom%20Formats%20,text))。

以上、本ドキュメント（サンプル.qmd）では、Quartoの主要機能を網羅的に紹介しました。実際にQuartoを用いることで、**1つのMarkdownベースのソース**から**高品質なHTML/PDFドキュメント**や**プレゼンテーション**、**論文/書籍**まで多彩な成果物を得ることができます。コードと文章を統合し、数式や図表の参照を自動管理することで、再現性の高いドキュメント作成が可能です。是非このサンプルを参考に、Quartoでのドキュメント作成を体験してみてください。各種機能の詳細は公式ドキュメントにも掲載されています([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=In%20this%20tutorial%20we%E2%80%99ll%20explore,references%2C%20and%20more))([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Image%3A%20Rendered%20page%20with%20linked,references%20to%20figures%20and%20equations))（本書中に引用したリンク先を参照）。Quartoを駆使して、リッチでメンテナブルなドキュメント作成に挑戦してみましょう。

**References（英語資料）**([1](https://quarto.org/docs/get-started/authoring/vscode.html#:~:text=Image%3A%20Rendered%20document%20with%20references,111))([11](https://quarto.org/docs/books/#:~:text=Quarto%20Books%20are%20combinations%20of,in%20a%20variety%20of%20formats))
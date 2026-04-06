# 環境構築ログ (Setup Log)

このドキュメントは、2026年1月19日に実施した Windows 環境でのプロジェクト初期設定手順を記録したものです。

---

## 📋 概要

| 項目 | 内容 |
|:---|:---|
| **実施日** | 2026年1月19日 |
| **OS** | Windows |
| **シェル** | PowerShell |
| **プロジェクト** | Quantum Information Study Notes |

---

## 🔧 インストールしたツール

| ツール | バージョン | 用途 |
|:---|:---|:---|
| **uv** | 0.9.26 | Python の超高速パッケージ管理・仮想環境制御 |
| **Just** | 1.46.0 | コマンドライン操作を標準化するタスクランナー |
| **Quarto** | 1.8.27 | 技術文書の出版・ドキュメンテーションシステム |

---

## 📝 詳細手順

### ステップ 1: uv のインストール

**uv** は Python の環境構築を高速かつ確実に行うためのパッケージマネージャーです。

#### 実行コマンド

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### 結果

```
Downloading uv 0.9.26 (x86_64-pc-windows-msvc)
Installing to C:\Users\hiroto yamada\.local\bin
```

#### インストール先

- `C:\Users\hiroto yamada\.local\bin\uv.EXE`

---

### ステップ 2: Just のインストール

**Just** はプロジェクト内のコマンド（ビルド、チェック、サーバー起動など）を実行するためのタスクランナーです。

#### 実行コマンド

```powershell
winget install casey.just --accept-source-agreements --accept-package-agreements
```

#### 結果

```
見つかりました Just [casey.just] バージョン 1.46.0
ダウンロード中 https://github.com/casey/just/releases/download/1.46.0/just-1.46.0-x86_64-pc-windows-msvc.zip
インストーラーハッシュが正常に検証されました
アーカイブを展開しています...
コマンド ライン エイリアスが追加されました: "just"
インストールが完了しました
```

#### インストール先

- `C:\Users\hiroto yamada\AppData\Local\Microsoft\WinGet\Packages\Casey.Just_Microsoft.Winget.Source_8wekyb3d8bbwe\just.EXE`

---

### ステップ 3: Quarto のインストール

**Quarto** は技術文書を作成・公開するためのドキュメンテーションシステムです。

#### 実行コマンド

```powershell
winget install Posit.Quarto --accept-source-agreements --accept-package-agreements
```

#### 結果

```
見つかりました Quarto [Posit.Quarto] バージョン 1.8.27
ダウンロード中 https://github.com/quarto-dev/quarto-cli/releases/download/v1.8.27/quarto-1.8.27-win.msi
インストーラーハッシュが正常に検証されました
パッケージのインストールを開始しています...
インストールが完了しました
```

#### インストール先

- `C:\Program Files\Quarto\bin\quarto.EXE`

---

### ステップ 4: プロジェクトのセットアップ

全ての依存ツールがインストールされた後、`just setup` コマンドでプロジェクトの依存関係をインストールしました。

#### 実行コマンド

```powershell
# 環境変数を更新してから実行
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
just setup
```

#### 処理内容

1. **環境チェック (`check-env`)**: 必要なツール (uv, just, quarto, npm) がインストールされているか確認
2. **Python 環境構築 (`uv sync --all-extras`)**:
   - Python 3.12.12 のダウンロード・インストール
   - 仮想環境 (`.venv`) の作成
   - 124 個の Python パッケージのインストール
3. **npm パッケージのインストール (`npm install`)**

#### 結果

```
🔍 Checking development environment...

✅ uv         Found: C:\Users\hiroto yamada\.local\bin\uv.EXE
   Version: uv 0.9.26 (ee4f00362 2026-01-15)
✅ just       Found: C:\Users\hiroto yamada\AppData\Local\Microsoft\WinGet\Packages\Casey.Just_Microsoft.Winget.Source_8wekyb3d8bbwe\just.EXE
   Version: just 1.46.0
✅ Quarto     Found: C:\Program Files\Quarto\bin\quarto.EXE
✨ All systems go! You are ready to develop.

📦 Setting up environment...
uv sync --all-extras
Resolved 128 packages in 3ms
Audited 124 packages in 19ms
npm install
✅ Environment setup complete!
```

---

## ⚠️ 重要な注意点

### 環境変数の更新について

新しくインストールしたツール（uv, just, quarto）は、**既に開いているターミナルでは自動的に認識されません**。

#### 解決方法

**方法 1: ターミナルを再起動する（推奨）**

現在のターミナルを閉じて、新しいターミナルを開いてください。

**方法 2: 環境変数を手動で更新する**

以下のコマンドを実行してから、他のコマンドを実行してください：

```powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
```

---

## 📂 インストール後のプロジェクト構造

```
Quantum-information/
├── .git/                    # Git リポジトリ
├── .github/                 # GitHub Actions 設定
├── .venv/                   # Python 仮想環境 (自動生成)
├── .vscode/                 # VSCode 設定
├── docs/                    # ドキュメント出力先
├── node_modules/            # npm パッケージ (自動生成)
├── quarto/                  # 学習ノートのソース
├── references/              # 参考資料
├── tests/                   # テストスクリプト
├── tools/                   # 開発支援スクリプト
├── AGENTS.md                # AI エージェント向けガイド
├── Justfile                 # タスクランナー設定
├── README.md                # プロジェクト説明
├── package.json             # npm 設定
├── pyproject.toml           # Python プロジェクト設定
└── uv.lock                  # Python 依存関係ロックファイル
```

---

## 🚀 利用可能なコマンド

セットアップ完了後、以下のコマンドが利用可能です：

| コマンド | 説明 |
|:---|:---|
| `just docs` | Quarto 文書のプレビューサーバー起動 (http://localhost:4312) |
| `just check` | 全体品質検証（フォーマット、Lint、型検査、テスト） |
| `just fix` | 自動修正（フォーマット、Lint エラー修正） |
| `just test` | ユニットテストの実行 |
| `just clean` | ビルド成果物やキャッシュの削除 |
| `just check-env` | 環境の整合性チェック |

---

## 📚 参考リンク

- [uv 公式ドキュメント](https://github.com/astral-sh/uv)
- [Just 公式ドキュメント](https://github.com/casey/just)
- [Quarto 公式サイト](https://quarto.org/)

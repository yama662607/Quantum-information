#!/usr/bin/env python3
"""
Mermaid Validator for Quarto Files

Quartoファイル（.qmd）からMermaidコードブロックを抽出し、
@mermaid-js/mermaid-cli (mmdc) を使用して構文を検証するツール

使用方法:
    python mermaid_validator.py <quarto_file.qmd>
    python mermaid_validator.py <directory_path>  # ディレクトリ内の全.qmdファイルを検証

要件:
    - Node.jsと@mermaid-js/mermaid-cliがインストールされ、PATHが通っていること
    - Python 3.6+

作成者: Daisuke Yamashiki
"""

import glob
import os
import re
import subprocess
import sys
from typing import List, Tuple


def extract_mermaid_blocks(content: str) -> List[str]:
    """
    Quartoファイルの内容からMermaidコードブロックを抽出する

    Args:
        content: ファイルのテキスト内容

    Returns:
        抽出されたMermaidコードブロックのリスト
    """
    # ````{mermaid}` から ```` ` までの内容を抽出
    # re.DOTALL は . が改行にもマッチするようにする
    # re.IGNORECASE は `mermaid` の大文字小文字を無視する
    pattern = re.compile(r"```\{\s*mermaid\s*\}\n(.*?)\n```", re.DOTALL | re.IGNORECASE)
    return pattern.findall(content)


def validate_mermaid_code(mermaid_code: str, block_index: int) -> Tuple[bool, str]:
    """
    単一のMermaidコードをmmdcで検証する

    Args:
        mermaid_code: 検証するMermaidコード
        block_index: ブロック番号（エラーメッセージ用）

    Returns:
        (検証結果, エラーメッセージ)
    """
    temp_mmd_file = f"temp_mermaid_block_{block_index}.mmd"
    temp_output_file = f"temp_mermaid_output_{block_index}.svg"

    try:
        # 1. 一時ファイルにMermaidコードを書き込む
        with open(temp_mmd_file, "w", encoding="utf-8") as temp_f:
            temp_f.write(mermaid_code.strip())

        # 2. mmdc コマンドを実行する
        subprocess.run(
            ["mmdc", "-i", temp_mmd_file, "-o", temp_output_file],
            capture_output=True,
            text=True,
            check=True,
            encoding="utf-8",
        )
        return True, ""

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() or e.stdout.strip()
        return False, error_msg

    except FileNotFoundError:
        return (
            False,
            "'mmdc' コマンドが見つかりません。@mermaid-js/mermaid-cli がインストールされ、PATHが通っているか確認してください。",
        )

    except Exception as e:
        return False, f"予期せぬエラー: {e}"

    finally:
        # 3. 一時ファイルを削除
        if os.path.exists(temp_mmd_file):
            os.remove(temp_mmd_file)
        if os.path.exists(temp_output_file):
            os.remove(temp_output_file)


def validate_quarto_file(qmd_filepath: str) -> bool:
    """
    Quartoファイルを検証する

    Args:
        qmd_filepath: 検証するQuartoファイルのパス

    Returns:
        全ブロックが検証成功した場合True
    """
    print(f"✅ ファイルを読み込み中: {qmd_filepath}")

    try:
        with open(qmd_filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ エラー: ファイルが見つかりません: {qmd_filepath}")
        return False
    except Exception as e:
        print(f"❌ エラー: ファイルの読み込みに失敗しました: {e}")
        return False

    mermaid_blocks = extract_mermaid_blocks(content)

    if not mermaid_blocks:
        print("💡 このファイルには Mermaid コードブロックが見つかりませんでした。")
        return True

    print(f"🔎 Mermaid コードブロックを {len(mermaid_blocks)} 件検出しました。")

    all_ok = True

    for i, mermaid_code in enumerate(mermaid_blocks, 1):
        print(f"\n--- ブロック {i} の検証開始 ---")

        # コードの最初の数行を表示（デバッグ用）
        lines = mermaid_code.strip().split("\n")
        preview = "\n".join(lines[:3]) + ("..." if len(lines) > 3 else "")
        print(f"コードプレビュー:\n{preview}")

        is_valid, error_msg = validate_mermaid_code(mermaid_code, i)

        if is_valid:
            print("✅ 構文エラーは見つかりませんでした。（レンダリング成功）")
        else:
            print("❌ 構文エラーが検出されました。")
            print("--- mmdc エラー出力 ---")
            print(error_msg)
            print("------------------------")
            all_ok = False

            # mmdcが見つからない場合はこれ以上続行しない
            if "'mmdc' コマンドが見つかりません" in error_msg:
                break

    return all_ok


def validate_directory(directory_path: str) -> bool:
    """
    ディレクトリ内のすべての.qmdファイルを検証する

    Args:
        directory_path: 検証するディレクトリのパス

    Returns:
        全ファイルが検証成功した場合True
    """
    print(f"📁 ディレクトリを検索中: {directory_path}")

    # ディレクトリ内の.qmdファイルを検索
    qmd_files = glob.glob(os.path.join(directory_path, "**/*.qmd"), recursive=True)

    if not qmd_files:
        print("💡 このディレクトリには .qmd ファイルが見つかりませんでした。")
        return True

    print(f"📄 {len(qmd_files)} 個の .qmd ファイルを検出しました。")

    all_ok = True
    for qmd_file in sorted(qmd_files):
        print(f"\n{'=' * 60}")
        file_ok = validate_quarto_file(qmd_file)
        all_ok = all_ok and file_ok

    return all_ok


def check_mmdc_installation() -> bool:
    """
    mmdcがインストールされているか確認する
    """
    try:
        result = subprocess.run(
            ["mmdc", "--version"], capture_output=True, text=True, check=True
        )
        print(f"🔧 mmdc バージョン: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ 'mmdc' コマンドが見つかりません。")
        print("💡 以下のコマンドでインストールしてください:")
        print("   npm install -g @mermaid-js/mermaid-cli")
        return False


def main():
    """メイン関数"""
    print("🎨 Mermaid Validator for Quarto Files")
    print("=" * 50)

    # mmdcのインストール確認
    if not check_mmdc_installation():
        sys.exit(1)

    if len(sys.argv) < 2:
        print("使用方法:")
        print("  python mermaid_validator.py <quarto_file.qmd>")
        print("  python mermaid_validator.py <directory_path>")
        print("\n例:")
        print("  python mermaid_validator.py docs/phase1/lesson01-autograd-intro.qmd")
        print("  python mermaid_validator.py docs/phase1/")
        sys.exit(1)

    target_path = sys.argv[1]

    if os.path.isfile(target_path):
        # 単一ファイルを検証
        all_ok = validate_quarto_file(target_path)
    elif os.path.isdir(target_path):
        # ディレクトリ内の全ファイルを検証
        all_ok = validate_directory(target_path)
    else:
        print(f"❌ エラー: パスが見つかりません: {target_path}")
        sys.exit(1)

    print(f"\n{'=' * 50}")
    if all_ok:
        print("🎉 すべての Mermaid コードブロックで構文エラーは見つかりませんでした。")
    else:
        print("⚠️ 1つ以上の Mermaid コードブロックで構文エラーが検出されました。")
        print("上記のエラーを確認してください。")

    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()

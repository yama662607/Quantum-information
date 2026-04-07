import argparse
import os
import sys
from extract_pdf import extract_pdf_text

# Note: extract_pdf_image needs to be updated or we use fitz directly
import fitz


def extract_pdf_images(pdf_path, start_page, end_page, out_dir="/tmp", dpi=300):
    saved_paths = []
    try:
        doc = fitz.open(pdf_path)
        for i in range(start_page - 1, min(len(doc), end_page)):
            page_num = i + 1
            out_path = os.path.join(out_dir, f"page_{page_num}.png")
            page = doc.load_page(i)
            pix = page.get_pixmap(dpi=dpi)
            pix.save(out_path)
            saved_paths.append(out_path)
        return saved_paths
    except Exception as e:
        print(f"Error extracting images: {e}", file=sys.stderr)
        return []


def main():
    parser = argparse.ArgumentParser(
        description="Process PDF pages for text, images, and LaTeX."
    )
    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("--start", type=int, default=1, help="Start page")
    parser.add_argument("--end", type=int, default=1, help="End page")
    parser.add_argument("--dpi", type=int, default=300, help="DPI for images")
    parser.add_argument("--out_dir", default="/tmp", help="Output directory for images")
    parser.add_argument("--no-latex", action="store_true", help="Skip LaTeX extraction")

    args = parser.parse_args()

    # 1. Extract Text
    print(f"\n--- Extracting Text (Pages {args.start}-{args.end}) ---")
    texts = extract_pdf_text(args.pdf_path, args.start, args.end, quiet=True)

    # 2. Extract Images
    print(f"\n--- Extracting Images (Pages {args.start}-{args.end}) ---")
    image_paths = extract_pdf_images(
        args.pdf_path, args.start, args.end, out_dir=args.out_dir, dpi=args.dpi
    )

    # 3. Extract LaTeX
    latex_results = []
    if not args.no_latex:
        print(f"\n--- Extracting LaTeX (Pages {args.start}-{args.end}) ---")
        try:
            from extract_pdf_latex import extract_latex_from_images

            latex_results = extract_latex_from_images(image_paths, quiet=True)
        except ImportError:
            print("Warning: extract_pdf_latex not found. Skipping LaTeX.")

    # Format Output
    for i in range(len(image_paths)):
        curr_page = args.start + i
        print(f"\n{'=' * 50}")
        print(f"PAGE {curr_page}")
        print(f"{'=' * 50}")

        print("\n[TEXT]")
        if i < len(texts):
            print(texts[i].strip())

        if not args.no_latex and i < len(latex_results):
            print("\n[MATH (LaTeX)]")
            print(latex_results[i].strip())

        print(f"\n[IMAGE PATH]\n{image_paths[i]}")
        print(
            "\n> [!IMPORTANT]\n> 必ず上記の画像ファイルを `read_file` 等で読み込み、数式やレイアウトを視覚的に精査してください。\n> OCR（Text/LaTeX）は添字や特殊記号を誤認する可能性があります。"
        )


if __name__ == "__main__":
    main()

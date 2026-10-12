import argparse
import os
import sys
import tempfile

# Add tools/utils and project root to path
tools_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(tools_dir, "utils"))
sys.path.append(os.path.abspath(os.path.join(tools_dir, "..")))

try:
    from pdf_processing import extract_pdf_text, get_default_img_dir
except ImportError:
    print("Error: Could not import pdf_processing from utils.", file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Extract text and LaTeX (OCR) from PDF pages."
    )
    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("--start", type=int, default=1, help="Start page")
    parser.add_argument("--end", type=int, default=1, help="End page")
    parser.add_argument(
        "--img_dir",
        default=None,
        help="Directory containing rendered images (default: auto-detected)",
    )
    parser.add_argument("--no-latex", action="store_true", help="Skip LaTeX extraction")
    parser.add_argument(
        "--save",
        default=None,
        help="Optional path to save extracted text and LaTeX OCR result to a file",
    )

    args = parser.parse_args()

    if not os.path.exists(args.pdf_path):
        print(f"Error: PDF file not found: {args.pdf_path}", file=sys.stderr)
        sys.exit(1)

    # Resolve image directory
    resolved_img_dir = args.img_dir
    if not resolved_img_dir:
        default_dir = get_default_img_dir(args.pdf_path)
        if os.path.exists(default_dir):
            resolved_img_dir = default_dir
        else:
            resolved_img_dir = tempfile.gettempdir()

    # 1. Extract Text
    print(
        f"📄 Extracting text from {os.path.basename(args.pdf_path)} (Pages {args.start}-{args.end})..."
    )
    texts = extract_pdf_text(args.pdf_path, args.start, args.end, quiet=True)

    # 2. Check for images and extract LaTeX
    latex_results = []
    image_paths = []

    for i in range(args.start, args.end + 1):
        img_path = os.path.join(resolved_img_dir, f"page_{i}.png")
        if os.path.exists(img_path):
            image_paths.append(img_path)
        else:
            # Fallback to tempfile.gettempdir()
            fallback_path = os.path.join(tempfile.gettempdir(), f"page_{i}.png")
            if os.path.exists(fallback_path):
                image_paths.append(fallback_path)
            else:
                print(
                    f"⚠️ Warning: Rendered image for page {i} not found at {img_path} (or {fallback_path})."
                )
                print("   Please run 'just render-pdf' first if you need LaTeX OCR.")

    if not args.no_latex and image_paths:
        print(f"⚛️ Extracting LaTeX via OCR from {len(image_paths)} images...")
        try:
            from latex_extraction import extract_latex_from_images

            latex_results = extract_latex_from_images(image_paths, quiet=True)
        except ImportError:
            print("Warning: latex_extraction not found in utils. Skipping LaTeX OCR.")

    output_lines = []
    for i in range(args.end - args.start + 1):
        curr_page = args.start + i
        header = f"\n{'=' * 50}\nPAGE {curr_page}\n{'=' * 50}"
        print(header)
        output_lines.append(header)

        text_block = "\n[TEXT]\n" + (
            texts[i].strip() if i < len(texts) else "(No text extracted)"
        )
        print(text_block)
        output_lines.append(text_block)

        if not args.no_latex:
            math_text = (
                latex_results[i].strip()
                if i < len(latex_results)
                else "(No OCR result)"
            )
            math_block = f"\n[MATH (LaTeX OCR)]\n{math_text}"
            print(math_block)
            output_lines.append(math_block)

        img_path = os.path.join(resolved_img_dir, f"page_{curr_page}.png")
        if not os.path.exists(img_path):
            img_path = os.path.join(tempfile.gettempdir(), f"page_{curr_page}.png")
        img_block = (
            f"\n[IMAGE PATH]\n{img_path if os.path.exists(img_path) else '(Not found)'}"
        )
        print(img_block)
        output_lines.append(img_block)

    if args.save:
        os.makedirs(os.path.dirname(os.path.abspath(args.save)), exist_ok=True)
        with open(args.save, "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines) + "\n")
        print(f"\n💾 Saved extracted content to: {args.save}")


if __name__ == "__main__":
    main()

import argparse
import os
import sys

# Add tools/utils and project root to path
tools_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(tools_dir, "utils"))
sys.path.append(os.path.abspath(os.path.join(tools_dir, "..")))

try:
    from pdf_processing import extract_pdf_images, get_default_img_dir
except ImportError:
    print("Error: Could not import pdf_processing from utils.", file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Render PDF pages as images (PNG).")
    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("--start", type=int, default=1, help="Start page (1-based)")
    parser.add_argument("--end", type=int, default=1, help="End page (1-based)")
    parser.add_argument("--dpi", type=int, default=300, help="DPI for images")
    parser.add_argument(
        "--out_dir",
        default=None,
        help="Output directory for images (default: /tmp/preskill_<pdf_name>)",
    )

    args = parser.parse_args()

    if not os.path.exists(args.pdf_path):
        print(f"Error: File not found: {args.pdf_path}", file=sys.stderr)
        sys.exit(1)

    target_dir = args.out_dir if args.out_dir else get_default_img_dir(args.pdf_path)
    print(f"🎨 Rendering PDF pages {args.start}-{args.end} to {target_dir}...")
    image_paths = extract_pdf_images(
        args.pdf_path, args.start, args.end, out_dir=args.out_dir, dpi=args.dpi
    )

    if not image_paths:
        print("❌ Failed to render images.")
        sys.exit(1)

    print("\n✅ Rendering complete. Saved images:")
    for path in image_paths:
        print(f" - {path}")


if __name__ == "__main__":
    main()

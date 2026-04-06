import argparse
import PyPDF2
import sys


def extract_pdf_text(pdf_path, start_page=None, end_page=None, quiet=False):
    """
    Extracts text from a PDF file within a specified page range.
    Returns a list of strings, where each string is the text of one page.
    """
    results = []
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            total_pages = len(reader.pages)

            start_idx = 0
            if start_page:
                start_idx = max(0, start_page - 1)

            end_idx = total_pages
            if end_page:
                end_idx = min(total_pages, end_page)

            if start_idx >= total_pages:
                if not quiet:
                    print(
                        f"Error: Start page {start_page} is out of range",
                        file=sys.stderr,
                    )
                return []

            for i in range(start_idx, end_idx):
                text = reader.pages[i].extract_text()
                results.append(text)
                if not quiet:
                    print(f"--- Page {i + 1} ---")
                    print(text)
                    print("\n")
        return results

    except Exception as e:
        if not quiet:
            print(f"An error occurred: {e}", file=sys.stderr)
        return []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from a PDF file.")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--start", type=int, help="Start page number (1-based)")
    parser.add_argument("--end", type=int, help="End page number (1-based)")

    args = parser.parse_args()
    extract_pdf_text(args.pdf_path, args.start, args.end)

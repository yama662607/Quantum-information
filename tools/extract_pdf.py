import argparse
import PyPDF2
import sys


def extract_pdf_text(pdf_path, start_page=None, end_page=None):
    """
    Extracts text from a PDF file within a specified page range.

    Args:
        pdf_path (str): Path to the PDF file.
        start_page (int, optional): Starting page number (1-based).
        end_page (int, optional): Ending page number (1-based).
    """
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            total_pages = len(reader.pages)

            # Adjust 1-based indexing to 0-based
            start_idx = 0
            if start_page:
                start_idx = max(0, start_page - 1)

            end_idx = total_pages
            if end_page:
                end_idx = min(total_pages, end_page)

            if start_idx >= total_pages:
                print(
                    f"Error: Start page {start_page} is out of range (Total pages: {total_pages})",
                    file=sys.stderr,
                )
                return

            print(
                f"--- Extracting from {pdf_path} (Pages {start_idx + 1}-{end_idx}) ---\n"
            )

            for i in range(start_idx, end_idx):
                print(f"--- Page {i + 1} ---")
                print(reader.pages[i].extract_text())
                print("\n")

    except FileNotFoundError:
        print(f"Error: File not found at {pdf_path}", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from a PDF file.")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--start", type=int, help="Start page number (1-based)")
    parser.add_argument("--end", type=int, help="End page number (1-based)")

    args = parser.parse_args()
    extract_pdf_text(args.pdf_path, args.start, args.end)

import PyPDF2

def extract_toc(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        # TOC is usually in the first few pages of FrontMatter
        # Physical pages 3-6 were mentioned before as TOC
        for i in range(2, 6):
            if i >= len(reader.pages): break
            print(f"--- Page {i+1} ---")
            print(reader.pages[i].extract_text())

if __name__ == "__main__":
    extract_toc("/Users/daisukeyamashiki/Code/Learning/Quantum-information/docs/divided/Chapter0_FrontMatter.pdf")

import pdfplumber

# Function to parse PDF resumes (pdfplumber is lightweight and effective as compared to langchain pdf parser)
def pdf_parser(file_obj: bytes) -> str:
    """
    Extract text from a single PDF resume file.
    """

    with pdfplumber.open(file_obj) as pdf:
        content = ""
        for page in pdf.pages:
            content += page.extract_text() or ""
        return content.strip()

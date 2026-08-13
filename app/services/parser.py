import fitz
from docx import Document


def extract_pdf_text(file_path: str) -> str:
    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


def extract_docx_text(file_path: str) -> str:
    document = Document(file_path)

    paragraphs = [
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    return "\n".join(paragraphs)


def extract_text(file_path: str) -> str:

    if file_path.lower().endswith(".pdf"):
        return extract_pdf_text(file_path)

    if file_path.lower().endswith(".docx"):
        return extract_docx_text(file_path)

    raise ValueError("Unsupported file format")

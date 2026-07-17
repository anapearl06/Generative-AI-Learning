import fitz
from docx import Document
from pydantic import BaseModel
from typing import List

def read_pdf(filepath):
    """
    Reads a PDF file and returns all text as a string.
    """

    text = ""

    document = fitz.open(filepath)

    for page in document:
        text += page.get_text()

    return text


def read_docx(filepath):
    """
    Reads a DOCX file and returns all text as a string.
    """

    document = Document(filepath)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def read_resume(filepath):
    """
    Decides which reader to use based on file extension.
    """

    if filepath.endswith(".pdf"):
        return read_pdf(filepath)

    elif filepath.endswith(".docx"):
        return read_docx(filepath)

    else:
        return None

# Testing PDF

pdf_file = "resumes/resume1.pdf"

pdf_text = read_resume(pdf_file)

print("=" * 70)
print("PDF OUTPUT")
print("=" * 70)

print(pdf_text)

# Testing DOCX

docx_file = "resumes/resume3.docx"

docx_text = read_resume(docx_file)

print("=" * 70)
print("DOCX OUTPUT")
print("=" * 70)

print(docx_text)

class Experience(BaseModel):

    company: str

    role: str

    duration: str

    description: str

    skills_used: List[str]

class Resume(BaseModel):

    name: str

    email: str

    phone: str

    total_experience_years: float

    skills: List[str]

    experience: List[Experience]

    projects: List[str]

    certifications: List[str]
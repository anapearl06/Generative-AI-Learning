import fitz
from docx import Document
from pydantic import BaseModel
from typing import List
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Pydantic Models

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


# Resume Readers

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
    Chooses the correct reader based on file extension.
    """

    if filepath.endswith(".pdf"):
        return read_pdf(filepath)

    elif filepath.endswith(".docx"):
        return read_docx(filepath)

    return None

def parse_resume(resume_text):
    """
    Sends resume text to the LLM and returns a structured Resume object.
    """

    completion = client.chat.completions.parse(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
                    You are an expert HR recruiter and resume parser.

                    Extract all resume information accurately.

                    Return the response according to the Resume schema.
                    """
            },
            {
                "role": "user",
                "content": resume_text
            }
        ],
        response_format=Resume,
    )

    parsed_resume = completion.choices[0].message.parsed

    return parsed_resume
# Testing

def main():

    # PDF

    pdf_file = "resumes/resume1.pdf"

    pdf_text = read_resume(pdf_file)

    print("=" * 70)
    print("PARSED PDF RESUME")
    print("=" * 70)

    parsed_resume = parse_resume(pdf_text)

    print(parsed_resume)

    print()

    # DOCX

    docx_file = "resumes/resume3.docx"

    docx_text = read_resume(docx_file)

    print("=" * 70)
    print("PARSED DOCX RESUME")
    print("=" * 70)

    parsed_resume = parse_resume(docx_text)

    print(parsed_resume)


if __name__ == "__main__":
    main()

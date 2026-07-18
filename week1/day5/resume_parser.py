import json
import os
from typing import List

import fitz
from docx import Document
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel


# Environment # 

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Pydantic Models #

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


# Resume Readers #

def read_pdf(filepath: str) -> str:
    """
    Read a PDF file and return its text.
    """

    text = ""

    with fitz.open(filepath) as document:
        for page in document:
            text += page.get_text()

    return text


def read_docx(filepath: str) -> str:
    """
    Read a DOCX file and return its text.
    """

    document = Document(filepath)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def read_resume(filepath: str) -> str:
    """
    Read a resume based on its file extension.
    """

    if filepath.endswith(".pdf"):
        return read_pdf(filepath)

    if filepath.endswith(".docx"):
        return read_docx(filepath)

    raise ValueError(
        "Unsupported file format. Only PDF and DOCX files are supported."
    )


# Resume Parser # 

def parse_resume(resume_text: str) -> Resume:
    """
    Parse resume text into a structured Resume object using the LLM.
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": """
You are an expert HR recruiter and resume parser.

Extract the resume into the following JSON schema.

Return ONLY valid JSON.

{
    "name": "",
    "email": "",
    "phone": "",
    "total_experience_years": 0,
    "skills": [],
    "experience": [
        {
            "company": "",
            "role": "",
            "duration": "",
            "description": "",
            "skills_used": []
        }
    ],
    "projects": [],
    "certifications": []
}
"""
            },
            {
                "role": "user",
                "content": resume_text
            }
        ]
    )

    response = completion.choices[0].message.content.strip()

    if response.startswith("```json"):
        response = response.replace("```json", "", 1)

    if response.endswith("```"):
        response = response[:-3]

    response = response.strip()

    try:
        data = json.loads(response)
        return Resume(**data)

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON returned by the LLM.\n\n{response}") from e

    except Exception as e:
        raise ValueError(f"Failed to parse resume.\n\n{e}") from e
    

# Testing # 

def main():
    resume_files = [
        ("PDF", "resumes/resume1.pdf"),
        ("DOCX", "resumes/resume3.docx"),
    ]

    for file_type, filepath in resume_files:
        print("=" * 70)
        print(f"PARSED {file_type} RESUME")
        print("=" * 70)

        try:
            resume_text = read_resume(filepath)
            parsed_resume = parse_resume(resume_text)

            print(type(parsed_resume))
            print()
            print(parsed_resume.model_dump_json(indent=4))

        except Exception as e:
            print(f"Error: {e}")

        print()


if __name__ == "__main__":
    main()
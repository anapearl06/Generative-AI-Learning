# 🚀 Generative AI Learning

<div align="center">

### 🤖 Learning • Building • Experimenting with Modern AI

A hands-on repository documenting my journey into **Generative AI**, where every folder represents a new concept and every commit captures a meaningful learning milestone.

<img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/Groq-API-black?style=for-the-badge" />
<img src="https://img.shields.io/badge/Llama-3.3%2070B-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/Pydantic-JSON%20Validation-E92063?style=for-the-badge" />
<img src="https://img.shields.io/badge/Package%20Manager-uv-6E56CF?style=for-the-badge" />

</div>

---

# 📖 About

This repository documents my journey of learning **Generative AI** from fundamentals to building production-ready AI applications.

Instead of only following tutorials, I build practical projects to understand how modern AI systems work behind the scenes.

My goal is to understand not only **how to use AI**, but also **how to build AI applications from scratch using industry-standard tools and workflows.**

---

# 🧠 Topics Explored

- 🤖 Large Language Models (LLMs)
- 💬 Prompt Engineering
- 📝 System & User Prompts
- 🌡️ Temperature Control
- 📊 Token Usage Analysis
- 📦 Structured JSON Outputs
- ✅ Pydantic Validation
- ⚡ Groq API Integration
- 📄 PDF & DOCX Parsing
- 🐍 Python for AI Development

---

# 📚 Learning Journey

## 📅 Week 1 — LLM Fundamentals & API Mastery

| Day | Concept | Status |
|------|----------|--------|
| Day 1 | First Groq API Request | ✅ |
| Day 2 | System Prompts & Temperature | ✅ |
| Day 3 | Token Usage Analysis | ✅ |
| Day 4 | Structured JSON with Pydantic | ✅ |
| Day 5 | AI Resume Parser (PDF & DOCX) | ✅ |

---

# 📂 Repository Structure

```text
Generative-AI-Learning
│
├── week1
│   ├── day1
│   ├── day2
│   ├── day3
│   ├── day4
│   └── day5
│       ├── resume_parser.py
│       ├── resumes/
│       ├── pyproject.toml
│       ├── uv.lock
│       └── .env.example
│
└── README.md
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| AI Model | Llama 3.3 70B |
| API | Groq API |
| Validation | Pydantic |
| Environment | python-dotenv |
| Package Manager | uv |
| Document Parsing | PyMuPDF, python-docx |
| Data Format | JSON |

---

# 🚀 Projects Completed

## ✅ AI Resume Parser

Built an AI-powered resume parser capable of:

- Reading PDF resumes
- Reading DOCX resumes
- Extracting resume text
- Sending resumes to a Large Language Model
- Returning structured JSON
- Validating output using Pydantic
- Supporting both PDF and DOCX formats

---

# ⚙️ Getting Started

Follow these steps to run the project on your local machine.

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/anapearl06/Generative-AI-Learning.git
```

---

## 2️⃣ Navigate to the Project Folder

```bash
cd Generative-AI-Learning/week1/day5
```

---

## 3️⃣ Install Dependencies

This project uses **uv** for dependency management.

```bash
uv sync
```

This command will:

- Create a virtual environment (if it doesn't already exist)
- Install all required packages
- Match package versions defined in `uv.lock`

---

## 4️⃣ Configure Environment Variables

Create a `.env` file inside the project directory.

Example:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your own Groq API key.

> Never upload your `.env` file or API keys to GitHub.

---

## 5️⃣ Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## 6️⃣ Run the Project

```bash
python resume_parser.py
```

The application will:

- Read PDF and DOCX resumes
- Extract text from documents
- Send the extracted text to the Groq LLM
- Generate structured JSON
- Validate the output using Pydantic
- Display the parsed resume in the terminal

---

## 📂 Testing Different Resumes

To test another resume:

1. Place your PDF or DOCX file inside the `resumes/` folder.

Example:

```text
resumes/
├── resume1.pdf
├── resume2.pdf
├── resume3.docx
├── my_resume.pdf
└── my_resume.docx
```

2. Open `resume_parser.py`.

3. Update the `resume_files` list.

Example:

```python
resume_files = [
    ("PDF", "resumes/my_resume.pdf"),
]
```

or

```python
resume_files = [
    ("DOCX", "resumes/my_resume.docx"),
]
```

4. Save the file and run:

```bash
python resume_parser.py
```

---

## 🔄 Future Improvements

The current implementation is designed for learning and development.

Future versions may include:

- Automatic folder scanning
- Batch resume parsing
- Resume upload through a web interface
- Database integration
- Resume vs Job Description matching
- AI-powered resume scoring
- Vector database integration (Qdrant)
- RAG-powered resume search

---

# 🚀 Current Highlights

✨ Built applications using the Groq API

✨ Learned prompt engineering fundamentals

✨ Controlled LLM behavior using System Prompts

✨ Measured token usage and API responses

✨ Generated structured JSON outputs

✨ Validated AI responses using Pydantic

✨ Built an AI-powered Resume Parser

✨ Practiced clean project architecture and Git workflows

---

# 🗺️ 8-Week Learning Roadmap

| Week | Focus |
|-------|-------|
| ✅ Week 1 | LLM Fundamentals & API Mastery |
| ⏳ Week 2 | Prompt Engineering & Streaming |
| ⏳ Week 3 | RAG Foundations |
| ⏳ Week 4 | Advanced RAG & Evaluation |
| ⏳ Week 5 | AI Agents & Tool Calling |
| ⏳ Week 6 | LangGraph, MCP & Multi-Agent Systems |
| ⏳ Week 7 | Guardrails, Observability & Security |
| ⏳ Week 8 | Deployment, Fine-Tuning & Capstone Project |

---

# 🎯 Upcoming Projects

- 💼 Resume vs Job Description Matcher
- 📊 Resume Scoring System
- 📄 Cover Letter Generator
- 🔍 Retrieval-Augmented Generation (RAG)
- 🗄️ Vector Databases (Qdrant)
- 🤖 AI Agents
- 🌐 LangChain
- 🦜 LangGraph
- 🚀 Production-Ready AI Applications

---

# 💡 Repository Philosophy

I believe the best way to learn AI is by building.

Every folder in this repository represents concepts that I've studied, implemented, tested, and documented through hands-on projects.

The goal is to gradually evolve these learning exercises into production-ready AI systems while developing a strong understanding of modern AI engineering.

---

<div align="center">

### 🌱 Learning one project at a time.

⭐ If you find this repository helpful, feel free to explore the code and follow my learning journey.

</div>
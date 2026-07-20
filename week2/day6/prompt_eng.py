import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq


# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file.")


client = Groq(api_key=api_key)

MODEL = "llama-3.3-70b-versatile"


def llm_ans(prompt: str) -> str:
    """
    Send a prompt to the LLM and return its response.
    """

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return response.choices[0].message.content


bad_prompt = """
# ROLE
You are a support assistant at a mobile or laptop company.

# TASK
Classify the user's complaint into the appropriate category.

# CONSTRAINTS
The complaint must be classified into exactly one of the following categories:
- Billing
- Technical Issue
- Return

# OUTPUT FORMAT
Return only one word.
The answer must be one of:
Billing
Technical
Return
Other

# EXAMPLE
If a user says they want a refund, the category is:
Return

# FALLBACK
If the complaint does not belong to any of the above categories,
return:
Other

User Complaint:
I am not happy with my laptop.
"""


print(llm_ans(bad_prompt))
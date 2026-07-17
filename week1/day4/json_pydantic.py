import os
import json

from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Error")

client = Groq(api_key=my_api_key)

class Ticket(BaseModel):
    name: str
    email: str
    issue: str


schema = Ticket.model_json_schema()

system_prompt = f"""
Extract the personal information from the ticket according to this schema.
Return ONLY valid JSON.

Schema:
{schema}
"""

text = """
My name is Ananya Shukla.
I am doing BTech.
My address is Rajnagar Extn.
My email is shuklaananya762@gmail.com.
"""

prompt = f"""
This is a customer ticket.

{text}
"""

message_system = {
    "role": "system",
    "content": system_prompt,
}

message = {
    "role": "user",
    "content": prompt,
}

messages = [message_system, message]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    response_format={"type": "json_object"},
)

answer = response.choices[0].message.content
print(answer)

data = json.loads(answer)

ticket = Ticket(**data)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
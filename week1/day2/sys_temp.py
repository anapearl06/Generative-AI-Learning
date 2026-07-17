import os

from pathlib import Path
from dotenv import load_dotenv

from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError ("api error")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"

role="user"

prompt=" My fiance is like Christian Grey "
#prompt="Blinkit"

message_system={
    "role": "system",
    "content": "I am like Anasthesia Steele"
}
message = {
    "role": role,
    "content": prompt,
}

messages=[message_system, message]

response = client.chat.completions.create(model=model, messages = messages, temperature=1)
#print(response)

print("###############################")

answer=response.choices[0].message.content
print(answer)
# Streaming


from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

my_api_key = os.getenv('GROQ_API_KEY')

if not my_api_key:
    raise ValueError("Invalid API key")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

prompt = '''
Explain about the Northern Lights.
'''

message = {
    "role" : "user",
    "content" : prompt
}

messages = [message]

# By default stream = False
stream = client.chat.completions.create(model=model, messages=messages, stream=True)


# with streaming
for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
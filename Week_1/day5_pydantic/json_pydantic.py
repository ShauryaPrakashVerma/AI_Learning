import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()

class Ticket(BaseModel):
    name: str
    email : str
    issue : str

schema = Ticket.model_json_schema()

response_format={
    "type" : "json_object"
}

system_prompt = f'''
Extract the personal information, issue from the ticket strictly based on the schema in json format.
{schema}
'''

message_system = {
    "role": "system", 
    "content": system_prompt 
}


my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not avaialaible")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"


role = "user"
text = "My name is Shaurya. I have purchased an IPhone 17 ans the issue is that it has stopped working. My address is lucknow and my email is xyz@gmail.com. My contact number is +91 9999999999"

prompt = f'''
This is a customer ticket. Please extract the personal information from this.
{text}
'''

message={
    "role": role,
    "content":prompt
}


messages =[message_system, message]
response = client.chat.completions.create(model = model, messages = messages, response_format=response_format)

answer = response.choices[0].message.content

print(answer)


# how to read this
import json
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
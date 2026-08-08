#---------------- Prompt engineering-----------------------

# Bad Prompt --> 6 Steps --> Good Prompt

# 6 Steps:
# 1 --> Role
# 2 --> Task
# 3 --> Constraints
# 4 --> Output Format
# 5 --> Zero/One Shot Prompting
# 6 --> Fallback


import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

def llm_answer(prompt):
    message = {
        "role": "user",
        "content": prompt
    }
    
    messages = [message]
    response = client.chat.completions.create(model=model, messages = messages)
    
    ans = response.choices[0].message.content
    return ans


# bad_prompt = '''
# This is a user complaint:
# My gf has left me
# Classify this.
# '''

prompt = '''
# ROLE:
You are a customer support assistant at a mobile/laptop company.

# TASK:
You have to classify the issue in a category.

# CONSTRAINTS:
You have to classify the issue in one of the three categories namely billing, technical, return.

# OUTPUT FORMAT:
Your answer should be in one word only, the one word should be one of the categories given in the categories given above.

# Zero/One Shot Prompting
For example the issue that laptop screen is not working should be categorized as technical probem

# Fallback
If the issue is unrelated to any of the categories mentioned in categories, then the answer should be other.

This is a user complaint:
I have not recieved the cashback on purchase of the laptop TUF Laptop
'''

print(llm_answer(prompt))

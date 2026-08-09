import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import time

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Invalid API key")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

JD = '''
We are hiring a Backend Python Developer.

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- AWS
- REST APIs
- 2+ years of Experience
'''

RESUME = '''
Name: Rahul Sharma

Experience: 3+ years as a Software Developer.

Skills:
Python, FastAPI, MySQL, Docker, REST APIs, Git

Projects:
Built a food delivery backend using FastAPI and MySQL

Deploed applications using Docker.
'''


def ask_llm(sytsem_prompt, user_prompt):
    system_message = {
        "role": "user",
        "content": sytsem_prompt
    }
    user_message = {
        "role": "user",
        "content": user_prompt
    }
    
    messages = [system_message, user_message]
    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer


def step1_resume_extract():
    # extract skills from resume
    system_prompt = '''
    You are a professional HR assistant. Extract the skills from the candidate's resume provided.
    Only return the skills no other information. Do not invent any skills by yourself.
    '''
    
    user_prompt = '''
    Extract the skills from this resume.
    {RESUME}
    '''
    
    return ask_llm(system_prompt, user_prompt)
    
    
def step2_jd_extract():
    # extract skills from resume
    system_prompt = '''
    You are a professional HR assistant. Extract the skills from the job description provided.
    Only return the skills no other information. Do not invent any skills by yourself.
    '''
    
    user_prompt = '''
    Extract the skills from this JD.
    {JD}
    '''
    
    return ask_llm(system_prompt, user_prompt)


def step3_match(candidate, jd):
    system_prompt = '''
    You are a professional HR assistant, compare the skills of the candidate and the skills required in the JD and produce a final score betweeen 1 and 100, also produce a short verdict whether the candidate is a good fit or not.
    '''
    
    user_prompt = '''
    Compare and match the skills
    JD: {JD}
    
    Candidate: {candidate}
    '''
    
    return ask_llm(system_prompt, user_prompt)


candidate = step1_resume_extract()
time.sleep(2)
jd = step2_jd_extract()
time.sleep(2)
score = step3_match(candidate, jd)
print(score)
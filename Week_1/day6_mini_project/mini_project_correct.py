import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
import pypdf

load_dotenv()

# ================================================================================================
class Report(BaseModel):
    candidate_name: str
    skill_percentage: str
    experience : str
    skills_present: list
    skills_absent: list
    
schema = Report.model_json_schema()

response_format = {
    "type" : "json_object"
}

# schema = Ticket.model_json_schema()

# response_format={
#     "type" : "json_object"
# }

# ================================================================================================

job_description = ""

with open("JD.pdf", "rb") as jd:
    reader = pypdf.PdfReader(jd)
    for page in reader.pages:
        job_description += page.extract_text() + "\n"
        

system_prompt = f'''
Evaluate the Resumes of candidates and compare it with the given job description and return their skill/compatability percentage to the given job description. Return the result in the json format strictly according to the schema provided.
{job_description}
{schema}
'''


# These are the Examples resumes i generated through ChatGPT

# Candidate 1 --- Aarav Sharma
resume1 = ""
with open("1_Aarav_Sharma.pdf", "rb") as jd:
    reader = pypdf.PdfReader(jd)
    for page in reader.pages:
        resume1 += page.extract_text() + "\n"

# Candidate 2 --- Priya Nair
resume2 = ""
with open("2_Priya_Nair.pdf", "rb") as jd:
    reader = pypdf.PdfReader(jd)
    for page in reader.pages:
        resume2 += page.extract_text() + "\n"

# Candidate 3 --- Ananya Mehta
resume3 = ""
with open("3_Ananya_Mehta.pdf", "rb") as jd:
    reader = pypdf.PdfReader(jd)
    for page in reader.pages:
        resume3 += page.extract_text() + "\n"

# Candidate 4 --- Karan Malhotra
resume4 = ""
with open("4_Karan_Malhotra.pdf", "rb") as jd:
    reader = pypdf.PdfReader(jd)
    for page in reader.pages:
        resume4 += page.extract_text() + "\n"

# Candidate 5 --- Rohan Verma
resume5 = ""
with open("5_Rohan_Verma.pdf", "rb") as jd:
    reader = pypdf.PdfReader(jd)
    for page in reader.pages:
        resume5 += page.extract_text() + "\n"


resumes = [resume1, resume2, resume3, resume4, resume5]




# system message
message_system = {
    "role": "system", 
    "content": system_prompt 
}

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not avaialaible")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"


# ================================================================================================
role = "user"
# text = "My name is Shaurya. I have purchased an IPhone 17 ans the issue is that it has stopped working. My address is lucknow and my email is xyz@gmail.com. My contact number is +91 9999999999"


for resume in resumes:
    
    prompt = f'''
    This is a resume of a candidate. Extract useful information from it.
    {resume}
    '''

    message={
        "role": role,
        "content":prompt
    }

    messages =[message_system, message]
    response = client.chat.completions.create(model = model, messages = messages, response_format=response_format)

    answer = response.choices[0].message.content

    print(answer)



    
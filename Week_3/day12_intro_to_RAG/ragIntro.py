from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Invalid API key")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

# STEP 1 : Creation of a Knowledge base
knowledge_base = {
    "age" : "Shaurya's Age is 22",
    "Language" : "his preferred languages are python, javascript"
}


# STEP 2 : Retrieval
def retrieve_info(question):
    question = question.lower()
    if "age" in question:
        return knowledge_base['age']
    elif "language" in question:
        return knowledge_base['Language']
    else:
        return None


def ask_llm(question):
    
    context = retrieve_info(question)
    
    system_prompt = f'''
    Answer in one line only. Answer the question strictly based on this context. do not invent information. Do not hallucinate.
    Context : {context}
    '''
    
    system_message = {
        "role" : "system", 
        "content" : system_prompt
    }
    
    message = {
        "role" : "user",
        "content" : question
    }
    
    messages = [system_message, message]
    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer
    
    
# question = "What is Age?" -----> This is a problematic question for this rigid ancient RAG
# question = "How old is Shaurya"  --------->  also a problematic question
question = "What is Age?"




print(ask_llm(question= question))
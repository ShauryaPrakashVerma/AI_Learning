import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not avaialaible")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"
prompt1 = "Hi"
prompt2 = "Explain about a digital twin but under 100 words"
prompt3 = "Write essay on smart TRaffic systems in 1000 words."

prompts = [prompt1, prompt2, prompt3]


for prompt in prompts:

    message={
        "role": role,
        "content":prompt
    }

    messages =[message]
    # response = client.chat.completions.create(model = model, messages = messages)
    
    # limiting the number of tokens
    response = client.chat.completions.create(model = model, messages = messages,  max_tokens=50)
    
    usage = response.usage
    # print(f"Prompt:{prompt} \nprompt tokens: {usage.prompt_tokens} \ncompletion_tokens: {usage.completion_tokens} \ntotal_tokens: {usage.total_tokens}\n")
    
    
    print(f"Prompt:{prompt} \nprompt tokens: {usage.prompt_tokens} \ncompletion_tokens: {usage.completion_tokens} \ntotal_tokens: {usage.total_tokens} \nfinish reason: {response.choices[0].finish_reason}\n")
    
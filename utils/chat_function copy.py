import os
import openai

from dotenv import load_dotenv
from code_snippets import (calculating_pi,
                           optimised_factorial,
                           fibonacci,
                           matrix_multiplication, 
                           web_scraping)

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

calc = open('calc.py').read()
db = open('flask_db.py').read()

model = 'gpt-3.5-turbo'

def chat(unoptimised_code):
  chat_response = openai.ChatCompletion.create(
    model=model,
    temperature=0.1,
    messages=[
    {
      "role": "system",
      "content": "Your task is to optimize the provided code. Improve its speed. Improve its algorithmic efficiency. Some optimisations may include connection pooling, inbuilt functions, parallel processing. The response should strictly follow this format: Start with the string [CODE_START], then the optimized code, followed by [CODE_END]. After that, start with [EXPLANATION_START], provide one line explanation of the optimisation and provide the complexities of the original code and complexities of the optimized code, and end with [EXPLANATION_END]."
    },
    {
      "role": "user",
      "content": f"Optimize this code: {unoptimised_code}"
    }
  ]
  )
  prompt_tokens = chat_response["usage"]["prompt_tokens"]
  completion_tokens = chat_response["usage"]["completion_tokens"]
  total_tokens = chat_response["usage"]["total_tokens"]
  chat_output = chat_response['choices'][0]['message']['content']
  print(chat_output)

# chat(calculating_pi)
# chat(optimised_factorial)
# chat(fibonacci)
# chat(matrix_multiplication)
# chat(web_scraping)
chat(db)
chat(calc)

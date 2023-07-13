import os
import openai

from dotenv import load_dotenv
from code_snippets import (
  create_large_array,
  factorial,
  fibonacci,
  list_flattening,
  list_sorting,
  list_duplicate_removal,
  string_reversal,
  matrix_multiplication,
  check_prime,
  calculating_pi,
  optimised_fibonacci
)

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

# Updated Chat


user_prompt = '''
Context: 
The goal is to reduce code carbon emissions.

Instruction: 
Minimise time and space complexity. 
Simplify the code.
If the code is in a function, let it remain in a function. 
Don't change variable names.
If necessary, use parallel processing, or a third party library.
If no simplification can be done, state that.

Output expectation:
Your output should be the optimised code.
Also provide a one line explanation.
If needed, include space and time complexity in the explanation.
Always comment the explanation (#).

Input:
Here is the unoptimised code: {}
'''

def chat(user_prompt, model, unoptimised_code):
  chat_response = openai.ChatCompletion.create(
    model=model,
    temperature=0,
    messages=[
      {
          "role": "user",
          "content": user_prompt.format(unoptimised_code)
      }
    ]
  )
  print(f'Prompt tokens: {chat_response["usage"]["prompt_tokens"]}')
  print(f'Completion tokens: {chat_response["usage"]["completion_tokens"]}')
  print(f'Total tokens: {chat_response["usage"]["total_tokens"]}')

  print('Chat response: \n')
  print(chat_response['choices'][0]['message']['content'], end='\n\n')

chat(user_prompt, 'gpt-3.5-turbo', calculating_pi)
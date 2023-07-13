import os
import openai
import pandas as pd

from dotenv import load_dotenv
from code_snippets import calculating_pi

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

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
Your output should be:
- optimised code
- a line of 5 dashes
- one line explanation for the optimisation
If needed, include space and time complexity in the explanation.

Input:
Here is the unoptimised code: {}
'''

# user_prompt = '''
# Context: 
# The goal is to reduce code carbon emissions.

# Instruction: 
# Minimise time and space complexity. 
# Simplify the code.
# If the code is in a function, let it remain in a function. 
# Don't change variable names.
# If necessary, use parallel processing, or a third party library.
# If no simplification can be done, state that.

# Output expectation:
# Your output should be:
# - optimised code
# - one line explanation for the optimisation
# If needed, include space and time complexity in the explanation.
# Give the entire output in json.

# Input:
# Here is the unoptimised code: {}
# '''

model = 'gpt-3.5-turbo'

def chat(unoptimised_code):
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
  prompt_tokens = chat_response["usage"]["prompt_tokens"]
  completion_tokens = chat_response["usage"]["completion_tokens"]
  total_tokens = chat_response["usage"]["total_tokens"]
  chat_output = chat_response['choices'][0]['message']['content']
  output_code, explanation = chat_output.split('-----', maxsplit=1)
  return output_code, explanation, total_tokens

# chat(calculating_pi)
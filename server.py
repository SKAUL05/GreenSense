import os
import openai
import tiktoken

openai.api_key = os.environ['OPENAI_API_KEY']

# Updated Chat


user_prompt = '''The goal is to reduce code carbon emissions. 
Minimise time and space complexity. Simplify the code.
Your output should be the optimised code and then a one liner explanation. 
Always comment out the explanation.
If code is in a function, let it remain in a function. 
Don't change variable names.
Here is the unoptimised code: {}'''

unoptimised_code_arr = '''
def create_large_list():
    large_list = []
    for i in range(1000000):
        large_list.append(i)
    return large_list
'''

unoptimised_code = '''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
'''

fibonacci = '''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
'''

def system_role_chat(user_prompt, model, unoptimised_code):
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

system_role_chat(user_prompt, 'gpt-3.5-turbo', fibonacci)
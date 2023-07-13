import os
import openai
import tiktoken

openai.api_key = os.environ['OPENAI_API_KEY']

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

unoptimised_code = '''
result = ''
for i in range(1000):
    result += str(i)
'''
prompt = "optimise this code for memory and time. Only give me executable code output and no other text. Optimise it for giving results: {}"

# Count tokens in prompt:
print('Number of tokens for prompt: {}'.format(
    num_tokens_from_string(prompt.format(unoptimised_code), "cl100k_base")
    )
)

# Chat
def chat(prompt, unoptimised_code):
  chat_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "user",
          "content": prompt.format(unoptimised_code)
      }
    ]
  )
  print('Chat response: \n')
  print(chat_response, end='\n\n')

# Completions
def complete(prompt, unoptimised_code):
  completed_code = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt.format(unoptimised_code),
    temperature=0.2
  )
  print(completed_code, end='\n\n')

# Edit
def edit(prompt, unoptimised_code):
  edited_code = openai.Edit.create(
    model="text-davinci-edit-001",
    input=unoptimised_code,
    instruction=prompt.format("")
  )
  print(edited_code, end='\n\n')

system_prompt = '''
You are legendary coder. You know how important every byte used and every millisecond spent in compute. 
As a part of the green coding initiative, you are optimising code to reduce carbon emissions. 
You are required to reduce memory usage. 
You are supposed to reduce time consumed by using better algorithms. 
You are required to use parallelism and concurrency where possible. 
You should use better inbuilt functions if they provide better memory and time consumption. 
Perform the optimisation if and when possible. Your input will be code snippets. 
You should output the optimised version only.  Return only code snippets and nothing else.'''

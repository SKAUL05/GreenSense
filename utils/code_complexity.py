import os
import openai
from radon.visitors import ComplexityVisitor
from code_snippets import calculating_pi, web_scraping, data_analysis, optimised_fibonacci, optimised_factorial, fibonacci, factorial
from dotenv import load_dotenv
import sys
import json
import re
import math

load_dotenv()
N = 10

# COMPLEXITY_TO_NUMBER= {
  

# }


openai.api_key = os.getenv("OPENAI_API_KEY")
def call_Chat_gpt_for_time_and_space_complexity(content):
  chat_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You will be provided with Python code, give only Time complexity and Space Complexity all functions in json fomat with no explation"
      },
      {
        "role": "user",
        "content": content
      }
    ],
    temperature=0,
    max_tokens=200,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  # print(chat_response)
  return chat_response['choices'][0]['message']['content']
  # return extract_time_and_space_complexity(chat_response['choices'][0]['message']['content'])

def get_cyclomitic_complexity(fun):
  v = ComplexityVisitor.from_code(fun)
  result = v.functions
  
  return result[0].complexity

def extract_time_and_space_complexity(res):
  res = json.loads(res)

  return res['time_complexity'], res['space_complexity']


def convert_complexity_to_number(complexity):
  final_comp = 1
  complexity = complexity[2:-1]
  log_indexes = [i.start() for i in re.finditer('log', complexity)]
  complexity = complexity.replace('log', '')
#   complexity = complexity.replace(r'[A-Za-z]', r'n')
  complexity = re.sub(r'[a-zA-Z]', r'n', complexity)
  for id in log_indexes:
    complexity = complexity[:id+1]+"log"+complexity[id+1:]
  complexity = complexity.replace('  ', '')
#   print(complexity)
  complexity = list(complexity)
#   print(complexity)
  i=0
  while i< len(complexity):
    if complexity[i]=="n":
       final_comp*=N
    elif complexity[i]=="l":
      final_comp*=1.2
      i+=3
    elif complexity[i]=="^":
      last=complexity[i-1]
      if last.isnumeric():
        last=int(last)
      else:
        last=N
      next = int(complexity[i+1]) if complexity[i+1].isnumeric() else N
    #   print(next,last)
      final_comp/=last
      final_comp=final_comp * 100#math.pow(last,next)
      i+=1
    i+=1
  return final_comp
#   if 
def give_start_rating(old_score,new_score):
  delta = ((old_score-new_score)/old_score)*100
  if delta<=0:
    print("No Optimisation Required")
    return {'old_code': "4.5 Star",
            'new_code': "4.5 Star"}
  
  else:
    if 0<delta<=20:
      return {'old_code': "4 Star",
            'new_code': "4.5 Star"}
    elif 20<delta<=50:
      return {'old_code': "3.1 Star",
            'new_code': "4.4 Star"}
    elif 50<delta<=75:
      return {'old_code': "2.5 Star",
            'new_code': "4.3 Star"}
    else:
      return {'old_code': "1 to 2 Star",
            'new_code': "4.7 Star"}
  
  



# precent_change = 

'''
print("factorial")
print("\nUnOptimised Code")
# res=call_Chat_gpt_for_time_and_space_complexity(factorial)
res= ["O(n)", "O(n)"]
print("Time Complexity: ", res[0])
print("Space Complexity: ", res[1])
cyclo = get_cyclomitic_complexity(factorial)
print("Cyclo Comp:", cyclo)
c1 = convert_complexity_to_number(res[0])
c2 = convert_complexity_to_number(res[1])
old_score = cyclo*(c1+c2) 
print("Score of Unoptimised Code: ",old_score)

print("\nOptimised Code")
# res=call_Chat_gpt_for_time_and_space_complexity(optimised_factorial)
res= ["O(n)", "O(1)"]
print("Time Complexity: ", res[0])
print("Space Complexity: ", res[1])
cyclo = get_cyclomitic_complexity(optimised_factorial)
print("Cyclo Comp:", cyclo)
c1 = convert_complexity_to_number(res[0])
c2 = convert_complexity_to_number(res[1])
new_score = cyclo*(c1+c2) 
print("Score of Optimised Code: ",new_score, end="\n")
print("\nstart Rating")
stars = give_start_rating(old_score, new_score)
print("Satrt Rating of Old Code: ",stars["old_code"])
print("Satrt Rating of New Code: ",stars["new_code"])

print("\n")
print("fibonacci")


print("\nUnOptimised Code")
# res=call_Chat_gpt_for_time_and_space_complexity(fibonacci)
res= ["O(2^n)", "O(n)"]
print("Time Complexity: ", res[0])
print("Space Complexity: ", res[1])
cyclo = get_cyclomitic_complexity(fibonacci)
print("Cyclo Comp: ", cyclo)
c1 = convert_complexity_to_number(res[0])
c2 = convert_complexity_to_number(res[1])
old_score = cyclo*(c1+c2)
print("Score of Unoptimised Code: ",old_score)

print("\nOptimised Code")
# res=call_Chat_gpt_for_time_and_space_complexity(optimised_fibonacci)
res= ["O(n)", "O(n)"]
print("Time Complexity: ", res[0])
print("Space Complexity: ", res[1])
cyclo = get_cyclomitic_complexity(optimised_fibonacci)
print("Cyclo Comp: ", cyclo)
c1 = convert_complexity_to_number(res[0])
c2 = convert_complexity_to_number(res[1])
new_score = cyclo*(c1+c2)
print("Score of Optimised Code: ",new_score)

print("\nstart Rating")
stars = give_start_rating(old_score, new_score)
print("Satrt Rating of Old Code: ",stars["old_code"])
print("Satrt Rating of New Code: ",stars["new_code"])
'''







# res= ["O(n^n)", "O(n)"]
# print("Time Complexity: ", res[0])
# print("Space Complexity: ", res[1])
# c1 = convert_complexity_to_number(res[0])
# c2 = convert_complexity_to_number(res[1])
# print(c1,c2)

# res= ["O(log n)", "O(n)"]
# print("Time Complexity: ", res[0])
# print("Space Complexity: ", res[1])
# c1 = convert_complexity_to_number(res[0])
# c2 = convert_complexity_to_number(res[1])
# print(c1,c2)
# res=call_Chat_gpt_for_time_and_space_complexity(optimised_factorial)
# print("time and spcae",res)
# # print(get_cyclomitic_complexity(optimised_factorial))

# ans= "{\n  \"time_complexity\": \"O(2^n)\",\n  \"space_complexity\": \"O(n)\"\n}"
# ans = extract_time_and_space_complexity(ans)
# cyclo = get_cyclomitic_complexity(optimised_factorial)
# c1 = convert_complexity_to_number(ans[0])
# c2 = convert_complexity_to_number(ans[1])
# print("Score: ",cyclo*(c1+c2))


# ans= "{\n  \"time_complexity\": \"O(n^2)\",\n  \"space_complexity\": \"O(logn)\"\n}"
# ans = extract_time_and_space_complexity(ans)
# cyclo = get_cyclomitic_complexity(optimised_factorial)
# c1 = convert_complexity_to_number(ans[0])
# c2 = convert_complexity_to_number(ans[1])
# print("Score: ",cyclo*(c1+c2))


# res=call_Chat_gpt_for_time_and_space_complexity(optimised_fibonacci)
# print("time and spcae optimised",res)
# print(get_cyclomitic_complexity(optimised_fibonacci))


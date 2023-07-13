import pandas as pd
from utils.code_snippets import codesnippets
from utils.chat_function import chat


outputDict = {
  'Title' : [],
  'Unoptimised code' : [],
  'GPT response' : [],
  'Total tokens' : [],
  'Explanation' : []
}

for title, unoptimised_code in codesnippets.items():
  print(f'Optimising {title}...')
  response, explanation, tokens = chat(unoptimised_code)
  outputDict['Title'].append(title)
  outputDict['Unoptimised code'].append(unoptimised_code)
  outputDict['GPT response'].append(response)
  outputDict['Total tokens'].append(tokens)
  outputDict['Explanation'].append(explanation)

print('Done')
df = pd.DataFrame(outputDict)
df.to_csv('Output.csv', index=False)
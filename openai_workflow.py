import sys
import openai

api_key = sys.argv[1]
query = sys.argv[3]
max_tokens = int(sys.argv[2]) + len(query)

openai.api_key = api_key

try:

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=query, 
    max_tokens=max_tokens, # the max number of tokens to generate
    temperature=0.7, # a measure of randomness
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  if response.usage.total_tokens > max_tokens:
    print("\n\nAnswer is longer than max tokens. Please adjust your settings.")
  else:
    sys.stdout.write(response.choices[0].text)

except Exception as e:
  print("OpenAI server error.", e)
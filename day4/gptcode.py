# checking openai version 
#!openai --version
# calling python moduel 
from openai import OpenAI
import time 
import json
# place apiKey HERE 
ashuApiKey = ""
# creating client 
client = OpenAI(api_key=ashuApiKey)
print(client)
# asking for user input 
user_prompt = input("Enter your prompt ... ")
# selecting model and asking for prompt input 
myresponse = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
  
    { "role": "user",  # prompt role 
      "content": user_prompt
      # "role" : "system", # model input role 
      # "content": ""
     }
  ]
)

#print(myresponse)
print('__________________________')
print('__________________________')
print('__________________________')
time.sleep(1)
print(myresponse.choices[0].message.content)
# storing output 
# myoutput = myresponse.choices[0].message.content
# newoutput = json.dumps(myoutput, indent=4)
# print('__________')
# time.sleep(2)
# print(newoutput)
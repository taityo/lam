import json
import sys
import ast

f = open('t2s/synthesize-input.json', 'r')
dict = json.load(f)
f = open('chatbot/bot_word.json', 'r')
in_dict = json.load(f) 

dict["input"]["text"] = in_dict["systemText"]["expression"]

print(in_dict["systemText"]["expression"])
f = open('t2s/synthesize-input.json', 'w')
json.dump(dict, f, indent=4, ensure_ascii=False) 

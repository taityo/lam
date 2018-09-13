import json
import sys
import ast

def write_t2s_json(content_dict):

  try:
    f = open('t2s/synthesize-input.json', 'r')
    dict = json.load(f)
    f.close()

    #f = open('chatbot/bot_word.json', 'r')
    #in_dict = json.load(f)
    #f.close() 
    #print("chatbot/bot_word.json loaded")

    dict["input"]["text"] = content_dict["systemText"]["expression"]

    #print(content_dict["systemText"]["expression"])
    f = open('t2s/synthesize-input.json', 'w')
    json.dump(dict, f, indent=4, ensure_ascii=False) 
    f.close()

  except error:
    print("write json error")



import json

f = open('t2s/resources/synthesize-output.json','r')
dict = json.load(f)

print(dict["audioContent"])

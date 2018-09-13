from s2t import stream_s2t 
import json

def write_conv(json_file):
  f = open(json_file, 'r')
  dict = json.load(f)

  word = stream_s2t.get_conv()

  if word != None:
    #print("Write word '"+ word + "'")
    dict["voiceText"] = word
    f = open(json_file, 'w')
    json.dump(dict,f,indent=4,ensure_ascii=False)
  else:
    print("Can't write json file")

if __name__ == "__main__":
  write_conv('../chatbot/chat/request.json')

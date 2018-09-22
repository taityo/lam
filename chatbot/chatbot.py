import sys
import ast
import requests
import json
import types

def get_docomo_chat():
  KEY = '563572704f466d67723632576d552f685569613463364e43446f684c564f5a4e53326f6941614768517733'

  #エンドポイントの設定
  url = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY=%s' % (KEY)
  #print(url)

  f = open('chatbot/chat/request.json', 'r')
  payload = json.load(f)
  headers = { 'Content-type': 'application/json;charset="UTF-8'}
  f.close()

  #送信
  #print(payload)
  r = requests.post(url, data=json.dumps(payload), headers=headers)
  #print(r)
  data = r.json()
  #print(data)
  return data


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



def chatbot_to_t2s():
  content_json = get_docomo_chat()

  write_t2s_json(content_json)


if __name__ == "__main__":
  chatbot_to_t2s()

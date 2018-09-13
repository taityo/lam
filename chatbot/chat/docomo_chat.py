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

if __name__ == "__main__":
  get_docomo_chat()




curl -X POST "https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY=$(printenv DOCOMO_CHAT_API_KEY)" -H "Content-Type:application/json;charset=UTF-8" -d @chatbot/chat/request.json




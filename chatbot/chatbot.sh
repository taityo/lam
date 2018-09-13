
#chatbot process
sh chatbot/chat/chat.sh > chatbot/bot_word.json


#written json file
python chatbot/write-json.py


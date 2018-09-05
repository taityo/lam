
#chatbot process
sh chatbot/chat.sh > chatbot/bot_word.json


#written json file
python chatbot/write-json.py $BOT_WORD


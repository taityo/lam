import subprocess
import sys
from start import start
from s2t import s2t
from chatbot import chatbot

def piece_of_conversation():
  s2t.write_conv("chatbot/chat/request.json")
  chatbot.chatbot_to_t2s()
  subprocess.call(["sh",  "t2s.sh"])

def conversation():
  while(True):
    #you loop 1 conversation
    piece_of_conversation()


while True:
  if start.start_conversation():
    conversation()


print("Lam finished")


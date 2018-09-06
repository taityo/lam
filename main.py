import subprocess
import sys

def piece_of_conversation():
  subprocess.call(["sh",  "s2t.sh"])
  subprocess.call(["sh",  "chatbot.sh"])
  subprocess.call(["sh",  "t2s.sh"])


while(True):
  #you loop 1 conversation
  piece_of_conversation()


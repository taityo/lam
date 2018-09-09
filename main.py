import subprocess
import sys
from start import start

def piece_of_conversation():
  subprocess.call(["sh",  "s2t.sh"])
  subprocess.call(["sh",  "chatbot.sh"])
  subprocess.call(["sh",  "t2s.sh"])

def conversation():
  while(True):
    #you loop 1 conversation
    piece_of_conversation()


while True:
  if start.start_conversation():
    conversation()


print("Lam finished")


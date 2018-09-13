from chatbot.chat import docomo_chat
from chatbot import write_json

def chatbot_to_t2s():
  content_json = docomo_chat.get_docomo_chat()

  write_json.write_t2s_json(content_json)


if __name__ == "__main__":
  chatbot_to_t2s()

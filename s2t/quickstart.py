import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources',
    'test.wav')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='ja-JP')

# Detects speech in the audio file
response = client.recognize(config, audio)

import json
f = open('t2s/synthesize-input.json', 'r')
dict = json.load(f)
res = ''

for result in response.results:
    text = result.alternatives[0].transcript
    print('Transcript: {}'.format(text))
    #print(result.alternatives[0].transcript)
    
    res = res + text 

print(res)
dict["input"]["text"] = res 
f = open('t2s/synthesize-input.json', 'w')
json.dump(dict,f,indent=4,ensure_ascii=False)

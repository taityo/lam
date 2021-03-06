import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def s2t():

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
    f = open('chatbot/chat/request.json', 'r')
    dict = json.load(f)
    res = ''

    for result in response.results:
        text = result.alternatives[0].transcript
        print('Transcript: {}'.format(text))
        #print(result.alternatives[0].transcript)
    
        res = res + text 

    if res.find('おやすみ') > -1:
        return 0

    print(res)
    dict["voiceText"] = res 
    f = open('chatbot/chat/request.json', 'w')
    json.dump(dict,f,indent=4,ensure_ascii=False)


s2t()

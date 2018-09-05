
#request t2s
curl -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application/json; charset=utf-8" -d @t2s/synthesize-input.json https://texttospeech.googleapis.com/v1beta1/text:synthesize > t2s/resources/synthesize-output.json

#python
python t2s/audio-pickup.py > t2s/resources/synthesize-output-base64.txt

#transform
base64 t2s/resources/synthesize-output-base64.txt --decode > t2s/resources/synthetic-audio.mp3
sox t2s/resources/synthetic-audio.mp3 t2s/resources/synthetic-audio.wav


aplay t2s/resources/synthetic-audio.wav


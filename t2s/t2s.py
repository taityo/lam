import json
import subprocess

def text_to_speech(text, output_wav_path):
  """Synthesizes speech from the input string of text or ssml.

  Note: ssml must be well-formed according to:
      https://www.w3.org/TR/speech-synthesis/
  """
  from google.cloud import texttospeech

  # Instantiates a client
  client = texttospeech.TextToSpeechClient()

  # Set the text input to be synthesized
  synthesis_input = texttospeech.types.SynthesisInput(text=text)

  # Build the voice request, select the language code ("ja-JP") and the ssml
  # voice gender ("neutral")
  voice = texttospeech.types.VoiceSelectionParams(
    language_code='ja-JP',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

  # Select the type of audio file you want returned
  audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16)

  # Perform the text-to-speech request on the text input with the selected
  # voice parameters and audio file type
  response = client.synthesize_speech(synthesis_input, voice, audio_config)

  # The response's audio_content is binary.
  with open(output_wav_path, 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    #print('Audio content written to file "%s"' % output_wav_path)

# 指定したjsonファイルをテキストに変換
def json_to_text(json_path):
  f = open(json_path, 'r')
  dict = json.load(f)
  return dict["input"]["text"]

# 指定したwav形式の音声ファイルを再生
def play_voice(wav_path):
  subprocess.call(["aplay", wav_path])

# t2s内のすべての処理を行う。
def t2s():
  json_path = "t2s/synthesize-input.json"
  output_wav_path = "t2s/resources/output.wav"

  text = json_to_text(json_path)
  text_to_speech(text, output_wav_path)
  play_voice(output_wav_path)


if __name__ == "__main__":
  t2s()
  #play_voice("resources/output.wav")


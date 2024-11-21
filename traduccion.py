from openai import OpenAI

client = OpenAI()

response = client.audio.translations.create(
    model="whisper-1",
    file=open("audio_input.response1.mp3", "rb")
)
print(response.to_json())

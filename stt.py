from openai import OpenAI

client = OpenAI()

response = client.audio.transcriptions.create(
    model="whisper-1",
    file=open("audio_input.response1.mp3", "rb"),
    prompt="Usaré algunas siglas como APIs y LLMs"
)

print(response)

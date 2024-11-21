from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input="HOLA! Este es el curso Conectando con LLMs a través de APIs"
)

print(response)
with open("tts.mp3", "wb") as f:
    f.write(response.content)

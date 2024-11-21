from openai import OpenAI
import base64

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={
        "voice": "sage",
        "format": "mp3"
    },
    messages=[{"role": "system", "content": "Responde en máximo 20 palabras, y siempre en español."}, {
        "role": "user", "content": "Que lugar me recomiendas para vacacionar?"}]
)

print(response.choices[0].message.audio.transcript)
audio_data = response.choices[0].message.audio.data

with open("audio_output.response1.mp3", "wb") as f:
    f.write(base64.b64decode(audio_data))

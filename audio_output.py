from openai import OpenAI
import base64

client = OpenAI()

messages = [{"role": "system", "content": "Responde en máximo 20 palabras, y siempre en español."}, {
    "role": "user", "content": "Que lugar me recomiendas para vacacionar?"}]

response = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={
        "voice": "shimmer",
        "format": "mp3"
    },
    messages=messages
)

audio = response.choices[0].message.audio
print(audio.transcript)
print(response.usage)
audio_data = audio.data

with open("audio_output.response1.mp3", "wb") as f:
    f.write(base64.b64decode(audio_data))

messages.append({
    "role": "assistant",
    "audio": {
        "id": audio.id
    }
})
messages.append({
    "role": "user",
    "content": "Y dentro de Chile?"
})

response = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={
        "voice": "shimmer",
        "format": "mp3"
    },
    messages=messages
)

audio = response.choices[0].message.audio
print(audio.transcript)
print(response.usage)
audio_data = audio.data

with open("audio_output.response2.mp3", "wb") as f:
    f.write(base64.b64decode(audio_data))

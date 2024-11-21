from openai import OpenAI
import base64

client = OpenAI()
audio_data = None
with open("audio_output.response2.mp3", "rb") as f:
    audio_data = base64.b64encode(f.read()).decode("utf-8")

response = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={
        "format": "mp3",
        "voice": "alloy"
    },
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text":  "Cuando no recomiendas lo indicado en esta recomendación de vacaciones?"},
            {"type": "input_audio", "input_audio": {
                "format": "mp3", "data": audio_data}}
        ]
    }]
)

audio = response.choices[0].message.audio
print(audio.transcript)
print(response.usage)


with open("audio_input.response1.mp3", "wb") as f:
    f.write(base64.b64decode(audio.data))

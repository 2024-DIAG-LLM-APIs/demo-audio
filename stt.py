from openai import OpenAI

client = OpenAI()


response = client.audio.transcriptions.create(
    model="whisper-1",
    file=open("audio_input.response1.mp3", "rb"),
    prompt="Usaré algunas siglas como APIs y LLMs",
    response_format="text"
)

print(response)
print("#####################")

response = client.audio.transcriptions.create(
    model="whisper-1",
    file=open("audio_input.response1.mp3", "rb"),
    prompt="Usaré algunas siglas como APIs y LLMs",
    response_format="srt"
)

print(response)
print("#####################")

response = client.audio.transcriptions.create(
    model="whisper-1",
    file=open("audio_input.response1.mp3", "rb"),
    prompt="Usaré algunas siglas como APIs y LLMs",
    response_format="json"
)

print(response)
print("#####################")

response = client.audio.transcriptions.create(
    model="whisper-1",
    file=open("audio_input.response1.mp3", "rb"),
    prompt="Usaré algunas siglas como APIs y LLMs",
    response_format="vtt"
)

print(response)
print("#####################")

response = client.audio.transcriptions.create(
    model="whisper-1",
    file=open("audio_input.response1.mp3", "rb"),
    prompt="Usaré algunas siglas como APIs y LLMs",
    response_format="verbose_json"
)

print(response.to_json())
print("#####################")

import whisper
from os import chdir, getcwd

model = whisper.load_model("medium")

chdir("D:\Master RESO\Memoire\Data\Echantillon\Videos\Emmanuel Macron")

transcript = open(".\Transcripts\emmanuelmacron_1.txt", 'w')
result = model.transcribe("emmanuelmacron_1.mp4", verbose=True)

print(result)

transcript.write(result["text"])
transcript.close()
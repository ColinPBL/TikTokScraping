import whisper
from os import chdir, getcwd

model = whisper.load_model("medium")

chdir("D:\Master RESO\Memoire\Data\Echantillon\Videos\Emmanuel Macron")


def transcribe_video(path):
    # Open output file in 'Transcripts' folder
    transcript = open("./Transcripts/" + path + ".txt", 'w')

    # Transcribe video
    result = model.transcribe(path + ".mp4", verbose=True)

    # Write each segment on one line
    for segment in result["segments"]:
        transcript.write(segment["text"])

    # Cleanup
    transcript.close()

name = "emmanuelmacron_"
for video in range(1, 28):
    transcribe_video(name + str(video))

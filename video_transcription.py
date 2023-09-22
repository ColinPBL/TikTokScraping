import whisper
from os import chdir, getcwd

model = whisper.load_model("large")

chdir("D:\Master RESO\Memoire\Data\Echantillon\Videos\Valerie Pecresse")


def transcribe_video(path):
    # Open output file in 'Transcripts' folder
    transcript = open("./Transcripts/" + path + ".txt", 'w', encoding='utf8')

    # Transcribe video
    result = model.transcribe(path + ".mp4", verbose=True)

    # Write each segment on one line
    for segment in result["segments"]:
        transcript.write(segment["text"])

    # Cleanup
    transcript.close()

name = "vpecresse_"
transcribe_video(name + '1')

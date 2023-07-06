from pyannote.audio import Pipeline
from os import chdir
from os import system

pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                    use_auth_token="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")

chdir("D:\Master RESO\Memoire\Data\Echantillon\Videos\Emmanuel Macron")
in_file = "emmanuelmacron_1.mp4"
system('ffmpeg -i -y {} -acodec pcm_s16le -ar 16000 {}.wav'.format(in_file, "emmanuelmacron_1"))

diarization = pipeline("emmanuelmacron_1.wav")
print(diarization)

with open("./Transcripts/emmanuelmacron_1.rttm", 'w') as rttm:
    diarization.write_rttm(rttm)
rttm.close()
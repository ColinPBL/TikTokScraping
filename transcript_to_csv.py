# Put all transcripts into a single .csv file

import csv
import re
import os

name = "Jean Lassalle"
os.chdir("D:/Master RESO/Memoire/Data/Echantillon/Videos/" + name + "/Transcripts")
print(os.curdir)
output_path = "transcripts.csv"
with open(output_path, 'w', encoding="utf8", newline='') as output:
    writer = csv.writer(output)
    writer.writerow(["Author", "ID_VID", "Transcript"])
    transcripts = os.listdir(".")
    pattern = re.compile("(.*)_([1-9][0-9]?)")
    for file in transcripts:
        if(os.path.isfile(file)):
            print(file)
            with open(file, 'r', encoding="utf8") as text:
                content = text.read()
                match = re.match(pattern, file)
                if(match):
                    writer.writerow([match.group(1), match.group(2), content])

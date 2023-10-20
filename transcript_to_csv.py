# Put all transcripts into a single .csv file

import csv
import re
import os

def sort_files(filename):
    pattern = re.compile("\w+_(\d*)")
    match = re.match(pattern, filename)
    if match:
        return int(match.group(1))
    return 0


os.chdir("C:\\Users\\colin\\Documents\\Master RESO\\Memoire\\Data\\Echantillon\\Videos")

video_directories = os.listdir(".")

output_path = "transcripts.csv"
with open(output_path, 'w', encoding="utf8", newline='') as output:
    writer = csv.writer(output)
    writer.writerow(["Author", "ID_VID", "Transcript", "Text length"])
    # Compile needed RE patterns to increase performance
    pattern = re.compile("(.*)_([1-9][0-9]?)")
    # Go through every account directory
    for directory in video_directories:
        if os.path.isdir(directory):
            os.chdir("./" + directory + "/Transcripts")
            transcripts = os.listdir(".")
            # Sort list to order files by their number rather than alphanumeric
            transcripts = sorted(transcripts, key=sort_files)

            for file in transcripts:
                if os.path.isfile(file):
                    print(file)
                    with open(file, 'r', encoding="utf-8") as text:
                        content = text.read()
                        match = re.match(pattern, file)
                        if match:
                            writer.writerow([match.group(1), match.group(2), content, len(content)])
            os.chdir("../../")

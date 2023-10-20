from os import chdir, listdir, path
from io import open
from tinytag import TinyTag
import csv
import re

chdir("C:\\Users\\colin\\Documents\\Master RESO\\Memoire\\Data\\Echantillon\\Videos")

video_directories = listdir(".")

with open("../videos_lengths.csv", "w", newline='') as output:

    writer = csv.writer(output)
    writer.writerow(["Account", "Video ID", "Video Length"])

    for directory in video_directories:
        if path.isdir(directory):
            chdir("./" + directory)
            files = listdir(".")
            for file in files:
                if(path.isfile(file)):
                    tag = TinyTag.get(file)
                    account = re.search("(\D*)_(\d*)", file)
                    print(f"Account : {account.group(1)}, Video ID : {account.group(2)}, Video Length : {tag.duration}")
                    writer.writerow([account.group(1), account.group(2), tag.duration])
            chdir("/")

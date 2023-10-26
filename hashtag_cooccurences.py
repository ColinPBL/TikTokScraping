import csv
from os import chdir
import re

chdir("C:\\Users\\colin\\Documents\\Master RESO\\Memoire\\Data\\Echantillon\\Analyse hashtags")

with open("hashtags.csv", 'r', newline='') as input_file:
    cooccurrence_dict = {}
    pattern = re.compile("'([^']+)'")
    output_file = open("hash_cooc.csv", "w", newline='', encoding="utf-8")
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(["Source", "Target"])
    for line in input_file:
        if line == "Challenges":
            continue
        challenges = re.findall(pattern, line)
        if challenges:
            for chall in challenges:
                if chall not in cooccurrence_dict.keys():
                    cooccurrence_dict[chall] = []
            length = len(challenges)
            if length > 1:
                for i in range(length):
                    source = challenges[i]
                    targets = challenges[i + 1:]
                    for target in targets:
                        csv_writer.writerow([source, target])
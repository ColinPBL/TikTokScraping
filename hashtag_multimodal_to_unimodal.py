from csv import writer, reader
from os import chdir

# Set working dir to the one where the data is
chdir("C:\\Users\\colin\\Documents\\Master RESO\\Memoire\\Data\\Echantillon\\Analyse hashtags")

# Open link file
with open("reseau bimodal.csv", "r") as input_file:
    # Create csv reader for ease of use
    file_reader = reader(input_file, delimiter=',')

    # Setup output file
    output_file = open("output.csv", "w", newline='')
    file_writer = writer(output_file, delimiter=',')
    file_writer.writerow(["Source", "Target", "Challenge"])

    # Data will be stored as a dict of the form target:[videos] (we reverse the link table basically)
    cooccurences = {}
    for line in file_reader:
        # Ignore first line
        if line[0] == "Source":
            continue
        # Only the first two elements of a row are relevant for our purpose here
        video, challenge, *rest = line
        if challenge not in cooccurences.keys():
            cooccurences[challenge] = []
        if video not in cooccurences[challenge]:
            cooccurences[challenge].append(video)
    print(cooccurences)
    # We now have a reversed link table, so we need to write the output to a csv file
    for key in cooccurences:
        video_list = cooccurences[key]
        length = len(video_list)
        if length > 1:
            """To avoid computing all combinations of links, we create one bidirectional link per pair. This reduces
            the complexity from o(2^n) to o(n^2) which is neat"""
            for i in range(length):
                source = video_list[i]
                targets = video_list[i + 1:]
                for target in targets:
                    file_writer.writerow([source, target, key])
    # Cleanup
    output_file.close()
input_file.close()
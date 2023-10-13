import csv
import re
from os import chdir
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
"""
Text processing requires several steps before analysis

The first step is data cleaning. The expected input format for this program is
a csv file with one document per line. A document can have several associated variables but they won't be used
in the processing step
"""

# Data cleaning
# Using this article : https://towardsdatascience.com/nlp-in-python-data-cleaning-6313a404a470
# Our text data is (relatively) clean, since it is organised in a csv file. This means we don't have to do a lot
# of cleaning
chdir("C:\\Users\\colin\\Documents\\Master RESO\\Memoire\\Data\\Echantillon\\Videos\\Emmanuel Macron\\Transcripts")

debug = True
# Importing data using pandas
documents = pd.read_csv("transcripts.csv")

if debug:
    print("Entry dataset")
    print(documents)

# Then we remove missing values : in my case, they correspond to videos that have no audio
documents.dropna(inplace=True)

if debug:
    print("Dataset after removal of missing values")
    print(documents)
# Tokenize
# Only download on first run
#nltk.download("punkt")
documents_list = documents["Transcript"]
if debug:
    print("Only text values")
    print(documents_list)

tokens = []
for document in documents_list.array:
    tokenized_doc = nltk.tokenize.word_tokenize(document)
    if debug:
        print(tokenized_doc)
    tokens += tokenized_doc

if debug:
    print("Number of tokens")
    print(len(tokens))
    print(tokens)

# Now we have our list of documents as bags of tokens
tokens = [w.lower() for w in tokens]

# Remove punctuation
if debug:
    print("Tokens to lowercase")
    print(len(tokens))
    print(tokens)

# This only removes single punctuation marks, i.e. "can't" won't be removed
for token in tokens:
    pattern = re.compile("\W+")
    match = re.match(pattern, token)
    if match:
        tokens.remove(token)

if debug:
    print("Tokens without punctuation")
    print(tokens)

# Lemmatize

stemmer = nltk.stem.SnowballStemmer("french")
stems = []
for token in tokens:
    stems.append(stemmer.stem(token))

if debug:
    print("Stemmed tokens")
    print(stems)

# Compute the tf-idf matrix from stems
tf_idf = TfidfVectorizer(input=stems)
print()
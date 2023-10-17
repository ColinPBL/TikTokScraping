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

def dummy_tokenizer(doc):
    return doc


# Data cleaning
# Using this article : https://towardsdatascience.com/nlp-in-python-data-cleaning-6313a404a470
# Our text data is (relatively) clean, since it is organised in a csv file. This means we don't have to do a lot
# of cleaning
chdir("C:\\Users\\colin\\Documents\\Master RESO\\Memoire\\Data\\Echantillon\\Videos\\")

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

documents_tokens = []
for document in documents_list.array:
    tokenized_doc = nltk.tokenize.word_tokenize(document)
    if debug:
        print(tokenized_doc)
    documents_tokens.append([w.lower() for w in tokenized_doc])

if debug:
    print("Number of tokens")
    print(len(documents_tokens))
    print(documents_tokens)

# Remove punctuation
if debug:
    print("Tokens to lowercase")
    print(len(documents_tokens))
    print(documents_tokens)

# This only removes single punctuation marks, i.e. "can't" won't be removed
for tokens in documents_tokens:
    for token in tokens:
        pattern = re.compile("\W+")
        match = re.match(pattern, token)
        if match:
            tokens.remove(token)

if debug:
    print("Tokens without punctuation")
    print(documents_tokens)

# Lemmatize

stemmer = nltk.stem.SnowballStemmer("french")
stems = []
for tokens in documents_tokens:
    stemmed_tokens = []
    for token in tokens:
        stemmed_tokens.append(stemmer.stem(token))
    stems.append(stemmed_tokens)

if debug:
    print("Stemmed tokens")
    print(stems)

# Compute the tf-idf matrix from stems
transformer = TfidfVectorizer(tokenizer=dummy_tokenizer, preprocessor=dummy_tokenizer)

tf_idf_matrix = transformer.fit_transform(stems)

if debug:
    print(tf_idf_matrix)
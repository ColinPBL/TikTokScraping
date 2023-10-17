import csv
import re
import matplotlib.pyplot as plt
from os import chdir
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

"""
Text processing requires several steps before analysis

The first step is data cleaning. The expected input format for this program is
a csv file with one document per line. A document can have several associated variables but they won't be used
in the processing step
"""


def dummy_tokenizer(doc):
    return doc


def plot_top_words(model, feature_names, n_top_words, title):
    fig, axes = plt.subplots(3, 5, figsize=(30, 15), sharex=True)
    axes = axes.flatten()
    for topic_idx, topic in enumerate(model.components_):
        top_features_ind = topic.argsort()[-n_top_words:]
        top_features = feature_names[top_features_ind]
        weights = topic[top_features_ind]

        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f"Topic {topic_idx + 1}", fontdict={"fontsize": 30})
        ax.tick_params(axis="both", which="major", labelsize=20)
        for i in "top right left".split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=40)

    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.show()


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
# nltk.download("punkt")
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
transformer = TfidfVectorizer(tokenizer=dummy_tokenizer, preprocessor=dummy_tokenizer, max_df=0.5)

tf_idf_matrix = transformer.fit_transform(stems)
tfidf_feature_names = transformer.get_feature_names_out()

if debug:
    print(tf_idf_matrix)
    print(transformer.vocabulary_)

# Topic extraction using NMF

# Define a number of topics
topics_number = 15

# Create the nmf model
nmf = NMF(n_components=topics_number, max_iter=500)

nmf.fit(tf_idf_matrix)

plot_top_words(nmf, tfidf_feature_names, 10, "Topics in NMF model (Frobenius norm)")
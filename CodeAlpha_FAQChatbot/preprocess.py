import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))


def preprocess(text):
    text = text.lower()

    tokens = word_tokenize(text)

    words = []

    for word in tokens:
        if word not in stop_words and word not in string.punctuation:
            words.append(word)

    return " ".join(words)

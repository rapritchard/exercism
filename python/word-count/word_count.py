import re
from collections import Counter
def word_count(phrase):
    phrase = phrase.lower().replace("_", " ")
    words = re.findall(r'\w+\'?\w|\w', phrase)
    wordcount = Counter(words)
    return wordcount


import string
def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    return not (set(alphabet) - set(sentence.lower()))

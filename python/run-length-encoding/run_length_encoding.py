from itertools import groupby
from re import sub
def decode(string):
    # Matched a number and something that is not a number. E.g. 12w
    return sub(r'(\d+)(\D)', lambda d: d.group(2) * int(d.group(1)), string)


def encode(string):
    # (.)\1* Matches a character and then 0 or more of the same.
    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1) if len(m.group(0)) > 1 else m.group(1), string )

from collections import Counter


def count(num):
    return lambda dice: num * Counter(dice)[num]

def straight(dice):
    min_dice = min(dice)
    length = 1
    while min_dice + length in dice:
        length += 1
    return length

def foak(dice):
    for key, value in Counter(dice).items():
        if 4 <= value:
            return key * 4
    return 0
# Score categories
# Change the values as you see fit
YACHT = lambda dice: 50 if len(dice) == 5 and len(set(dice)) == 1 else 0
ONES = count(1)
TWOS = count(2)
THREES = count(3)
FOURS = count(4)
FIVES = count(5)
SIXES = count(6)
FULL_HOUSE = lambda dice: sum(dice) if sorted(tuple(Counter(dice).values())) == [2, 3] else 0
FOUR_OF_A_KIND = foak
LITTLE_STRAIGHT = lambda dice: 30 if 5 == straight(dice) and max(dice) == 5 else 0
BIG_STRAIGHT = lambda dice: 30 if 5 == straight(dice) and max(dice) == 6 else 0
CHOICE = lambda dice: sum(dice)


def score(dice, category):
    return category(dice)

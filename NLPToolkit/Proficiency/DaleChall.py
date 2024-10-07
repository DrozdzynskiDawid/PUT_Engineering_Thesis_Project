from .CounterHelper import *
from .ModuleException import *


def daleChall(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    difficultWords = counter.getDifficultWords("dale_chall_word_list.txt")

    try:
        score = 0.1579 * (difficultWords / words * 100) + 0.0496 * (words / sentences)
        if round(difficultWords / words, 2) * 100 > 0.05:
            score += 3.6365

        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

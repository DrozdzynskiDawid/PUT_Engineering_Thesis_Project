from .CounterHelper import *
from ..ModuleException import *


def daleChall(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    difficultWords = counter.getDifficultWords("dale_chall_word_list.txt")

    try:
        score = 15.79 * (difficultWords / words) + 0.0496 * (words / sentences) + 3.6365
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

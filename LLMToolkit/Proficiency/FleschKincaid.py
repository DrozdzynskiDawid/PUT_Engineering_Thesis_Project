from .CounterHelper import *
from .ModuleException import *


def fleschKincaid(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    syllables = counter.getSyllables()

    try:
        score = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()


def gradeLevelFleschKincaid(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    syllables = counter.getSyllables()

    try:
        score = 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

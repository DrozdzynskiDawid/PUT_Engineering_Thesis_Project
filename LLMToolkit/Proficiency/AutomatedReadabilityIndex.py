from .CounterHelper import *
from .ModuleException import *


def ARI(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    characters = counter.getCharacters()

    try:
        score = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

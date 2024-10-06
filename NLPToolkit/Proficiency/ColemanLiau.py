from .CounterHelper import *
from .ModuleExcetion import *


def colemanLiau(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    characters = counter.getCharacters()

    try:
        score = 0.0588 * round((characters / words) * 100) - 0.296 * round((sentences / words) * 100, 2) - 15.8
        return score
    except ZeroDivisionError:
        getDivideByZeroError()

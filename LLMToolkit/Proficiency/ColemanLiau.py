from .CounterHelper import *
from ..ModuleException import *


def colemanLiau(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    characters = counter.getCharacters()

    try:
        score = 5.88 * (characters / words) - 29.6 * (sentences / words) - 15.8
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

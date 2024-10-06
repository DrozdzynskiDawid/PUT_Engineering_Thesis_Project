from .CounterHelper import *
from .ModuleExcetion import *


def gunningFog(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    complexWords = counter.getComplexWords()

    try:
        score = 0.4 * ((words / sentences) + 100 * (complexWords / words))
        return score
    except ZeroDivisionError:
        getDivideByZeroError()

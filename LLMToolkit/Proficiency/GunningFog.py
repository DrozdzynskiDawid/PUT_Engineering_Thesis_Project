from .CounterHelper import *
from ..ModuleException import *


def gunningFog(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    complexWords = counter.getComplexWords()

    try:
        score = 0.4 * ((words / sentences) + 100 * (complexWords / words))
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

import random
from .CounterHelper import *
from ..ModuleException import *


def forcast(text: str):
    if type(text) != str:
        getTypeError()
    lengthText = len(text.split(" "))

    if lengthText <= 150:
        counter = CounterHelper(text)
        words = counter.getWords()
        oneSyllables = counter.getOneSyllablesWords()
    else:
        lengthText = 150
        textPrim = random.sample(text.split(), lengthText)
        counter = CounterHelper(textPrim)
        words = counter.getWords()
        oneSyllables = counter.getOneSyllablesWords()

    try:
        score = 20 - (oneSyllables * lengthText) / (words * 10)
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

from .CounterHelper import *
from .ModuleExcetion import *
import math


def readabilitySMOG(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    sentences = counter.getSentences()
    complexWords = counter.getComplexWords()
    if sentences < 30:
        getStatisticError()

    try:
        score = 1.043 * math.sqrt(complexWords * (30 / sentences)) + 3.1291
        return score
    except ZeroDivisionError:
        getDivideByZeroError()


def easierSMOG(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    sentences = counter.getSentences()
    complexWords = counter.getComplexWords()
    print(sentences)
    if sentences < 30:
        getStatisticError()

    try:
        score = round(math.sqrt((complexWords * (30 / sentences)))) + 3
        return score
    except ZeroDivisionError:
        getDivideByZeroError()

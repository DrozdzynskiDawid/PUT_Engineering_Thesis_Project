from .CounterHelper import *
from ..ModuleException import *
import math


def readabilitySMOG(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    sentences = counter.getSentences()
    complexWords = counter.getComplexWords()
    if sentences < 30:
        getStatisticError("30 sentences")

    try:
        score = 1.043 * math.sqrt(complexWords * (30 / sentences)) + 3.1291
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()


def easierSMOG(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    sentences = counter.getSentences()
    complexWords = counter.getComplexWords()
    if sentences < 30:
        getStatisticError("30 sentences")

    try:
        score = round(math.sqrt((complexWords * (30 / sentences)))) + 3
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

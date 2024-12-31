from .CounterHelper import *
from ..ModuleException import *
import random


def linsearWrite(text: str):
    if type(text) != str:
        getTypeError()

    if len(text.split(' ')) < 100:
        counter = CounterHelper(text)
    else:
        textPrim = random.sample(text.split(), 100)
        counter = CounterHelper(" ".join(textPrim))
    easyWord, hardWord = counter.getEasyWords()
    sentences = counter.getSentences()
    try:
        r = (3 * hardWord + easyWord) / sentences

        if r > 20:
            return round(r / 2, 2)
        else:
            return round(r / 2 - 2, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

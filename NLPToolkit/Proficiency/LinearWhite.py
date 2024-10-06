from .CounterHelper import *
from .ModuleExcetion import *
import random


def linearWhite(text: str):
    if type(text) != str:
        getTypeError()

    if len(text.split(' ')) < 100:
        counter = CounterHelper(text)
    else:
        textPrim = random.sample(text.split(), 100)
        counter = CounterHelper(textPrim)
    try:
        r = (3 * counter.getComplexWords() + counter.getEasyWords()) / counter.getSentences()

        if r > 20:
            return r / 2
        else:
            return r / 2 - 1
    except ZeroDivisionError:
        getDivideByZeroError()

from .CounterHelper import *
from .ModuleException import *
import random


def linearWhite(text: str):
    if type(text) != str:
        getTypeError()

    if len(text.split(' ')) < 100:
        counter = CounterHelper(text)
    else:
        textPrim = random.sample(text.split(), 100)
        counter = CounterHelper(" ".join(textPrim))
    try:

        r = (3 * counter.getComplexWords() + counter.getEasyWords()) / counter.getSentences()

        if r > 20:
            return round(r / 2, 2)
        else:
            return round(r / 2 - 1, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

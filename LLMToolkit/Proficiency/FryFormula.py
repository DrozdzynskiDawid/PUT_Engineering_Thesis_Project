from .CounterHelper import *
from .ModuleException import *
import random


def fryFormula(text: str):
    if type(text) != str:
        getTypeError()

    if len(text.split(" ")) < 100:
        getStatisticError("100 words")
    else:
        textPrim = random.sample(text.split(), 100)
        counter = CounterHelper(" ".join(textPrim))
        sentences = counter.getSentences()
        syllables = counter.getSyllables()
        try:
            return round(syllables / 100, 2), round(sentences / 100, 2)
        except ZeroDivisionError:
            getDivideByZeroError()

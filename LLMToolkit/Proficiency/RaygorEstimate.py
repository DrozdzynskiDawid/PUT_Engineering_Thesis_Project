from .CounterHelper import *
from .ModuleException import *
import random


def raygorEstimate(text: str):
    if type(text) != str:
        getTypeError()
    textPrim = ""
    splitText = text.split(" ")
    splitTextLen = len(splitText)
    if splitTextLen < 100:
        getStatisticError("100 words")

    elif 100 <= splitTextLen < 200:
        textPrim = splitText[0:100]

    elif 200 <= splitTextLen < 300:
        textPrim = splitText[0:100] + splitText[splitTextLen - 101:splitTextLen - 1]

    else:
        textPrim = splitText[0:100] + splitText[round(splitTextLen / 2) - 51: round(splitTextLen / 2) + 50] + splitText[splitTextLen - 100: splitTextLen - 1]

    n = len(textPrim)
    textPrim = " ".join(textPrim)
    counter = CounterHelper(" ".join(textPrim))
    sentences = counter.getSentences()
    syllables = counter.getSyllables()

    try:
        return round(syllables / n, 2), round(sentences / n, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

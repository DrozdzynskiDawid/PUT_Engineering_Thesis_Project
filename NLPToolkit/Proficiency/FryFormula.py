from .CounterHelper import *
from .ModuleException import *


def fryFormula(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    sentences = counter.getSentences()
    syllables = counter.getSyllables()

    try:
        return round(gradeGraph(syllables / 100, sentences / 100), 2)
    except ZeroDivisionError:
        getDivideByZeroError()


def gradeGraph(x, y):
    if y < 2.5:
        return 12
    elif y < 3.5:
        if x < 112:
            return 1
        elif x < 120:
            return 2
        else:
            return 3
    elif y < 4.5:
        if x < 120:
            return 3
        elif x < 128:
            return 4
        else:
            return 5
    elif y < 5.5:
        if x < 130:
            return 5
        elif x < 140:
            return 6
        else:
            return 7
    elif y < 6.5:
        if x < 140:
            return 6
        elif x < 150:
            return 7
        else:
            return 8
    elif y < 7.5:
        if x < 150:
            return 7
        elif x < 160:
            return 8
        else:
            return 9
    elif y < 8.5:
        if x < 160:
            return 8
        elif x < 168:
            return 9
        else:
            return 10
    elif y < 9.5:
        if x < 168:
            return 9
        elif x < 172:
            return 10
        else:
            return 11
    elif y < 10.5:
        if x < 172:
            return 10
        else:
            return 11
    elif y < 11.5:
        if x < 172:
            return 11
        else:
            return 12
    else:  # y >= 12.5
        return 12

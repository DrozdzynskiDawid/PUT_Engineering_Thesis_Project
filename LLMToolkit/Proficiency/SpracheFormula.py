from .CounterHelper import *
from ..ModuleException import *


def spracheOriginalFormula(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    difficultWords = counter.getDifficultWords("sprache_formula_word_list.txt")

    try:
        score = 0.141 * words / sentences + 8.6 * difficultWords / words + 0.839
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()


def spracheRevisedFormula(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    difficultWords = counter.getDifficultWords("sprache_formula_word_list.txt")

    try:
        score = 0.121 * words / sentences + 8.2 * difficultWords / words + 0.659
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

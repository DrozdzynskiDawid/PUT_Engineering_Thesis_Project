from .CounterHelper import *
from ..ModuleException import *


def spracheOriginalFormula(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    difficultWords = counter.getDifficultWords("dale_chall_word_list.txt")

    try:
        avgSentenceLength = words / sentences
        perDifficult = difficultWords / words * 100
        score = 0.141 * avgSentenceLength + 0.086 * perDifficult + 0.839
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()


def spracheRevisedFormula(text: str):
    if type(text) != str:
        getTypeError()
    counter = CounterHelper(text)
    words = counter.getWords()
    sentences = counter.getSentences()
    difficultWords = counter.getDifficultWords("dale_chall_word_list.txt")

    try:
        avgSentenceLength = words / sentences
        perDifficult = difficultWords / words * 100
        score = 0.121 * avgSentenceLength + 0.082 * perDifficult + 0.659
        return round(score, 2)
    except ZeroDivisionError:
        getDivideByZeroError()

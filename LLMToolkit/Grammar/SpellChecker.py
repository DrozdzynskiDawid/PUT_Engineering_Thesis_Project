from spellchecker import SpellChecker
import nltk
from ..ModuleException import *

def checkSpelling(text: str):
    if type(text) != str:
        getTypeError()
    spell = SpellChecker()
    text_tokenized = nltk.tokenize.word_tokenize(text)
    misspelled = spell.unknown(text_tokenized)
    corrections = {word: spell.correction(word) for word in misspelled}
    return corrections

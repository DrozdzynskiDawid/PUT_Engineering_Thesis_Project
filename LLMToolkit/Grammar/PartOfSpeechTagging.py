import spacy
from collections import Counter
from ..ModuleException import *

def getPartOfSpeechTagging(text: str):
    if type(text) != str:
        getTypeError()
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    pos_counts = Counter(token.pos_ for token in doc)
    return pos_counts

def getNouns(text: str):
    result = getPartOfSpeechTagging(text)
    nouns = result['NOUN']
    return nouns

def getVerbs(text: str):
    result = getPartOfSpeechTagging(text)
    verbs = result['VERB']
    return verbs
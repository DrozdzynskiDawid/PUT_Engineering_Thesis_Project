from ..ModuleException import *
import requests
import nltk

def check(text: str):
    api_url = "https://api.languagetool.org/v2/check"
    data = {
            'text': text,
            'language': 'en-US',
        }
    response = requests.post(api_url, data=data)
    matches = response.json().get('matches', [])
    return matches

def getGER(text: str):
    if type(text) != str:
        getTypeError()
    
    sentences = nltk.tokenize.sent_tokenize(text)
    sentences_length = len(sentences)
    count_errors = 0

    for s in sentences:
        matches = check(s)
        if matches:
            count_errors += 1

    return count_errors / sentences_length * 100

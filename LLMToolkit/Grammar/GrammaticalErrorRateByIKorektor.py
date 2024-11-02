from ..ModuleException import *
import requests
import nltk

api_url = 'https://api.ikorektor.pl'
api_key = '75b4fd805a'

def check(text: str):
    params = {
        'text': text,
        'key': api_key,
        'info': 1
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    result = response.json()
    return result

def getGERIKorektor(text: str):
    if type(text) != str:
        getTypeError()
    
    sentences = nltk.tokenize.sent_tokenize(text)
    sentences_length = len(sentences)
    count_errors = 0
    result_text = check(text)
    for s in sentences:
        result = check(s)
        if 'succs' in result:
            count_errors += 1

    return (count_errors / sentences_length * 100, result_text)

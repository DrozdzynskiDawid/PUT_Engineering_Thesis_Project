import spacy
import textstat
from spacy.language import Language
from spacy.tokens import Token
import importlib.resources


@Language.component("syllables")
def syllables_component(doc):
    if not Token.has_extension("syllables_count"):
        Token.set_extension("syllables_count", getter=lambda token: textstat.syllable_count(token.text))
    return doc


class CounterHelper:
    text: str
    suffixes = ['ness', 'tion', 'ment', 'ity', 'er', 'or', 'ance', 'ence', 'ship', 'ism', 'ist', 'cy', 'al',
                'en', 'ify', 'ize', 'ate', 'able', 'ible', 'ful', 'ous', 'ic', 'ive', 'less', 'y', 'ish', 'ant',
                'ly', 'ward', 'wise', 's', 'es', '’s', 'er', 'est', 'ing', 'ed']

    def __init__(self, text: str):
        self.text = text

    def setup(self):
        nlp = spacy.load("en_core_web_sm")
        return nlp(self.text)

    def textWithoutSuffixes(self):
        doc = self.setup()
        Token.set_extension("syllables_count", getter=lambda token: textstat.syllable_count(token.text), force=True)

        words = []
        for token in doc:
            if not token.is_punct:
                word = token.text
                for suffix in self.suffixes:
                    if word.endswith(suffix):
                        word = word.removesuffix(suffix)
                        break
                words.append(word)

        nlp = spacy.load('en_core_web_sm')
        return nlp(" ".join(words))

    def listFromFile(self, file):
        with importlib.resources.open_text('LLMToolkit.Proficiency', 'dale_chall_word_list.txt') as file:
            words = file.read().splitlines()

        listWord = set()
        for word in words:
            forms = [word]
            for suffix in self.suffixes:
                forms.append(word + suffix)
            listWord.update(forms)

        return listWord

    def getDifficultWords(self, file='dale_chall_word_list.txt'):
        wordFrom = self.listFromFile(file)
        count = 0
        doc = self.setup()
        tokens = [token.text.lower() for token in doc if not token.is_punct and not token.is_space]

        for token in tokens:
            if token not in wordFrom:
                count += 1
        return count

    def getWords(self):
        doc = self.setup()
        words = [token.text for token in doc if not token.is_space and not token.is_punct]
        return len(words)

    def getSentences(self):
        doc = self.setup()
        return len(list(doc.sents))

    def getSyllables(self):
        nlp = spacy.load("en_core_web_sm")
        nlp.add_pipe("syllables", after="tagger")
        doc = nlp(self.text)

        return sum([token._.syllables_count for token in doc if not token.is_punct and not token.is_digit])

    def getOneSyllablesWords(self):
        nlp = spacy.load("en_core_web_sm")
        nlp.add_pipe("syllables", after="tagger")

        doc = nlp(self.text)
        return sum([token._.syllables_count for token in doc if
                    not token.is_punct and not token.is_digit and token._.syllables_count == 1])

    def getCharacters(self):
        doc = self.setup()
        characters = ''.join([token.text for token in doc if not token.is_space and not token.is_punct])
        return len(characters)

    def getComplexWords(self):
        count = 0
        text = self.textWithoutSuffixes()

        for difficult in text:
            if difficult._.syllables_count >= 3:
                count += 1

        return count

    def getMoreThan6LettersWords(self):
        count = 0
        doc = self.setup()
        words = [token.text for token in doc if not token.is_space and not token.is_punct]

        for word in words:
            if len(word) >= 6:
                count += 1
        return count

    def getEasyWords(self):
        countEasy, countHard = 0, 0
        text = self.textWithoutSuffixes()
        for easy in text:
            if easy._.syllables_count < 3:
                countEasy += 1
            else:
                countHard += 1

        return countEasy, countHard

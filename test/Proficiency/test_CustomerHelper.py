import unittest
from LLMToolkit.Proficiency.CounterHelper import *
from test.TestHelper import *

class TestColemanLiau(unittest.TestCase):
    def test_get_words(self):
        counter = CounterHelper(text=getTestText1())
        self.assertEqual(counter.getWords(), 148)

    def test_get_sentences(self):
        counter = CounterHelper(text=getTestText1())
        self.assertEqual(counter.getSentences(), 7)

    def test_get_difficult_words(self):
        counter = CounterHelper(text=getTestText1())
        self.assertEqual(counter.getDifficultWords(), 27)

    def test_get_syllables(self):
        counter = CounterHelper(text=getTestText1())
        self.assertEqual(counter.getSyllables(), 219)

    def test_get_characters(self):
        counter = CounterHelper(text=getTestText1())
        self.assertEqual(counter.getCharacters(), 739)

    def test_get_one_syllables_words(self):
        counter = CounterHelper(text=getTestText1())
        self.assertEqual(counter.getOneSyllablesWords(), 101)

    def test_get_complex_words(self):
        counter = CounterHelper(text=getTestText1())
        self.assertEqual(counter.getComplexWords(), 9)

    def test_get_long_words(self):
        counter = CounterHelper(text="This is an example sentence to test difficult counting.")
        self.assertEqual(counter.getMoreThan6LettersWords(), 4)

    def test_get_easy_words(self):
        counter = CounterHelper(text=getTestText1())
        self.assertEqual(counter.getEasyWords(), (139,9))

if __name__ == '__main__':
    unittest.main()
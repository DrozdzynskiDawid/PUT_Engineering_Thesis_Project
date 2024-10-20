import unittest
from LLMToolkit.Grammar.PartOfSpeechTagging import *
from test.TestHelper import *


class TestPOSTagging(unittest.TestCase):
    def test_nouns_text1(self):
        value = getNouns(text=getTestText1())
        self.assertEqual(value, 44)

    def test_verbs_text1(self):
        value = getVerbs(text=getTestText1())
        self.assertEqual(value, 20)

    def test_verbs_text2(self):
        value = getVerbs(text=getTestText2())
        self.assertEqual(value, 5)


if __name__ == '__main__':
    unittest.main()
import unittest
from LLMToolkit.Grammar.LanguageDetection import *
from test.TestHelper import *


class TestLanguageTool(unittest.TestCase):
    def test_should_be_english(self):
        value = getLanguageConfidenceValue(text=getTestText2(), top=3)
        self.assertEqual(str(value[0].language), "Language.ENGLISH")
        self.assertGreater(value[0].value, 0.9)

    def test_should_be_polish(self):
        value = getLanguageConfidenceValue(text=getTestText5(), top=3)
        self.assertEqual(str(value[0].language), "Language.POLISH")
        self.assertGreater(value[0].value, 0.9)

if __name__ == '__main__':
    unittest.main()
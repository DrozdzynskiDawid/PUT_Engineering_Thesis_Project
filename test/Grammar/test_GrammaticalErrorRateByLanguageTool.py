import unittest
from LLMToolkit.Grammar.GrammaticalErrorRateByLanguageTool import *
from test.TestHelper import *


class TestGrammaticalErrorRateByLanguageTool(unittest.TestCase):
    def test_text_with_no_errors(self):
        value = getGER(text=getTestText1())
        self.assertEqual(value[0], 0.0)

    def test_should_be_errors(self):
        value = getGER(text=getTestText4())
        self.assertEqual(value[0], 80.0)

    def test_polish_text(self):
        value = getGER(text=getTestText5())
        self.assertEqual(value[0], 25.0)

if __name__ == '__main__':
    unittest.main()
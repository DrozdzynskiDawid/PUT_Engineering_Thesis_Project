import unittest
from LLMToolkit.Grammar.GrammaticalErrorRate import *
from test.TestHelper import *


class TestGrammaticalErrorRate(unittest.TestCase):
    def test_text_with_no_errors(self):
        value = getGER(text=getTestText1())
        self.assertEqual(value, 0.0)

    def test_should_be_errors(self):
        value = getGER(text=getTestText4())
        self.assertEqual(value, 80.0)


if __name__ == '__main__':
    unittest.main()
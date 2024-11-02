import unittest
from LLMToolkit.Grammar.GrammaticalErrorRateByIKorektor import *
from test.TestHelper import *


class TestGrammaticalErrorRateByIKorektor(unittest.TestCase):
    def test_polish_text(self):
        value = getGER(text=getTestText5())
        self.assertEqual(value[0], 25.0)

if __name__ == '__main__':
    unittest.main()
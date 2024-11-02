import unittest
from LLMToolkit.Grammar.SpellChecker import *
from test.TestHelper import *


class TestSpellChecker(unittest.TestCase):
    def test_spellChecker(self):
        value = checkSpelling(text=getTestText3())
        self.assertGreater(len(value), 10)


if __name__ == '__main__':
    unittest.main()
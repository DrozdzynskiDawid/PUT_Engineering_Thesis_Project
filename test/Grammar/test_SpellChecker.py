import unittest
from LLMToolkit.Grammar.SpellChecker import *
from test.TestHelper import *


class TestSpellChecker(unittest.TestCase):
    def test_spellChecker(self):
        value = check_spelling(text=getTestText3())
        self.assertEqual(len(value), 20)


if __name__ == '__main__':
    unittest.main()
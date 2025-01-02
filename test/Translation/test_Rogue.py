import unittest
from LLMToolkit.Translation.Rogue import calculate_rouge
class TestCalculateRouge(unittest.TestCase):
    def test_normal_case(self):
        ref = "This is a test reference"
        hyp = "This is a reference test"
        score = calculate_rouge(ref, hyp)
        self.assertGreater(score, 0)

    def test_empty_reference(self):
        with self.assertRaises(ValueError):
            calculate_rouge("", "Non-empty hypothesis")

    def test_empty_hypothesis(self):
        with self.assertRaises(ValueError):
            calculate_rouge("Non-empty reference", "")

    def test_identical_strings(self):
        text = "Exact match case"
        score = calculate_rouge(text, text)
        self.assertAlmostEqual(score, 1.0, delta=1e-5)

    def test_partially_similar_strings(self):
        ref = "This is a longer reference text"
        hyp = "This is a shorter reference"
        score = calculate_rouge(ref, hyp)
        self.assertTrue(0 < score < 1.0)

if __name__ == '__main__':
    unittest.main()

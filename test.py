
import unittest

from main import AhoCorasick

class TestAhoCorasick(unittest.TestCase):
    def test_empty_trie(self):
        ac = AhoCorasick()
        self.assertEqual(ac.search("text", []), {})

    def test_single_pattern(self):
        ac = AhoCorasick()
        self.assertEqual(ac.search("abc", ["a"]), {"a": [0]})

    def test_multiple_patterns(self):
        ac = AhoCorasick()
        self.assertEqual(ac.search("she", ["he", "she"]), {'he': [1], 'she': [0]})

    def test_no_match(self):
        ac = AhoCorasick()
        self.assertEqual(ac.search("abc", ["xyz"]), {"xyz": []})

    def test_fail_transitions(self):
        ac = AhoCorasick()
        self.assertEqual(ac.search("abc", ["ab", "bc"]), {"ab": [0], "bc": [1]})

    def test_complex_condition(self):
        ac = AhoCorasick()
        self.assertEqual(ac.search("longest", ["long", "longer", "longest"]), {"long": [0], "longer": [], "longest": [0]})


if __name__ == "__main__":
    unittest.main()
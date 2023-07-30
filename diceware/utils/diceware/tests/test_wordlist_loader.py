import os

import pytest
import sys

sys.path.append('.')

from diceware.utils.diceware.wordlist_loader import make_wordlist, make_dict, load_lines_from_file


@pytest.mark.wordlist_loader
class TestWordlistLoader:
    wordlist = os.path.join(os.path.dirname(__file__), "wordlist.txt")

    def test_make_dict(self):
        line = "11111 a"
        assert make_dict(line) == {"number": "11111", "word": "a"}

    def test_make_wordlist(self):
        wordlist = ["11111 a", "11112 b", "11113 c"]
        assert make_wordlist(wordlist) == [{"number": "11111", "word": "a"}, {"number": "11112", "word": "b"}, {"number": "11113", "word": "c"}]

    def test_load_lines_from_file(self):
        print(self.wordlist)
        assert load_lines_from_file(self.wordlist) == [{"number": "11111", "word": "abacus"}, {"number": "11112", "word": "abdomen"}, {"number": "11113", "word": "abdominal"}]
import pytest
import sys

sys.path.append('.')

from diceware.utils.diceware.passgen import find_index, get_word


@pytest.mark.passgen
class TestPassgen:
    wordlist = [
        {"number": "11111", "word": "a"},
        {"number": "22222", "word": "b"},
        {"number": "33333", "word": "c"},
        {"number": "44444", "word": "d"},
        {"number": "55555", "word": "e"},
        {"number": "66666", "word": "f"},
        {"number": "77777", "word": "g"},
        {"number": "88888", "word": "h"},
        {"number": "99999", "word": "i"},
        {"number": "12345", "word": "j"},
        {"number": "23456", "word": "k"},
        {"number": "34567", "word": "l"},
        {"number": "45678", "word": "m"},
        {"number": "56789", "word": "n"},
        {"number": "67890", "word": "o"},
        {"number": "98765", "word": "p"},
        {"number": "87654", "word": "q"},
        {"number": "76543", "word": "r"},
        {"number": "65432", "word": "s"},
        {"number": "54321", "word": "t"},
    ]

    @pytest.mark.parametrize("number, expected", [
        ("11111", 0),
        ("22222", 1),
        ("33333", 2),
        ("44444", 3),
        ("55555", 4),
        ("66666", 5),
        ("77777", 6),
        ("88888", 7),
        ("99999", 8),
        ("12345", 9),
        ("23456", 10),
        ("34567", 11),
        ("45678", 12),
        ("56789", 13),
        ("67890", 14),
        ("98765", 15),
        ("87654", 16),
        ("76543", 17),
        ("65432", 18),
        ("54321", 19),
    ])
    def test_find_index(self, number, expected):
        assert find_index(self.wordlist, number) == expected

    @pytest.mark.parametrize("index, expected", [
        (0, "a"),
        (1, "b"),
        (2, "c"),
        (3, "d"),
        (4, "e"),
        (5, "f"),
        (6, "g"),
        (7, "h"),
        (8, "i"),
        (9, "j"),
        (10, "k"),
        (11, "l"),
        (12, "m"),
        (13, "n"),
        (14, "o"),
        (15, "p"),
        (16, "q"),
        (17, "r"),
        (18, "s"),
        (19, "t"),
    ])
    def test_get_word(self, index, expected):
        assert get_word(self.wordlist, index) == expected

    # Correctness of the passphrase_generation is tested in test_diceware.py

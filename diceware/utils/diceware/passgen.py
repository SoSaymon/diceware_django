import os
import sys

sys.path.append('.')

import diceware.utils.diceware.dice as dice
import diceware.utils.diceware.wordlist_loader as wordlist_loader


def find_index(wordlist: list[dict[str, str]], number: str) -> int:
    """
    Find the index of the word in the wordlist
    :param wordlist:  The wordlist
    :param number:  The number to search for
    :return:  The index of the word
    """
    for index, element in enumerate(wordlist):
        if element.get("number") == number:
            return index

    return -1


def get_word(wordlist: list[dict[str, str]], index: int) -> str:
    """
    Get the word from the wordlist
    :param wordlist:  The wordlist
    :param index:  The index of the word
    :return:  The word
    """
    tmp = wordlist[index]
    return tmp.get("word")


def passphrase_generation(number_of_words: int, separator: str = "-", capitalize: bool = True) -> str:
    """
    Generate a passphrase
    :param number_of_words: The number of words to generate
    :param separator: The separator to use
    :param capitalize: Whether to capitalize the first letter of each word
    :return: The passphrase
    """
    filename = os.path.join(os.path.dirname(__file__), "wordlist.txt")
    wordlist = wordlist_loader.load_lines_from_file(filename)
    passphrase = ""

    for i in range(number_of_words):
        number = dice.generate_string_of_numbers()
        index = find_index(wordlist, number)
        word = get_word(wordlist, index)

        if capitalize:
            word = word.capitalize()

        if i == 0 or i == number_of_words:
            passphrase += word
        else:
            passphrase += separator + word

    return passphrase

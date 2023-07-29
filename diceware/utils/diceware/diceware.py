import sys

sys.path.append('.')
import diceware.utils.diceware.passgen as passgen


def generate(number_of_words: int, separator: str, capitalize: bool) -> str:
    """
    Generate a passphrase
    :param number_of_words: The number of words to generate
    :param separator: The separator to use
    :param capitalize: Whether to capitalize the first letter of each word
    :return: The passphrase
    """
    try:
        validate(number_of_words, separator, capitalize)
    except ValueError as error:
        raise error

    return passgen.passphrase_generation(number_of_words, separator, capitalize)


def validate(number_of_words: int, separator: str, capitalize: bool) -> None:
    """
    Validate the input from the user
    :param number_of_words: The number of words to generate
    :param separator: The separator to use
    :param capitalize: Whether to capitalize the first letter of each word
    :return: None
    """
    if number_of_words > 10:
        raise ValueError("Cannot generate more than 10 words")

    if number_of_words < 3:
        raise ValueError("Cannot generate less than 3 words")

    if not capitalize and separator == '':
        raise ValueError('Cannot capitalize first letter without a separator')

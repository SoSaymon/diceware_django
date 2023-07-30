import re
import pytest
import sys

sys.path.append('.')

from diceware.utils.diceware.diceware import generate, validate


@pytest.mark.diceware
class TestDiceware:
    """
    Test the diceware module

    Methods

    test_generate:
        Test the generate function
    test_validate:
        Test the validate function
    """
    @pytest.mark.parametrize('number_of_words', [3, 4, 5, 6, 7, 8, 9, 10])
    @pytest.mark.parametrize('separator', ['', ' ', '-', '_'])
    @pytest.mark.parametrize('capitalize', [True, False])
    def test_generate(self, number_of_words, separator, capitalize):
        if not capitalize and separator == '':
            capitalize = True

        passphrase = generate(number_of_words, separator, capitalize)
        if separator == '':
            words = re.findall(r'[A-Z][a-z]*', passphrase)
            assert len(words) == number_of_words
        else:
            assert len(passphrase.split(separator)) == number_of_words

            if capitalize:
                for word in passphrase.split(separator):
                    assert word[0].isupper()
            else:
                for word in passphrase.split(separator):
                    assert word[0].islower()

    @pytest.mark.parametrize(
        'number_of_words, separator, capitalize, error_message',
        [
            (2, '', True, 'Cannot generate less than 3 words'),
            (11, '', True, 'Cannot generate more than 10 words'),
            (3, '', False, 'Cannot capitalize first letter without a separator'),
        ]
    )
    def test_validate(self, number_of_words, separator, capitalize, error_message):

        with pytest.raises(ValueError) as error:
            validate(number_of_words, separator, capitalize)

        assert error_message in str(error.value)
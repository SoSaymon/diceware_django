import pytest
import sys

sys.path.append('.')

from diceware.utils.diceware.dice import generate_numbers, concat_all_numbers, generate_string_of_numbers


@pytest.mark.dice
class TestDice:
    """
    Test the dice module

    Methods

    test_generate_number:
        Test the generate_numbers function
    test_concat_all_numbers:
        Test the concat_all_numbers function
    test_generate_string_of_numbers:
        Test the generate_string_of_numbers function
    """
    @pytest.mark.parametrize('number_of_numbers', [3, 4, 5, 6, 7, 8, 9, 10])
    def test_generate_numbers(self, number_of_numbers):
        numbers = generate_numbers(number_of_numbers)
        assert len(numbers) == number_of_numbers
        for number in numbers:
            assert 1 <= number <= 6

    @pytest.mark.parametrize('number_of_numbers', [3, 4, 5, 6, 7, 8, 9, 10])
    def test_concat_all_numbers(self, number_of_numbers):
        numbers = generate_numbers(number_of_numbers)
        string_of_numbers = concat_all_numbers(numbers)
        assert len(string_of_numbers) == number_of_numbers
        for number in string_of_numbers:
            assert '1' <= number <= '6'

    @pytest.mark.parametrize('number_of_numbers', [3, 4, 5, 6, 7, 8, 9, 10])
    def test_generate_string_of_numbers(self, number_of_numbers):
        string_of_numbers = generate_string_of_numbers(number_of_numbers)
        assert len(string_of_numbers) == number_of_numbers
        for number in string_of_numbers:
            assert '1' <= number <= '6'

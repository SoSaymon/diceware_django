# IMPORTS
import random


def generate_numbers(number_of_numbers: int = 5) -> list[int]:
    """
    Generate a list of numbers
    :param number_of_numbers:  The number of numbers to generate
    :return:  The list of numbers
    """
    num_arr = []
    i = 0
    while i < number_of_numbers:
        num = round(random.random() * 10)
        if num > 6 or num < 1:
            continue
        num_arr.append(num)
        i += 1
    return num_arr


def concat_all_numbers(num_array: list[int]) -> str:
    """
    Concatenate all numbers in the list
    :param num_array:  The list of numbers
    :return:  The concatenated string
    """
    return ''.join(str(i) for i in num_array)


def generate_string_of_numbers(number_of_numbers: int = 5) -> str:
    """
    Generate a string of numbers
    :param number_of_numbers:  The number of numbers to generate
    :return:  The string of numbers
    """
    return concat_all_numbers(generate_numbers(number_of_numbers))

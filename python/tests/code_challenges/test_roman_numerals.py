import pytest
from code_challenges.roman_numerals import roman_to_arabic


def test_exists():
    assert roman_to_arabic


def test_number_1():
    val = roman_to_arabic("MCMLXXXIV")
    assert val == 1984


def test_number_2():
    val = roman_to_arabic("CXLII")
    assert val == 142

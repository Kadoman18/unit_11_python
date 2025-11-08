import pytest
from Lab11_kbreinholt1 import calculate_rotation

"""
        I know I probably should have created tests for the radians function
        but I added it last and had to move on to my other homework. Might
        add them later.
"""

def test_within_range() -> None:
        assert calculate_rotation("90") == 90
        assert calculate_rotation("180") == 180
        assert calculate_rotation("0") == 0

def test_equal_to_360() -> None:
        assert calculate_rotation("360") == 0

def test_above_360() -> None:
        assert calculate_rotation("450") == 90
        assert calculate_rotation("1080") == 0
        assert calculate_rotation("820") == 100
        assert calculate_rotation("720") == 0

def test_negative_values() -> None:
        assert calculate_rotation("-1") == 359
        assert calculate_rotation("-90") == 270
        assert calculate_rotation("-359") == 1
        assert calculate_rotation("-450") == 270

def test_large_numbers() -> None:
        assert calculate_rotation("1000000") == (1000000 % 360)
        assert calculate_rotation("-1000000") == (-1000000 % 360)


def test_whitespace_numbers() -> None:
        assert calculate_rotation("   45 ") == 45
        assert calculate_rotation("   -90   ") == 270

def test_invalid_input() -> None:
        assert calculate_rotation("abc") is None
        assert calculate_rotation("") is None
        assert calculate_rotation("   ") is None
        assert calculate_rotation(None) is None
        assert calculate_rotation(["90"]) is None
        assert calculate_rotation({"num": 90}) is None
        assert calculate_rotation(3 + 4j) is None


def test_float_strings_are_invalid() -> None:
        assert calculate_rotation("45.5") is None
        assert calculate_rotation("3.14") is None


def test_symbol_input() -> None:
        assert calculate_rotation("!") is None
        assert calculate_rotation("-") is None
        assert calculate_rotation("+") is None

def test_boolean_input() -> None:
        assert calculate_rotation(True) == 1
        assert calculate_rotation(False) == 0

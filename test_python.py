import pytest
import math

# Тесты для встроенной функции filter
def test_filter_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6]
    result = list(filter(lambda x: x % 2 == 0, numbers))
    assert result == [2, 4, 6]

def test_filter_non_empty_strings():
    strings = ["hello", "", "world", "", "python"]
    result = list(filter(lambda x: x, strings))
    assert result == ["hello", "world", "python"]

def test_filter_greater_than_five():
    numbers = [2, 3, 5, 6, 8, 10]
    result = list(filter(lambda x: x > 5, numbers))
    assert result == [6, 8, 10]

# Тесты для встроенной функции map
def test_map_square_numbers():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * x, numbers))
    assert result == [1, 4, 9, 16, 25]

def test_map_uppercase_strings():
    strings = ["hello", "world"]
    result = list(map(lambda x: x.upper(), strings))
    assert result == ["HELLO", "WORLD"]

def test_map_addition():
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]
    result = list(map(lambda x, y: x + y, numbers1, numbers2))
    assert result == [5, 7, 9]

# Тесты для встроенной функции sorted
def test_sorted_numbers():
    numbers = [4, 2, 9, 1, 5, 6]
    result = sorted(numbers)
    assert result == [1, 2, 4, 5, 6, 9]

def test_sorted_strings():
    strings = ["banana", "apple", "cherry"]
    result = sorted(strings)
    assert result == ["apple", "banana", "cherry"]

def test_sorted_by_length():
    strings = ["banana", "apple", "cherry"]
    result = sorted(strings, key=len)
    assert result == ["apple", "banana", "cherry"]

def test_sorted_reverse():
    numbers = [4, 2, 9, 1, 5, 6]
    result = sorted(numbers, reverse=True)
    assert result == [9, 6, 5, 4, 2, 1]

# Тесты для функций из библиотеки math
def test_math_pi():
    assert math.pi == 3.141592653589793

def test_math_sqrt():
    assert math.sqrt(4) == 2
    assert math.sqrt(9) == 3
    assert math.sqrt(0) == 0

def test_math_pow():
    assert math.pow(2, 3) == 8
    assert math.pow(5, 2) == 25
    assert math.pow(9, 0.5) == 3

def test_math_hypot():
    assert math.hypot(3, 4) == 5
    assert math.hypot(5, 12) == 13
    assert math.hypot(8, 15) == 17

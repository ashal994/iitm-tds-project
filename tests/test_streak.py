import pytest
from streak import longest_positive_streak

def test_empty():
    assert longest_positive_streak([]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 1, 1]) == 3

def test_multiple_streaks():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    assert longest_positive_streak([0, -1, 1, 2, -3, 4, 5, 6]) == 3

def test_single_negative():
    assert longest_positive_streak([-5]) == 0


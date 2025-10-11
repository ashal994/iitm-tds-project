import pytest
from streak import longest_positive_streak

@pytest.mark.parametrize("nums, expected", [
    ([], 0),
    ([1], 1),
    ([0], 0),
    ([-1], 0),
    ([1, 1, 1], 3),
    ([0, 0, 0], 0),
    ([-1, -2, -3], 0),
])
def test_basic_cases(nums, expected):
    assert longest_positive_streak(nums) == expected

def test_multiple_streaks_longest_wins():
    nums = [1, 2, 0, -1, 3, 4, 5, 6, 0]
    assert longest_positive_streak(nums) == 4

def test_zeros_and_negatives_break_streaks():
    nums = [2, 3, -1, 5, 6, 7, 0, 4]
    assert longest_positive_streak(nums) == 3

def test_streak_at_start_and_end():
    nums = [5, 6, 0, -1, 2, 3]
    assert longest_positive_streak(nums) == 2

def test_large_mixed_input():
    nums = [0, 1, 2, 3, 0, 1, 0, 1, 2, -1, 2, 2, 2, 2]
    assert longest_positive_streak(nums) == 4

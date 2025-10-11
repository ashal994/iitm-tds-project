# streak.py
from typing import List

def longest_positive_streak(nums: List[int]) -> int:
    """
    Return the length of the longest run of consecutive values strictly greater than 0.

    Rules:
    - Empty list -> 0
    - Non-positive numbers (0 or negatives) break the streak.
    - Deterministic and pure: no randomness, prints, or global state.
    """
    max_streak = 0
    current = 0

    for n in nums:
        if n > 0:
            current += 1
            if current > max_streak:
                max_streak = current
        else:
            current = 0

    return max_streak

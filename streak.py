def longest_positive_streak(nums: list[int]) -> int:
    max_streak = 0
    current_streak = 0
    for n in nums:
        if n > 0:
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            current_streak = 0
    return max_streak
# verification 04194491


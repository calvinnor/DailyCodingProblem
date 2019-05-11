# Problem

"""

Given an array of numbers, find the maximum sum of
any contiguous subarray of the array.

For example,
given the array [34, -50, 42, 14, -5, 86],
the maximum sum would be 137,
since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9],
the maximum sum would be 0,
since we would not take any elements.

Do this in O(N) time.

Asked by: Amazon

"""


# Code Section


def maximum_contiguous_sum(array: list) -> int:
    """
    We simply need to iterate over the array, maintaining the sum.

    Assuming that we have a huge negative entry in the middle, then we stop
    the sum. The total sum is updated.

    Once we get to the end of the array, we've found the maximum contiguous sum
    while ignoring the negative elements.
    """

    # Keeps the maximum sum
    max_contiguous_sum = 0

    # Keeps the sum of current chain
    chain_sum = 0

    for number in array:

        # If taking this value leads to a break, use 0 as minimum
        if chain_sum + number < 0:
            chain_sum = 0

        # Else add to the chain
        else:
            chain_sum += number

        # If our current sum exceeds the maximum contiguous sum
        if chain_sum > max_contiguous_sum:
            max_contiguous_sum = chain_sum

    return max_contiguous_sum


# Test Cases

# Example
assert maximum_contiguous_sum([34, -50, 42, 14, -5, 86]) == 137
assert maximum_contiguous_sum([-5, -1, -8, -9]) == 0

# Huge Negative Break
assert maximum_contiguous_sum([1, 2, 3, -100, 4, 5, 6]) == 15

# All Negative except edges
assert maximum_contiguous_sum([1, -90, -90, -90, -100, 1]) == 1

# Total Sum
assert maximum_contiguous_sum([1, 2, 3, 4, -4, 3, 2, 1]) == 12

# All Negatives
assert maximum_contiguous_sum([-1, -2, -3, -4, -5]) == 0

# Alternating Positives & Negatives of same value
assert maximum_contiguous_sum([1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 5

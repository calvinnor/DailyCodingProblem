# Problem

"""

Given an array of integers where every integer occurs
three times except for one integer, which only occurs once,
find and return the non-duplicated integer.

For example,

Given [6, 1, 3, 3, 3, 6, 6], return 1.
Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

Asked by: Google

"""


# Code Section

def find_unrepeated_number(integers: list) -> int:
    """
    This is essentially a math problem. We have a bunch of numbers in the array, and all of them
    except one is repeated thrice. To find this number, we can solve this as simultaneous equations

    Consider 'a', 'b', 'c' as repeated integers, and 'd' as the unrepeated one
    eg: Input array is [a, a, a, b, b, b, c, d, c, c]

    If we sum the input array, we'll get 3a + 3b + 3c + d --- [I]

    Now, if we find the unique integers in the array, assume that all integers are repeated and sum them,
    we get 3a + 3b + 3c + 3d --- [II]

    Subtracting [II] - [I] we get 2d. Just divide this by 2 to get the non-repeated integer
    """

    integers_sum = 0
    unique_integers = set()  # A set makes sure that only unique elements are added

    # Capture the sum of all numbers, as well as finding the unique numbers
    for number in integers:
        integers_sum += number
        unique_integers.add(number)

    # Calculate the ideal sum if all numbers were repeated thrice
    ideal_integers_sum = 0
    for number in unique_integers:
        ideal_integers_sum += number * 3

    # Find the difference in sums, which will give us 2 * unrepeated integer
    sum_difference = ideal_integers_sum - integers_sum

    # Finally, divide by 2 and return
    return int(sum_difference / 2)


# Test Cases

# Example
assert find_unrepeated_number([6, 1, 3, 3, 3, 6, 6]) == 1
assert find_unrepeated_number([13, 19, 13, 13]) == 19

# Unrepeated at start
assert find_unrepeated_number([1, 2, 2, 2, 3, 3, 3]) == 1

# Unrepeated at end
assert find_unrepeated_number([1, 1, 1, 2, 2, 2, 3]) == 3

# Sequence with number in between
assert find_unrepeated_number([1, 2, 3, 1, 2, 3, 4, 1, 2, 3]) == 4
assert find_unrepeated_number([1, 2, 3, 4, 1, 2, 3, 1, 2, 3]) == 4

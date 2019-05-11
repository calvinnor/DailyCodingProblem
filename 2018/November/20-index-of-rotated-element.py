# Problem

"""

An sorted array of integers was rotated an unknown number of times.

Given such an array,
find the index of the element in the array in faster than linear time.
If the element doesn't exist in the array, return null.

For example,
given the array [13, 18, 25, 2, 8, 10]
and the element 8,
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.

Asked by: Amazon

"""


# Code Section

def index_of_rotated_element(array: list, element: int) -> int:
    """
    Since the array is sorted, we can apply a modified version of
    Binary Search.

    Whenever we want to make a move left or right, we need to look
    at the left and right ends as well.

    When we encounter a move, as opposed to Binary Search, we first
    check if the Binary Search move is logical:

    1. If the element is smaller than our mid, move left only if the
       leftmost element is smaller than our element. Else move right.

    2. If the element is larger than our mid, move right only if the
       rightmost element is larger than our element. Else move left.

    """

    left_index = 0
    right_index = len(array) - 1

    while left_index != right_index:

        # Calculate the mid
        mid_index = (left_index + right_index) // 2
        mid_element = array[mid_index]

        # If we've found the element
        if mid_element == element:
            return mid_index

        # If the element is less than our mid
        if element < mid_element:

            # Modification to Binary Search, check the left end
            # to see if a left move is logical
            if array[left_index] <= element:
                right_index = mid_index

            # Rotation, go right
            else:
                left_index = mid_index + 1

        # Else it's greater than our mid
        else:

            # Modification to Binary Search, check the right end
            # to see if a right move is logical
            if array[right_index] >= element:
                left_index = mid_index + 1

            # Rotation, go left
            else:
                right_index = mid_index

    # Final check for equality when converged to a single element
    if array[left_index] == element:
        return left_index

    # Not found, return -1
    return -1


# Test Cases

# Example
assert index_of_rotated_element([13, 18, 25, 2, 8, 10], 8) == 4

# Sorted array
assert index_of_rotated_element([1, 2, 3, 4, 5], 4) == 3
assert index_of_rotated_element([1, 2, 3, 4, 5, 6], 2) == 1

# Rotated once
assert index_of_rotated_element([50, 10, 20, 30, 40, 50], 20) == 2
assert index_of_rotated_element([50, 10, 20, 30, 40], 20) == 2

# Rotated twice
assert index_of_rotated_element([50, 60, 10, 20, 30], 10) == 2
assert index_of_rotated_element([50, 60, 10, 20, 30, 40], 40) == 5

# Rotated N times, element on left of mid (opp of Binary Search)
assert index_of_rotated_element([40, 50, 60, 10, 20, 30, 32, 34], 50) == 1

# Rotated N times, element on right of mid (opp of Binary Search)
assert index_of_rotated_element([40, 50, 60, 70, 80, 10, 20], 10) == 5

# Not found
assert index_of_rotated_element([1, 2, 3, 4, 5], 6) == -1
assert index_of_rotated_element([10, 20, 30, 1, 2, 3, 4, 5], 6) == -1

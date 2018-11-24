# Problem

'''
Given an array of integers, find the first missing positive integer in 
linear time and constant space. In other words, find the lowest positive 
integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. 
The input [1, 2, 0] should give 3.

You can modify the input array in-place.

Asked by: Stripe
'''


# Code Section

def findMissingNumber(inputList):
    '''
    We'll use indexes to figure out the first missing positive integer.

    Since the array can contain zeroes and negative numbers, we'll need to filter
    out those entities first.

    Once the negatives and zeroes are at the start of the array, go over the
    positive integers and mark the value in the array index as negative, if not already.

    Then, starting at the positive location, find the first number index which is positive.
    That index will be the missing number.

    If we can't find any positive number, then the missing number is the largest number + 1 
    '''

    swapIndex = 0

    # Find the maximum element, before affecting the list
    maxElement = 0

    # Sort the negative and zeros in the input
    for index, number in enumerate(inputList):
        if number <= 0:
            # Python allows swapping elements like this
            inputList[swapIndex], inputList[index] = inputList[index], inputList[swapIndex]
            swapIndex += 1

        # Finding the maximum element in same loop
        if number > maxElement:
            maxElement = number

    # Sorted by negative & positive, find the first positive integer index
    positiveIndex = -1
    for index, number in enumerate(inputList):
        if number > 0:
            positiveIndex = index
            break

    # If no positive numbers exist, return 1
    if positiveIndex < 0:
        return 1

    # Start iterating over the positive numbers and mark their indexes
    for index, element in enumerate(inputList[positiveIndex:]):
        # Destination at which we should mark the element as present
        # -1 because we want to start positive integers from 1, not 0
        destinationIndex = positiveIndex + element - 1

        # If we can mark this index in list (not out of bounds) and that element is not marked
        if destinationIndex < len(inputList) and inputList[destinationIndex] > 0:
            inputList[destinationIndex] = -inputList[destinationIndex]

    # Iterate over the positive list and find the first positive index
    missingElement = -1
    for index, element in enumerate(inputList[positiveIndex:]):
        if element > 0:
            missingElement = index + 1  # Since we're beginning at 1
            break

    # If we found the missing element
    if missingElement != -1:
        return missingElement

    # We didn't find the element.
    # All positive numbers are present, just return the max element + 1
    return maxElement + 1


# Test Cases

assert findMissingNumber([3, 4, -1, 1]) == 2            # Example 1
assert findMissingNumber([1, 2, 0]) == 3                # Example 2
assert findMissingNumber([1, 2, 3, 4, 6]) == 5          # Normal case
assert findMissingNumber([6, 4, 3, 2, 1]) == 5          # Normal case reversed
assert findMissingNumber([-1, -2, -3, -4, -5]) == 1     # Negatives
assert findMissingNumber([2, 2, 3, -1, -1]) == 1        # Duplicate 1
assert findMissingNumber([1, 1, 2, 2, 3, 3]) == 4       # Duplicate 2
assert findMissingNumber([]) == 1                       # Empty array

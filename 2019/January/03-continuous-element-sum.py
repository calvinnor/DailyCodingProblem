# Problem

'''
Given a list of integers and a number K,
return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5]
and K is 9, then it should return [2, 3, 4].

Asked by: Lyft
'''


# Code Section

def contiguousSum(inputList, totalSum):
    """
    We can iterate over the list and figure out if some contiguous elements
    sum up to K.

    We store the start index, along with the total sum till iteration
    in a map.

    On each iteration, we check if the current element can add up to our
    previous sums to make K.
    If true, return all elements from that index.
    Else add this element (index, sum) to the map and continue.
    """

    # A dictionary to map startIndex -> currentSum
    sumMap = dict()

    # Iterating over each element
    for index, element in enumerate(inputList):

        # Creating a copy since Python does not allow modifications to iterable
        mapCopy = sumMap.copy()

        # Iterating over our currently formed contiguous elements
        for startIndex, currentSum in mapCopy.items():

            finalSum = currentSum + element

            # If we found a pair that satisfies the condition
            if finalSum == totalSum:
                return inputList[startIndex: index + 1]

            # If we exceeded our K, we should remove this group
            elif finalSum > totalSum:
                sumMap.pop(startIndex)

            # We're deficit of some number, add element to the total sum
            else:
                sumMap[startIndex] += element

        # Could not find such elements that add up to K in our current
        # contiguous elements.

        # Add this new element to the map
        sumMap[index] = element

    # Could not find a contiguous pair, return an empty list
    return []


# Test Cases

# Example
assert contiguousSum([1, 2, 3, 4, 5], 9) == [2, 3, 4]

# 2 elements
assert contiguousSum([1, 2, 3, 4, 5], 3) == [1, 2]

# Pair [2, 3] over single element [5] - FCFS
assert contiguousSum([1, 2, 3, 4, 5], 5) == [2, 3]

# Negative integers
assert contiguousSum([-1, 2, 3, 4, 5], 1) == [-1, 2]

# Whole list
assert contiguousSum([1, 2, 3, 4, 5], 15) == [1, 2, 3, 4, 5]

# Not present
assert contiguousSum([1, 2, 3, 4, 5], 8) == []

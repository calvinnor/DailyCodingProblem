# Problem

'''
Given a number represented by a list of digits,
find the next greater permutation of a number,
in terms of lexicographic ordering.

If there is not greater permutation possible,
return the permutation with the lowest value/ordering.

For example,
the list [1,2,3] should return [1,3,2].
The list [1,3,2] should return [2,1,3].
The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra
memory (disregarding the input memory)?

Asked by: Palantir
'''


# Code Section

def greaterPermutation(inputNumList):
    '''
    We can find a greater permutation by simply shifting a set of
    digits to the left.

    If all the digits are ordered in descending order, then no
    greater permutation exists, return the list in reverse.

    Else, we need to find the lowest index where numbers are ordered
    in ascending order, and switch them.
    '''

    isDescending = True
    previousElement = inputNumList[0]
    for element in inputNumList:
        if element > previousElement:
            isDescending = False
            break

        previousElement = element

    # If descending, the lowest element will be the reverse of this list
    if isDescending:
        return inputNumList[::-1]

    # Find the permutation that isn't ordered in descending
    lastElement = inputNumList[-1]
    removeIndex = -1
    for index, element in reversed(list(enumerate(inputNumList))):
        if element >= lastElement:
            continue

        # Pull out this element and add to the end
        removeIndex = index
        break

    # Remove the last element
    lastElement = inputNumList.pop(-1)

    # Add it to the found position
    inputNumList.insert(removeIndex, lastElement)

    return inputNumList


# Test Cases

print(greaterPermutation([1, 3, 2]))
assert greaterPermutation([1, 2, 3]) == [1, 3, 2]           # Example 1
assert greaterPermutation([1, 3, 2]) == [2, 1, 3]           # Example 2
assert greaterPermutation([3, 2, 1]) == [1, 2, 3]           # Example 3
assert greaterPermutation([0, 0, 0]) == [0, 0, 0]           # Zeros
assert greaterPermutation([1, 2, 0]) == [2, 0, 1]           # Wrap around
assert greaterPermutation([2, 0, 1]) == [2, 1, 0]           # Swap
assert greaterPermutation([5, 0, 0]) == [0, 0, 5]           # No greater permutation
assert greaterPermutation([5, 1, 2, 3]) == [5, 2, 1, 3]     # Four digit swap
assert greaterPermutation([5, 2, 1, 3]) == [5, 2, 3, 1]     # Four digit swap

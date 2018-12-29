# Problem

'''
Given a number in the form of a list of digits,
return all possible permutations.

For example, given [1,2,3],
return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

Asked by: Microsoft
'''


# Code Section

def findPermutations(inputList):
    '''
    We can find all permutations of a list by slicing it and
    performing recursion.

    For every element, find all permutations of the list without
    this element, then add the current element to available
    positions between the permutations.
    '''

    # Empty list
    if len(inputList) == 0:
        return []

    # Single element
    if len(inputList) == 1:
        return [inputList]

    # Find the permutations of the sublist, excluding the current element
    currentElement = inputList[0]
    sublistPermutations = findPermutations(inputList[1:])

    resultPermutations = []

    # For each sublist permutation
    for permutation in sublistPermutations:

        # For each position that we'd want to add our current element
        for position in range(0, len(permutation) + 1):

            # Make a copy of this permutation
            newPermutation = permutation.copy()

            # Append our element to a specific position
            newPermutation.insert(position, currentElement)

            # Add this new permutation to our result
            resultPermutations.append(newPermutation)

    return resultPermutations


# Test Cases

# We're sorting the assertions since our function can return permutations
# in any order

# Example
assert sorted(findPermutations([1, 2, 3])) == sorted([
    [1, 2, 3], [1, 3, 2],
    [2, 1, 3], [2, 3, 1],
    [3, 1, 2], [3, 2, 1]
])

# 2 elements
assert sorted(findPermutations([1, 2])) == sorted([[1, 2], [2, 1]])

# 4 elements
assert sorted(findPermutations([1, 2, 3, 4])) == sorted([
    [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2],
    [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1],
    [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1],
    [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1],
])

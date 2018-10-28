# Problem

'''
Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in the 
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output 
would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

Asked by: Uber
'''

# Code Section

def arrayProduct(inputNums):
    '''
    We're trying to achieve this in linear time, so we first iterate over
    all elements and calculate the product. We'll then divide the result
    by each number and return the list.

    Edge cases: 
    1. When our input array contains 0, we can't divide. In this case,
    the position of 0 would contain the product result, and other columns would be 0.
    2. If we find more than one 0 then our output would simply be all 0s.
    '''

    productResult = 1
    numOfZeros = 0

    for element in inputNums:
        if (element == 0):   # We found a zero, don't multiply!
            numOfZeros += 1

        else:
            productResult *= element

    # This list will contain just 0s.
    if numOfZeros >= 2:
        return [0] * len(inputNums)     # Python allows creation of a list filled with x

    # List contains less than two 0s.
    outputNums = []

    for element in inputNums:
        if element == 0:        # Don't divide by zero!
            outputNums.append(productResult)

        elif numOfZeros >= 1:   # Found a zero somewhere, so this product should be 0
            outputNums.append(0)

        else:                   # Divide by the element
            outputNums.append(productResult / element)

    return outputNums

def arrayProductWithoutDivision(inputNums):
    '''
    We're not allowed to use division, so there's nothing we can optimise
    besides number of zeros > 2.

    Fallback to O(n^2) algorithm, and this will take care of all cases
    without exceptions, since we are multiplying now, not division.
    '''

    # Optimisation, check if list contains more than one zero
    numOfZeros = 0

    for element in inputNums:
        if element == 0:
            numOfZeros += 1

    # This list will contain just 0s.
    if numOfZeros >= 2:
        return [0] * len(inputNums)     # Python allows creation of a list filled with x

    # Fall back to traditional O(n^2) product.
    outputNums = []

    for index1, _ in enumerate(inputNums):      # Python allows ignoring values with _. In this case, we're not interested in the iteration element
        productResult = 1
        for index2, element2 in enumerate(inputNums):
            if (index1 == index2):
                continue

            productResult *= element2

        outputNums.append(productResult)

    return outputNums


# Test Cases

## With Division

assert arrayProduct([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]           # Example 1
assert arrayProduct([3, 2, 1]) == [2, 3, 6]                             # Example 2
assert arrayProduct([1, 2, 3, 4, 0]) == [0, 0, 0, 0, 24]                # Single zero
assert arrayProduct([0, 0, 0]) == [0, 0, 0]                             # Multiple zeros
assert arrayProduct([0, -1, -2, -3, -4]) == [24, 0, 0, 0, 0]            # Negatives
assert arrayProduct([-1, 2, 3, 4]) == [24, -12, -8, -6]                 # Single Negative

## Without Division

assert arrayProductWithoutDivision([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]           # Example 1
assert arrayProductWithoutDivision([3, 2, 1]) == [2, 3, 6]                             # Example 2
assert arrayProductWithoutDivision([1, 2, 3, 4, 0]) == [0, 0, 0, 0, 24]                # Single zero
assert arrayProductWithoutDivision([0, 0, 0]) == [0, 0, 0]                             # Multiple zeros
assert arrayProductWithoutDivision([0, -1, -2, -3, -4]) == [24, 0, 0, 0, 0]            # Negatives
assert arrayProductWithoutDivision([-1, 2, 3, 4]) == [24, -12, -8, -6]                 # Single Negative

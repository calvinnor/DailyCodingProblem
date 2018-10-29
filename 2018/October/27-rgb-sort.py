# Problem

'''
Given an array of strictly the characters 'R', 'G', and 'B', segregate
the values of the array so that all the Rs come first, the Gs come second,
and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it
should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

Asked by: Google
'''

# Code Section

def sortRgb(inputArray):
    '''
    We will use a version of Counting Sort for this problem.
    This can be done in linear time and constant space.

    Since we know that the array will contain only 'R', 'G' and 'B', we can run
    counters for these elements, and then simply write over the existing array.
    '''

    colorCount = { 'R': 0, 'G': 0, 'B': 0 }

    for element in inputArray:
        colorCount[element] += 1

    # Writing over the array in-place
    writeIndex = 0

    # Write R
    redCount = colorCount['R']
    while redCount != 0:
        inputArray[writeIndex] = 'R'
        redCount -= 1
        writeIndex += 1

    # Write G
    greenCount = colorCount['G']
    while greenCount != 0:
        inputArray[writeIndex] = 'G'
        greenCount -= 1
        writeIndex += 1

    # Write B
    blueCount = colorCount['B']
    while blueCount != 0:
        inputArray[writeIndex] = 'B'
        blueCount -= 1
        writeIndex += 1

    return inputArray


# Test Cases

assert sortRgb(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']  # Example
assert sortRgb(['R', 'G', 'B']) == ['R', 'G', 'B']                                          # Sorted
assert sortRgb(['B', 'G', 'R']) == ['R', 'G', 'B']                                          # Reversed
assert sortRgb(['B', 'G', 'B', 'G', 'B']) == ['G', 'G', 'B', 'B', 'B']                      # No R's
assert sortRgb(['R', 'G', 'R', 'G', 'R']) == ['R', 'R', 'R', 'G', 'G']                      # No B's
assert sortRgb(['R', 'B', 'R', 'B', 'R']) == ['R', 'R', 'R', 'B', 'B']                      # No G's

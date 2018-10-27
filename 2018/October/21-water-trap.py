# Problem

'''
You are given an array of non-negative integers that represents a 
two-dimensional elevation map where each element is unit-width wall 
and the integer is the height. Suppose it will rain and all spots 
between two walls get filled up.

Compute how many units of water remain trapped on the map in 
O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of 
water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first 
index, 2 in the second, and 3 in the fourth index 
(we cannot hold 5 since it would run off to the left), so we can trap 
8 units of water.

Asked by: Facebook
'''

# Code Section

def getWaterTrapped(wallHeights):
    '''
    We will iterate over the heights, keeping the highest peak in memory.
    We are searching for raises (i.e. going from low to high)

    Once we find a raise, go backward till we reach the highest peak,
    filling up the water spaces.

    After filling the space, mark it as filled so that if we approach a
    higher peak later, we can re-fill the portion above height till the new peak.
    '''

    waterTrapped = 0
    tallestPeak = wallHeights[0]

    for index, height in enumerate(wallHeights):
        if (index == 0):
            continue

        if (height <= wallHeights[index - 1]): # Falling / stagnant edge
            continue

        amountToFill = min(height, tallestPeak) # Fill up depending on which is min at this point

        # Iterate backwards and fill up the spaces
        for index2, height2 in reversed(list(enumerate(wallHeights[0: index]))):

            if (height2 >= amountToFill): # We've reached the filled up portion
                break

            # We can fill some spaces, equal to the difference between current and peak
            waterTrapped += (amountToFill - height2)

            # Mark this entry as filled
            wallHeights[index2] = amountToFill

        # We've filled the hollow spaces, update the peak if necessary
        tallestPeak = max(tallestPeak, height)

    return waterTrapped


# Test Cases

assert getWaterTrapped([2, 1, 2]) == 1                              # Example 1
assert getWaterTrapped([3, 0, 1, 3, 0, 5]) == 8                     # Example 2
assert getWaterTrapped([1, 1, 1, 1, 1]) == 0                        # Plateau
assert getWaterTrapped([0, 1, 2, 3, 4, 5]) == 0                     # Left Leak
assert getWaterTrapped([1, 2, 3, 4, 5, 0]) == 0                     # Right Leak
assert getWaterTrapped([1, 0, 1, 0, 1]) == 2                        # Spaces in between
assert getWaterTrapped([1, 2, 3, 4, 3, 2, 1]) == 0                  # Pyramid
assert getWaterTrapped([5, 4, 3, 2, 1, 0, 1, 2, 3, 4]) == 16        # Valley
assert getWaterTrapped([3, 3, 3, 5, 3, 3, 3]) == 0                  # Pillar in between
assert getWaterTrapped([3, 3, 5, 3, 3, 4]) == 2                     # Pillar in between, fill only right container
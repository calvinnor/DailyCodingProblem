# Problem

'''
Given a list of numbers and a number k, return whether any two numbers
from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true 
since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Asked by: Google
'''


# Code Section

def doesAddUp(inputList, k):
    '''
    We will use a Set for fast {O(1)} lookups for the balance element.
    
    We'll iterate over the list and add each element to the Set.
    For each element, we check if {k - element} is present in the set.

    If we get to the end of the list, we know for sure that no 2 elements are
    present which add up to k.
    '''

    memorySet = set()

    for element in inputList:
        # If we have seen the element with difference before, we're done
        if (k - element in memorySet):
            return True

        # Not found, add to the Set and continue
        memorySet.add(element)

    # End of iteration, we don't have such a pair
    return False


# Test Cases

assert doesAddUp([10, 15, 3, 7], 17) == True                # True case
assert doesAddUp([10, 15, 3, 7], 16) == False               # False case
assert doesAddUp([-1, 11, 15, 14, 13], 10) == True          # Negative numbers
assert doesAddUp([0, 10, 9, 8, 7], 10) == True              # Zero case
assert doesAddUp([90, 80, 70, 60, 50, 40], -10) == False    # Negative result
assert doesAddUp([], 10) == False                           # Edge

# Problem

"""

There exists a staircase with N steps,
and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

- 1, 1, 1, 1
- 2, 1, 1
- 1, 2, 1
- 1, 1, 2
- 2, 2

What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

Asked by: Amazon

"""


# Code Section

def number_of_ways(choices: set, steps: int, memo: dict = None) -> int:
    """
    A Recursive Algorithm to choose one choice from the set
    of choices, that is less than the remaining steps.

    When our steps count gets to zero, this is counted as a valid
    permutation and we return it.

    Else, we keep finding such permutations.

    Use Memoization to remember unique ways for a given step size
    """

    if memo is None:
        memo = dict()

    # Base condition: If we've found a permutation, return it
    if steps == 0:
        return 1

    # Base condition: If we've overstepped our goal, return 0
    if steps < 0:
        return 0

    # Check if we've already computed this before
    if steps in memo:
        return memo[steps]

    # We still have steps to go. Find a permutation
    total_ways = 0

    # Pick a choice
    for choice in choices:

        # Given this choice, how many steps are remaining
        pending_steps = steps - choice

        # Compute the number of ways, given this choice
        total_ways += number_of_ways(choices, pending_steps, memo)

    # Add it to our Memoization
    memo[steps] = total_ways

    return total_ways


# Test Cases

# Example
assert number_of_ways(choices={1, 2}, steps=4) == 5

# Single choice
assert number_of_ways(choices={1}, steps=5) == 1

# Not possible
assert number_of_ways(choices={3}, steps=7) == 0

# Simple Examples
assert number_of_ways(choices={1}, steps=1) == 1
assert number_of_ways(choices={1}, steps=2) == 1
assert number_of_ways(choices={1, 2}, steps=2) == 2

# Complex Choices
assert number_of_ways(choices={1, 3, 5}, steps=5) == 5
assert number_of_ways(choices={1, 3, 5}, steps=10) == 47
assert number_of_ways(choices={1, 2, 3, 4, 5}, steps=50) == 256641310658978

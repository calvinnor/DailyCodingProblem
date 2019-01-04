# Problem

'''
Given an even number (greater than 2),
return two prime numbers whose sum will be equal to the given number.
A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4

If there are more than one solution possible,
return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.

Asked by: Alibaba
'''


# Code Section

# Utility function to check if a number is prime
def isPrime(inputNum):
    if inputNum == 2 or inputNum == 3:
        return True

    # Even numbers are not prime
    if inputNum % 2 == 0 or inputNum < 2:
        return False

    # Iterate from 3 till sqrt of input, in jumps of 2
    for i in range(3, int(inputNum ** 0.5) + 1, 2):
        if inputNum % i == 0:
            return False

    return True


def primePair(evenNumber):
    """
    We need to find a prime number which is less than the given even number.
    Then, we can check if the other half (evenNumber - prime) is also a prime.

    If true, we've found that pair, return it.
    Else, go on to find other primes and check the same.
    """

    if evenNumber < 4:
        raise Exception("Goldbach's Conjecture isn't valid for numbers below 4!")

    # Special check for 2 - so that we can optimise the next for loop
    otherCandidate = evenNumber - 2
    if isPrime(otherCandidate):
        return [2, otherCandidate]

    # Check all odd numbers - From 3 in steps of 2
    for candidate in range(3, evenNumber, 2):

        # Check if the candidate is a prime
        if not isPrime(candidate):
            continue

        # First candidate is prime - check the other half
        otherCandidate = evenNumber - candidate
        if not isPrime(otherCandidate):
            continue

        # Both are prime numbers
        return [candidate, otherCandidate]

    # Never satisfies, return None
    return None


# Test Cases

# Example
assert primePair(4) == [2, 2]

# More assertions
assert primePair(8) == [3, 5]
assert primePair(20) == [3, 17]
assert primePair(42) == [5, 37]
assert primePair(52) == [5, 47]
assert primePair(60) == [7, 53]

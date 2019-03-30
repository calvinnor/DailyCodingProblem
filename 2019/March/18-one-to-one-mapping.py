# Problem

"""

Determine whether there exists a one-to-one character mapping
from one string s1 to another s2.

For example,
given s1 = abc and s2 = bcd,
return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar,
return false since the o cannot map to two characters.

Asked by: Bloomberg

"""


# Code Section


def mapping_exists(first: str, second: str) -> bool:
    """
    We can use a Map to compare letters for both strings.
    When we find a letter from string A, add it to the HashMap
    as key = letter1, value = letter2.
    """

    # If the lengths don't match, return false
    if len(first) != len(second):
        return False

    letter_map = dict()

    # Iterating over the letters

    for index, letter in enumerate(first):

        second_letter = second[index]

        # If we've seen this letter, and the mapping on the RHS doesn't match
        if letter in letter_map and letter_map[letter] != second_letter:
            return False

        # Add the mapping to the Map
        letter_map[letter] = second_letter

    # We've iterated over the string successfully
    return True


# Test Cases

# Examples
assert mapping_exists("abc", "bcd")
assert not mapping_exists("foo", "bar")

# Empty Strings
assert mapping_exists("", "")

# Uneven Lengths
assert not mapping_exists("abcd", "efg")

# Recurring character on the right
assert mapping_exists("abcd", "ffff")

# Recurring alphabets
assert mapping_exists("abcdabcd", "efghefgh")

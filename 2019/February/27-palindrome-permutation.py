# Problem

"""

Given a string, determine whether any permutation of it is a palindrome.

For example,
carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
daily should return false, since there's no rearrangement that can form a palindrome.

Asked by: Amazon

"""


# Code Section

def is_permutation_palindrome(word: str) -> bool:
    """
    A palindrome is a word which, when read in reverse order, has the same spelling.

    Palindromes have a unique property. All letters in them appear exactly 'even' times
    When the string is of odd length, then only 1 character appears 'odd' times while others are 'even'

    Given any order of a permutation of a palindrome does not matter,
    since we can count the instances of each letter and add them to a Map.

    Once iterated, check the map for the above conditions to find if it's a Palindrome.
    """

    letter_map = dict()

    # Iterating over the letters to maintain their counts
    for letter in word:

        # If we've found the letter, add a count
        if letter in letter_map:
            letter_map[letter] += 1

        # Else add to the map and initialise to 1
        else:
            letter_map[letter] = 1

    is_even_length = len(word) % 2 == 0

    # In case of odd palindrome, one letter should be of odd count
    found_odd_length = False

    # Iterating over counts
    for letter, count in letter_map.items():

        # Even counts are allowed
        if count % 2 == 0:
            continue

        # We've found an odd count

        # If this is an even length string, we can't find a palindrome
        # with an odd count letter
        if is_even_length:
            return False

        # An odd length string, but we've already encountered a letter
        # having an odd count
        elif found_odd_length:
            return False

        else:
            found_odd_length = True

    # We've passed the iteration successfully
    return True


# Test Cases

# Examples
assert is_permutation_palindrome("carrace")  # racecar
assert not is_permutation_palindrome("daily")

# Simple Palindromes
assert is_permutation_palindrome("abcdefedcba")  # abcdefedcba
assert is_permutation_palindrome("abcdeffedcba")  # abcdeffedcba

# Non-Palindrome but permutations are Palindrome
assert is_permutation_palindrome("aabbccdd")  # abcddcba
assert is_permutation_palindrome("aabbbccdd")  # abcdbdcba
assert is_permutation_palindrome("abcabca")  # abcacba

# Non-Palindrome and permutations cannot be Palindrome
assert not is_permutation_palindrome("palindrome")
assert not is_permutation_palindrome("calvin")
assert not is_permutation_palindrome("abcabcabc")

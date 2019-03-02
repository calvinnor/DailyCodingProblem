# Problem

"""

Given a string, return the first recurring character in it,
or null if there is no recurring character.

For example,
Given the string "acbbac", return "b".
Given the string "abcdef", return null.

Asked by: Google

"""

# Code Section

from typing import Optional


def first_recurring_character(word: str) -> Optional[str]:
    """
    We can simply insert all the letters into a Set.

    Iterating over the word, we first check if the letter is present in the Set
    If yes, then this was seen more than once, return it
    Else, add it to the Set and keep moving

    We can simply return None if we get to the end of the word, since we
    haven't found a recurring character
    """

    letter_set = set()

    for letter in word:

        # If we've seen this letter before, return it
        if letter in letter_set:
            return letter

        # Add this to the map and move on
        letter_set.add(letter)

    # Not found, return None
    return None


# Test Cases

# Examples
assert first_recurring_character("acbbac") == 'b'
assert first_recurring_character("abcdef") is None

# Ends
assert first_recurring_character("fabcdef") == 'f'
assert first_recurring_character("ff") == 'f'

# Single Character & Empty String
assert first_recurring_character("f") is None
assert first_recurring_character("") is None

# Non Recurring
assert first_recurring_character("helowrd") is None
assert first_recurring_character("thequickbrown") is None

# Recurring in the middle & Palindrome
assert first_recurring_character("abcffed") == 'f'
assert first_recurring_character("abcdefedcba") == 'e'

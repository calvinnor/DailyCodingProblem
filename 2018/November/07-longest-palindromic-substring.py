# Problem

"""

Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example,
the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".

Asked by: Amazon

"""


# Code Section

def is_palindrome(input_str: str) -> bool:
    for index in range(len(input_str) // 2):

        # Checking the first with last - Python allows negative indexing
        if input_str[index] != input_str[-index - 1]:
            return False

    return True


def longest_palindromic_substring(input_str: str) -> str:
    """
    The longest palindromic substring begins with a letter in
    the string and can end at any location.

    We can run 2 loops to find the substrings of the input string,
    find if this is a palindrome, and then store the largest one.
    """

    longest_palindrome = ""

    for index, character in enumerate(input_str):

        # Keep track of the substrings we're checking
        current_substring = ""

        for index2 in range(index, len(input_str)):

            # Add the current letter to the substring
            current_substring += input_str[index2]

            # If our current substring is longer, and is a palindrome
            if len(current_substring) > len(longest_palindrome) and is_palindrome(current_substring):
                longest_palindrome = current_substring

    return longest_palindrome


# Test Cases

# Example
assert longest_palindromic_substring("aabcdcb") == "bcdcb"
assert longest_palindromic_substring("bananas") == "anana"

# No Palindrome - A single letter output
assert longest_palindromic_substring("abcdefg") == "a"
assert longest_palindromic_substring("xyz") == "x"

# Entire Palindromes
assert longest_palindromic_substring("abcdeffedcba") == "abcdeffedcba"
assert longest_palindromic_substring("abcdedcba") == "abcdedcba"
assert longest_palindromic_substring("racecar") == "racecar"

# Center Palindromes
assert longest_palindromic_substring("helloworld") == "owo"
assert longest_palindromic_substring("abcdefhehzzz") == "heh"
assert longest_palindromic_substring("abcdehellehzzz") == "helleh"

# Edge Cases
assert longest_palindromic_substring("") == ""

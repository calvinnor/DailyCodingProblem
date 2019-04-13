# Problem

"""

Given an integer k and a string s,
find the length of the longest substring that contains
at most k distinct characters.

For example,
given s = "abcba" and k = 2,
the longest substring with k distinct characters is "bcb".

Asked by: Amazon

"""


# Code Section

def length_of_substring(input: str, distinct_count: int) -> int:
    """
    We can iterate over the input string, while maintaining the distinct
    characters we see.

    Keep adding the character to the substring till we find that we've exhausted
    the distinct_count i.e. the length of characters in our memory > k.

    Once done, remember this length and move on to the next character.
    """

    longest_substring_count = 0

    for index, character in enumerate(input):

        # A map to keep track of distinct characters
        memory_map = set()

        # The string for counting the length
        local_longest_substring = ""

        # Iterate over the input to add them to the substring
        for char in input[index:]:

            # If this is not a seen character, and we've exhausted our unique characters
            if char not in memory_map and len(memory_map) == distinct_count:
                break

            # Add this character to the map, and the substring
            memory_map.add(char)
            local_longest_substring += char

            # Update the count of longest substring
            longest_substring_count = max(longest_substring_count, len(local_longest_substring))

    return longest_substring_count


# Test Cases

# Example
assert length_of_substring("abcba", 2) == 3

# Full length
assert length_of_substring("abcdefgh", 10) == 8

# Repeated characters
assert length_of_substring("aaaaaaaaaa", 1) == 10
assert length_of_substring("abcabcabcabc", 3) == 12

# In Between
assert length_of_substring("xyzababcabzyx", 3) == 7

# Clash of counts
assert length_of_substring("abcdefabcdefuvwxyzuvwxyz", 6) == 12

# At End
assert length_of_substring("helloworldabcabcabc", 3) == 9

# At Beginning
assert length_of_substring("abcabcabchelloworld", 3) == 9

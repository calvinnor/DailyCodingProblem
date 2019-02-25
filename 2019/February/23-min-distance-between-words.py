# Problem

"""

Find an efficient algorithm to find the smallest distance
(measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of
"dog cat hello cat dog dog hello cat world",
return 1 because there's only one word "cat" in between the two words.

"""

# Code Section

import sys


def distance_between(first_word: str, second_word: str, text_content: str) -> int:
    """
    We'll first split the text_content by space to get the list of all words.
    Then we check if the words we want are present in the first place. If not, return None.

    We now know that both words are present, store the indexes of them and when we find both words,
    calculate the absolute difference between their indices.
    Finally, return the minimum distance.
    """

    # Split by space
    text_words = text_content.split(' ')

    # If any of the words are not present
    if first_word not in text_words or second_word not in text_words:
        return -1

    # Initialise indices for tracking distances of words
    first_word_index = -1
    second_word_index = -1

    # Initialise distance to the maximum integer
    min_distance = sys.maxsize

    for index, word in enumerate(text_words):

        if first_word == word:
            first_word_index = index

        elif second_word == word:
            second_word_index = index

        else:
            continue

        # If we've found both words
        if first_word_index != -1 and second_word_index != -1:

            # Subtracting 1 because we don't consider the current word as distance
            min_distance = min(min_distance, abs(second_word_index - first_word_index) - 1)

    return min_distance


# Test Cases


# Example
assert distance_between("hello", "world", "dog cat hello cat dog dog hello cat world") == 1

# Second word appearing first
assert distance_between("hello", "world", "world abc def ghi hello") == 3

# Ends
assert distance_between("hello", "world", "hello dog cat dog cat dog cat world") == 6

# Repeated Words
assert distance_between("hello", "world", "hello world hello world hello world hello world") == 0

# Replaced by shorter distance
assert distance_between("hello", "world", "hello abc world hello") == 0

# Not replaced by longer distance
assert distance_between("hello", "world", "hello world hello abc def ghi jkl mno pqr world") == 0

# Cannot find distance
assert distance_between("hello", "world", "hello dog cat dog cat dog cat") == -1

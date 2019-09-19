# Problem

"""

You are given a string formed by concatenating several words
corresponding to the integers zero through nine and then anagramming.

For example,
the input could be 'niesevehrtfeev',
which is an anagram of 'threefiveseven'.

Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order.
In the example above, this would be 357.

Asked by: Slack

"""

# Code Section

from collections import OrderedDict


def get_letter_counts_dict(input_string: str) -> dict:
    letter_counts = dict()
    for letter in input_string:
        letter_counts[letter] = letter_counts[letter] + 1 if letter in letter_counts else 1

    return letter_counts


# Populate the decimal numbers map
# eg:
# {
#   1: "one",
#   4: "four",
#   9: "nine"
# }
decimal_numbers_map = OrderedDict()
decimal_numbers_map[0] = "zero"
decimal_numbers_map[1] = "one"
decimal_numbers_map[2] = "two"
decimal_numbers_map[3] = "three"
decimal_numbers_map[4] = "four"
decimal_numbers_map[5] = "five"
decimal_numbers_map[6] = "six"
decimal_numbers_map[7] = "seven"
decimal_numbers_map[8] = "eight"
decimal_numbers_map[9] = "nine"

# Populate the decimal letter counts
# eg:
# {
#   "one": { 'o': 1, 'n': '1', 'e': 1 },
#   "seven": { 's': 1, "e": 2, "v": 1, "n": 1 }
# }
decimal_numbers_letter_counts = OrderedDict()
for number_in_words in decimal_numbers_map.values():
    decimal_numbers_letter_counts[number_in_words] = get_letter_counts_dict(number_in_words)


def get_decoded_number(anagram: str) -> int:
    """
    We will first compute the occurrences of letters in all number words, stored in 'decimal_numbers_letter_counts'
    Then compute the letter occurrences in the anagram.

    We then try to find a decimal number, such that the number of letters required are less than the number of letters
    in the anagram i.e. this decimal number "exists" in the anagram.

    Once found, we decrement the number of letters required to form that number, and repeat the process of finding
    the next number.

    We stop once the number of letters in the anagram are zero i.e. we've found a set of numbers that can be
    decoded from this anagram.

    We then take this string and simply convert into a number. We don't need to do any post-sorting since we're
    iterating the decimal numbers in an OrderedDict
    """

    global decimal_numbers_map
    anagram_letter_counts = get_letter_counts_dict(anagram)

    # Sanity
    if not anagram_letter_counts:
        return -1

    decoded_number_string = get_decoded_number_string(anagram_letter_counts)
    decoded_number_solution = ""
    while True:
        if not decoded_number_string:
            break

        for number in decimal_numbers_map:
            number_in_words = decimal_numbers_map[number]
            if decoded_number_string.startswith(number_in_words):
                decoded_number_solution += str(number)
                decoded_number_string = decoded_number_string[len(number_in_words):]
                break

    return int(decoded_number_solution)


def get_decoded_number_string(anagram_letter_counts: dict) -> str:

    # If all the counts are zero, we've found a combination
    if all(anagram_letter_count == 0 for anagram_letter_count in anagram_letter_counts.values()):
        return ""

    # Search the numbers in the anagram, to find if we can satisfy some letter requirement
    for key_number_in_words in decimal_numbers_letter_counts:

        letter_counts = decimal_numbers_letter_counts[key_number_in_words]
        satisfied_letter_counts = True
        for key_letter in letter_counts:

            # We've not found the required letter
            if key_letter not in anagram_letter_counts:
                satisfied_letter_counts = False
                break

            # Check the number of required letters
            required_letter_count = letter_counts[key_letter]
            if anagram_letter_counts[key_letter] < required_letter_count:
                satisfied_letter_counts = False
                break

            # Satisfied this letter count, will decrement later

        if not satisfied_letter_counts:
            continue

        # Copy the map, decrement letter counts and recurse
        anagram_letter_counts_copy = anagram_letter_counts.copy()
        for key_letter in letter_counts:
            anagram_letter_counts_copy[key_letter] -= letter_counts[key_letter]

        recursive_solution = get_decoded_number_string(anagram_letter_counts_copy)
        if recursive_solution is not None:
            return key_number_in_words + recursive_solution

    return None


# Test Cases

# Example
assert get_decoded_number("niesevehrtfeev") == 357

# Single integers
assert get_decoded_number("eon") == 1
assert get_decoded_number("vefi") == 5
assert get_decoded_number("nnie") == 9

# Numbers are sorted
assert get_decoded_number("ninefiveone") == 159
assert get_decoded_number("fivefivefiveone") == 1555

# Multiple integers
assert get_decoded_number("eneforthoutwore") == 1234
assert get_decoded_number("ennuifieforoven") == 1459

# Repeated integers
assert get_decoded_number("eneeoneoneonono") == 11111
assert get_decoded_number("effefffivevivievivie") == 55555

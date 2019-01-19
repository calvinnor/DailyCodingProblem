# Problem

'''

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

Asked by: Facebook
'''

# Code Section

import string

# Create the dictionary for letters
letterKeys = dict()
for index, alphabet in enumerate(string.ascii_lowercase):
    letterKeys[index + 1] = alphabet


def waysToDecodeMessage(message, decodeCache = dict()):
    """
    We can use recursion to find the ways that we can decode the message.
    Assuming an input of 111, we can either decode it (a:1, k:11)
    aaa, ka, ak

    We found this because at each letter, we check if the combination of the
    current 2 letters make an alphabet.

    The total number of ways we can decode is the sum of decoding the rest of message
    considering the first digit, and decoding the rest of message considering the first 2 digits.

    We can further optimise the recursion by maintaining a Hash Table as cache, so we never have to
    recalculate the ways for a known input further down the recursion.
    """

    # Signify that a message is completely decoded, this is one way of decoding
    if not message:
        return 1

    waysToDecode = 0

    # If we've already computed this string before, return it
    if message in decodeCache:
        waysToDecode = decodeCache[message]

    else:
        # Pass the pending message to decode
        waysToDecode += waysToDecodeMessage(message[1:], decodeCache)

        # If we have a next letter, and can decode it to an alphabet ( < 26 )
        if len(message) > 1 and int(message[0:2]) in letterKeys:
            waysToDecode += waysToDecodeMessage(message[2:], decodeCache)

        # Save this value in cache, so that we don't have to decode again
        decodeCache[message] = waysToDecode

    return waysToDecode


# Test Cases

assert waysToDecodeMessage("111") == 3          # Example (aaa, ka, ak)
assert waysToDecodeMessage("21") == 2           # Single (ba, v)
assert waysToDecodeMessage("3112") == 3         # Multiple (caab, ckb, cal)
assert waysToDecodeMessage("13512") == 4        # Multiple (aceab, meab, acel, mel)
assert waysToDecodeMessage("9") == 1            # Single alphabet (i)

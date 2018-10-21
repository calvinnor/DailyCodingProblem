# Problem

'''
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a 
single count and character. For example, the string "AAAABBBCCDAA" 
would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string 
to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.

Asked by: Amazon
'''


# Code Section

def encode(input):
    '''
    When encoding a given string, iterate over the string and find repeated characters.
    When we encounter a change in characters, pick up the last character and append to output.
    Else, increment the counter and go on.

    After complete iteration, we are left with the last character (since we can't find a 'changed' state)
    For this, simply pick up the character and counter, and append to the output.
    '''

    encodedText = ""
    currentCharacter = ''
    currentCounter = 0

    for char in input:
        # Base case, we don't have a character to compare with
        if (currentCharacter == ''):
            currentCharacter = char
            currentCounter = 1
            continue

        # Repeated case, increment the counter
        if (currentCharacter == char):
            currentCounter += 1
            continue

        # Changed case, append to the output
        encodedText += str(currentCounter) + currentCharacter

        # Set variables to current
        currentCharacter = char
        currentCounter = 1

    # End of iteration, add the last character if exists
    if (currentCounter > 0):
        encodedText += str(currentCounter) + currentCharacter

    return encodedText

def decode(input):
    '''
    When decoding a given string, iterate over the string and search for numbers / characters.
    If we find a character, add it to the output as many times as the counter.
    Reset the counter to 1 as soon as we encounter a character.
    Set the counter when we come to a number.
    '''

    decodedText = ""
    charCount = ""

    for char in input:
        if (char.isdigit()):
            # We found a number, add it to our counter and continue
            charCount += char
            continue

        # We found a character, output as many times as the counter
        finalCount = 1 if not charCount else int(charCount)                 # Python treats empty strings as falsy. So "not string" is true if empty
        decodedText += char * finalCount                                    # Python prints A * 4 as "AAAA"

        # Reset the counter
        charCount = ""

    return decodedText


# Test Cases

## Encoding
assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"       # Example
assert encode("ABCD") == "1A1B1C1D"                 # Single Counters
assert encode("AAAAAAAAAAAAAAABCD") == "15A1B1C1D"  # Double digit Counter
assert encode("") == ""                             # Edge

## Decoding
assert decode("4A3B2C1D2A") == "AAAABBBCCDAA"       # Example
assert decode("1A1B1C1D") == "ABCD"                 # Single Counters
assert decode("15A1B1C1D") == "AAAAAAAAAAAAAAABCD"  # Double digit Counter
assert decode("") == ""                             # Edge

## Encoding + Decoding
assert "AAAABBBCCDAA" == decode(encode("AAAABBBCCDAA"))
assert "ABCD" == decode(encode("ABCD"))
assert "AAAAAAAAAAAAAAABCD" == decode(encode("AAAAAAAAAAAAAAABCD"))
assert "" == decode(encode(""))

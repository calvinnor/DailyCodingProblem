# Problem

'''
Implement a URL shortener with the following methods:

1. shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
2. restore(short), which expands the shortened string into the original url. 
   If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?

Asked by: Microsoft
'''

# Code Section

shortUrlLookup = dict()
fullUrlLookup = dict()

import string, random

# Utility function to generate a random shortened URL from the full.
def getShortenedUrl(fullUrl, size = 6):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))    

def shorten(fullUrl):
    '''
    We will use a random generator for shortening the URL.
    We'll also make use of a Hash Tables to store the full URL 
    vs the shortened version.

    If our Hash Table already contains the URL, then return the
    same shortened version.

    Optimisation: We want O(1) lookups, so we'll use 2 Hash Tables.
    One will hash against the short URL, other the long.
    '''

    # If we've already generated this before, return the same
    if fullUrl in shortUrlLookup:
        return shortUrlLookup[fullUrl]

    # New entry, generate
    shortenedUrl = getShortenedUrl(fullUrl)

    # Add to both HashTables for faster lookups
    shortUrlLookup[fullUrl] = shortenedUrl
    fullUrlLookup[shortenedUrl] = fullUrl
    
    return shortenedUrl

def restore(shortenedUrl):
    '''
    We just need to look up our shortened version.
    If not found, return None.
    '''
    
    # If we don't have this URL, return None
    if shortenedUrl not in fullUrlLookup:
        return None

    # We've found the URL. Pop entries and return it
    fullUrl = fullUrlLookup.pop(shortenedUrl)
    shortUrlLookup.pop(fullUrl)

    return fullUrl


# Test Cases

## 1. Testing the Random URL Generator
## For six-character URLs, the maximum permutations are 56,800,235,584

duplicateCount = 0
generatedSet = set()
for element in range(100000):
    generated = getShortenedUrl(element)
    if generated in generatedSet:
        duplicateCount += 1

    generatedSet.add(generated)

## Assert that our randomized algorithm succeeds most of the time
assert duplicateCount == 0

## 2. Testing the URL shortener + restore
## 2.1 Assert that we get the same URL back
assert restore(shorten("https://www.google.com")) == "https://www.google.com"

## 2.2 Assert that we get different shortened URLs for different URLs
assert shorten("https://www.google.com") != shorten("https://www.microsoft.com")

## 2.2 Assert that a different shortened version is not returned for duplicate URLs
assert shorten("https://www.google.com") == shorten("https://www.google.com")

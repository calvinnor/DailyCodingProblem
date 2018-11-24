# Problem

'''
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the 
first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.

Asked by: Jane Street
'''


# Given

def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


# Code Section

def extract(a, b):
    return (a, b)

def car(pair):
    '''
    Python function passing, nothing algorithmic about this problem.

    We'll pass an extractor function to pair, which returns a tuple.
    We can then use this tuple to pull out the first and second element.
    '''

    first, _ = pair(extract)
    return first

def cdr(pair):

    _, second = pair(extract)
    return second


# Test Cases

assert car(cons(3, 4)) == 3     # Example 1
assert cdr(cons(3, 4)) == 4     # Example 2
assert car(cons(1, 2)) == 1     # Simple
assert cdr(cons(1, 2)) == 2
assert car(cons(-1, -2)) == -1  # Negative
assert cdr(cons(-1, -2)) == -2
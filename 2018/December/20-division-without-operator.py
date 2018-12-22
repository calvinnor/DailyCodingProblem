# Problem

'''
Implement division of two positive integers without using the 
division, multiplication, or modulus operators. 

Return the quotient as an integer, ignoring the remainder.

Asked by: ContextLogic
'''

# Code Section

def performDivision(dividend, divisor):
    '''
    Division is simply the inversion of multiplication.

    For the given dividend & divisor, we loop and keep adding the
    divisor till we get the dividend.

    The number of times we can do this operation is the quotient.
    '''
    
    # Avoid Divison by zero or divided by zero
    if dividend is 0 or divisor is 0:
        return 0

    # Rules of Math: Quotient sign is based on dividend / divisor
    isDividendNegative = dividend < 0
    isDivisorNegative = divisor < 0

    # Optimisations for 1
    if divisor is 1:
        return dividend

    if divisor is -1:
        return abs(dividend) if isDividendNegative else -dividend

    # Actual Division: Keep adding divisor till we reach the dividend
    quotient = 0
    addedDivisor = 0
    absDividend, absDivisor = abs(dividend), abs(divisor)

    while (addedDivisor < absDividend):
        addedDivisor += absDivisor
        quotient += 1
    
    # If both signs are same, the quotient is positive (no change)
    # Else, need to reverse the sign
    if isDivisorNegative != isDividendNegative:
        quotient = -quotient 

    if addedDivisor is absDividend:
        return quotient
    
    else:
        return quotient - 1


# Test Cases

assert performDivision(dividend = 4, divisor = 2) == 2          # Simple case
assert performDivision(dividend = 4, divisor = 1) == 4          # Room for optimisation
assert performDivision(dividend = 10, divisor = 0) == 0         # Divide by zero
assert performDivision(dividend = 0, divisor = 100) == 0        # Dividend is zero
assert performDivision(dividend = -10, divisor = 2) == -5       # Negative dividend
assert performDivision(dividend = 20, divisor = -4) == -5       # Negative divisor
assert performDivision(dividend = 20, divisor = 3) == 6         # Remainder division
assert performDivision(dividend = 100, divisor = 5) == 20       # One more
assert performDivision(dividend = 100, divisor = -1) == -100    # Division by -1
assert performDivision(dividend = -100, divisor = -1) == 100    # Division by -1 with -ve dividend

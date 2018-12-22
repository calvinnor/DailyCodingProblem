# Problem

'''
Given a string of parentheses, write a function to compute the minimum number 
of parentheses to be removed to make the string valid 
(i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. 
Given the string ")(", you should return 2, since we must remove all of them.

Asked by: Google
'''

# Code Section

def countInvalidParenthesis(inputStr):
    '''
    We'll use a Stack for this problem.

    Iterating over the input, we'll check what the incoming character is.

    If we find an opening '(' then we simply push into the stack.
    Else if we find a closing ')' then we check the top of the stack.
        If the top contains a '(' then this parenthesis pair is complete, pop the top.
        Else, append this to the stack.

    The total elements (count) at the end in the stack is the number of mismatched elements.
    '''
    
    # Using a List as a Stack since it allows #append and #pop
    symbolStack = []

    for symbol in inputStr:
        
        if symbol is '(':
            symbolStack.append(symbol)
            continue

        elif symbol is ')':
            if not symbolStack:             # An empty list is falsy
                symbolStack.append(symbol)
                continue

            # List indexing: -1 is last element
            stackTop = symbolStack[-1]      

            # If we've found an opening parenthesis for this
            if stackTop is '(':
                symbolStack.pop()
                continue

            # No match, add to stack
            else:
                symbolStack.append(symbol)

        else:
            raise Exception("Invalid symbol:", symbol)

    return len(symbolStack)


# Test Cases

assert countInvalidParenthesis("()())()") == 1      # Example 1
assert countInvalidParenthesis(")(") == 2           # Example 2
assert countInvalidParenthesis("") == 0             # Empty case
assert countInvalidParenthesis("))))") == 4         # All closing parens
assert countInvalidParenthesis("((((") == 4         # All opening parens
assert countInvalidParenthesis("((((()))))") == 0   # Palindrome
assert countInvalidParenthesis("()()()()()") == 0   # Perfect open-close

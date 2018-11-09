# Problem

'''
You have an N by N board. Write a function that, given N, returns the 
number of possible arrangements of the board where N queens can be placed 
on the board without threatening each other, 
i.e. no two queens share the same row, column, or diagonal.

Asked by: Microsoft
'''


# Code Section

'''
Utility function to check if 2 queens attack each other
'''
def attacksEachOther(queen1, queen2):
    # If same row, same column, or if the slope = 1 i.e. dialonal to each other
    return queen1[0] == queen2[0] or queen1[1] == queen2[1] or abs(queen1[0] - queen2[0]) / abs(queen1[1] - queen2[1]) == 1

'''
Utility function to print the board
'''
def printBoard(queens, boardSize):
    for row in range(boardSize):
        for col in range(boardSize):
            if (row, col) in queens:
                print("[Q]", end = "")
            else:
                print("[ ]", end = "")

        print("")


def findSolution(boardSize, solutionCount = 0, currentQueens = []):
    '''
    Recursion + Backtracking seems like the best way to perform this.
    We'll store the queen positions as a tuple (x, y)
    Once we get to BOARD_SIZE queens, increment the solution count and return. Else, return current.

    In each iteration, try to add a queen to the existing set.
    If we can, clone the current solution, add the candidate and go on till we get to BOARD_SIZE queens.

    Optimisation: On each iteration, we try to add a new queen to the next row.
    If we can't add a queen here, we return solutionCount since we know that queens
    can attack each other in the same row. Hence each queen NEEDS to be in a different row.
    '''

    # We've found a solution
    if len(currentQueens) == boardSize:
        return solutionCount + 1

    # If we don't have queens, start at 0. Else, start at the next row of the last queen.
    startRow = 0 if not currentQueens else currentQueens[-1][0] + 1

    # Finding a position in columns where a newly placed queen won't attack the others
    for col in range(boardSize):
        candidateQueen = (startRow, col)
        isCandidateAttackingOther = False

        for queen in currentQueens:
            if attacksEachOther(queen, candidateQueen):
                isCandidateAttackingOther = True
                break

        # This queen is attacking some other queen, continue the search.
        if isCandidateAttackingOther:
            continue

        # The candidate is successful, add to the list of possible solution
        # Clone the existing list so we don't affect this call stack, we want to backtrack.
        newSolution = currentQueens.copy()
        newSolution.append(candidateQueen)

        # Call forward to see if we did find a solution
        solutionCount = findSolution(boardSize, solutionCount, newSolution)


    # We've reached the end of the row, we won't be able to find a solution
    return solutionCount


# Test Cases (See: https://en.wikipedia.org/wiki/Eight_queens_puzzle#Counting_solutions)

assert findSolution(boardSize = 5) == 10
assert findSolution(boardSize = 6) == 4
assert findSolution(boardSize = 7) == 40
assert findSolution(boardSize = 8) == 92
assert findSolution(boardSize = 9) == 352
assert findSolution(boardSize = 10) == 724
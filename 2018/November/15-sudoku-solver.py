# Problem

'''
Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. 
The objective is to fill the grid with the constraint that every row, column, 
and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.

Asked by: Dropbox
'''

# Code Section

N = 3 # denoting a 3 x 3 grid

# Utility method to get indexes of cells in a box.
def getCellsInBox(inputRow, inputCol):
    boxRow = inputRow // N     # Python allows Integer division using '//'
    boxCol = inputCol // N

    indexPairs = []
    startCol = boxCol * N
    startRow = boxRow * N
    for row in range(startRow, startRow + N):
        for col in range(startCol, startCol + N):
            indexPairs.append((row, col))

    return indexPairs

# Utility method to check if we can place a value in the given cell.
# We ideally follow Sudoku collision rules here.
def canPlaceInCell(board, cellRow, cellCol, candidateValue):
    
    # Check if this element is present in row
    for rowElement in board[cellRow]:
        if rowElement == candidateValue:
            return False
    
    # Check if this element is present in column
    for colElement in [row[cellCol] for row in board]:
        if colElement == candidateValue:
            return False

    # Check if this value is present in the given box
    for (row, col) in getCellsInBox(cellRow, cellCol):
        if board[row][col] == candidateValue:
            return False

    # We're done with the rules, we can insert this element
    return True

# Utility method to generate all possibilites for the given cell.
def possibilitiesForCell(board, cellRow, cellCol):
    possibilities = []
    for num in range(1, N * N + 1):
        if canPlaceInCell(board, cellRow, cellCol, num):
            possibilities.append(num)

    return possibilities

# Utility method to check if a board is complete
def isBoardComplete(board):
    for row in board:
        for col in row:
            if col == 0:
                return False

    return True

# Utility function to print out the board
def printBoard(board):
    for row in board:
        for col in row:
            print(col, end = " ")

        print()

def solveBoard(board):
    '''
    Sudoku can be solved using Backtracking.

    First, we'll iterate over the board to find a position where we need to
    insert a number from top-left.

    Once found, we find all the possibilities of this cell 
    i.e. numbers from 1-9 that do not exist in the block, row or column.

    Then we can add one of these to the board and recursively call the method
    with the new board.

    If we're able to find a solution i.e. all blocks are filled, we're done and
    we return the board as is.

    Else, we backtrack one step and try the next possibility for the cell.
    '''

    # Find the first empty cell
    emptyRow = emptyCol = -1
    for index1, row in enumerate(board):
        for index2, colElement in enumerate(row):
            if colElement == 0:
                emptyRow, emptyCol = index1, index2
                break

        if emptyRow != -1: # Break from outer for if found inner
            break

    if emptyRow == emptyCol and emptyCol == -1: # We can't find an empty position, the board is complete
        return board

    # Iterate over possibilities for given cell
    for possibility in possibilitiesForCell(board, emptyRow, emptyCol):

        # Make a copy of the board. We don't want to mutate the current board since
        # we need backtracking.
        newBoard = [row[:] for row in board]

        # Add the new possibility to the solution
        newBoard[emptyRow][emptyCol] = possibility

        # Recursively call the method
        newBoard = solveBoard(newBoard)

        # If we've completed the board in this iteration, return the solution
        if isBoardComplete(newBoard):
            return newBoard

        # Else, try the next possibility

    # We cannot solve the board, return as-is to try other possibilities
    return board


# Test Cases

board = [
    [0, 0, 0, 5, 0, 0, 3, 0, 0],
    [0, 7, 0, 0, 3, 2, 0, 0, 5],
    [0, 3, 0, 7, 6, 0, 0, 0, 9],
    [0, 0, 0, 4, 0, 7, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [2, 5, 0, 0, 0, 0, 9, 0, 7],
    [7, 2, 0, 3, 0, 9, 5, 0, 0],
    [8, 9, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 6]
]

solvedBoard = solveBoard(board)

# Assert that all cells are filled
assert isBoardComplete(solvedBoard)

# Assert that each row contains all the required numbers
allNumbers = [i for i in range(1, N * N + 1)]
for row in solvedBoard:
    assert sorted(row) == allNumbers

# Assert that each column contains all the required numbers
solvedBoardTranspose = [[solvedBoard[j][i] for j in range(len(solvedBoard))] for i in range(len(solvedBoard[0]))]
for col in solvedBoardTranspose:
    assert sorted(col) == allNumbers

# Assert that each box contains all the required numbers
for rowBox in range(N * N):
    for colBox in range(N * N):
        cellEntries = [solvedBoard[row][col] for (row, col) in getCellsInBox(rowBox, colBox)]
        assert sorted(cellEntries) == allNumbers

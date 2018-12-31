# Problem

'''
Given a 2D board of characters and a word,
find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

exists(board, "ABCCED") returns true,
exists(board, "SEE") returns true,
exists(board, "ABCB") returns false.

Asked by: Coursera
'''


# Code Section

# Recursive function to search a word in a board
def searchWord(board, wordToSearch, currentPath):

    # Utility function to check if the row, col has our word
    def recursivelyCallIfFound(letterToFind, candidateRow, candidateCol):

        # Check the bounds of the board
        if len(board) > candidateRow >= 0 and len(board[0]) > candidateCol >= 0:

            # Check if we can use this letter
            if board[candidateRow][candidateCol] is letterToFind and (candidateRow, candidateCol) not in currentPath:
                updatedWord = wordToSearch[1:]

                # Copy the path, append the current and recursively call
                updatedPath = currentPath.copy()
                updatedPath.append((candidateRow, candidateCol))

                if searchWord(board, updatedWord, updatedPath):
                    return True

    # No word, we've successfully found it
    if not wordToSearch:
        return True

    # We need to search the word, in the neighboring cells of the last path
    lastRow, lastCol = currentPath[-1]
    letterToSearch = wordToSearch[0]

    # Search all neighboring cells for the first letter of the word

    # 1. Check Left
    if recursivelyCallIfFound(letterToSearch, lastRow, lastCol - 1):
        return True

    # 2. Check Top
    if recursivelyCallIfFound(letterToSearch, lastRow - 1, lastCol):
        return True

    # 3. Check Right
    if recursivelyCallIfFound(letterToSearch, lastRow, lastCol + 1):
        return True

    # 4. Check Bottom
    if recursivelyCallIfFound(letterToSearch, lastRow + 1, lastCol):
        return True

    # Not found
    return False


def wordExists(board, wordToSearch):
    """
    We can recursively search for this word in the board.

    We begin by finding the first letter of the word on the board.
    Then, we can recursively search the location of the next letters
    and checking if any valid neighbors have it.

    We must keep track of the path so that we shouldn't return a success
    if we have a N letter word and use the same cell twice or more to achieve it.
    """

    # The board always contains empty word
    if not wordToSearch:
        return True

    letterToSearch = wordToSearch[0]

    for ind, row in enumerate(board):
        for ind2, letter in enumerate(row):
            if letter is letterToSearch:

                # Slice the rest of the word
                pendingWord = wordToSearch[1:]

                # Create a path, so that this letter isn't reused for a word
                currentPath = [(ind, ind2)]

                # If we've found the word through recursion, return True
                if searchWord(board, wordToSearch = pendingWord, currentPath = currentPath):
                    return True

                # Else, go on to find the next occurrence

    # We could not find the word
    return False


# Test Cases

# 1. Examples

wordBoard = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

assert wordExists(wordBoard, "ABCCED")
assert wordExists(wordBoard, "SEE")
assert not wordExists(wordBoard, "ABCB")

# 2. Additional assertions

assert wordExists(wordBoard, "ABCE")            # Same Row
assert wordExists(wordBoard, "ASA")             # Same Col
assert wordExists(wordBoard, "ABFCEE")          # Diagonal by row, col
assert not wordExists(wordBoard, "AFEE")        # No Diagonals
assert not wordExists(wordBoard, "SEEES")       # Should not re-use the E
assert not wordExists(wordBoard, "SEECS")       # Should not re-use the S
assert wordExists(wordBoard, "ABCESEEDAS")      # Round the board
assert wordExists(wordBoard, "")                # Edge case

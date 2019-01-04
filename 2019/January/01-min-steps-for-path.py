# Problem

'''
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to
cover the points. Give the minimum number of steps in which you can
achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1).
It takes one more step to move from (1, 1) to (1, 2).

Asked by: Google
'''


# Code Section

ROW = 0
COL = 1

# Utility method to check if 2 points are on the same diagonal (slope = 1)
def isDiagonal(point1, point2):
    return abs(point1[ROW] - point2[ROW]) / abs(point1[COL] - point2[COL]) == 1

def minSteps(pathPoints):
    """
    We must calculate the distance between the previous and next point,
    while maximising diagonal movements to reduce the number of steps.

    If the 2 points are on the same row, then we'll need the difference.
    If the 2 points are on the same column, we'll need the difference.
    Else, find which way we need to move diagonally to reach the point.

    Optimisation:
    Below, we've consider single steps for diagonal movements.
    We can make this faster by finding the point of intersection between the
    next point axis and current point diagonal.
    """

    totalSteps = 0
    nextIndex = 1
    currentPoint = pathPoints[nextIndex - 1]

    while nextIndex < len(pathPoints):

        nextPoint = pathPoints[nextIndex]

        # If both points are in the same row, add the column difference
        if currentPoint[ROW] == nextPoint[ROW]:
            totalSteps += abs(nextPoint[COL] - currentPoint[COL])
            currentPoint = nextPoint
            nextIndex += 1
            continue

        # If both points are in the same column, add the row difference
        if currentPoint[COL] == nextPoint[COL]:
            totalSteps += abs(nextPoint[ROW] - currentPoint[ROW])
            currentPoint = nextPoint
            nextIndex += 1
            continue

        # If both points are in the same diagonal, add any difference
        if isDiagonal(currentPoint, nextPoint):
            totalSteps += abs(nextPoint[ROW] - currentPoint[ROW])
            currentPoint = nextPoint
            nextIndex += 1
            continue

        # We need to move diagonally to the next point
        # Find out which direction we should move, looking at both points
        rowDelta = 1 if currentPoint[ROW] < nextPoint[ROW] else -1
        colDelta = 1 if currentPoint[COL] < nextPoint[COL] else -1

        # Move and add a step
        currentPoint = (currentPoint[ROW] + rowDelta, currentPoint[COL] + colDelta)
        totalSteps += 1

    return totalSteps


# Test Cases

# Example
assert minSteps([(0, 0), (1, 1), (1, 2)]) == 2

# Row and back
assert minSteps([(0, 50), (50, 50), (0, 50)]) == 100

# Column and back
assert minSteps([(50, 0), (50, 50), (50, 0)]) == 100

# Diagonal and back
assert minSteps([(100, 100), (0, 0), (100, 100)]) == 200

# Chess Horse piece - Front and back - Diagonal Optimisation
assert minSteps([(0, 0), (2, 1), (4, 2), (6, 3), (4, 2), (2, 1), (0, 0)]) == 12

# Negative movement
assert minSteps([(0, 0), (-100, -100), (0, 0)]) == 200

# Problem

"""

You are given an N by M matrix of 0s and 1s.
Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down.
0 represents an empty space while
1 represents a wall you cannot walk through.

For example, given the following matrix:
[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

Return two, as there are only two ways to get to the bottom right:
- Right, down, down, right
- Down, right, down, right

The top left corner and bottom right corner will always be 0.

Asked by: Slack

"""

# Code Section

X = 0
Y = 1

MOVE = 0
WALL = 1
STUCK = -1


# Utility function to check if we can move to the given position
def can_move(matrix: list, position: tuple) -> bool:
    within_x_bound = 0 <= position[Y] < len(matrix[0])
    within_y_bound = 0 <= position[X] < len(matrix)

    if not within_x_bound or not within_y_bound:
        return False

    # Checking if there's a wall here
    return matrix[position[X]][position[Y]] != WALL


def ways_to_bottom(matrix: list, current_position=(0, 0), memo_map=None) -> int:
    """
    We can define the number of ways to move using the following conditions:

    1. If we can move only to the right, no. of ways[x][y] = no. of ways[x+1][y]
    2. If we can move only down, no. of ways[x][y] = no. of ways[x][y+1]
    3. Else if we can move both directions, no. of ways[x][y] =
       additional_move + 1 + no. of ways[x+1][y] + no. of ways[x][y+1]

    We need to add 1 to the moves if we are beginning at initial position.

    We also have to worry about blockers. If we can't move in either direction, return -1
    so we can choose alternative routes

    This can be solved recursively, but we find repetitive computations for some cells
    We can use Memoization (memo_map) to remember our computation trees
    """

    # Initialise the Memoization map if not passed
    if memo_map is None:
        memo_map = dict()

    current_x = current_position[X]
    current_y = current_position[Y]

    # If we've reached the destination, return 0
    if current_x == len(matrix) - 1 and current_y == len(matrix[0]) - 1:
        return 0

    can_move_right = can_move(matrix, (current_x + 1, current_y))
    can_move_down = can_move(matrix, (current_x, current_y + 1))

    # We are stuck, return -1
    if not can_move_down and not can_move_right:
        return STUCK

    # We can move, check which direction is blocked or if both are available

    # Need to add 1 to denote a start move if at initial position
    ways_to_move = 1 if current_position == (0, 0) else 0

    # If we can't move down, simply check the right movement
    if not can_move_down:

        # Memoization
        next_move = (current_x + 1, current_y)
        if next_move not in memo_map:
            memo_map[next_move] = ways_to_bottom(matrix, next_move, memo_map)

        ways_to_move += memo_map[next_move]

    # If we can't move right, simply check the down movement
    elif not can_move_right:

        # Memoization
        next_move = (current_x, current_y + 1)
        if next_move not in memo_map:
            memo_map[next_move] = ways_to_bottom(matrix, next_move, memo_map)

        ways_to_move += memo_map[next_move]

    # Can move both ways, add 1 to the additional move and recursively call
    else:

        # Memoization
        next_move_1 = (current_x + 1, current_y)
        next_move_2 = (current_x, current_y + 1)

        if next_move_1 not in memo_map:
            memo_map[next_move_1] = ways_to_bottom(matrix, next_move_1, memo_map)

        if next_move_2 not in memo_map:
            memo_map[next_move_2] = ways_to_bottom(matrix, next_move_2, memo_map)

        ways_to_move += 1 + memo_map[next_move_1] + memo_map[next_move_2]

    return ways_to_move


# Test Cases

# Example
matrix = [
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0]
]
assert ways_to_bottom(matrix) == 2

# Simple lines, No walls
assert ways_to_bottom([[0, 0, 0, 0, 0]]) == 1
assert ways_to_bottom([[0], [0], [0], [0], [0]]) == 1

# Simple lines, Blocking walls,
assert ways_to_bottom([[0, 0, 1, 0, 0]]) == 0
assert ways_to_bottom([[0], [0], [1], [0], [0]]) == 0

# Matrix, No walls
matrix = [
    [0, 0, 0],
    [0, 0, 0]
]
assert ways_to_bottom(matrix) == 3

# Large Matrix, No walls
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
assert ways_to_bottom(matrix) == 6

# Large Matrix, centered walls
matrix = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]
assert ways_to_bottom(matrix) == 2

# Large Matrix, random walls
matrix = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0]
]
assert ways_to_bottom(matrix) == 3

# Matrix, Blocking walls
matrix = [
    [0, 0, 0],
    [0, 1, 1],
    [0, 1, 0]
]
assert ways_to_bottom(matrix) == 0

# Large Matrix, single path
matrix = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0]
]
assert ways_to_bottom(matrix) == 1

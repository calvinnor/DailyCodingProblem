# Problem

"""

Given a 2-D matrix representing an image, a location of a pixel in the screen
and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B

Becomes

B B G
G G G
G G G
B B B

"""


# Code Section


def flood_fill(image_matrix: list, location: tuple, new_color: str, old_color: str = "") -> list:
    """
    This is essentially a flood-fill algorithm.

    We first fill the given location with the new color and then recursively call around the
    neighboring cells for filling. If we find that the neighboring cell is not the same color, we stop.

    We keep doing this till we have filled the old_color with new_color
    """

    # Utility function to call the method recursively if old color in the new location
    def call_recursive_on_same_color(new_location: tuple):
        new_x, new_y = new_location

        # Checking for X boundary
        if new_x < 0 or new_x >= len(image_matrix):
            return

        # Checking for Y boundary
        if new_y < 0 or new_y >= len(image_matrix[0]):
            return

        # Checking if old_color is in the given cell
        if image_matrix[new_x][new_y] == old_color:
            flood_fill(image_matrix, new_location, new_color, old_color)

    location_x, location_y = location

    # If we don't have an old color, use the location
    if not old_color:
        old_color = image_matrix[location_x][location_y]

    # Replace the color with the new one
    image_matrix[location_x][location_y] = new_color

    # Recursively call on neighboring pixels
    call_recursive_on_same_color((location_x - 1, location_y))  # Left
    call_recursive_on_same_color((location_x, location_y - 1))  # Top
    call_recursive_on_same_color((location_x + 1, location_y))  # Right
    call_recursive_on_same_color((location_x, location_y + 1))  # Down

    # Recursively call on diagonal adjacents
    call_recursive_on_same_color((location_x - 1, location_y + 1))  # Bottom Left
    call_recursive_on_same_color((location_x + 1, location_y + 1))  # Bottom Right
    call_recursive_on_same_color((location_x - 1, location_y - 1))  # Top Left
    call_recursive_on_same_color((location_x + 1, location_y - 1))  # Top Right

    return image_matrix


# Test Cases

# 1. Example

initial_image = [
    ['B', 'B', 'W'],
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['B', 'B', 'B']
]

final_image = flood_fill(image_matrix=initial_image, location=(2, 2), new_color='G')

# Check that our 'B' pixels are intact
assert final_image[0][0] == 'B' and final_image[0][1] == 'B' and 'G' not in final_image[3]

# Check that our 'W' pixels are replaced with 'G' ones
assert final_image[0][2] == 'G' and final_image[1][0] == 'G' and len(set(final_image[1])) == 1 \
       and final_image[2][0] == 'G' and len(set(final_image[2])) == 1


# 2. No Flood

initial_image = [
    ['B', 'B', 'B'],
    ['B', 'W', 'B'],
    ['B', 'B', 'B'],
]

final_image = flood_fill(image_matrix=initial_image, location=(1, 1), new_color='G')

# Check that our 'B' pixels are intact
assert final_image[0][0] == 'B' and len(set(final_image[0])) == 1 and final_image[1][0] == 'B' and final_image[1][
    2] == 'B' and final_image[2][0] == 'B' and len(set(final_image[2])) == 1

# Check that our 'W' pixels are replaced with 'G' ones
assert final_image[1][1] == 'G'

# Problem

'''

Given an array of time intervals (start, end)
for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

Asked by: Snapchat
'''


# Code Section

START = 0
END = 1

def minRoomsRequired(intervals):
    """
    We can maintain a zero array and store 1 for each lecture from
    range (start) to (end)
    If another lecture is scheduled somewhere in between, we simply increment
    the counter in that interval.

    However, we don't need to actually store the number of classrooms for each
    interval, we just need the increment / decrement intervals.

    We can then iterate over this array and figure out the max number of required
    classrooms from looking at the interval changes.
    """

    # Find the minimum and maximum values in the intervals
    minValue = min(0, min([interval[START] for interval in intervals]))
    maxValue = max([interval[END] for interval in intervals])

    # Python allows creation of a zero array of size (max - min)
    # +1 for zero indexing
    intervalArray = [0] * (maxValue - minValue + 1)

    # Record the intervals in the intervalArray
    for interval in intervals:

        # Increment number of classrooms for a lecture start
        intervalArray[interval[START]] += 1

        # Decrement number of classrooms for a lecture end
        intervalArray[interval[END]] -= 1

    # Iterate over the array to find the largest number
    maxClassroomsNeeded = 0
    currentClassrooms = 0
    for interval in intervalArray:

        # Add the interval to the current requirement
        currentClassrooms += interval

        # If we found a larger requirement at time
        if currentClassrooms > maxClassroomsNeeded:
            maxClassroomsNeeded = currentClassrooms

    return maxClassroomsNeeded

# Test Cases


# Example
assert minRoomsRequired([(30, 75), (0, 50), (60, 150)]) == 2

# Distinct lectures, single classroom
assert minRoomsRequired([(0, 10), (10, 20), (20, 30)]) == 1

# All lectures at the same time
assert minRoomsRequired([(1, 50), (2, 50), (3, 50), (4, 55)]) == 4

# Reusing classes
assert minRoomsRequired([(1, 50), (55, 70), (10, 40), (41, 50)]) == 2

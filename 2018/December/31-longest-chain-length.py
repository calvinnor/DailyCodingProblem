# Problem

'''
Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2],
the longest consecutive element sequence is [1, 2, 3, 4].
Return its length: 4.

Your algorithm should run in O(n) complexity.

Asked by: Microsoft
'''


# Code Section

# Represents a Node of a Doubly Linked List
class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Utility function to connect nodes into a LinkedList
def connectNodes(leftNode, rightNode):
    leftNode.right = rightNode
    rightNode.left = leftNode


def longestChainLength(inputList):
    """
    We'll use a Hash Table with a Doubly Linked List for this problem.

    Our goal is to connect elements in the map via a LinkedList.
    On adding an element X to the map, check if it's consecutive elements
    (X - 1) and (X + 1) exist in the map.
    If found, connect these elements.

    This algorithm is now O(n^2) because we'll have the chains
    in the Hash Map, but we'll also need to iterate the sub-chains,
    since we'll be iterating over the hash table entries.
    So, we only keep the ends of the chains in the Map.

    Once we have this, iterate over our generated chains and find the longest one.
    """

    hashTable = dict()

    for element in inputList:

        elementNode = Node(val=element)

        leftElement = element - 1
        rightElement = element + 1

        # Try to pull out the elements from the hash table
        leftElementFromTable = hashTable.get(leftElement) if leftElement in hashTable else None
        rightElementFromTable = hashTable.get(rightElement) if rightElement in hashTable else None

        hasLeftSequence = leftElementFromTable is not None
        hasRightSequence = rightElementFromTable is not None

        # Connect to left node if exists
        if hasLeftSequence:
            connectNodes(leftElementFromTable, elementNode)

        # Connect to right node if exists
        if hasRightSequence:
            connectNodes(elementNode, rightElementFromTable)

        # Since we want to keep only the end nodes in the table, we check the neighbors

        # Does not have a neighbor on one side, this is an end node
        if not hasLeftSequence or not hasRightSequence:
            hashTable[element] = elementNode

        # If we have a left neighbor, check if that neighbor has a left neighbor
        if hasLeftSequence:
            if leftElementFromTable.left is not None:
                # Pop the left neighbor from the table - we're connecting a left and right chain
                hashTable.pop(leftElement)

        # If we have a right neighbor, check if that neighbor has a right neighbor
        if hasRightSequence:
            if rightElementFromTable.right is not None:
                # Pop the right neighbor from the table - we're connecting a right and left chain
                hashTable.pop(rightElement)

    # All our elements are in the hash table, connected with chains
    # Iterate over the chains and find the longest one

    longChainLength = 0

    for element, elementNode in hashTable.items():
        currentNode = elementNode
        currentChainLength = 1
        while currentNode.right is not None:
            currentChainLength += 1
            currentNode = currentNode.right

        if currentChainLength > longChainLength:
            longChainLength = currentChainLength

    return longChainLength


# Test Cases

# Example
assert longestChainLength([100, 4, 200, 1, 3, 2]) == 4

# Complete chain
assert longestChainLength([1, 2, 3, 4, 5]) == 5

# Single length chain
assert longestChainLength([1, 3, 5, 7]) == 1

# Negative numbers
assert longestChainLength([-1, 5, 4, 0, 2, 3, 1]) == 7

# Descending order
assert longestChainLength([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 11

# Competing chains
assert longestChainLength([1, 3, 5, 4, 2, 10, 13, 12, 11]) == 5

# Same length chains
assert longestChainLength([1, 3, 4, 2, 5, 10, 12, 11, 15, 14]) == 5

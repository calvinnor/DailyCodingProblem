# Problem

'''

Given a binary tree, return all paths from the root to leaves.

For example, given the tree

    1
   / \
  2   3
     / \
    4   5

it should return [[1, 2], [1, 3, 4], [1, 3, 5]].

Asked by: Facebook
'''


# Code Section

# Class for storing a Binary Tree node (with left and right children)
class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Utility method to check if a list is nested
def isNestedList(inputList):
    return any(isinstance(i, list) for i in inputList)


def getAllPaths(rootNode):
    """
    We'll use a Depth-first traversal for this problem.

    At each node, append self and recursively call the children.
    If we have no children, this is a leaf node, so just return self.

    Each recursion will return a list of paths.
    """

    # Sanity check
    if rootNode is None:
        return None

    # Leaf condition
    if rootNode.left is None and rootNode.right is None:
        return [rootNode.val]

    # We have children, get their paths
    totalPaths = []

    if rootNode.left is not None:
        leftPaths = getAllPaths(rootNode.left)

        # If this list is already nested, we just need to add self to each
        if isNestedList(leftPaths):
            for path in leftPaths:
                path.insert(0, rootNode.val)

            # Append all of these to the final solution
            totalPaths += leftPaths

        else:
            # Create a list for them
            totalPaths.append([rootNode.val] + leftPaths)

    if rootNode.right is not None:
        rightPaths = getAllPaths(rootNode.right)

        # If this list is already nested, we just need to add self to each
        if isNestedList(rightPaths):
            for path in rightPaths:
                path.insert(0, rootNode.val)

            # Append all of these to the final solution
            totalPaths += rightPaths

        else:
            # Create a list for them
            totalPaths.append([rootNode.val] + rightPaths)

    return totalPaths


# Test Cases


# Example
rootNode = Node(val=1, left=Node(2), right=Node(3, left=Node(4), right=Node(5)))
assert getAllPaths(rootNode) == [[1, 2], [1, 3, 4], [1, 3, 5]]

# Simple example
rootNode = Node(val=10, left=Node(20), right=Node(30))
assert getAllPaths(rootNode) == [[10, 20], [10, 30]]

# Left Tree
rootNode = Node(val=10, left=Node(9, left=Node(8, left=Node(7))))
assert getAllPaths(rootNode) == [[10, 9, 8, 7]]

# Right Tree
rootNode = Node(val=10, right=Node(9, right=Node(8, right=Node(7))))
assert getAllPaths(rootNode) == [[10, 9, 8, 7]]

# Zigzag Binary Tree
rootNode = Node(20, left=Node(10, right=Node(15, left=Node(8))))
assert getAllPaths(rootNode) == [[20, 10, 15, 8]]

# Complete Tree
rootNode = Node(20, left=Node(10, left=Node(5), right=Node(15)), right=Node(30, left=Node(25), right=Node(35)))
assert getAllPaths(rootNode) == [[20, 10, 5], [20, 10, 15], [20, 30, 25], [20, 30, 35]]

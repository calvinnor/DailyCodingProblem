# Problem

'''
Given the root to a binary search tree, 
find the second largest node in the tree.

Asked by: Dropbox
'''

# Code Section

class Node:
    def __init__(self, val, left = None, right =None):
        self.val = val
        self.left = left
        self.right = right

def findSecondLargest(rootNode):
    '''
    Since this is a Binary Search Tree, the largest element will be the right-most
    element of the tree i.e. a node after going right, that doesn't have a right child.

    The second-largest can be found depending on 3 conditions:
    1. If the root does not have a right child, the right-most element of the left child is second-largest
    2. If the right-most element has a left child, that is the second-largest.
    3. If the right-most has no children, the root of it is the second-largest.

    We return the second-largest node object for convenience.
    '''

    parentNode = rootNode
    rightTraversal = parentNode.right
    rootHasRightChild = True

    if parentNode.right is None:
        rootHasRightChild = False
        rightTraversal = parentNode.left

    # Keep going right until we can't
    while rightTraversal is not None and rightTraversal.right is not None:
        parentNode = rightTraversal
        rightTraversal = rightTraversal.right

    # Condition 1
    if rootHasRightChild is False:
        return rightTraversal

    # Condition 2
    if rightTraversal.left is not None:
        return rightTraversal.left

    # Condition 3 is already satisfied at this point, return parent
    return parentNode

'''
Utility function to create a binary tree
'''
def buildBst(rootNode, newData):
    if rootNode is None:
        return Node(newData)

    # We have a node, check if this should be the left or right child
    if newData <= rootNode.val:
        rootNode.left = buildBst(rootNode.left, newData)

    else:
        rootNode.right = buildBst(rootNode.right, newData)

    return rootNode

'''
Utility function to build a BST from list items
'''
def buildBstFromList(dataItems):
    rootNode = buildBst(None, dataItems[0])
    for data in dataItems[1:]:
        buildBst(rootNode, data)

    return rootNode


# Test Cases

## Simple Case
rootNode = buildBstFromList([2, 1, 3])
assert findSecondLargest(rootNode).val == 2

## Left Case
rootNode = buildBstFromList([4, 3, 2, 1])
assert findSecondLargest(rootNode).val == 3

## Right Case
rootNode = buildBstFromList([1, 2, 3, 4])
assert findSecondLargest(rootNode).val == 3

## Left Right Case
rootNode = buildBstFromList([4, 2, 1, 3])
assert findSecondLargest(rootNode).val == 3

## Example
rootNode = buildBstFromList([8, 10, 3, 1, 6, 13, 7, 4, 14])
assert findSecondLargest(rootNode).val == 13

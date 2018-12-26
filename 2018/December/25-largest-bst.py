# Problem

'''
Given a tree, find the largest tree/subtree that is a BST.
Given a tree, return the size of the largest tree/subtree that is a BST.

Asked by: Apple
'''

# Code Section

# Class for storing a BST node (with left and right children)
class Node:
    def __init__(self, val, left = None, right =None):
        self.val = val
        self.left = left
        self.right = right

# Utility method to get the Inorder of a tree
def getInorderElements(rootNode):
    
    if rootNode is None:
        return []

    leftElements = getInorderElements(rootNode.left)
    rightElements = getInorderElements(rootNode.right)

    # Inorder: Left, Root, Right
    leftElements.append(rootNode.val)
    return leftElements + rightElements

def checkValidityAndReturnSize(rootNode):
    '''
    A valid BST is one that satisfies the following conditions:
    1. Contains at most 2 children
    2. The root data must be greater than or equal to it's left children (including grand)
    3. The root data must be less than it's right children (including grand)

    A valid BST has a simple property that it's Inorder produces elements in ascending order.
    We can take the Inorder and validate the BST.

    We simply return the size of this BST if valid, else 0. 
    '''
    
    inorderElements = getInorderElements(rootNode)
    
    # Empty trees are BSTs
    if not inorderElements:
        return 0

    # Comparing each element with the previous
    lastElement = inorderElements[0]
    for element in inorderElements:

        # If an element is smaller than the previous - invalid
        if element < lastElement:
            return 0

        lastElement = element

    # All elements in ascending order
    return len(inorderElements)

def lengthOfLargestBst(rootNode):
    '''
    For this problem, we need to traverse the tree breadth-first.

    For each node, check if it forms a BST with it's child subtrees.
    If yes, then this is the largest BST, return it.
    Else, get the max size of the largest BST of left & right child and return.
    '''

    if rootNode is None:
        return 0

    bstFromRoot = checkValidityAndReturnSize(rootNode)
    if bstFromRoot > 0:
        # This entire tree is a BST
        return bstFromRoot

    # Find the max from left & right subtrees
    return max(lengthOfLargestBst(rootNode.left), lengthOfLargestBst(rootNode.right))


# Test Cases

# 1 Valid BST
rootNode = Node(val = 10, left = Node(10), right = Node(20))
assert lengthOfLargestBst(rootNode) == 3

# 2 Invalid BST
rootNode = Node(val = 10, left = Node(20), right = Node(10))
assert lengthOfLargestBst(rootNode) == 1

# 3 Left BST
rootNode = Node(val = 10, left = Node(9, left = Node(8, left = Node(7))))
assert lengthOfLargestBst(rootNode) == 4

# 4 Right invalid BST
rootNode = Node(val = 10, right = Node(9, right = Node(8, right = Node(7))))
assert lengthOfLargestBst(rootNode) == 1

# 4 Right BST
rootNode = Node(val = 10, right = Node(11, right = Node(12, right = Node(20))))
assert lengthOfLargestBst(rootNode) == 4

# 5 Zigzag BST (Edge Case: Cannot have 8 as left of 15 since it's a right grandchild of 10)
rootNode = Node(20, left = Node(10, right = Node(15, left = Node(8))))
assert lengthOfLargestBst(rootNode)

# 6 Empty condition
rootNode = None
assert lengthOfLargestBst(rootNode) == 0

# 7 BST Nested - Invalid root BST, but contains a BST within children
rootNode = Node(val = 20, left = Node(val = 30, left = Node(15), right = Node(35)), right = Node(15))
assert lengthOfLargestBst(rootNode) == 3

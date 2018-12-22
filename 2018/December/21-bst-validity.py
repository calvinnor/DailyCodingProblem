# Problem

'''
Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, 
and satisfies the constraint that
the key in the left child must be less than or equal to the root 
and the key in the right child must be greater than or equal to the root.

Asked by: LinkedIn
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


def isValidBst(rootNode):
    '''
    A valid BST is one that satisfies the following conditions:
    1. Contains at most 2 children
    2. The root data must be greater than or equal to it's left children (including grand)
    3. The root data must be less than it's right children (including grand)

    A valid BST has a simple property that it's Inorder produces elements in ascending order.
    We can take the Inorder and validate the BST.
    '''
    
    inorderElements = getInorderElements(rootNode)
    
    # Empty trees are BSTs
    if not inorderElements:
        return True

    # Comparing each element with the previous
    lastElement = inorderElements[0]
    for element in inorderElements:

        # If an element is smaller than the previous - invalid
        if element < lastElement:
            return False

        lastElement = element

    # All elements in ascending order
    return True


# Test Cases

# 1 Valid BST
rootNode = Node(val = 10, left = Node(10), right = Node(20))
assert isValidBst(rootNode)

# 2 Invalid BST
rootNode = Node(val = 10, left = Node(20), right = Node(10))
assert not isValidBst(rootNode)

# 3 Left BST
rootNode = Node(val = 10, left = Node(9, left = Node(8, left = Node(7))))
assert isValidBst(rootNode)

# 4 Right invalid BST
rootNode = Node(val = 10, right = Node(9, right = Node(8, right = Node(7))))
assert not isValidBst(rootNode)

# 4 Right BST
rootNode = Node(val = 10, right = Node(11, right = Node(12, right = Node(20))))
assert isValidBst(rootNode)

# 5 Zigzag BST (Edge Case: Cannot have 8 as left of 15 since it's a right grandchild of 10)
rootNode = Node(20, left = Node(10, right = Node(15, left = Node(8))))
assert not isValidBst(rootNode)

# 6 Empty condition
rootNode = None
assert isValidBst(rootNode)

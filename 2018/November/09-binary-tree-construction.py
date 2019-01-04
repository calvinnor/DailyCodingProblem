# Problem

'''
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:
[a, b, d, e, c, f, g]

And the following inorder traversal:
[d, b, e, a, f, c, g]

You should return the following tree:

      a
     / \
    b   c
   / \ / \
  d  e f  g

Asked by: Google
'''

# Code Section

class Node:
    def __init__(self, val, left = None, right =None):
        self.val = val
        self.left = left
        self.right = right

# Utility function to print a tree's preorder
def preorder(rootNode):
    if rootNode is None:
        return ""

    return rootNode.val + preorder(rootNode.left) + preorder(rootNode.right)

# Utility function to print a tree's inorder
def inorder(rootNode):
    if rootNode is None:
        return ""

    return inorder(rootNode.left) + rootNode.val + inorder(rootNode.right)


def constructTree(preorder, inorder):
    '''
    The tree can be reconstructed from the Preorder + Inorder

    First, we know that Preorder is Root, Left, Right
    Inorder is Left, Root, Right

    So, the first node appearing in the Preorder is the root. We can then
    find this element in the Inorder. Nodes before this element will be
    part of the left sub-tree, while nodes to the right are part of
    right sub-tree. Recursively do this until we finish iterating 
    over the preorder.

    Note: At each iteration, once we find the left and right subtrees, we will
    need to filter the entire preorder list so that it does not contain unknowns
    i.e. there should not be an element existing in preorder and not inorder
    '''

    # If we don't have an element, return None
    if not preorder:
        return None

    rootElement = Node(val = preorder[0])
    rootPositionInorder = inorder.index(rootElement.val)

    # Divide into 2 sublists
    leftSubtreeInorder = inorder[0 : rootPositionInorder]
    rightSubtreeInorder = inorder[rootPositionInorder + 1 : len(inorder)]

    # Filter the preorder for left subtree in the same order
    leftSubtreePreorder = []
    for element in preorder:
        if element in leftSubtreeInorder:
            leftSubtreePreorder.append(element)

    # Filter the preorder for right subtree in the same order
    rightSubtreePreorder = []
    for element in preorder:
        if element in rightSubtreeInorder:
            rightSubtreePreorder.append(element)

    # Set the left and right children via recursion
    rootElement.left = constructTree(preorder = leftSubtreePreorder, inorder = leftSubtreeInorder)
    rootElement.right = constructTree(preorder = rightSubtreePreorder, inorder = rightSubtreeInorder)
    
    return rootElement


# Test Cases

## Example
tree = constructTree(preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g'], inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
assert preorder(tree) == "abdecfg"
assert inorder(tree) == "dbeafcg"

## Left tree
tree = constructTree(preorder = ['a', 'b', 'c', 'd', 'e', 'f'], inorder = ['f', 'e', 'd', 'c', 'b', 'a'])
assert preorder(tree) == "abcdef"
assert inorder(tree) == "fedcba"

## Right tree
tree = constructTree(preorder = ['a', 'b', 'c', 'd', 'e', 'f'], inorder = ['a', 'b', 'c', 'd', 'e', 'f'])
assert preorder(tree) == "abcdef"
assert inorder(tree) == "abcdef"

## Left Right Left Right Left
tree = constructTree(preorder = ['a', 'b', 'c', 'd', 'e', 'f'], inorder = ['b', 'a', 'd', 'c', 'f', 'e'])
assert preorder(tree) == "abcdef"
assert inorder(tree) == "badcfe"

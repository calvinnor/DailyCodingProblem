# Problem

'''
Given the root to a binary tree, implement serialize(root), which 
serializes the tree into a string, and deserialize(s), which deserializes 
the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

Asked by: Google
'''


# Given

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Code Section

# Utility function to print a tree's preorder
def preorder(rootNode):
    if rootNode is None:
        return ""

    leftSubtree = preorder(rootNode.left)
    rightSubtree = preorder(rootNode.right)
    resultString = rootNode.val

    if leftSubtree:
        resultString += " " + leftSubtree

    if rightSubtree:
        resultString += " " + rightSubtree

    return resultString

def serialize(inputTree):
    '''
    We serialize the tree by storing it's Preorder + Inorder.
    However, we can optimise space by storing just it's Preorder with missing nodes
    as -1.

    If a tree consists of a root node with value "root" with left child as "root.left" 
    and right as "root.right"
    then the serialized version will be "root root.left -1 -1 root.right -1 -1"

    Conditions: Node values cannot contain spaces, since we're using space as limiters.
    Can be replaced by some other symbol.
    '''

    '''
    Utility function to convert the preorder of the tree to a list, marking absent nodes
    '''
    def preorderToList(root, currentList = []):
        if root is None:    # Empty node, use -1
            currentList.append(-1)
            return

        # 1. Root
        currentList.append(root.val)

        # 2. Left
        preorderToList(root.left, currentList)

        # 3. Right
        preorderToList(root.right, currentList)

        return currentList

    return " ".join(map(str, preorderToList(inputTree)))    # Pythonic way of joining elements in a list by " "


def deserialize(inputString):

    # Utility function to remove empty nodes
    # Modifies the tree in-place
    def removeEmptyNodes(root):
        if root is None:
            return

        if root.left is not None and root.left.val == "-1":
            root.left = None

        if root.right is not None and root.right.val == "-1":
            root.right = None

        # Recursively call for children
        removeEmptyNodes(root.left)
        removeEmptyNodes(root.right)

    '''
    Iterating over the serialized string, we create Nodes and follow pre-order.
    If a node is marked as -1, we ignore this and move on.
    '''

    treeAsList = inputString.split()    # Splitting by " " to get the tree as list
    if not treeAsList:                  # Empty lists are falsy
         return None

    rootNode = Node(treeAsList[0])
    treeStack = [rootNode]          # Start with the root element

    for element in treeAsList[1:]:
        newNode = Node(val = element)

        rootElement = treeStack[-1]            # Fetch the last element
        if rootElement.left is None:
            rootElement.left = newNode
        
        elif rootElement.right is None:
            rootElement.right = newNode

        if rootElement.left is not None and rootElement.right is not None:
            treeStack.pop()                     # This root is full, remove it

        # Add this node for servicing children if it's not -1
        if newNode.val != "-1":
            treeStack.append(newNode)

    # Removing -1 nodes from the tree since we created them for convenience
    removeEmptyNodes(rootNode)

    return rootNode


# Test Cases

## Example
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

## Left Child
node = Node(val = '12', left = Node(val = '13'))
rootNode = deserialize(serialize(node))
assert rootNode.val == '12'
assert rootNode.left.val == '13'

## Right Child
node = Node(val = '12', right = Node(val = '13'))
rootNode = deserialize(serialize(node))
assert rootNode.val == '12'
assert rootNode.right.val == '13'

## Both Children
node = Node(val = '20', left = Node('8'), right = Node('22'))
rootNode = deserialize(serialize(node))
assert rootNode.val == '20'
assert rootNode.left.val == '8'
assert rootNode.right.val == '22'

## Left Tree
node = Node(val = '20', left = Node(val = '8', left = Node(val = '10', left = Node('5'))))
rootNode = deserialize(serialize(node))
assert rootNode.val == '20'
assert rootNode.left.val == '8'
assert rootNode.left.left.val == '10'
assert rootNode.left.left.left.val == '5'

## Right Tree
node = Node(val = '20', right = Node(val = '8', right = Node(val = '10', right = Node('5'))))
rootNode = deserialize(serialize(node))
assert rootNode.val == '20'
assert rootNode.right.val == '8'
assert rootNode.right.right.val == '10'
assert rootNode.right.right.right.val == '5'

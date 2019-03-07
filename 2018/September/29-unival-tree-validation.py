# Problem

"""

A unival tree (which stands for "universal value") is a tree
where all nodes under it have the same value.

Given the root to a binary tree,
count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

Asked by: Google

"""


# Code Section

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_unival_subtrees(root: Node):

    # Empty trees are Unival but don't count
    if root is None:
        return True, 0

    # Leaf nodes are Unival, Count + 1
    if root.left is None and root.right is None:
        return True, 1

    # Find unival tree counts
    is_left_unival, left_unival_subtrees = get_unival_subtrees(root.left)
    is_right_unival, right_unival_subtrees = get_unival_subtrees(root.right)

    # Total Unival subtrees found
    total_unival_count = left_unival_subtrees + right_unival_subtrees

    # Checking if this tree is Unival
    is_tree_unival = is_left_unival and is_right_unival

    if is_tree_unival and \
            (root.left is None or root.left.val == root.val) and \
            (root.right is None or root.right.val == root.val):
        is_tree_unival = True
        total_unival_count += 1

    return is_tree_unival, total_unival_count


def unival_subtrees(root: Node) -> int:
    """
    A unival tree is a tree where all nodes have the same value.

    Hence, any tree can be defined as a Unival tree if they satisfy the
    following conditions:
    1. Left subtree is Unival
    2. Right subtree is Unival
    3. Left.value = Right.value = Root.value

    We can traverse the tree, returning a count of whether the tree
    is a unival tree.

    Note: A single leaf node is also a unival tree.
    """

    is_unival, total_subtrees = get_unival_subtrees(root)
    return total_subtrees


# Example
assert unival_subtrees(Node(val=0, left=Node(val=1),
                            right=Node(val=0, left=Node(val=1, left=Node(val=1), right=Node(val=1)),
                                       right=Node(val=0)))) == 5

# Complete Unival Tree of 3 nodes
assert unival_subtrees(Node(val=1, left=Node(val=1), right=Node(val=1))) == 3

# Single Node
assert unival_subtrees(Node(val=1)) == 1

# Left Unival Tree
assert unival_subtrees(Node(val=1, left=Node(val=1, left=Node(val=1)))) == 3

# Left non-Unival Tree
assert unival_subtrees(Node(val=1, left=Node(val=0, left=Node(val=1)))) == 1

# Right Unival Tree
assert unival_subtrees(Node(val=1, right=Node(val=1, right=Node(val=1)))) == 3

# Right non-Unival Tree
assert unival_subtrees(Node(val=1, right=Node(val=0, right=Node(val=1)))) == 1

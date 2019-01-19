# Problem

'''
Given two singly linked lists that intersect at some point,
find the intersecting node. The lists are non-cyclical.

For example, given
A = 3 -> 7 -> 8 -> 10 and
B = 99 -> 1 -> 8 -> 10,
return the node with value 8.

In this example, assume nodes with the same value
are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists)
and constant space.

Asked by: Google
'''


# Code Section

# Represents a Node of a Linked List
class Node:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next


# Utility function to create a LinkedList from a Python list
def createLinkedList(inputList):
    rootNode = Node(inputList[0])
    currentNode = rootNode

    for element in inputList[1:]:
        newNode = Node(element)
        currentNode.next = newNode

        currentNode = newNode

    return rootNode


# Utility function to find the length of a LinkedList, given it's head
def lengthOfLL(head):
    if head is None:
        return 0

    return 1 + lengthOfLL(head.next)


# Utility function to print a LinkedList
def printLinkedList(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.val, "")
        currentNode = currentNode.next


def findIntersectionIntl(head1, head2):

    # Recursively call till we reach the end of lists
    intersectingNode = findIntersectionIntl(head1.next, head2.next) if head1.next is not None else None

    # Check the nodes at heads
    # If they are equal, return this node
    if head1.val is head2.val:
        return head1

    # Else, return the last intersecting element
    else:
        return intersectingNode


def findIntersection(head1, head2):
    """
    Since we have to achieve this in O(M + N) time and constant space, we'll
    use recursion on the lists.

    Find the length of both lists, figure out which of them is shorter, and then
    go to the point where both lists have an equal length.
    Then, recursively go till the end of both lists.

    Once we're at the deepest recursion, check the values at both nodes.
    If they match, return the node.
    The previous recursion needs to compare it's nodes now and return if they match.

    Once we've found a point where the nodes don't match, simply return the
    result from the previous recursion up the tree.
    """

    # Sanity check
    if head1 is None or head2 is None:
        return None

    firstListLength = lengthOfLL(head1)
    secondListLength = lengthOfLL(head2)

    # If the first list is bigger, ignore the starting elements
    if firstListLength > secondListLength:
        for count in range(firstListLength - secondListLength):
            head1 = head1.next

    # If the second list is bigger, ignore the starting elements
    elif secondListLength > firstListLength:
        for count in range(secondListLength - firstListLength):
            head2 = head2.next

    # Both are now at the same lengths, call recursively
    return findIntersectionIntl(head1, head2)


# Test Cases

# Example
firstList = createLinkedList([3, 7, 8, 10])
secondList = createLinkedList([99, 1, 8, 10])
assert findIntersection(firstList, secondList).val == 8

# Simple
firstList = createLinkedList([1, 2, 3, 4])
secondList = createLinkedList([5, 2, 3, 4])
assert findIntersection(firstList, secondList).val == 2

# Intersection at end
firstList = createLinkedList([100, 200, 300, 4])
secondList = createLinkedList([500, 600, 700, 4])
assert findIntersection(firstList, secondList).val == 4

# Intersection at start (same lists)
firstList = createLinkedList([1, 2, 3, 4])
secondList = createLinkedList([1, 2, 3, 4])
assert findIntersection(firstList, secondList).val == 1

# Intersection with variable sizes
firstList = createLinkedList([1, 2, 3, 4, 5])
secondList = createLinkedList([3, 4, 5])
assert findIntersection(firstList, secondList).val == 3

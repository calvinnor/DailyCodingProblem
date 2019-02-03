# Problem

"""
Let's represent an integer in a linked list format by having each node represent a digit in the number.
The nodes make up the number in reversed order.

For example, the following linked list:
1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given
9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1

Asked by: Microsoft
"""


# Code Section

# Represents a Node of a Linked List
class Node:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next


# Utility function to create a LinkedList from a Python list
def createLinkedList(inputList: list) -> Node:
    rootNode = Node(inputList[0])
    currentNode = rootNode

    for element in inputList[1:]:
        newNode = Node(element)
        currentNode.next = newNode

        currentNode = newNode

    return rootNode


# Utility function to create a list from a LinkedList
def createList(head: Node) -> list:
    elementList = []
    currentNode = head

    while currentNode is not None:
        elementList.append(currentNode.val)
        currentNode = currentNode.next

    return elementList


def calculateSum(leftHead: Node, rightHead: Node, hasCarry: bool = False) -> Node:
    """
    We'll use a simple iteration over the elements of both Linked Lists.
    On each addition, calculate the sum and carry.

    Pass the carry to the next pointers. Once we reach the end, if we have a carry,
    create a new node and return it.

    Else, we should go on adding the elements till both lists are empty.
    """

    # If we don't have lists to iterate, but have a pending carry
    # Note: Carry can be 1 or 0, hence it's a boolean
    if leftHead is None and rightHead is None:
        return Node(val = 1) if hasCarry else None

    totalSum = 0

    if leftHead is not None:
        totalSum += leftHead.val

    if rightHead is not None:
        totalSum += rightHead.val

    if hasCarry:
        totalSum += 1

    # Extract the digits from the sum
    digitSum = totalSum % 10
    hasCarry = totalSum // 10 is not 0

    # Create a Node for the sum, and pass the carry to the next recursion
    sumNode = Node(val = digitSum)
    sumNode.next = calculateSum(leftHead = leftHead.next if leftHead is not None else None,
                                rightHead = rightHead.next if rightHead is not None else None,
                                hasCarry = hasCarry)

    return sumNode


# Test Cases


# Example (99 + 25 = 124)
leftNode, rightNode = createLinkedList([9, 9]), createLinkedList([5, 2])
assert createList(calculateSum(leftNode, rightNode)) == [4, 2, 1]

# Simple case
leftNode, rightNode = createLinkedList([0, 0, 1]), createLinkedList([1, 1])
assert createList(calculateSum(leftNode, rightNode)) == [1, 1, 1]

# Left List (99 + 0 = 99)
leftNode, rightNode = createLinkedList([9, 9]), createLinkedList([0])
assert createList(calculateSum(leftNode, rightNode)) == [9, 9]

# Right List (0 + 99 = 99)
leftNode, rightNode = createLinkedList([9, 9]), createLinkedList([0])
assert createList(calculateSum(leftNode, rightNode)) == [9, 9]

# Carry List (999 + 999 = 1998)
leftNode, rightNode = createLinkedList([9, 9, 9]), createLinkedList([9, 9, 9])
assert createList(calculateSum(leftNode, rightNode)) == [8, 9, 9, 1]

# Zeros
leftNode, rightNode = createLinkedList([0]), createLinkedList([0])
assert createList(calculateSum(leftNode, rightNode)) == [0]

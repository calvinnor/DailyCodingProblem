# Problem

'''
Given the head of a singly linked list, reverse it in-place.

Asked by: Google
'''


# Code Section

# Represents a Node of a Linked List
class Node:

    def __init__(self, val, next=None):
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


# Utility function to create a list from a LinkedList
def createList(head):
    elementList = []
    currentNode = head

    while currentNode is not None:
        elementList.append(currentNode.val)
        currentNode = currentNode.next

    return elementList

# Utility function to print a LinkedList
def printLinkedList(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.val, "")
        currentNode = currentNode.next


def reverseLinkedList(head):
    """
    We simply need to iterate over the LinkedList and reverse the pointers.

    We need to make sure to get the pointer to next node before we change
    the current node's pointer to the previous element.
    """

    # Either an empty or single node LinkedList
    if head is None or head.next is None:
        return head

    previousNode = head
    currentNode = previousNode.next

    # The head is now the last element, point to None
    head.next = None

    while currentNode is not None:

        # Store the location of our next step
        nextLocation = currentNode.next

        # Point the current node to it's previous
        currentNode.next = previousNode

        # Assign the new values for iteration
        previousNode = currentNode
        currentNode = nextLocation

    # Return the last node, since this is the new head
    return previousNode


# Test Cases


# Standard case
assert createList(reverseLinkedList(createLinkedList([1, 2, 3, 4]))) == [4, 3, 2, 1]

# Negative numbers
assert createList(reverseLinkedList(createLinkedList([1, -1, 1, -1]))) == [-1, 1, -1, 1]

# Repeated numbers, no change
assert createList(reverseLinkedList(createLinkedList([1, 1, 1, 1]))) == [1, 1, 1, 1]

# Palindrome
assert createList(reverseLinkedList(createLinkedList([1, 2, 3, 2, 1]))) == [1, 2, 3, 2, 1]

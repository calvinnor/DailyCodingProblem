# Problem

"""

Implement a stack that has the following methods:

- push(val), which pushes an element onto the stack

- pop(), which pops off and returns the topmost element of the stack.
  If there are no elements in the stack, then it should throw an error or return null.

- max(), which returns the maximum value in the stack currently.
  If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

Asked by: Amazon

"""


# Code Section

# Class to denote an Element in a Stack
# Additional next_max pointer to form a LinkedList with the next maximum element
class StackElement:

    def __init__(self, value: int, next_max=None):
        self.value = value
        self.next_max = next_max


# Class to denote the required Stack.
class Stack:

    def __init__(self):
        self.elements = []
        self.current_max = None

    def push(self, element):
        """
        Push an element onto the Stack.
        Internally checks and updates the Max pointer if we've received a higher element.
        """
        new_element = StackElement(element)

        # Check if this element is greater than our max
        if self.current_max is None or self.current_max.value < new_element.value:

            # Hold the old max in a variable
            old_max = self.current_max

            # Assign the new max
            self.current_max = new_element

            # Add a link from the new max to the old
            self.current_max.next_max = old_max

        # Finally push the element
        self.elements.append(new_element)

    def pop(self):
        """
        Pops an element from the Stack.
        Internally updates the Max pointer if we popped the current max.
        """

        # If we have an empty set, return None
        if not self.elements:
            return None

        # Get the element to pop
        pop_element = self.elements.pop()

        # If this element is the current max, update the max to next pointer
        if self.current_max == pop_element:
            self.current_max = pop_element.next_max

        # Finally, return the element
        return pop_element.value

    def max(self):
        """
        Returns the max element of the stack.
        Since we're maintaining that element, this is a O(1) operation
        """
        return None if self.current_max is None else self.current_max.value


# Test Case

test_stack = Stack()

# Empty assertions
assert test_stack.pop() is None
assert test_stack.max() is None

# Push elements
test_stack.push(5)
test_stack.push(3)
test_stack.push(9)
test_stack.push(2)
test_stack.push(1)

"""

|   |
| 1 |
| 2 |
| 9 |
| 3 |
| 5 |
|___|

"""

# Assert the max of this stack
assert test_stack.max() == 9

# Assert pop operations till max is popped
assert test_stack.pop() == 1
assert test_stack.pop() == 2
assert test_stack.pop() == 9

"""

|   |
| 3 |
| 5 |
|___|

"""

# Assert that the max element is updated
assert test_stack.max() == 5

# Pushing some more elements in ascending order
test_stack.push(10)
test_stack.push(11)
test_stack.push(12)
test_stack.push(13)
test_stack.push(14)

"""

|    |
| 14 |
| 13 |
| 12 |
| 11 |
| 10 |
|  3 |
|  5 |
|___ |

"""

# Asserting the max element
assert test_stack.max() == 14

# Asserting pops & max element updates
assert test_stack.pop() == 14
assert test_stack.max() == 13

assert test_stack.pop() == 13
assert test_stack.max() == 12

assert test_stack.pop() == 12
assert test_stack.max() == 11

assert test_stack.pop() == 11
assert test_stack.max() == 10

assert test_stack.pop() == 10
assert test_stack.max() == 5

"""

|   |
| 3 |
| 5 |
|___|

"""

# Final assertions till stack is empty
assert test_stack.pop() == 3
assert test_stack.max() == 5
assert test_stack.pop() == 5

# Empty stack assertions
assert test_stack.pop() is None
assert test_stack.max() is None

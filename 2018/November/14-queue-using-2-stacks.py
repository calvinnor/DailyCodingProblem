# Problem

'''
Implement a queue using two stacks.
Recall that a queue is a FIFO (first-in, first-out) data structure
with the following methods:

enqueue, which inserts an element into the queue, and
dequeue, which removes it.

Asked by: Apple
'''

# Code Section

"""
We can implement a Queue using 2 stacks by pushing / popping elements between the
stacks and emulating a FIFO.

It can be done in 3 ways:

#1: Top of stack is element to dequeue:
    This means an enqueue operation needs to put all elements from stack1 into stack2,
    then push the element to stack1 and pop all elements back to stack1.
    
    Enqueue is O(n), Dequeue is O(1)
    
#2: Top of stack is element to enqueue:
    This means enqueue is a simple push operation, but dequeue will need to push
    all elements from stack1 to stack2, pop the bottom element, then move all
    elements back to stack1.
    
    Enqueue is O(1), Dequeue is O(n)

#3: Dequeue is decidable by flags:
    We'll maintain flags to push / pop from stack1 and stack2.
    Enqueue & dequeue operations will push / pop based on the flags, alternatively on the
    stacks and then invert it for the next operation.
    We can increase the number of stacks to improve the performance in this scenario.

    This keeps the complexity for enqueue constant, while halving the cost of dequeue
    in practical application.

    Enqueue is O(1), Dequeue is O(n / no. of stacks)

We'll use approach #3 for this solution.
"""


# Custom class to implement a stack
class Stack:

    def __init__(self):
        self.contents = []

    # Push an element onto the stack
    def push(self, element):
        self.contents.append(element)

    # Pop the last element from the stack
    def pop(self):
        return self.contents.pop(len(self.contents) - 1)

    # Returns the top of stack
    def peek(self):
        if not self.contents:
            return None

        return self.contents[-1]


# Custom class to implement a Queue using 2 stacks
class Queue:
    STACK_ONE = 1
    STACK_TWO = 2

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

        self.enqueueOn = self.STACK_ONE
        self.dequeueFrom = self.STACK_ONE

    def enqueue(self, element):

        # Enqueue an element depending on the position
        if self.enqueueOn is self.STACK_ONE:
            self.stack1.push(element)
            self.enqueueOn = self.STACK_TWO

        elif self.enqueueOn is self.STACK_TWO:
            self.stack2.push(element)
            self.enqueueOn = self.STACK_ONE

    def dequeue(self):
        # For Dequeue, push all elements onto the next stack, then pop the topmost
        # element and push everything back.

        # Utility function to perform the stack operations for dequeue
        def performOp(originStack, spareStack):

            # Count the total elements pushed onto the other stack
            totalElements = 0

            while originStack.peek() is not None:
                spareStack.push(originStack.pop())
                totalElements += 1

            # Pop the top element of spare stack
            dequeueElement = spareStack.pop()

            # Return all elements to the first stack
            for count in range(totalElements - 1):
                originStack.push(spareStack.pop())

            return dequeueElement

        dequeuedElement = None

        if self.dequeueFrom is self.STACK_ONE:
            dequeuedElement = performOp(self.stack1, self.stack2)
            self.dequeueFrom = self.STACK_TWO

        elif self.dequeueFrom is self.STACK_TWO:
            dequeuedElement = performOp(self.stack2, self.stack1)
            self.dequeueFrom = self.STACK_ONE

        return dequeuedElement

    def isEmpty(self):
        return self.stack1.peek() is None and self.stack2.peek() is None


# Test Cases

# 1: Simple enqueue-dequeue phases
testQueue = Queue()
testQueue.enqueue(1)
testQueue.enqueue(2)
testQueue.enqueue(3)
testQueue.enqueue(4)
assert testQueue.dequeue() == 1
assert testQueue.dequeue() == 2
assert testQueue.dequeue() == 3
assert testQueue.dequeue() == 4
assert testQueue.isEmpty()

# 2: Mixed operations
testQueue = Queue()
testQueue.enqueue(1)
testQueue.enqueue(3)
assert testQueue.dequeue() == 1
testQueue.enqueue(5)
assert testQueue.dequeue() == 3
testQueue.enqueue(7)
assert testQueue.dequeue() == 5
assert testQueue.dequeue() == 7
assert testQueue.isEmpty()

# 3: Negative, repeated, zero numbers
testQueue = Queue()
testQueue.enqueue(-1)
testQueue.enqueue(0)
testQueue.enqueue(-1)
testQueue.enqueue(1000)
assert testQueue.dequeue() == -1
assert testQueue.dequeue() == 0
assert testQueue.dequeue() == -1
testQueue.enqueue(2000)
assert testQueue.dequeue() == 1000
assert testQueue.dequeue() == 2000
assert testQueue.isEmpty()

# Push an element to test not empty scenario
testQueue.enqueue(1)
assert not testQueue.isEmpty()

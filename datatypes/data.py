"""
Data types implementations
"""

class Node:

    """
    Linked List Data Structure
    """

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    """
    Stack with Linked List Data Type
    """

    def __init__(self):
        self.top = None
        self.count = 0

    def __len__(self):
        return self.count

    def push(self, x):

        """
        Add new item to the top
        """

        temp = Node(x)
        temp.next = self.top
        self.top = temp
        self.count += 1

    def pop(self):

        """
        Delete an item from the top
        """

        if self.is_empty():
            raise IndexError("Stack is empty")

        temp = self.top
        self.top = self.top.next
        val = temp.data
        self.count -= 1
        return val

    def peek(self):

        """
        Return the top item
        """

        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.top.data

    def is_empty(self):

        """
        Emptiness of the Stack
        """

        return self.top is None

class Queue:

    """
    Queue with Linked List Data Type
    """

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):

        """
        Emptiness of the Queue
        """

        return self.front is None

    # Add element to the queue
    def add(self, data):

        """
        Add new item to the edge
        """

        new_node = Node(data)

        if self.is_empty():
            self.front = self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def pop(self):

        """
        Delete the first item
        """

        if self.is_empty():
            raise IndexError("Queue is empty")

        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None

        self.size -= 1

        return removed

    def peek(self):

        """
        Return the first item
        """

        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.front.data

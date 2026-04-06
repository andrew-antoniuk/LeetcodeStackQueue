"""
Data types implementations
"""

from collections import deque

class Stack:

    """
    Stack Data Type
    """

    def __init__(self):
        self.__items = []

    def is_empty(self) -> bool:

        """
        Emptiness of the Stack
        """

        return not self.__items

    def push(self, item):

        """
        Add new item to the top
        """

        self.__items.append(item)

    def pop(self):

        """
        Delete an item from the top
        """

        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.__items.pop()

    def peek(self):

        """
        Return the top item
        """

        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.__items[-1]

    def __len__(self) -> int:
        return len(self.__items)

    def __str__(self) -> str:
        return f"Stack({self.__items})"

class Queue:

    """
    Queue Data Type
    """

    def __init__(self):
        self.__items = deque()

    def is_empty(self):

        """
        Emptiness of the Queue
        """

        return not self.__items

    def add(self, item):

        """
        Add new item to the edge
        """

        self.__items.append(item)

    def pop(self):

        """
        Delete the first item
        """

        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.__items.popleft()

    def peek(self):

        """
        Return the first item
        """

        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.__items[0]

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return f"Queue({self.__items})"

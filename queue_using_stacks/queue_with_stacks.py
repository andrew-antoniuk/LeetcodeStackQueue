"""
Docstring for queue_with_stacks
"""

from datatypes.data import Stack

class MyQueue:

    """
    Docstring for MyQueue
    """

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:

        """
        Add item to the back of the queue
        """

        if not isinstance(x, int):
            raise TypeError("Incorrect data type for push")

        self.stack_in.push(x)

    def transfer(self):

        """
        Helper method for transfering data from stack_in into stack_out.
        Used for rearrangement, which makes .pop() and .peek() methods correct and possible
        """
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

    def pop(self) -> int:

        """
        Remove and return item from the front of the queue
        """

        if self.stack_in.is_empty():
            raise IndexError("Queue is empty")
        self.transfer()

        return self.stack_out.pop()

    def peek(self) -> int:

        """
        Return item from the front of the queue
        """

        if self.stack_in.is_empty():
            raise IndexError("Queue is empty")
        self.transfer()

        return self.stack_out.peek()

    def empty(self) -> bool:

        """
        Check emptiness of the queue
        """

        return self.stack_in.is_empty() and self.stack_out.is_empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

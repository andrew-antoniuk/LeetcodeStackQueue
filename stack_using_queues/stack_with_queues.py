"""
Docstring for Stack using Queues.stack_with_queues
"""

from datatypes.data import Queue

class MyStack:

    """
    Docstring for MyStack
    """

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:

        """
        Add item to the top of the stack
        """

        if not isinstance(x, int):
            raise TypeError("Incorrect data type for push")

        self.q2.add(x)

        while not self.q1.is_empty():
            self.q2.add(self.q1.pop())

        self.q1, self.q2 = self.q2, self.q1


    def pop(self) -> int:

        """
        Remove item form the front of the stack
        """

        if self.empty():
            raise IndexError("Queue is empty")

        return self.q1.pop()

    def top(self) -> int:

        """
        Remove and return item from the front of the stack
        """

        if self.empty():
            raise IndexError("Stack is empty")

        return self.q1.peek()

    def empty(self) -> bool:

        """
        Check emptiness of the stack
        """

        return self.q1.is_empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

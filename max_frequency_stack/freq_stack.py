"""
Docstring for max_frequency_stack.freq_stack
"""

from datatypes.data import Stack

class FreqStack:

    """
    Docstring for FreqStack
    """

    def __init__(self):
        self.stack = Stack()

    def push(self, val: int) -> None:

        """
        Docstring for push
        """

        if not isinstance(val, int):
            raise TypeError("Incorrect data type for push")

        self.stack.push(val)

    def pop(self) -> int:

        """
        Docstring for pop
        """

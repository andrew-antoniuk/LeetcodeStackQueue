"""
Docstring for max_frequency_stack.freq_stack
"""

from datatypes.data import Stack

class FreqStack:

    """
    Docstring for FreqStack
    """

    def __init__(self):
        self.freqs = {}
        self.group = {}
        self.max_freq = 0 # current

    def push(self, val: int) -> None:

        """
        Docstring for push
        """

        # current freq
        freq = self.freqs.get(val, 0) + 1
        self.freqs[val] = freq

        self.max_freq = max(self.max_freq, freq)

        # add number to the stack
        if freq not in self.group:
            self.group[freq] = Stack() # new stack for new freq

        self.group[freq].push(val)

    def pop(self) -> int:

        """
        Docstring for pop
        """

        val = self.group[self.max_freq].pop()
        self.freqs[val] -= 1

        # decrease max_freq if its stack is empty
        if self.group[self.max_freq].is_empty():
            self.max_freq -= 1

        return val

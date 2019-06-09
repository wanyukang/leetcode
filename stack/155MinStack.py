#coding: utf-8


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        def push(self, x: int) -> None:
        """
        self.stack.append(x)
        

    def pop(self):
        """
        def pop(self) -> None:
        """
        self.stack.pop()
        

    def top(self):
        """
        def top(self) -> int:
        """
        return self.stack[-1:][0]
        

    def getMin(self):
        """
        def getMin(self) -> int:
        """
        return min(self.stack)

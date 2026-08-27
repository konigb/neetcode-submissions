class MinStack:

    def __init__(self):
        self.minStack = []
        self.minVal = 0
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) == 0:
            self.minVal = val
        else:
            self.minVal = min(self.minVal, val)
        
        self.minStack.append(self.minVal)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if self.minStack:
            self.minVal = self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]
        

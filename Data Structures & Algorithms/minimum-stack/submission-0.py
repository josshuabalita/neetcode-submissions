class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Time: O(1)
# Space: O(n)

# stack = [1 3 0 -5]
# minStack = [1 0 -5]
        
# O(n) - n is the size of the stack
# valMin = self.stack[0]
# for i in range(len(self.stack)):
#     valMin = min(self.stack[i], valMin)
# return valMin



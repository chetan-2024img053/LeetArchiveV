class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([value, value])
            return

        mini = min(value, self.stack[-1][1])
        self.stack.append([value, mini])

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return
        return self.stack[-1][1]
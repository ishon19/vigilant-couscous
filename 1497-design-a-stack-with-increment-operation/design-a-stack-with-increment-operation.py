class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.capacity = maxSize

    def push(self, x: int) -> None:
        if not len(self.stack) >= self.capacity:
            self.stack = [x] + self.stack
        
    def pop(self) -> int:
        if not len(self.stack) <= 0:
            ele = self.stack[0]
            self.stack = self.stack[1:]
            return ele
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[len(self.stack) - 1 - i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
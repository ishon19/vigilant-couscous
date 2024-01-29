class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # empty the first stack to second
        # if self.empty():
        #     print('direct append')
        #     self.s1.append(x)
        # else:
        #     while not self.empty():
        #         self.s2.append(self.s1.pop())
            
        #     print('s2 rn', self.s2)
        #     self.s1.append(x)

        #     while not len(self.s2) == 0:
        #         self.s1.append(self.s2.pop())
        #     print('s2 finally', self.s2)
        #     print('s1 finally', self.s1)
        self.s1.append(x)
        

    def pop(self) -> int:
        if self.empty(): return -1

        while not len(self.s1) == 1:
            self.s2.append(self.s1.pop())
        
        val = self.s1.pop()

        while not len(self.s2) == 0:
            self.s1.append(self.s2.pop())

        return val
        

    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
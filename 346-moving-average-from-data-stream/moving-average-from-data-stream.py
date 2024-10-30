class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.elements = []

    def next(self, val: int) -> float:
        self.elements.append(val)
        return sum(self.elements[-self.size:])/min(self.size, len(self.elements))



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
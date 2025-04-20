class MedianFinder:

    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap, -num)

        if self.leftHeap and self.rightHeap and -self.leftHeap[0] > self.rightHeap[0]:
            heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))
        
        if len(self.leftHeap) > len(self.rightHeap) + 1:
            heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))
        if len(self.rightHeap) > len(self.leftHeap) + 1:
            heapq.heappush(self.leftHeap, -heapq.heappop(self.rightHeap))

    def findMedian(self) -> float:
        if len(self.leftHeap) == len(self.rightHeap):
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2
        elif len(self.leftHeap) > len(self.rightHeap):
            return -self.leftHeap[0]
        else:
            return self.rightHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
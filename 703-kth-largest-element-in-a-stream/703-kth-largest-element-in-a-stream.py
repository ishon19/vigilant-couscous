class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # create the min heap with only k elements
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)
        
        # keep only k elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # simply push the element in the heap
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
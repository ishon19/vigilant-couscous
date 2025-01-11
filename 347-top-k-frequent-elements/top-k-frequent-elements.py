class Solution:
    def __init__(self):
        self.res = []
        self.pq = []

    def getCounts(self, arr):
        counts = Counter(arr)
        return [(-v, k) for k, v in counts.items()]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        self.pq = self.getCounts(nums)
        heapify(self.pq)

        while k:
            _, num = heappop(self.pq)
            self.res.append(num)
            k -= 1
        
        return self.res



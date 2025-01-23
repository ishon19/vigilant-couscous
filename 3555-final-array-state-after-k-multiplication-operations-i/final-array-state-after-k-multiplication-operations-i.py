class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            heappush(heap, (nums[i], i))
        
        while k:
            val, idx = heappop(heap)
            heappush(heap, (val * multiplier, idx))
            k -= 1
        
        heap.sort(key=lambda x: x[1])
        res = []
        for val, _ in heap:
            res.append(val)
        
        return res
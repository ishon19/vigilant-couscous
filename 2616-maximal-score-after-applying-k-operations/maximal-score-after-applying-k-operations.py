class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = []
        res = 0

        for i in range(len(nums)):
            heappush(pq, -nums[i])
        
        while k:
            k -= 1
            num = -heappop(pq)
            res += num
            heappush(pq, -ceil(num/3))

        return res
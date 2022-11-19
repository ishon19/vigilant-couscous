class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")        
        l, r = 0, 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                res = min(res, i+1-l)
                s -= nums[l]
                l += 1
        return 0 if res == float("inf") else res
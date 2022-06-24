class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l,r,s,b = 0,0,0,0
        cache = set()
        while r<len(nums):
            while(nums[r] in cache):
                cache.remove(nums[l])
                s -= nums[l]
                l += 1
            s += nums[r]
            cache.add(nums[r])
            b = max(s, b)
            r += 1
        return b
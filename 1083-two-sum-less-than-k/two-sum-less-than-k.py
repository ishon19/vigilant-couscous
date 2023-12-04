class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r  = 0, len(nums) - 1
        res = -1
        while l<r:
            cur = nums[l] + nums[r]
            if cur < k:
                cur = nums[l] + nums[r]
                res = cur if cur > res else res
            
            if cur >= k:
                r -= 1
            else:
                l += 1
        return res
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def helper(idx, cur_sum):
            if idx >= len(nums):                   
                return 1 if cur_sum == target else 0
            plus_ways = helper(idx+1, cur_sum+nums[idx])
            minus_ways = helper(idx+1, cur_sum-nums[idx])
            return plus_ways + minus_ways
        return helper(0,0)
            
                
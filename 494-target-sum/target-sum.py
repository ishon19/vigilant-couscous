class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}

        def helper(idx, cur_sum):
            if idx >= len(nums):                   
                return 1 if cur_sum == target else 0
            
            if (idx, cur_sum) in self.memo:
                return self.memo[(idx, cur_sum)]

            plus_ways = helper(idx+1, cur_sum+nums[idx])
            minus_ways = helper(idx+1, cur_sum-nums[idx])
            
            self.memo[(idx, cur_sum)] = plus_ways + minus_ways
            return self.memo[(idx, cur_sum)]
        
        return helper(0,0)
            
                
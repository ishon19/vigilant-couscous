class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) +1)
        
        dp[len(nums)], dp[len(nums)-1] = 0, nums[len(nums)-1]
        
        for i in range(len(nums)-2, -1, -1):
            dp[i] = max(dp[i+1], dp[i+2] + nums[i])
        
        return dp[0]
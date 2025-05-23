#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # actual_total = sum(nums)
        # expected_total = (n * (n + 1)) // 2
        # return expected_total - actual_total    
        res = len(nums)

        for i in range(len(nums)):
            res ^= nums[i] ^ i
        
        return res
# @lc code=end


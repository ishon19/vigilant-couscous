#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = min_so_far = res = nums[0]

        for num in nums[1:]:
            options = [num, num * max_so_far, num * min_so_far]
            max_so_far = max(options)
            min_so_far = min(options)
            res = max(res, max_so_far)
        
        return res
# @lc code=end


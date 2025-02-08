#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_idx = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_idx] = nums[i]
                last_non_zero_idx += 1
        
        for i in range(last_non_zero_idx, len(nums)):
            nums[i] = 0
        
 # @lc code=end


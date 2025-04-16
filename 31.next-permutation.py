#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - 2
        while k >= 0:
            if nums[k] < nums[k+1]:
                break 
            k -= 1
        
        if k < 0:
            nums.reverse()
        else:
            l = len(nums) - 1
            while l < k:
                if nums[l] > nums[k]:
                    break
                l -= 1
            
            nums[l], nums[k] = nums[k], nums[l]
            nums[k+1:] = reversed(nums[k+1:])

# @lc code=end


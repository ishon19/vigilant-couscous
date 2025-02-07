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
        n = len(nums)
        if n <= 1:
            return 

        # find the first decreasing number from the end
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]: 
            i -= 1
        
        # find element to swap with 
        if i >= 0:
            j = n - 1
            while  nums[j] <= nums[i]:
                j -= 1
        
            nums[i], nums[j] = nums[j], nums[i]

        # reverse sublist 
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


# @lc code=end


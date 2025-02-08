#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#

# @lc code=start
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []

        # the whole ranges are missing
        if not nums:
            return [[lower, upper]]
        
        # check if nums starts with lower
        if nums[0] > lower:
            res = [[lower, nums[0]-1]]
        
        # in between the numbers
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                res.append([nums[i-1] + 1, nums[i] - 1])
        
        # after the last element
        if nums[-1] < upper:
            res.append([nums[-1] + 1, upper])


        return res
# @lc code=end


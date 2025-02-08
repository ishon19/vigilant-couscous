#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window baby
        start = 0
        res = 0
        zeros = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[start] == 0:
                    zeros -= 1
                start += 1
            
            res = max(res, end - start + 1)
        
        return res
# @lc code=end


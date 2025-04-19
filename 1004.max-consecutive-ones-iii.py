#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window baby
        left = res = zeroes = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
# @lc code=end


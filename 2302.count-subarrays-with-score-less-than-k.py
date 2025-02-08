#
# @lc app=leetcode id=2302 lang=python3
#
# [2302] Count Subarrays With Score Less Than K
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        count = 0

        while l < len(nums):
            if sum(nums[l:r+1]) * (r - l + 1) < k:
                count += 1
                r += 1
            else:
                l += 1
                r = l
        
        return count
            

# @lc code=end


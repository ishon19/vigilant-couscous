#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        for i in range(k, len(nums)):
            curr_sum = curr_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum/k 
# @lc code=end


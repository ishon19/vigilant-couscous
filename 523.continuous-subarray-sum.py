#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}
        cur_sum = 0

        for i, num in enumerate(nums):
            cur_sum += num

            if k != 0:
                cur_sum %= k
            
            if cur_sum in remainder_map:
                if i - remainder_map[cur_sum] >= 2:
                    return True
            else:
                remainder_map[cur_sum] = i
        
        return False
# @lc code=end


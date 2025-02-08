#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cum_sum = 0

        sum_map = {0: 1}

        for num in nums:
            cum_sum += num

            if (cum_sum - k) in sum_map:
                count += sum_map[cum_sum - k]
            
            if cum_sum in sum_map:
                sum_map[cum_sum] += 1
            else:
                sum_map[cum_sum] = 1
        
        return count

# @lc code=end


#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # circular subarray means there is a potential start part 
        # and the end part which are "connected" leaving a portion 
        # in the middle which we can refer as the "minimum sum subarray"
        # since we want the circular subarray sum, we must "exclude"
        # this middle part and so subtracting this min subarray sum from 
        # the total sum gives us the final answer.
        def kadanes(arr):
            res = max_ending_here = arr[0]

            for i in range(1, len(arr)):
                max_ending_here = max(arr[i], arr[i] + max_ending_here)
                res = max(res, max_ending_here)
            
            return res
        
        max_kadane = kadanes(nums)
        total = sum(nums)
        min_kadane = kadanes([-x for x in nums])

        # adding since the min_kadane is negative in nature
        max_circular = total + min_kadane

        # whole array is min sum array
        if max_circular == 0:
            return max_kadane
        
        return max(max_kadane, max_circular)
# @lc code=end


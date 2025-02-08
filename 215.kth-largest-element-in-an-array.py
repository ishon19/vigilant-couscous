#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)

        while len(nums) > k:
            heappop(nums)
        
        return nums[0]
        
# @lc code=end


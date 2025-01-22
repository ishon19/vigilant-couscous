#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we can use the binary search based approach here
        # based on the observation that a number n
        # should be less than or equal to sum of (1, n-1)
        l, r = 1, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            count = sum(1 for num in nums if num <= mid)

            if count > mid:
                r = mid
            else:
                l = mid + 1

        return l


# @lc code=end

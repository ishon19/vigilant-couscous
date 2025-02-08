#
# @lc app=leetcode id=3371 lang=python3
#
# [3371] Identify the Largest Outlier in an Array
#

# @lc code=start
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        freq = Counter(nums)
        total = sum(nums)
        res = float("-inf")

        for num in nums:
            outlier = total - (2 * num)
            if outlier in freq:
                if (outlier == num and freq[num] > 1) or (outlier != num and freq[outlier] > 0):
                    res = max(res, outlier)
        
        return res
# @lc code=end


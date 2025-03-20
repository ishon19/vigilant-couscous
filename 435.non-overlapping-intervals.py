#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev = -inf

        for start, end in intervals:
            if start < prev:
                count += 1
            else:
                prev = end

        return count    
# @lc code=end


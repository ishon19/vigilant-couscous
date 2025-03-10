#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()

        res = [intervals[0]]
        for interval in intervals[1:]:
            if res[-1][1] >= interval[0]:
                res[-1] = [min(interval[0], res[-1][0]), max(interval[1], res[-1][1])]
            else:
                res.append(interval)
        
        return res
# @lc code=end


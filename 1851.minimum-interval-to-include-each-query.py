#
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#

# @lc code=start
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        intervals.sort(key=lambda x: x[0])
        heap = []
        i = 0

        for query in sorted(queries):
            while i < len(intervals) and intervals[i][1] <= query:
                start, end = intervals[i]
                heappush(heap, (end - start + 1, end))
                i += 1
            
            while heap and:



        return res
# @lc code=end


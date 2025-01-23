#
# @lc app=leetcode id=2054 lang=python3
#
# [2054] Two Best Non-Overlapping Events
#

# @lc code=start
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        maxSingleVal = 0
        res = 0

        for start, end, value in events:
            while pq and pq[0][0] < start:
                # check if the earlier event can be considerd
                _, prev_value = heappop(pq)
                maxSingleVal = max(maxSingleVal, prev_value)
            
            res = max(res, maxSingleVal + value)
            heappush(pq, [end, value])
        
        return res
# @lc code=end


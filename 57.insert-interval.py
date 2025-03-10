#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for start, end in intervals:
            new_start, new_end = newInterval

            if end < new_start:
                res.append([start, end])
            elif new_end < start:
                res.append([new_start, new_end])
                newInterval = [start, end]
            else:
                newInterval = [
                    min(start, new_start), max(end, new_end)
                ]
                
        res.append(newInterval)
        return res
# @lc code=end


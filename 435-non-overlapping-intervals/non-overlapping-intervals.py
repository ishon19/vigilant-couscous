class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the input list
        # intervals.sort()
        # prevEnd = intervals[0][1]
        # res = 0
        # for interval in intervals[1:]:
        #     if interval[0]>=prevEnd:
        #         prevEnd = interval[1]
        #     else:
        #         res += 1
        #         prevEnd = min(interval[1], prevEnd)
        # return res

        intervals.sort()
        res = [intervals[0]]

        for interval in intervals[1:]:
            if res[-1][1] > interval[0]:
                res[-1] = [min(res[-1][0], interval[0]), min(res[-1][1], interval[1])]
            else:
                res.append(interval)
        
        return len(intervals) - len(res)
        

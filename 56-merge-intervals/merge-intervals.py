class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]

        for interval in intervals[1:]:
            # if there is an overlap
            if res[-1][1] >= interval[0]:
                res[-1] = [min(res[-1][0], interval[0]), max(res[-1][1], interval[1])]
            else:
                res.append(interval)
        
        return res
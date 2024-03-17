class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:        
        # res = []
        
        # for i in range(len(intervals)):
        #     # if the new one is before the new one 
        #     if newInterval[1]<intervals[i][0]:
        #         res.append(newInterval)
        #         return res + intervals[i:]
        #     elif newInterval[0]>intervals[i][1]:
        #         # keep on adding to results till you find 
        #         # one which matches the if case
        #         res.append(intervals[i])
        #     else:
        #         # overlap
        #         newInterval = [
        #             min(intervals[i][0], newInterval[0]), 
        #             max(intervals[i][1], newInterval[1])
        #         ]
        # res.append(newInterval)
        # return res

        # binary search way
        l, r  = 0, len(intervals)-1
        goal = newInterval[0]

        while l<=r:
            mid = (l+r)//2
            if intervals[mid][0] < goal:
                l = mid + 1
            else:
                r = mid - 1
        
        intervals.insert(l, newInterval)
        
        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res


                

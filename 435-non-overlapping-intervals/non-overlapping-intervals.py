class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        prev_end = float("-inf")
        intervals.sort(key=lambda x: x[1])
        to_remove = len(intervals)

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end 
                to_remove -= 1
        
        return to_remove
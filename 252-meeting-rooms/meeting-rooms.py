class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # the only way a person won't be able to attend the meeting if there's an overlap
        if not intervals:
            return True
        
        intervals.sort(key=lambda x: x[1])

        prev_start, prev_end = intervals[0]

        for interval in intervals[1:]:
            start, end = interval
            if start < prev_end or prev_end > start :
                return False
            prev_start, prev_end = interval
        return True
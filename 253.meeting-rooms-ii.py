#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])

        rooms = []
        heappush(rooms, intervals[0][1])

        for i in range(1, len(intervals)):
            if rooms[0] <= intervals[i][0]:
                heappop(rooms)
            
            heappush(rooms, intervals[i][1])
        
        return len(rooms)
# @lc code=end


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # starts = sorted([i[0] for i in intervals])
        # ends = sorted([i[1] for i in intervals])
        # s = e = 0
        # count = res = 0

        # while s<len(intervals):
        #     if starts[s]<ends[e]:
        #         count += 1
        #         s += 1
        #     else:
        #         count -= 1
        #         e += 1
        #     res = max(res, count)
        # return res
        if not intervals: return 0

        rooms = []
        intervals.sort(key=lambda x: x[0])
        rooms.append(intervals[0][1])
        heapq.heapify(rooms)

        for interval in intervals[1:]:
            if rooms[0] <= interval[0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, interval[1])
        
        return len(rooms)
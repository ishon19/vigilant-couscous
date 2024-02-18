class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = list(range(n))
        occupied_rooms = []
        heapq.heapify(available_rooms)
        meeting_count = [0] * n

        for start, end in sorted(meetings):
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _, room = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room)
            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(occupied_rooms, [end, room])
            else:
                earliest_end, room = heapq.heappop(occupied_rooms)
                heapq.heappush(occupied_rooms, [earliest_end + end - start, room])
            meeting_count[room] += 1
        
        return meeting_count.index(max(meeting_count))
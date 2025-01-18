"""

times = [[1,4], [2,3], [4,6]]

Simulation

Real time events need to be simulated through some sort of data structure

I want to priorize the seats with lowest indices 


occupied = (0)

1 => 4
2 => 3
3 =>
4 =>

we are assuming that the friend who arrives comes  when the simulation is done
"""

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # times.sort()
        # target_time = times[targetFriend]

        # free_time = [0] * len(times)

        # for time in times:
        #     for i in range(len(times)):
        #         # if a chair before the current time is free assign it
        #         if free_time[i] <= time[0]:
        #             free_time[i] = time[1]
        #             if time == target_time:                        
        #                 return i
        #             break
        # return 0
        events = []

        for i in range(len(times)):
            events.append([times[i][0], i])
            events.append([times[i][1], ~i])
        
        events.sort()

        chairs = list(range(len(times)))
        occupied = []

        for event in events:
            time, friend = event

            while occupied and occupied[0][0] <= time:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(chairs, chair)
            
            if friend >= 0:
                chair = heapq.heappop(chairs)
                if friend == targetFriend:
                    return chair
                # chair occupied till this time
                heapq.heappush(occupied, [times[friend][1], chair])
        
        return -1



                

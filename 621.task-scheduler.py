#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # the idea is to push the most frequent task to the heap 
        # since the most frequent task dictates the whole timing
        # then we can create a cooldown queue to track items that
        # are cooling down at the monment.
        taskQueue = [-count for count in Counter(tasks).values()]
        heapify(taskQueue)

        clock = 0
        coolDownQueue = deque()
        while taskQueue or coolDownQueue:
            clock += 1

            if taskQueue:
                count = -heappop(taskQueue) - 1
                if count > 0:
                    # add to the cooldown
                    coolDownQueue.append((count, clock + n))
            
            if coolDownQueue and coolDownQueue[0][1] == clock:
                heappush(taskQueue, -coolDownQueue.popleft()[0])
        
        return clock

# @lc code=end


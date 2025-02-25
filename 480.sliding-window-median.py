#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
from heapq import * 

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def move(h1, h2, val):
            heappush(h2, -heappop(h1))
        
        minHeap = []
        maxHeap = []
        res = []

        for i in range(k):
            heappush(maxHeap, -nums[i])
        
        for _ in range(k//2):
            move(maxHeap, minHeap, None)
        
        for i in range(k, len(nums)):
            if k % 2 == 0:
                median = (-maxHeap[0] + minHeap[0]) / 2
            else:
                median = float(-maxHeap[0])
            res.append(median)

            outgoing = nums[i-k]
            incoming = nums[i]

            balance = 0

            if outgoing <= -maxHeap[0]:
                balance -= 1
                if outgoing == -maxHeap[0]:
                    heappop(maxHeap)  
                else:
                    maxHeap.remove(-outgoing)
                    heapify(maxHeap)
            else:
                balance += 1
                minHeap.remove(outgoing)
                heapify(minHeap)
            
            if len(maxHeap) > 0 and incoming <= -maxHeap[0]:
                heappush(maxHeap, -incoming)
                balance += 1
            else:
                heappush(minHeap, incoming)
                balance -= 1
            
            while balance > 0:
                move(maxHeap, minHeap, None)
                balance -= 2
            while balance < 0 :
                move(minHeap, maxHeap, None)
                balance += 2
        
        if k % 2 == 0:
            median = (-maxHeap[0] + minHeap[0]) / 2
        else:
            median = float(-maxHeap[0])
        res.append(median)

        return res       

# @lc code=end


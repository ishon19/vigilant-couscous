#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            dist = -(x**2 + y**2)
            heappush(max_heap, (dist, [x, y]))

            if len(max_heap) > k:
                heappop(max_heap)
        
        return [point for (dist, point) in max_heap]
            
# @lc code=end


#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            dist = [(x**2 + y**2), [x, y]]
            heappush(min_heap, dist)

        res = []
        while len(res) != k:
            _, point = heappop(min_heap)
            res.append(point)
        
        return res
# @lc code=end


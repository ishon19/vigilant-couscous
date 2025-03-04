#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isFeasible(k):
            time = 0
            for pile in piles:
                currentTime = ceil(pile / k)
                time += currentTime
            return time <= h

        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2
            if isFeasible(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
            
# @lc code=end


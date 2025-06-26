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
            for items in piles:
                time += ceil(items / k)
            return time <= h
        
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2

            if isFeasible(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
            
# @lc code=end


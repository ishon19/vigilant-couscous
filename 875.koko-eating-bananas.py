#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.k = 0
    
    def isFeasible(self, h, piles, approx):
        time = 0
        for pile in piles:
            time += ceil(pile/approx)
        return time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            rate = (l+r)//2

            if self.isFeasible(h, piles, rate):
                self.k = rate
                r = rate - 1
            else:
                l = rate + 1
        
        return self.k
# @lc code=end


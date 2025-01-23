#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isFeasible(day):
            bouquets = 0
            flowers = 0
            
            for bloomingDays in bloomDay:
                if bloomingDays <= day:
                    



# @lc code=end


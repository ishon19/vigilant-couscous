#
# @lc app=leetcode id=1231 lang=python3
#
# [1231] Divide Chocolate
#

# @lc code=start
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def isFeasible(amount):
            count = 0
            total = 0

            for sweet in sweetness:
                total += sweet
                if total >= amount:
                    count += 1
                    total = 0
            
            return count >= k + 1
        
        left, right = min(sweetness), sum(sweetness) // (k + 1)

        while left < right:
            mid = (left + right) // 2
            if isFeasible(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
# @lc code=end


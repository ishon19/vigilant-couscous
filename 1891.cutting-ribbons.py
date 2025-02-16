#
# @lc app=leetcode id=1891 lang=python3
#
# [1891] Cutting Ribbons
#

# @lc code=start
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if sum(ribbons) < k:
            return 0
        
        left, right = 1, max(ribbons)

        def isFeasible(length):
            pieces = 0
            for ribbon in ribbons:
                pieces += ribbon // length
                if pieces >= k:
                    return True 
            return False
    
        while left < right:
            mid = (left + right + 1) // 2
            if isFeasible(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
        
# @lc code=end


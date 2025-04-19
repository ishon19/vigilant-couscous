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

        def isFeasible(x):
            # how many pieces of length x 
            # can be cut from each ribbon 
            count = 0
            for ribbon in ribbons:
                count += ribbon // x
            return count >= k

        l, r = 1, max(ribbons)

        while l <= r:
            mid = (l + r) // 2

            if isFeasible(mid):
                l = mid + 1
            else:
                r = mid -1 
        
        return r
        
# @lc code=end


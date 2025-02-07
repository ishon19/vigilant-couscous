#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1

        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1
        prod = x

        while n > 0:
            if n % 2 == 1:
                res *= prod
            prod *= prod
            n //= 2

        return res
# @lc code=end


#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        a = a & mask
        b = b & mask 

        while b != 0:
            carry = (a & b) & mask # Find position that generates carry
            a = (a ^ b) & mask # Add without carries
            b = (carry << 1) & mask # Carries for the next iteration
        
        return a
        
# @lc code=end


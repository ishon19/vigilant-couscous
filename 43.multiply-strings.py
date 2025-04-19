#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        value = 0
        i, j = len(num1)-1, len(num2)-1
        carry = 0 

        while i or j or carry:
            current = (num1[i] if i>=0 else 1) * (num2[j] if j>=0 else 1) + carry 
            carry = current // 10
            value = value * 10 + current % 10
            i -= 1
            j -= 1

        return str(value)[::-1]
            
        
# @lc code=end


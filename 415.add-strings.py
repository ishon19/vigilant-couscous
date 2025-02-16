#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            x1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            x2 = ord(num2[j]) - ord('0') if j >=0  else 0

            total = x1 + x2 + carry
            carry = total // 10
            digit = total % 10

            res.append(str(digit))
            i -= 1
            j -= 1

        return ''.join(res[::-1])
            
# @lc code=end


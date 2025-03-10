#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            count = 0
            num = i
            while num:
                num &= num - 1
                count += 1
            res.append(count)
        return res
        
# @lc code=end


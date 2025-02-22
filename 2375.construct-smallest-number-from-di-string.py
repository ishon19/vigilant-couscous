#
# @lc app=leetcode id=2375 lang=python3
#
# [2375] Construct Smallest Number From DI String
#

# @lc code=start
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        nums = []
        start = 1

        for char in pattern:
             nums.append(start)
             start += 1

             if char == 'I':
                while nums:
                    stack.append(nums.pop())
        
        nums.append(start)
        while nums:
            stack.append(nums.pop())
        
        return ''.join(map(str, stack))
# @lc code=end


#
# @lc app=leetcode id=1762 lang=python3
#
# [1762] Buildings With an Ocean View
#

# @lc code=start
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for i, height in enumerate(heights):
            if stack:
                while height > stack[-1]:
                    stack.pop()
            else:
                stack.append(i)
        
        return stack

# @lc code=end


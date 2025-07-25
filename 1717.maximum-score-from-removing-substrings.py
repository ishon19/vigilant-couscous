#
# @lc app=leetcode id=1717 lang=python3
#
# [1717] Maximum Score From Removing Substrings
#

# @lc code=start
class Solution:
    def getPoints(self, s, stack, lookup, point):
        points = 0
        
        for c in s:
            if stack and stack[-1] + c == lookup:
                stack.pop()
                points += point
            else:
                stack.append(c)
        
        return points
    
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        maxGain = 0
        
        maxGain += self.getPoints(s, stack, "ab" if x > y else "ba", x if x > y else y)
        maxGain += self.getPoints(''.join(stack), [], "ba" if x > y else "ab", y if x > y else x)
        
        return maxGain
                
# @lc code=end
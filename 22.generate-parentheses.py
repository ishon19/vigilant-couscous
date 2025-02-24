#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(openCount, closedCount, path, res):
            if len(path) == 2 * n:
                res.append(path)
                return 
            
            if openCount < n:
                backtrack(openCount + 1, closedCount, path + '(', res)
            
            if closedCount < openCount:
                backtrack(openCount, closedCount + 1, path + ')', res)
            
        res = []
        backtrack(0, 0, '', res)
        return res
# @lc code=end


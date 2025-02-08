#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        stack = []

        for part in parts:
            if part == '.' or part == '':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        return '/' + '/'.join(stack)
# @lc code=end


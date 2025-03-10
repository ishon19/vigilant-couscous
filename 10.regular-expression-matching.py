#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            matched = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if (j + 1) < len(p) and p[j+1] == '*':
                return dfs(i, j+2) or (matched and dfs(i+1, j))

            return matched and dfs(i+1, j+1)

        return dfs(0, 0)
# @lc code=end


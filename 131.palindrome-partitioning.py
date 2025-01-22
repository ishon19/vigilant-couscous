#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def dfs(index):
            if index == len(s):
                res.append(path[:])
                return 

            for end in range(index, len(s)):
                if isPalindrome(index, end):
                    path.append(s[index:end+1])
                    dfs(end+1)
                    path.pop()
        
        dfs(0)
        return res
# @lc code=end


#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        charMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        path = []

        def dfs(idx):
            if idx == len(digits):
                res.append("".join(path))
                return

            for char in charMap[digits[idx]]:
                path.append(char)
                dfs(idx + 1)
                path.pop()

        dfs(0)
        return res


# @lc code=end

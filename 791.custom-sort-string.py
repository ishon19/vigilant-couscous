#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        res = ""

        for char in order:
            res += char * counter[char]
            del counter[char]

        
        if counter:
            for key, value in counter.items():
                res += key * value

        return res
# @lc code=end


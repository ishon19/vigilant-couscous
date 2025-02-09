#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        res = []

        for char in order:
            if char in counter:
                res.append(char * counter[char])
                del counter[char]
        
        for char, count in counter.items():
            res.append(char * count)
        
        return "".join(res)
# @lc code=end


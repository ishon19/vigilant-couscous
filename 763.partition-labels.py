#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurances = {char: idx for idx, char in enumerate(s)}
        res = []

        start, end = 0, 0

        for i, char in enumerate(s):
            end = max(end, last_occurances[char])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        
        return res
        
# @lc code=end


#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = defaultdict(list)

        for i, c in enumerate(s):
            counts[c].append(i)
        
        uniques = list(indices for indices in counts.values() if len(indices) == 1)
        # print('uniques', uniques)
        lowest = float("inf")
        for indices in uniques:
            for idx in indices:
                lowest = min(lowest, idx)
        
        return lowest if lowest != float("inf") else -1
                
# @lc code=end


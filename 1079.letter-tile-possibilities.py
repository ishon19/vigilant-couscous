#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#

# @lc code=start
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.res = set()

        def helper(curr, remaining):
            if curr:
                self.res.add(curr)

            for i in range(len(remaining)):
                if i > 0 and remaining[i] == remaining[i-1]:
                    continue
                helper(curr + remaining[i], remaining[:i] + remaining[i+1:])
        
        helper("", sorted(tiles))
        return len(self.res)

# @lc code=end


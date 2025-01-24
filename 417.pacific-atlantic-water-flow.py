#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # base checks
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        altanlic = set()

        def dfs(row, col, seen):
            seen.add((row, col))

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = row + dr, col + dc
                if (nr, nc) not in seen and \
                nr in range(rows) and nc in range(cols) and \
                heights[nr][nc] >= heights[row][col]:
                    dfs(nr, nc, seen)
        
        # start dfs from each of the edges
        for i in range(rows):
            dfs(i, 0, pacific)
        for j in range(cols):
            dfs(0, j, pacific)
        
        # bottom and right
        for i in range(rows):
            dfs(i, cols-1, altanlic)
        for j in range(cols):
            dfs(rows-1, j, altanlic)
        
        return list(pacific & altanlic)

# @lc code=end


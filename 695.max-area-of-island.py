#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(row, col):
            if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                grid[row][col] = 0
                
                area = 1
                for dr, dc in [(-1,0), (0,-1), (1,0), (0,1)]:
                    nr, nc = row + dr, col + dc
                    area += dfs(nr, nc)
                return area
            return 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))
        return res

# @lc code=end


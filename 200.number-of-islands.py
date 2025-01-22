#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def dfs(self, row, col):
        if 0<=row<self.rows and 0<=col<self.cols and self.grid[row][col] == '1':
            dirs = [(0,1),(1,0),(0,-1),(-1,0)]
            self.grid[row][col] = '0'
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                self.dfs(nr, nc)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == "1":
                    self.res += 1
                    # perform a dfs from this point
                    self.dfs(r, c)

        return self.res
        
# @lc code=end


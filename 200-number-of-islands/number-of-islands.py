class Solution:
    def dfs(self, grid, row, col):
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,-1), (0,1)]
        if 0<=row<rows and 0<=col<cols and grid[row][col] == '1':
            grid[row][col] = '0'
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc        
                self.dfs(grid, nr, nc)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    res += 1
                    self.dfs(grid, row, col)       
        return res
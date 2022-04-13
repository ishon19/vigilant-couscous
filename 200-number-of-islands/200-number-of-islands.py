class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        num_islands = 0
        
        def dfs(r,c):
            grid[r][c] = '0'
            if(r+1 < rows and grid[r+1][c] == '1'): dfs(r+1,c)
            if(c+1 < cols and grid[r][c+1] == '1'): dfs(r,c+1)
            if(r-1 >= 0 and grid[r-1][c] == '1'): dfs(r-1,c)
            if(c-1 >= 0 and grid[r][c-1] == '1'): dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)
        
        return num_islands
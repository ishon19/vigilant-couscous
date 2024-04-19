class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:    
        rows, cols = len(grid), len(grid[0])
        
        def dfs(row, col):
            if row in range(rows) and col in range(cols) and grid[row][col] != '0':
                # mark this point as visited
                grid[row][col] = '0'

                # traverse all of the directions
                dfs(row, col+1)
                dfs(row, col-1)
                dfs(row - 1, col)
                dfs(row + 1, col)            
        
        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    ans += 1
                    dfs(row, col)
        
        return ans
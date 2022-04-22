class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid)<=0:
            return 0
        
        ans, cols, rows = 0, len(grid[0]), len(grid)
        
        def dfs(r,c):
            if(r<0 or c<0 or r>=rows or c>= cols or grid[r][c]==0):
                return False
            
            grid[r][c] = 0
            up = dfs(r-1,c)
            down = dfs(r+1, c)
            right = dfs(r,c+1)
            left = dfs(r,c-1)
            
            return up and down and right and left
        
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==1 and (r==0 or c==0 or r==rows-1 or c==cols-1)):
                    dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 1):
                    ans+=1
            
        return ans
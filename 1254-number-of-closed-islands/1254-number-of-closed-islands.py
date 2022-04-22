class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:        
        ans, cols, rows = 0, len(grid[0]), len(grid)
        # withInBoundary = lambda r,c: 0<r<rows-1 and 0<c<cols-1
        
        def dfs(r,c):
            if(r<0 or c<0 or r>=rows or c>=cols):
                return False;          
            if grid[r][c] == 1:
                return True
            grid[r][c] = 1
            up = dfs(r-1,c)
            down = dfs(r+1,c)
            left = dfs(r,c-1)
            right = dfs(r,c+1)
            return up and down and left and right
                                
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    if dfs(i,j): ans += 1
        
        return ans
        
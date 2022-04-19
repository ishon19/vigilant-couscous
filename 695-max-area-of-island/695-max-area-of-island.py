class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r,c):
            # bounds check
            if((r<0 or r>=rows) or (c<0  or  c>=cols)): return 0
            # already visited check
            if(grid[r][c] == 0): return 0
            # mark as visited and perform the dfs
            grid[r][c] = 0
            return 1+dfs(r,c-1)+dfs(r-1,c)+dfs(r+1,c)+dfs(r,c+1)
        
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 1):
                    maxArea = max(maxArea, dfs(r,c))
        
        return maxArea
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid1 or not grid2:
            return 0

        rows, cols = len(grid1), len(grid1[0])
        ans = 0

        def dfs(r, c):
            if r in range(rows) and c in range(cols):
                
                if grid2[r][c] != 1:
                    return
                
                grid2[r][c] = 0
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c+1)
                dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid1[r][c] == 0 and grid2[r][c] == 1:
                    dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    dfs(r,c)
                    ans += 1
        
        return ans



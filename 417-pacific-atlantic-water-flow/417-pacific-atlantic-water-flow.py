class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r,c,v,l):
            if (r,c) in v or r==rows or c==cols or c<0 or r<0 or heights[r][c]<l:
                return            
            v.add((r,c))
            
            dfs(r+1,c,v,heights[r][c])
            dfs(r,c-1,v,heights[r][c])
            dfs(r,c+1,v,heights[r][c])
            dfs(r-1,c,v,heights[r][c])
        
        # start off from the first and the last row
        for c in range(cols):
            # since pacific is at the top
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res
            
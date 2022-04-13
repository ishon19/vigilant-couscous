class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        cur_color = image[sr][sc]
        
        # if we have already colored return
        if newColor == cur_color:
            return image
        
        # else perform dfs
        def dfs(r, c):
            if image[r][c] == cur_color:
                image[r][c] = newColor
                if r>=1: dfs(r-1,c)
                if r+1<rows: dfs(r+1, c)
                if c>=1: dfs(r, c-1)
                if c+1 < cols: dfs(r, c+1)
        
        dfs(sr, sc)
        return image
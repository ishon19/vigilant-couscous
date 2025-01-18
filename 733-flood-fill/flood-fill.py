class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        old_color = image[sr][sc]
        
        # if already colored, return 
        if old_color == color:
            return image  

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and image[r][c] == old_color:
                image[r][c] = color 
                for dr, dc in dirs:
                    dfs(r + dr, c + dc)
        dfs(sr, sc)
        return image
        """
            # rows, cols = len(image), len(image[0])
            # def dfs(r, c):
            #     if 1<=r<rows and 1<=c<cols and image[r][c] == image[sr][sc]:
            #         image[r][c] = color
            #         dfs(r+1, c)
            #         dfs(r-1, c)
            #         dfs(r, c+1)
            #         dfs(r, c-1)
            # dfs(sr, sc)
            # return image
        """
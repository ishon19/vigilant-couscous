class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        originalColor = image[sr][sc]

        def dfs(row, col):
            if row in range(rows) and col in range(cols) and image[row][col] == originalColor and image[row][col] != color:
                image[row][col] = color

                for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr, nc = row + dr, col + dc
                    dfs(nr, nc)
        
        dfs(sr, sc)
        return image
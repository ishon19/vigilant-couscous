class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue

                temp = 0
                for x, y in dirs:
                    if 0<=(r+x)<len(grid) and 0<=(c+y)<len(grid[0]):
                        if grid[r+x][c+y] == 0: temp += 1
                    else:
                        temp += 1
                perimeter += temp
        
        return perimeter
                    

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        res = []

        def get_rect(r, c):
            x2, y2 = r, c

            # Expand downwards
            while x2 + 1 < rows and land[x2 + 1][c] == 1:
                x2 += 1
                
            # Expand rightwards
            while y2 + 1 < cols and all(land[x][y2 + 1] == 1 for x in range(r, x2 + 1)):
                y2 += 1

            # set all the digit in the rect to 0
            for i in range(r, x2+1):
                for j in range(c, y2+1):
                    land[i][j] = 0
            
            return [r, c, x2, y2]
        
        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1:
                    res.append(get_rect(r, c))
        
        return res
             
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        
        rows, cols = len(mat), len(mat[0])
        res = []
        row, col = 0, 0
        direction = 1

        while len(res) < rows * cols:
            res.append(mat[row][col])

            if direction == 1:
                if col == cols-1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:
                if row == rows-1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1
        
        return res
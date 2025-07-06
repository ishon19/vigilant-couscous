class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        diagonalMap = defaultdict(set)

        for row in range(rows):
            for col in range(cols):
                diagonalMap[row-col].add(matrix[row][col])
        
        print(diagonalMap)
        
        for key, val in diagonalMap.items():
            if len(val) != 1:
                return False 
        return True

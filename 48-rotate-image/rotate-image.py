class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # base case
        if not matrix or len(matrix) != len(matrix[0]):
            return matrix
            
        n = len(matrix)
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            
            for i in range(first, last):
                offset = i - first
                
                # Save top
                top = matrix[first][i]
                
                # Left -> Top
                matrix[first][i] = matrix[last - offset][first]
                
                # Bottom -> Left
                matrix[last - offset][first] = matrix[last][last - offset]
                
                # Right -> Bottom
                matrix[last][last - offset] = matrix[i][last]
                
                # Top -> Right
                matrix[i][last] = top
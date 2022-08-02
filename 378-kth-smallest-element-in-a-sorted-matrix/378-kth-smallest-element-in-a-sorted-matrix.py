class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def flatten(matrix):
            mat = []
            
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    mat.append(matrix[i][j])        
            mat.sort()
            return mat
        
        flat = flatten(matrix)
        
        return flat[k-1]
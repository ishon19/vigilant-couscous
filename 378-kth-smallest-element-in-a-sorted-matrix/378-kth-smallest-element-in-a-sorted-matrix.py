class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat = []
        
        for i in range(len(matrix)):
            flat += matrix[i]
        
        flat.sort()
        
        return flat[k-1]
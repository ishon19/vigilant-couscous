class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:           
        r,c = len(matrix), len(matrix[0])
        temp = [[0 for j in range(r)] for i in range(c)]        
        for i in range(c):
            for j in range(r):
                temp[i][j] = matrix[j][i]
        matrix = temp
        return matrix
                    
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:           
        r,c = len(matrix), len(matrix[0])        
        if r == c:
            for i in range(r):
                for j in range(c):
                    if j<i:                    
                        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  
        else:
            temp = [[0 for j in range(r)] for i in range(c)]
            print(temp)
            for i in range(c):
                for j in range(r):
                    temp[i][j] = matrix[j][i]
            matrix = temp
        return matrix
                    
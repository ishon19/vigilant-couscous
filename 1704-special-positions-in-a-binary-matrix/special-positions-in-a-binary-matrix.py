class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def checkRowColZeros(row, col):
            if mat[row][col] != 1:
                return False
            
            # row check 
            for i in range(len(mat)):
                if i != row and mat[i][col] != 0:
                    return False
            
            # col check 
            for j in range(len(mat[0])):
                if j != col and mat[row][j] != 0:
                    return False
            
            return True
            
        
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if checkRowColZeros(i, j):
                    count += 1
        return count
from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)    
        d1 = [mat[x][y] for x in range(l) for y in range(l) if x == y]
        d2 = [mat[x][l-1-x] for x in range(l)]
        if l%2 != 0:
            d1.remove(d1[(len(d1)//2)])
        d1.extend(d2)        
        return sum(d1)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans, rows, cols = 0, len(matrix), len(matrix[0])        
        cache = {}
        
        def helper(r, c):
            # bounds check
            if r>=rows or c>=cols:
                return 0
                            
            if (r,c) not in cache:
                cache[(r,c)] = 0                
                down = helper(r+1,c)
                diag = helper(r+1, c+1)
                right = helper(r,c+1)
                if matrix[r][c] == '1':
                    cache[(r,c)] = min(down, diag, right) + 1
            return cache[(r,c)]
        
        helper(0,0)
        # print(cache)
        return max(cache.values()) ** 2
                
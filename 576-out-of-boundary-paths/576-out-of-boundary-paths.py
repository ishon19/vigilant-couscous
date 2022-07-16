class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:                            
        @cache
        def dfs(moves,i,j):
            # bounds check
            if (i==m or j==n or i<0 or j<0):
                return 1
            # max moves check
            elif moves==0:
                return 0
            # perform dfs in all the directions
            ans = 0
            ans +=  (dfs(moves-1,i - 1, j) + dfs(moves-1,i + 1, j) + dfs(moves-1,i, j - 1) + dfs(moves-1,i, j + 1))%(1000000007)
            return ans
        
        return dfs(maxMove, startRow, startColumn)
        
        
        
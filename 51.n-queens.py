#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col_set = set()
        pos_diag = set()
        neg_diag = set()
        grid = [['.'] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in grid])
                return 
        
            for col in range(n):
                pd = row + col
                nd = row - col

                if col in col_set or pd in pos_diag or nd in neg_diag:
                    continue
               
                grid[row][col] = 'Q'
                col_set.add(col)
                pos_diag.add(pd)
                neg_diag.add(nd)

                backtrack(row+1)

                grid[row][col] = '.'
                col_set.remove(col)
                pos_diag.remove(pd)
                neg_diag.remove(nd)
        
        backtrack(0)
        return res   
# @lc code=end


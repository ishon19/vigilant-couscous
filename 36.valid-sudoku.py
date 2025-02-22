#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = 9, 9
        rowSet = [set() for _ in range(rows)]
        colSet = [set() for _ in range(cols)]
        boxSet = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rowSet[r] \
                    or board[r][c] in colSet[c] \
                    or board[r][c] in boxSet[r//3][c//3]:
                    return False
                
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                boxSet[r//3][c//3].add(board[r][c])

        return True
# @lc code=end


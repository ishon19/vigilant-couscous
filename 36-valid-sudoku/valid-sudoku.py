class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(r, c, k):
            row_check = board[r].count(k) == 1
            col_check = [board[i][c] for i in range(9)].count(k) == 1
            box_check = [board[i][j] for i in range(r//3*3, r//3*3 + 3) for j in range(c//3*3, c//3*3 + 3)].count(k) == 1
            return row_check and col_check and box_check
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and not isValid(i, j, board[i][j]):
                    return False
        
        return True
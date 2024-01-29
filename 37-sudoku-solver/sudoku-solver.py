class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def checkIfValid(r,c,k):
            not_in_row = k not in board[r]
            not_in_column = k not in [board[i][c] for i in range(9)]
            not_in_box = k not in [board[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)]
            return not_in_row and not_in_column and not_in_box
        
        def solver(r, c):
            if r == 9:
                return True
            elif c == 9:
                return solver(r+1, 0)
            elif board[r][c] != '.':
                return solver(r, c+1)
            else:
                for k in range(1, 10):
                    if checkIfValid(r, c, str(k)):
                        board[r][c] = str(k)
                        if solver(r, c+1):
                            return True
                        board[r][c] = '.'
                return False
        
        solver(0, 0)
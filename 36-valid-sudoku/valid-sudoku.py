class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                curr = board[row][col]
                if curr == '.':
                    continue

                if curr in row_set[row]:
                    return False
                if curr in col_set[col]:
                    return False
                if curr in box_set[row//3][col//3]:
                    return False
                
                row_set[row].add(curr)
                col_set[col].add(curr)
                box_set[row//3][col//3].add(curr)
        
        return True
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        # find the champions of the tournament
        # find a row in the grid that has all ones expect for self
        # or find a column in the grid that has all zeroes expect for self
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            wins = 0
            for j in range(cols):
                if grid[i][j] == 1:
                    wins += 1
            if wins == cols - 1:
                return i
        
        return -1


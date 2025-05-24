class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pattern = [''] * numRows
        direction = 1
        row = 0

        for i in range(len(s)):
            pattern[row] += s[i]
            row = (row + direction) % numRows

            if row == numRows-1 or row == 0:
                direction = -direction
        
        return ''.join(pattern)
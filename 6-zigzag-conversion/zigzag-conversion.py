"""
paypalishiring

rows = 4

p     i   n
a   l s  ig
y a   h r
p     i

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        goingDown = False
        curRow = 0

        for char in s:
            rows[curRow] += char            
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
        
        return "".join(rows)

        
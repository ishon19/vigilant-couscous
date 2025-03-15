class Solution:
    def checkValidString(self, s: str) -> bool:
        open_max, open_min = 0, 0

        for char in s:
            if char == '(':
                open_max += 1
                open_min += 1
            elif char == ')':
                open_min -= 1
                open_max -= 1
            else:
                open_min -= 1
                open_max += 1
            
            if open_max < 0:
                return False
            
            open_min = max(open_min, 0)
        
        return open_min == 0
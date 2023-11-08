class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        width = abs(fx - sx)
        height = abs(fy - sy)

        if width == 0 and height == 0 and t == 1:
            return False
        
        return t >= max(width, height)
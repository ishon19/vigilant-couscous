class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def search(num):
            l, r = 0, num
            while l <= r:
                mid = (l + r) // 2
                if mid * mid == num:
                    return True
                elif mid * mid > num:
                    r = mid - 1
                else:
                    l = mid + 1
            
        a = 0
        while a * a <= c:
            b = c - a * a # check if c - a^2 is perfect square
            if search(b):
                return True
            a += 1
        return False
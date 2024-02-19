class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            # print(n)
            n = n / 2.0
        return n == 1.0
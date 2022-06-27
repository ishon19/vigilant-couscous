class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        
        a, b, c = 0, 1, 1
        
        for i in range(n-2):            
            a = b
            b = c
            c = a + b            
        
        return c
        
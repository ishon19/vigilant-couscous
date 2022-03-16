class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        
        fibo = [0] * (n+1)
        fibo[1] = 1
        
        for i in range(2, n+1):
            fibo[i] =   fibo[i-1] + fibo[i-2]
        
        return fibo[n]
        
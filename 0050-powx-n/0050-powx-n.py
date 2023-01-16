class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case 
        if n == 0:
            return 1.0
        
        def fastPow(x, n):
            # base case 
            if n == 0:
                return 1.0
            if n<0:
                n = -n
                x = 1/x
            half = fastPow(x,n//2)
            if n%2 == 0:
                return half*half
            return half*half*x
        
        return fastPow(x, n)
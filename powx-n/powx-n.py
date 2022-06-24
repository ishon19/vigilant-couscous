class Solution:
    def myPow(self, x: float, n: int) -> float:        
        x = 1/x if n<0 else x
        n = -n if n<0 else n
        def helper(n):
            if n==0:
                return 1.0
            half = helper(math.floor(n/2))
            if n%2==0:
                return half * half
            else:
                return half * half * x
        return helper(n)
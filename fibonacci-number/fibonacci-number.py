class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        cache = {}
        
        def helper(num):
            if num in cache:
                return cache[num]
            
            if num<2:
                return num
            
            val =  helper(num-1) + helper(num-2)
            
            cache[num] = val
            
            return val
        
        return helper(n)
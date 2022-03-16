class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=0:
            return 0
        elif(n==1):
            return 1
        elif n==2:
            return 1
        
        tribo = [0] * (n+2)
        tribo[1] = 1
        tribo[2] = 1
        
        for i in range(3, n+2):
            tribo[i] = tribo[i-1] + tribo[i-2] + tribo[i-3]
        
        return tribo[n]
        
        
        
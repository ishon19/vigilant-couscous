class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = 0
        total = 0
        banned = set(banned)

        for num in range(1, n+1):
            if num not in banned:
                if total + num <= maxSum:
                    total += num
                    res += 1  
                else:
                    break      
        return res

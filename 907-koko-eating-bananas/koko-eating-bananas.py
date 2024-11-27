class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, res = 1, 10**9, -1

        def isFeasible(k):
            hours = 0
            for p in piles:
                hours += ceil(float(p)/k)
            return hours <= h
        
        while l<=r:
            mid = (l+r)//2
            if isFeasible(mid):
                r = mid - 1
                res = mid
            else:
                l = mid + 1        
        return res
            
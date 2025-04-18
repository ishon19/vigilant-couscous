# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if isBadVersion(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        res = 0

        while l <= r:
            res = max(res, (min(maxl, maxr) * (r - l)))
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
            else:
                r -= 1
                maxr = max(maxr, height[r])            
        
        return res
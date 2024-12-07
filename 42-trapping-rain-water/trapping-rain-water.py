class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        res = 0

        while l < r:
            if maxr < maxl:
                r -= 1
                maxr = max(maxr, height[r])
                res += maxr - height[r]
            else:
                l += 1
                maxl = max(maxl, height[l])
                res += maxl - height[l]

        return res 
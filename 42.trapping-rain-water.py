#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
       l, r = 0, len(height)-1
       trapped = 0
       maxl, maxr = height[l], height[r]

       while l < r:
           if height[l] < height[r]:
               maxl = max(maxl, height[l])
               trapped += maxl - height[l]
               l += 1
           else:
               maxr = max(maxr, height[r])
               trapped += maxr - height[r] 
               r -= 1
       
       return trapped
        
# @lc code=end


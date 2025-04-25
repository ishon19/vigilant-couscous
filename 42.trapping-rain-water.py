#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
       l, r = 0, len(height)-1
       res = 0
       maxl, maxr = height[l], height[r]

       while l <= r:
           if height[l] < height[r]:
              res = max(res, res + maxl - height[l])
              maxl = max(maxl, height[l])
              l += 1
           else:
              res = max(res, res + maxr - height[r])
              maxr = max(maxr, height[r])
              r -= 1
        
       return res
          
# @lc code=end


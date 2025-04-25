#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        l, r = 0, x

        while l <= r:
            px = (l + r) // 2
            py = (x + y + 1) // 2 - px

            left1 = float("-inf") if px == 0 else nums1[px-1]
            right1 = float("inf") if px == x else nums1[px]

            left2 = float("-inf") if py == 0 else nums2[py-1]
            right2 = float("inf") if py == y else nums2[py]

            if left1 <= right2 and right1 >= left2:
                if (x + y) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                r = px - 1
            else:
                l = px + 1
        
        return -1          
        
# @lc code=end


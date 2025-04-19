#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m-1, n-1, m+n-1

        while i>=0:
            if j>=0 and nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                i -= 1
            else:
                nums1[k] = nums1[i]
                j -= 1
            k -= 1
# @lc code=end


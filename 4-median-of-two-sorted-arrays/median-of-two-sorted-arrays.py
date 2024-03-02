class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        # binary search the smaller array
        l, r = 0, m

        while l <= r:
            i = (l + r) // 2
            j = half - i

            nums1maxLeft = float("-inf") if i == 0 else nums1[i-1]
            nums1minRight = float("inf") if i == m else nums1[i]
            
            nums2maxLeft = float("-inf") if j == 0 else nums2[j-1]
            nums2minRight = float("inf") if j == n else nums2[j]

            if nums1maxLeft <= nums2minRight and nums2maxLeft <= nums1minRight:
                if total % 2 == 0:
                    return (max(nums1maxLeft, nums2maxLeft) + min(nums1minRight, nums2minRight)) / 2
                return max(nums1maxLeft, nums2maxLeft)
            elif nums1maxLeft > nums2minRight:
                r = i - 1
            else:
                l = i + 1
        
        
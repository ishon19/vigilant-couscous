class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        nums1.sort()
        nums2.sort(reverse=True)
        for i,j in zip(nums1, nums2):
            ans += i*j
        return ans
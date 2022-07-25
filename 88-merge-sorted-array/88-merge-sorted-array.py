class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if 0 not in nums1:
            return nums1
        zIndex = nums1.index(0)
        l1 = len(nums1) - len(nums2)
        for i in range(len(nums2)): nums1[l1+i] = nums2[i]
        nums1.sort()
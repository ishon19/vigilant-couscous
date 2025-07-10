class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num_not_in_n1 = set()
        num_not_in_n2 = set()

        for num in nums2:
            if num not in nums1:
                num_not_in_n1.add(num)
        
        for num in nums1:
            if num not in nums2:
                num_not_in_n2.add(num)

        return [list(num_not_in_n2), list(num_not_in_n1)]
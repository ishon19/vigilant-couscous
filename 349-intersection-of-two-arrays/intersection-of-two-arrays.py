class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
            nums2, nums1 = nums1, nums2
        
        hashmap = collections.Counter(nums1)
        res = []

        for num in nums2:            
            if num in hashmap:
                res.append(num)
        
        return list(set(res))
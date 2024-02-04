class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = collections.defaultdict(int)

        for num in nums2:
            if not stack:
                stack.append(num)
            else:
                while stack and stack[-1] < num:
                    hashmap[stack.pop()] = num
                stack.append(num)
        
        while stack:
            hashmap[stack.pop()] = -1
        
        res = [0] * len(nums1)
        for i, num in enumerate(nums1):
            res[i] = hashmap[num]
        return res
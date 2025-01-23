class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums) 

        for _ in range(2):
            for idx, num in enumerate(nums):
                while stack and num > nums[stack[-1]]:
                    res[stack.pop()] = num
                stack.append(idx)
        
        return res
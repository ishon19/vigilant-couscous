from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [x for x in nums if x!=0]
        temp.extend([0] * (len(nums) - len(temp)))
        for i in range(len(temp)):
            nums[i] = temp[i]
        return nums 
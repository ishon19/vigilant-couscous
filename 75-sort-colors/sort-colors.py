class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        middle = 0
        high = len(nums) - 1

        while middle <= high:
            if nums[middle] == 0:
                nums[middle], nums[low] = nums[low], nums[middle]
                low += 1
                middle += 1
            elif nums[middle] == 1:
                middle += 1
            else:
                nums[high], nums[middle] = nums[middle], nums[high]
                high -= 1

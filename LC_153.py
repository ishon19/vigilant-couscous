class Solution:
    def findMin(self, nums: List[int]) -> int:        
        low = 0
        high = len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]
        
        if nums[low]<nums[high]:
            return nums[low]
        
        while low <= high:
            mid = low + (high-low)//2
            # if found the inflection point then return the value
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[low] < nums[mid]:
                low = mid + 1                
            else:
                high = mid - 1
        
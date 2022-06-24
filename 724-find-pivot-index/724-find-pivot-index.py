class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)        
        for i in range(len(nums)):            
            if (total-nums[i])%2==0:                
                left_sum = sum(nums[0:i])
                right_sum = sum(nums[i+1:len(nums)])                
                if left_sum == right_sum:
                    return i                
        return -1
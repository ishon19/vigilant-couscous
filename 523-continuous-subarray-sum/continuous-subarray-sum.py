class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cache = {0:-1}
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            remainder = curr_sum % k

            if remainder in cache:
                if i - cache[remainder] >= 2:
                    return True 
            else:
                cache[remainder] = i
        
        return False 

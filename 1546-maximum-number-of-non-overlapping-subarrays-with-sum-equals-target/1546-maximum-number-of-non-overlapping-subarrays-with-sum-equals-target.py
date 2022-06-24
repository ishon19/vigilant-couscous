class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefixMap = {}
        prefixMap[0] = -1
        
        prefixSum = 0
        lastIdx = -1
        ans = 0
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            
            if (prefixSum - target) in prefixMap and prefixMap[prefixSum - target] >= lastIdx:                
                lastIdx = i
                ans+=1
            prefixMap[prefixSum] = i
        return ans
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
            
        @cache
        def robFrom(houseIndex, costs):
            if houseIndex >= len(costs):
                return 0
            return max(costs[houseIndex] + robFrom(houseIndex+2, costs), robFrom(houseIndex+1,costs))
        
        return max(robFrom(0, tuple(nums[1:])), robFrom(0, tuple(nums[:-1])))
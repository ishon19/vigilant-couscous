class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        imposter = 0 

        for num in nums:
            imposter = imposter ^ num
        
        return imposter
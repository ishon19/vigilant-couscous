class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # TLE
        # res, i, window = 0, 0, 0
        # prod = 1
        # while i < len(nums):                        
        #     if i + window < len(nums) and prod < k:  
        #         # print('arr', nums[i: i + window + 1])          
        #         prod *= nums[i + window]
        #         if prod >= k:
        #             continue
        #         res += 1
        #         window += 1
        #     else:
        #         window = 0
        #         i += 1
        #         prod = 1
        # return res
        if k <= 1:
            return 0
             
        res = 0
        prod = 1
        l = 0
        for r, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod //= nums[l]
                l += 1
            res += r - l + 1
        return res
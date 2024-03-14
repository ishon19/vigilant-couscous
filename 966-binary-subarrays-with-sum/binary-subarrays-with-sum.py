class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # brute force
        # res = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if sum(nums[i:j+1]) == goal:
        #             res += 1
        #         elif nums[i] + nums[j] > goal:
        #             break        
        # return res

        # prefix sum way
        res = 0
        cur_sum = 0

        freq = {0: 1}

        for num in nums:
            cur_sum += num
            target_sum = cur_sum - goal
            res += freq.get(target_sum, 0)
            freq[cur_sum] = freq.get(cur_sum, 0) + 1
            
        return res

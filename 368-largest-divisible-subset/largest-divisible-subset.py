class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # nums.sort() 
        # memo = {}

        # def recurse(index, prev_index):
        #     if index == len(nums):
        #         return []
            
        #     if (index, prev_index) in memo:
        #         return memo[(index, prev_index)]
                
        #     included = []
        #     if prev_index == -1 or nums[index] % nums[prev_index] == 0:
        #         included = [nums[index]] + recurse(index + 1, index)
        #     not_included = recurse(index + 1, prev_index)
        #     # Choose the longer subset
        #     memo[(index, prev_index)] = included if len(included) > len(not_included) else not_included
        #     return memo[(index, prev_index)]

        # return recurse(0, -1)
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)

        dp = [1] * n
        prev = [-1] * n

        max_size = 1
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_idx = i
        
        results = []
        while max_idx>=0:
            results.append(nums[max_idx])
            max_idx = prev[max_idx]
        return results[::-1]



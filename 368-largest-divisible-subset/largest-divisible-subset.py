class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort() 
        memo = {}

        def recurse(index, prev_index):
            if index == len(nums):
                return []
            
            if (index, prev_index) in memo:
                return memo[(index, prev_index)]
                
            included = []
            if prev_index == -1 or nums[index] % nums[prev_index] == 0:
                included = [nums[index]] + recurse(index + 1, index)
            not_included = recurse(index + 1, prev_index)
            # Choose the longer subset
            memo[(index, prev_index)] = included if len(included) > len(not_included) else not_included
            return memo[(index, prev_index)]

        return recurse(0, -1)


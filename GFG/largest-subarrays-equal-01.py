'''
Problem Link
https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/
https://leetcode.com/problems/contiguous-array/

Description
Given an array containing only 0s and 1s, find the largest subarray which contains equal no of 0s and 1s. The expected time complexity is O(n).
'''

'''
Naive Approach
Check all the possible subarrays, take the cumulative sum of 0 as -1 and 1 as 1,
if the sum reaches 0 then this subarray contains the equal number of 0s and 1s.

Optimal approach
Use hashmap
'''

def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if i == 0 else i for i in nums]
        cache = {}
        # print('modified nums', nums)
        res = 0
        cur = 0
        endingIdx = -1

        for i in range(len(nums)):
            cur += nums[i]
            if cur == 0:
                res = i + 1 # since contiguous
                endingIdx = i
            if cur in cache:
                if res<i-cache[cur]:
                    res = i - cache[cur]
                    endingIdx = i
            else:
                cache[cur] = i
        return res


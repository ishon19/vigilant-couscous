#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # more unsorted the array is, lesser chunks we need
        # if it's sorted we need to chunk it for maximization
        res = 0
        seen = [0] * len(arr)
        maxIdx = 0

        for num in arr:
            maxIdx = max(maxIdx, num)
            seen[num] = 1

            if sum(seen[:maxIdx+1]) == maxIdx+1:
                res += 1
        
        return res        
# @lc code=end


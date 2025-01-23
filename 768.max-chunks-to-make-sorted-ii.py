#
# @lc app=leetcode id=768 lang=python3
#
# [768] Max Chunks To Make Sorted II
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
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


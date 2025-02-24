#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            bucket[freq].append(num)
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            result.extend(bucket[i])
            if len(result) >= k:
                return result[:k]
            
        return result[:k]
        
# @lc code=end


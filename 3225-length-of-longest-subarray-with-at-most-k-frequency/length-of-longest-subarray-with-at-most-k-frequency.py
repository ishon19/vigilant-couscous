class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        start = -1
        counter = collections.defaultdict(int)

        for end in range(len(nums)):
            counter[nums[end]] += 1

            while counter[nums[end]] > k:
                start += 1
                counter[nums[start]] -= 1
            
            res = max(res, end - start)
        
        return res
        

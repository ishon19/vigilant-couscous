class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        ans = 0
        for k,v in counter.items():
            if v == 1:
                return -1
            ans += ceil(v/3)
        return ans
            
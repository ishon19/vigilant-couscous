class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(prefix[-1] + num)
        
        suffix = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            suffix.append(suffix[-1]+ nums[i])
        suffix = suffix[::-1]

        res = 0
        for i in range(len(nums)-1):
            if prefix[i] >= suffix[i+1]:
                res += 1
        return res
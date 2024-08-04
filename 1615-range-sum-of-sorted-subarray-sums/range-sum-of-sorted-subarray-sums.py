class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []

        for i in range(len(nums)):
            runSum = 0
            for j in range(i, len(nums)):
                runSum += nums[j]
                sums.append(runSum)        
        sums.sort()
        return sum(sums[left-1: right]) % 1000000007
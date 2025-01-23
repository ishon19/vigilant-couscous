#
# @lc app=leetcode id=2357 lang=python3
#
# [2357] Make Array Zero by Subtracting Equal Amounts
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        self.res = 0
        self.zeros = 0

        pq = []
        for num in nums:
            if num == 0:
                self.zeros += 1
            else:
                pq.append(num)
        heapify(pq)


        while pq:
            num = heappop(pq)
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= num
                    if nums[i] == 0:
                        self.zeros += 1
            heapify(pq)
            print(nums)
            self.res += 1

        return self.res
# @lc code=end


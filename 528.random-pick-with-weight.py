#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        self.totalWeight = 0
        self.prefix_sums = []

        for weight in w:
            self.totalWeight += weight
            self.prefix_sums.append(self.totalWeight)
    
    def pickIndex(self) -> int:
        target = random.randint(1, self.totalWeight)

        low, high = 0, len(self.prefix_sums) - 1
        while low < high:
            mid = (low + high) // 2
            if self.prefix_sums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end


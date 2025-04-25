class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.counts = defaultdict(list)

        for i, num in enumerate(self.nums):
            self.counts[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.counts[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
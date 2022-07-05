class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr, best = 0, 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                curr = 1
                temp = num

                while (temp + 1) in num_set:
                    temp += 1
                    curr += 1

                best = max(best,curr)
        return best
        
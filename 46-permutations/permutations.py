class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # the only difference from combinations is that we can not reuse the same elements here
        res = []
        path = []
        used = [False] * len(nums)

        def dfs(start_index):
            if start_index == len(nums):
                # append the copy not the reference
                res.append(path[:])
                return

            for idx, num in enumerate(nums):
                if used[idx]:
                    continue
                path.append(num)
                used[idx] = True
                dfs(start_index + 1)
                path.pop()
                used[idx] = False
        dfs(0)
        return res

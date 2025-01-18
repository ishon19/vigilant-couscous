class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        or_table = [[0] * n for _ in range(n)]

        # Precalculate OR values
        for i in range(n):
            or_table[i][i] = nums[i]
            for j in range(i + 1, n):
                or_table[i][j] = or_table[i][j - 1] | nums[j]

        start = 0
        res = float("inf")
        val = 0

        for end in range(n):
            val = or_table[start][end]  # Use precalculated value

            while val >= k:
                res = min(res, end - start + 1)
                start += 1
                if start <= end:
                    val = or_table[start][end]  # Update val using the table
                else:
                    break

        return res if res != float("inf") else -1
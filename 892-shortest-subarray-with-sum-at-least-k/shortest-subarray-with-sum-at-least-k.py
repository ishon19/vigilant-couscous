from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], K: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        deque_indices = deque()
        min_length = float('inf')

        for end in range(n + 1):
            # Check if the subarray sum condition is met
            while deque_indices and prefix_sum[end] - prefix_sum[deque_indices[0]] >= K:
                min_length = min(min_length, end - deque_indices.popleft())

            # Maintain monotonicity in the deque
            while deque_indices and prefix_sum[end] <= prefix_sum[deque_indices[-1]]:
                deque_indices.pop()

            # Add the current index to the deque
            deque_indices.append(end)

        return min_length if min_length != float('inf') else -1

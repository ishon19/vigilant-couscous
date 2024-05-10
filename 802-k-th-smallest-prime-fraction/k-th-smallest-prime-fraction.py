class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        return sorted([[[arr[i], arr[j]], arr[i]/arr[j]] for i in range(len(arr)) for j in range(i, len(arr))],key=lambda x: x[1])[k-1][0]
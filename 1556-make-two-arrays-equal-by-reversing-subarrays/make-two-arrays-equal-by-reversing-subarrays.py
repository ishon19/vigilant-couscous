class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr): return False
        if sorted(target) != sorted(arr): return False
        return True
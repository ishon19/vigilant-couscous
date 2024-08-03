class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # sorting
        # if len(target) != len(arr): return False
        # if sorted(target) != sorted(arr): return False
        # return True

        # dictionary
        return collections.Counter(target) == collections.Counter(arr)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        patterns = []

        def generate_subsets(arr):
            if not arr: return [[]]
            subsets = generate_subsets(arr[1:])
            return subsets + [subset + [arr[0]] for subset in subsets]

        subsets = generate_subsets(nums)
        
        for subset in subsets:
            xor = 0
            for num in subset:
                xor = xor ^ num
            res += xor
        return res
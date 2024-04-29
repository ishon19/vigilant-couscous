class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # core idea is to compare the mismatched bits in cumulative xor of nums and k
        final_xor = reduce(xor, nums)
        print(final_xor)

        count = 0
        while k or final_xor:
            if k % 2 != final_xor % 2:
                count += 1
            k //= 2
            final_xor //= 2

        return count
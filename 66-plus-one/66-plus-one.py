class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = [str(i) for i in digits]
        numstr = "".join(nums)
        ans = (int(numstr) + 1)
        return [int(x) for x in str(ans)]
        
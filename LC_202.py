# LC 202 - Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()

        # if n is in nums, then we are in a cyclic loop
        while n not in nums:
            nums.add(n)
            n = sum([int(i)**2 for i in str(n)])
        return n==1
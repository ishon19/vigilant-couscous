class Solution:
    def fractionAddition(self, expression: str) -> str:
       # extract the numbers in the expression
       nums = map(int, re.findall(r'[+-]?\d+', expression))
       Nr, Dr = 0, 1

       for nr in nums:
        dr = next(nums)
        Nr = Nr * dr + nr * Dr
        Dr *= dr
        g = math.gcd(Nr, Dr)
        Nr //= g
        Dr //= g
                
       return "%d/%d" % (Nr, Dr)
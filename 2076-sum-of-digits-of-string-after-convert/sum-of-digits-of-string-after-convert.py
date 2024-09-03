class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''.join(str(ord(c)-96) for c in s)
        print(num_str)
        res = 0
        while k:
            localSum = sum(int(c) for c in num_str)
            res = localSum
            num_str = str(localSum)
            k -= 1
        return res
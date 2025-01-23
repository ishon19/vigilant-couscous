class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        res = 0
        has_odd = False

        for char, count in counts.items():
            if count % 2 != 0:
                has_odd = True
                res += count - 1
            else:
                res += count
                
        return res + 1 if has_odd else res

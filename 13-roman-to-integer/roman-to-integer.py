class Solution:
    def romanToInt(self, s: str) -> int:
        charMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        res = 0        
        
        for i in range(len(s)):
            if i < len(s) - 1 and charMap[s[i+1]] > charMap[s[i]]:
                res -= charMap[s[i]]
            else:
                res += charMap[s[i]]

        return res
class Solution:
    def removeVowels(self, s: str) -> str:
        res = ''
        for char in s:
            if char not in ['a', 'e', 'i', 'o', 'u']:
                res += char
        return res
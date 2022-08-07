class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowelMap = {
            "$": ["a", "e", "i", "o", "u"],
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"]
        }
        
        @cache
        def recurse(i, letter):
            if i == n:
                return 1
            
            res = 0
            for nextLetter in vowelMap[letter]:
                res += recurse(i + 1, nextLetter)
                        
            return res
        
        return recurse(0, "$") % (pow(10, 9) + 7)
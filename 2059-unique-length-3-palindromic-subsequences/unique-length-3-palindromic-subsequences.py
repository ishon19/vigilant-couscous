class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # leverage the fact that the question is asking about
        # length 3 palindromes, which means, first and last 
        # characters are the same with a unique character 
        # sandwiched in between
        letters = set(s)
        res = 0

        for letter in letters:
            lIndex, rIndex = s.index(letter), s.rindex(letter)
            between = set()

            for i in range(lIndex + 1, rIndex):
                between.add(s[i])
                
            res += len(between)
        return res
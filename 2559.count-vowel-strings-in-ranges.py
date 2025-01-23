#
# @lc app=leetcode id=2559 lang=python3
#
# [2559] Count Vowel Strings in Ranges
#

# @lc code=start
class Solution:
    def isVowel(self, letter: str) -> bool:
        return letter.lower() in ['a', 'e', 'i', 'o', 'u']
    
    def checkStartsEndsVowel(self, word: str) -> bool:
        return self.isVowel(word[0]) and self.isVowel(word[-1])
    
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * len(words)

        prefix[0] = 1 if self.checkStartsEndsVowel(words[0]) else 0
        for i in range(1, len(words)):
            prefix[i] = prefix[i-1] + (1 if self.checkStartsEndsVowel(words[i]) else 0)
        
        res = [0] * len(queries)

        for i, [l, r] in enumerate(queries):
            if l == 0:
                res[i] = prefix[r]
            else:
                res[i] = prefix[r] - prefix[l - 1]
        
        return res
        
# @lc code=end


"""
allowed -> "ab"
words -> ["ad", "bd", "aaab", "baa", "badab"]
                       "ab"   "ba"   
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0

        for word in words:
            flag = False
            for char in word:
                if char not in allowed:
                    flag = True
                    break
            if not flag:
                res += 1        
                
        return res
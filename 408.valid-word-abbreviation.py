#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#

# @lc code=start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False

                skip = 0
                while j < len(abbr) and abbr[j].isdigit():
                    skip = skip * 10 + int(abbr[j])
                    j += 1
                
                i += skip
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        return i == len(word) and j == len(abbr)
# @lc code=end


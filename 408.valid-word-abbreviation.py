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
            if abbr[j].isalpha():
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == '0':
                    return False

                count = 0
                while j < len(abbr) and abbr[j].isdigit():
                    count = count * 10 + int(abbr[j])
                    j += 1
                
                i += count
        
        return i == len(word) and j == len(abbr)
            
            
# @lc code=end


#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banndedSet = set(banned)
        wordlist = []

        char = ''
        for i in range(len(paragraph)):
            if paragraph[i]== " " or paragraph[i] == ',':
                if char != '':
                    wordlist.append(char.lower())
                char = ""
            else:
                if paragraph[i].isalnum():
                    char += paragraph[i]
        
        if char:
            wordlist.append(char.lower())

        counts = Counter(wordlist)

        res = ''
        maxCount = 0
        for k, v in counts.items():
            if v > maxCount and k not in banndedSet:
                maxCount = v
                res = k
        
        return res
# @lc code=end


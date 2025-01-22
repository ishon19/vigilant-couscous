#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        res = []

        q = deque([(beginWord, 1)])

        while q:
            word, length = q.popleft()

            if word == endWord:
                res.append(endWord)
                return res
            
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + char + word[i+1:]

                    if newWord in wordSet:
                        res.append(newWord)
                        wordSet.remove(newWord)
                        q.append((newWord, length + 1))
        
        return res
        
# @lc code=end


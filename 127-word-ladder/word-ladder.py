class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0        
        q = deque([(beginWord, 1)])

        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + char + word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        q.append((newWord, length + 1))

        return 0
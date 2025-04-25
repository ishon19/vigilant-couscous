class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        q = deque([(beginWord, 1)])
        seen = set()

        while q:
            current, steps = q.popleft()

            if current == endWord:
                return steps

            for i in range(len(current)):
                for c in 'abcdefghijklmnonpqrstuvwxyz':
                    newWord = current[:i] + c + current[i+1:]
                    if newWord in wordSet and newWord not in seen:
                        seen.add(newWord)
                        q.append((newWord, steps+1))
        return 0
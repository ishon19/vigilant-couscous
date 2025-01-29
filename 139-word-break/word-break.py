class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True
    
    def searchPrefix(self, s, start):
        result = []
        node = self.root
        for i in range(start, len(s)):
            char = s[i]
            if char not in node.children:
                break
            node = node.children[char]
            if node.isWord:
                result.append(i+1)
        return result

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()

        for word in wordDict:
            trie.insert(word)
        
        n = len(s)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(n+1):
            if not dp[i]:
                continue
            
            for end in trie.searchPrefix(s, i):
                dp[end] = True
        
        return dp[n]

        t = 0

        

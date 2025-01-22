#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False
        self.word = ''

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        node.word = word
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        rows, cols = len(board), len(board[0])
        for word in words:
            trie.insert(word)
        
        found_words = set()

        def dfs(row, col, node):
            if row not in range(rows) or col not in range(cols):
                return 
            
            char = board[row][col]
            if char not in node.children:
                return 
            
            curr = node.children[char]
            if curr.is_word:
                found_words.add(curr.word)
                curr.is_word = False
            
            board[row][col] = '#'
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = row + dr, col + dc
                dfs(nr, nc, curr)
            board[row][col] = char

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, trie.root)
        
        return list(found_words)
        
# @lc code=end


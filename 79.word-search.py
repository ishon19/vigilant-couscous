#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]        
        node.is_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
    
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        trie = Trie()
        trie.insert(word)

        def dfs(row, col, node):
            if node.is_word:
                return True
            
            if row in range(rows) and col in range(cols):
                char = board[row][col]
                if char not in node.children:
                    return False
            
                board[row][col] = '#'
                dirs = [[-1,0],[1,0],[0,-1],[0,1]]
                found = False
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    found = found or dfs(nr, nc, node.children[char])
                board[row][col] = char
                return found
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, trie.root):
                    return True
        return False
        
# @lc code=end


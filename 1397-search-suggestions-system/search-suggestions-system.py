class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
class AutoComplete:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    
    def find_suggestions(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        suggestions = []
        self.dfs(node, prefix, suggestions)
        return suggestions[:3]
        
    def dfs(self, node, prefix, suggestions):
        if len(suggestions) == 3:
            return 

        if node.is_word:
            suggestions.append(prefix)
        
        for char, child in node.children.items():
            self.dfs(child, prefix + char, suggestions)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        auto_complete = AutoComplete()

        for product in sorted(products):
            auto_complete.insert(product)
        
        res = []
        prefix = ""
        for char in searchWord:
            prefix += char
            suggestions = auto_complete.find_suggestions(prefix)
            res.append(suggestions)
        return res
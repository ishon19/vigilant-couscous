class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def get_suggestions(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # reached the end of the prefix, now build up suggestions
        suggestions = []
        self.dfs(node, prefix, suggestions)
        return suggestions
    
    def dfs(self, node, current, suggestions):
        if len(suggestions) == 3:
            return suggestions

        if node.is_end:
            suggestions.append(current)
        
        for char, child in node.children.items():
            self.dfs(child, current + char, suggestions)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in sorted(products):
            trie.insert(product)
        
        res = []
        prefix = ''

        for letter in searchWord:
            prefix += letter
            res.append(trie.get_suggestions(prefix))

        return res
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfNode = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # need a reference to the root node
        cur = self.root  
        # print(cur.children)
        for c in word:
            i = ord(c) - ord('a')           
            if not cur.children[i]:                
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfNode = True
                

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                return False
            cur = cur.children[i]
        return cur.endOfNode
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                return False
            cur = cur.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
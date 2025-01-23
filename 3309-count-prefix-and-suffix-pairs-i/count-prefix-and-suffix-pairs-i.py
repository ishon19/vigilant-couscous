class Solution:
    def __init__(self):
        self.res = 0
        self.words = []
    
    def isValid(self, a, b):
        return a.startswith(b) and a.endswith(b)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        self.words = words

        if not words:
            return 0
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                
                if i < j:
                    if self.isValid(words[j], words[i]):
                        self.res += 1

        return self.res
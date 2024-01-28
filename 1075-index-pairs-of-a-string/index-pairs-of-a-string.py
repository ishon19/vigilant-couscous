class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []

        for word in words:
            n = len(word)
            i = 0
            j = n-1
            while j < len(text):
                if text[i:j+1] == word:
                    res.append([i, j])
                j += 1
                i += 1
        
        return sorted(res)
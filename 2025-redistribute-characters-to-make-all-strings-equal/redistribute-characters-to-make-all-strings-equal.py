class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = {}
        for word in words:
            for char in word:
                if char not in counter:
                    counter[char] = 1
                else:
                    counter[char] += 1
        
        # check if the count of every character is equal to the number of words
        for k, v in counter.items():
            if v % len(words) !=0:
                return False
        
        return True
class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""

        l, r = 0, 0

        while l < len(word) and r < len(word):
            count = 0
            while r < len(word) and word[l] == word[r]:
                count += 1
                r += 1
            if count <= 9:
                comp += str(count) + word[l]
            else:
                while count>=9:
                    comp += "9"+ word[l]
                    count = count - 9
                if count > 0:
                    comp += str(count) + word[l]
            l = r
        
        return comp
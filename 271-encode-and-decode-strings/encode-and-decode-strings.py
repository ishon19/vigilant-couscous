class Codec:
    def __init__(self):
        self.SHIIFT = 1973
        self.DELIMITER = '~DELIM~'

    def shift(self, letter, amount):
        if 'a' <= letter <= 'z':
            return chr(((ord(letter) - ord('a') + amount) % 26) + ord('a'))
        elif 'A' <= letter <= 'Z':
            return chr(((ord(letter) - ord('A') + amount) % 26) + ord('A'))
        else:
            return letter

    def obsfuscate(self, words, mode="ENCODE"):
        shifted = []        
        for word in words:
            encoded = ''    
            for char in word:
                encoded += self.shift(char, amount=self.SHIIFT if mode == 'ENCODE' else -self.SHIIFT)
            shifted.append(encoded)
        return self.DELIMITER.join(shifted)

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return self.obsfuscate(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        encodedList = s.split(self.DELIMITER)
        decodedStr = self.obsfuscate(encodedList, 'DECODE')
        return decodedStr.split(self.DELIMITER)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
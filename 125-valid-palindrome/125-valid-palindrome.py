class Solution:
    def isPalindrome(self, s: str) -> bool:
        plainText = [i.lower() if (65<=ord(i)<91 or 97<=ord(i)<123 or 48<=ord(i)<58) else '' for i in s]
        filteredText = "".join(plainText)
        print(filteredText)
        return filteredText[::-1] == filteredText
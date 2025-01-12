class Solution:
    def isValid(self, letter):
        return ord('a')<=ord(letter)<=ord('z') or ord('0')<=ord(letter)<=ord('9')

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()

        while l <= r:
            if self.isValid(s[l]) and self.isValid(s[r]):
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            elif self.isValid(s[l]):
                r -= 1
            else:
                l += 1
        
        return True
            

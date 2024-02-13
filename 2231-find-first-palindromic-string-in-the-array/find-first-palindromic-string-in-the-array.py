class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            l, r = 0, len(word) - 1
            palindrome = True
            while l<r:
                if word[l] != word[r]:
                    palindrome = False
                    break
                l += 1
                r -= 1
            if palindrome: return word
        return ""
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = {}

        def validate_palindrome(i, j):
            if i >= j:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if s[i] == s[j]:
                memo[(i,j)] = validate_palindrome(i+1, j-1)
            else:
                memo[(i,j)] = 1 + min(validate_palindrome(i+1, j), validate_palindrome(i, j-1))
            
            return memo[(i,j)]
        
        return validate_palindrome(0, len(s) - 1) <= k
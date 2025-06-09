class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False 
                left += 1
                right -= 1
            return True 
        
        left, right = 0, len(s)-1

        if isValid(left, right):
            return True

        while left < right:
            if s[left] != s[right]:
                return isValid(left + 1, right) or isValid(left, right - 1)  
            left += 1
            right -= 1
        
        return True
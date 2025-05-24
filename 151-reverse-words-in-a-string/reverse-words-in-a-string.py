class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        left = 0
        n = len(s)

        while left < n:
            while left < n and s[left] == ' ':
                left += 1
            
            if left >= n:
                break 
            
            right = left 
            while right < n and s[right] != ' ':
                right += 1
            
            words.append(s[left:right])
            left = right
        
        return ' '.join(words[::-1])

        
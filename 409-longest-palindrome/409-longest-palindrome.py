class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashtable = {key:s.count(key) for key in s}
        if len(hashtable) == 1:
            return len(s)
        # print(hashtable)
        max_len = 0        
        seen = False
        for key in hashtable:
            max_len += hashtable[key]//2 * 2
            if max_len%2==0 and hashtable[key]%2==1:
                max_len += 1        
        return max_len
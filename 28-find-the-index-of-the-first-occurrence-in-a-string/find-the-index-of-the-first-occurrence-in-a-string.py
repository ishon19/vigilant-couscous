class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        
        start = 0
        
        for end in range(len(needle), len(haystack)+1):
            # print(start, end, haystack[start:end])
            if haystack[start:end] == needle:
                return start
            else:
                start += 1
        
        return -1
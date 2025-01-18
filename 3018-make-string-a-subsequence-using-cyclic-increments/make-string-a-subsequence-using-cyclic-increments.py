class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        a = [ord(c)-97 for c in str1]
        b = [ord(c)-97 for c in str2]
        i = 0
        for c in a:
            if b[i] == c or b[i] == (c+1)%26:
                i += 1
                if i == len(b):
                    return True
        return False
        # if len(str2) > len(str1): 
        #     return False
        # # iterate over str2 and check if one increment early is in str1
        # i = 0
        # for c in str2:
        #     incremented = 'z' if c == 'a' else chr(ord(c) - 1)
        #     while i < len(str1) and str1[i] != c and str1[i] != incremented:
        #         i += 1            
        #     if i >= len(str1): return False
        # return True

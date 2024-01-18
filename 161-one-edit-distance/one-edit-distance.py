class Solution:
    def isOneEditDistance(self, s1: str, s2: str) -> bool:
        if abs(len(s1) - len(s2)) > 1 or s1 == s2:
            return False
        
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        foundDiff = False
        i = 0
        j = 0

        while i<len(s1) and j<len(s2):
            if s1[i] != s2[j]:
                if foundDiff:
                    return False
                foundDiff = True
                
                if len(s1) == len(s2):
                    i += 1
            else:
                i += 1
            j += 1

        return True
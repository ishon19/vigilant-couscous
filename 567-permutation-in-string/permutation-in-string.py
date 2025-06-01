class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
            
        w1, w2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            w1[ord(s1[i]) - ord('a')] += 1
            w2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if w1[i] == w2[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True 
            
            index = ord(s2[right]) - ord('a')
            w2[index] += 1
            if w1[index] == w2[index]:
                matches += 1
            elif w1[index] == w2[index] - 1:
                matches -= 1
            
            index = ord(s2[left]) - ord('a')
            w2[index] -= 1
            if w1[index] == w2[index]:
                matches += 1
            elif w1[index] == w2[index] + 1:
                matches -= 1
            
            left += 1
        
        return matches == 26
            

            
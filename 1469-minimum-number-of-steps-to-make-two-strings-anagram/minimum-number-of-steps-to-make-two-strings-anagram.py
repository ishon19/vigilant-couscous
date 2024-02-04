class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_counts = [0] * 26

        for i in range(len(s)):
            char_counts[ord(t[i]) - ord('a')] += 1
            char_counts[ord(s[i]) - ord('a')] -= 1
        
        # print(char_counts)
        res = 0
        for i in range(26):
            res += max(0, char_counts[i])
        
        return res

